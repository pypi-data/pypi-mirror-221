import json
import os
import subprocess as sb

from intelliw.interface.apihandler import Request
from intelliw.core.pipeline import Pipeline, Const
from intelliw.utils import message
from intelliw.utils.logger import _get_framework_logger
from intelliw.utils.util import get_json_encoder

logger = _get_framework_logger()


class StarterMode:
    CMD = 'cmd'


class ProcedureType:
    INFER = 'infer'
    TRAIN = 'train'
    IMPORT_ALG = 'importalg'
    IMPORT_MODEL = 'importmodel'
    IMPORT = [IMPORT_ALG, IMPORT_MODEL]


class CustomError(Exception):
    def __init__(self, msg) -> None:
        self.msg = msg

    def __str__(self) -> str:
        return '自定义算法异常, {}'.format(self.msg)


class Custom:
    """
    Custom entrypoint
    """

    def __init__(self, path, reporter_addr=None, procedure_type=None, starter_mode=StarterMode.CMD):
        """
        init custom entrypoint
        args:
            path -- algorithm's path
            procedure_type -- custom algorithm procedure type (infer/train)
            starter_mode -- custom algorithm start mode (default: CMD)
        """
        self.config = None
        self.algorithm_path = path
        self.procedure_type = procedure_type
        self.is_import = procedure_type in ProcedureType.IMPORT

        self.pipeline = Pipeline(reporter_addr)
        self.starter_mode = starter_mode
        self.report = self.pipeline.recorder.report

    def load_config(self, path):
        yaml_path = os.path.join(path, Const.model_yaml)
        return self.pipeline.load_config(yaml_path)

    def start_engine(self):
        # 获取启动方式, 目前就命令行方式
        if self.starter_mode == StarterMode.CMD:
            return self._get_command()
        return self._get_command()

    def format_msg(self, msg: message.CommonResponse):
        msg.other = {'businessType': self.procedure_type}
        return msg

    def run_import(self):
        # 项目初始化成功
        if self.is_import:
            self.report(message.ok_import_algorithm)
        else:
            self.report(message.ok_import_model)

    def run_process(self):
        try:
            starter = self.start_engine()
            self.report(message.ok_import_model)
            logger.info(f"\033[33mCustom Mode:\033[0m {starter}")
            starter.run()
        except Exception as e:
            # 项目运行失败
            self.pipeline.raise_exception(
                self.format_msg(message.err_custom_process), e
            )
        # 项目运行成功
        self.report(self.format_msg(message.ok_custom_finish))

    def run(self):
        if self.procedure_type in ProcedureType.IMPORT:
            # 导入模式
            self.run_import()
        else:
            # 运行模式
            self.config = self.load_config(self.algorithm_path)
            self.run_process()

    def _get_command(self):
        # 获取command
        command = self.config['Model'].get('boot', [])
        # 获取环境变量
        parameters = self.config['Model'].get('parameters', {})
        os.environ.setdefault(
            'PARAMETERS', json.dumps(parameters, ensure_ascii=False)
        )
        return CMD(command)


class CMD:
    def __init__(self, cmd):
        self.cmd = cmd

    def run(self):
        if not self.cmd:
            raise CustomError("启动命令为空")
        res = sb.Popen(self.cmd, stdout=sb.PIPE, stderr=sb.PIPE, env=os.environ)
        while True:
            out = res.stdout.readline().strip().decode('utf-8')
            if out:
                logger.info(out)

            print(sb.Popen.poll(res))
            if sb.Popen.poll(res) is not None and not out:
                print(res.returncode)
                if res.returncode > 0:
                    err_msg = res.stderr.read().decode('utf-8')
                    raise CustomError(err_msg)
                return None

    def __str__(self):
        return f"\033[33mCMD\033[0m - {self.cmd}"
