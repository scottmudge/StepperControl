import logging
import os
import sys
import datetime
import coloredlogs
import globalvars


LOG_TO_DISK = globalvars.LOG_TO_DISK


def get_cur_directory(file_name: str=__file__) -> str:
    if hasattr(sys, 'frozen') and sys.frozen:
        path, filename = os.path.split(sys.executable)
        directory = path
    else:
        directory = os.path.dirname(os.path.realpath(file_name))
    return directory


def get_root_directory() -> str:
    return "{}/../".format(get_cur_directory(__file__))


class FormatterWithHeader(logging.Formatter):
    def __init__(self, header, fmt=None, datefmt=None, style='%'):
        super().__init__(fmt, datefmt, style)
        self.header = header  # This is hard coded but you could make dynamic
        # Override the normal format method
        self.format = self.first_line_format

    def first_line_format(self, record):
        # First time in, switch back to the normal format function
        self.format = super().format
        return self.header + "\n" + self.format(record)


class LoggerMaster:

    def __init__(self, name: str, log_dir: str):
        handler = None

        if LOG_TO_DISK:
            if len(log_dir) > 3:
                self.log_dir = log_dir + "/logs/"
            else:
                self.log_dir = get_root_directory() + "/logs/"

            if not os.path.exists(self.log_dir):
                os.makedirs(self.log_dir)

            if not os.path.exists(self.log_dir):
                raise FileNotFoundError("Could not create log directory: \n\t> {}".format(self.log_dir))

            self.log_file = self.log_dir + name + ".log"
                            # + datetime.datetime.now().strftime('%Y-%m-%d') + \
                            # ".log"

            write_full_header = False

            if not os.path.exists(self.log_file):
                write_full_header = True

            handler = logging.FileHandler(self.log_file, 'a')
            handler.setLevel(logging.INFO)

            if write_full_header:
                formatter = FormatterWithHeader('#################################################################\n'
                                                '#     Log for: ' + name + '\n' +
                                                '#     Date: ' + datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S') + '\n'
                                                '#################################################################\n',
                                                '%(asctime)s %(message)s')
            else:
                formatter = FormatterWithHeader('\n############################ APP START ##########################\n',
                                                '%(asctime)s %(message)s')

            handler.setFormatter(formatter)
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)

        if "logconsole" in sys.argv:
            coloredlogs.DEFAULT_LOG_FORMAT = '%(asctime)s %(message)s'
            coloredlogs.DEFAULT_FIELD_STYLES = dict(
                asctime=dict(color='green'),
                hostname=dict(color='magenta'),
                levelname=dict(color='cyan'),
                programname=dict(color='cyan'),
                threadname=dict(color='magenta'),
                name=dict(color='blue'))
            coloredlogs.install(logging.INFO)

        # self.logger.addHandler(ch)
        if LOG_TO_DISK and handler is not None:
            self.logger.addHandler(handler)


logger = None

MESSAGE_INFO = 0
MESSAGE_DEBUG = 1
MESSAGE_WARN = 2
MESSAGE_ERROR = 3

queue = []
logger_dict = {}
logger_set = False

name_color = 'magenta'
info_level_color = 'cyan'
err_level_color = 'red'
warn_level_color = 'yellow'
debug_level_color = 'green'


class LogEntry:

    def __init__(self, message: str, msg_type=0):
        if msg_type > 3:
            msg_type = 0
        self.message = message
        self.msg_type = msg_type


class Logger:
    def __init__(self, name: str):
        self._name = name

    def info(self, message: str):
        global queue
        global logger
        global logger_set

        if not logger_set:
            entry = LogEntry("[{}]".format(self._name) + " INFO" +
                             ": {}".format(message), MESSAGE_INFO)
            queue.append(entry)
            return
        logger.logger.info("[{}]".format(self._name) + " INFO" +
                           ": {}".format(message))

    def warn(self, message: str):
        global queue
        global logger
        global logger_set

        if not logger_set:
            entry = LogEntry("[{}]".format(self._name) + " WARN" +
                             ": {}".format(message), MESSAGE_WARN)
            queue.append(entry)
            return
        logger.logger.warn("[{}]".format(self._name) + " WARN" +
                           ": {}".format(message))

    def error(self, message: str):
        global queue
        global logger
        global logger_set

        if not logger_set:
            entry = LogEntry("[{}]".format(self._name) + " ERR" +
                             ": {}".format(message), MESSAGE_ERROR)
            queue.append(entry)
            return
        logger.logger.error("[{}]".format(self._name) + " ERR" +
                            ": {}".format(message))

    def debug(self, message: str):
        global queue
        global logger
        global logger_set

        if not logger_set:
            entry = LogEntry("[{}]".format(self._name) + " DBG" +
                             ": {}".format(message), MESSAGE_DEBUG)
            queue.append(entry)
            return
        logger.logger.debug("[{}]".format(self._name) + " DBG" +
                            ": {}".format(message))


def create_logger(name: str) -> Logger:
    global logger_dict

    if name not in logger_dict:
        logger_dict[name] = Logger(name)

    return logger_dict[name]


def info(message: str):
    global queue
    global logger
    global logger_set

    if not logger_set:
        entry = LogEntry("[{}]".format("General") + " INFO" +
                         ": {}".format(message), MESSAGE_INFO)
        queue.append(entry)
        return
    logger.logger.info("[{}]".format("General") + " INFO" +
                       ": {}".format(message))


def warn(message: str):
    global queue
    global logger
    global logger_set

    if not logger_set:
        entry = LogEntry("[{}]".format("General") + " WARN" +
                         ": {}".format(message), MESSAGE_INFO)
        queue.append(entry)
        return
    logger.logger.info("[{}]".format("General") + " WARN" +
                       ": {}".format(message))


def error(message: str):
    global queue
    global logger
    global logger_set

    if not logger_set:
        entry = LogEntry("[{}]".format("General") + " ERR" +
                         ": {}".format(message), MESSAGE_INFO)
        queue.append(entry)
        return
    logger.logger.info("[{}]".format("General") + " ERR" +
                       ": {}".format(message))


def debug(message: str):
    global queue
    global logger
    global logger_set

    if not logger_set:
        entry = LogEntry("[{}]".format("General") + " DBG" +
                         ": {}".format(message), MESSAGE_INFO)
        queue.append(entry)
        return
    logger.logger.info("[{}]".format("General") + " DBG" +
                       ": {}".format(message))


_Loggers = {}


def get_logger(name: str) -> Logger:
    global logger_set
    global logger
    if not logger_set:
        initialize(globalvars.APP_NAME, True)
    if name not in _Loggers:
        _Loggers[name] = Logger(name)
    return _Loggers[name]


def _check_queue():
    global queue
    global logger
    global logger_set

    if not logger_set:
        return

    for log_entry in queue:
        if log_entry.msg_type == MESSAGE_DEBUG:
            debug(log_entry.message)
        elif log_entry.msg_type == MESSAGE_ERROR:
            info(log_entry.message)
        elif log_entry.msg_type == MESSAGE_WARN:
            warn(log_entry.message)
        elif log_entry.msg_type == MESSAGE_INFO:
            info(log_entry.message)

    queue.clear()


def initialize(name: str = "", log_to_disk=True, log_dir: str = "") -> LoggerMaster:
    global logger
    global logger_set
    global queue
    global LOG_TO_DISK

    LOG_TO_DISK = log_to_disk

    if logger is None:
        if len(name) > 0:
            logger = LoggerMaster(name, log_dir)
            logger_set = True
            _check_queue()
            return logger
        else:
            raise TypeError("Must pass a name and a stream")
