import os, sys, threading, queue, datetime, re
from typing import Optional

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from CheeseType import NonNegativeInt

class Level:
    def __init__(self, weight: NonNegativeInt, color: Optional[str] = None, messageTemplate: Optional[str] = None, timerTemplate: Optional[str] = None):
        '''
        ## Args

        - weight：权重。小于日志过滤权重的消息会被忽略。

        - color：控制台打印的等级标签样式。

        - messageTemplate：消息格式，默认为`logger.messageTemplate`。

        - timerTemplate：日期格式，默认为`logger.timerTemplate`。
        '''

        self.weight: NonNegativeInt = weight
        self.color: Optional[str] = color
        self.messageTemplate: Optional[str] = messageTemplate
        self.timerTemplate: Optional[str] = timerTemplate

class Logger(threading.Thread):
    def __init__(self):
        self.filePath: Optional[str] = None
        self.messageTemplate: str = '(%level) %timer > %content'
        self.timerTemplate: str = '%Y-%m-%d %H:%M:%S.%f'
        self.filter: NonNegativeInt | list[str] = []
        self.levels: dict[str, Level] = {
            'DEBUG': Level(10, '34', None, None),
            'INFO': Level(20, '32', None, None),
            'STARTING': Level(20, '32', None, None),
            'ENDING': Level(20, '34', None, None),
            'HTTP': Level(20, None, None, None),
            'WEBSOCKET': Level(20, None, None, None),
            'WARNING': Level(30, '33', None, None),
            'DANGER': Level(40, '31', None, None),
            'ERROR': Level(50, '35', None, None)
        }
        self.colorful: bool = True
        self._queue: queue.Queue = queue.Queue()
        self._flag: bool = False

        super().__init__(daemon = True)

    def run(self):
        self._flag = True
        while self._flag or not self._queue.empty():
            level, now, message = self._queue.get()

            message = (logger.levels[level].messageTemplate or logger.messageTemplate).replace('%level', level).replace('%timer', now.strftime(logger.levels[level].timerTemplate or logger.timerTemplate)).replace('%content', message).replace('\n', '\n    ') + '\n'
            if self.filePath is not None:
                os.makedirs(os.path.dirname(self.filePath), exist_ok = True)
                with open(self.filePath, 'a', encoding = 'utf-8') as f:
                    f.write(message)
            else:
                self._flag = False

    def stop(self):
        self._flag = False
        self.join()

logger = Logger()

def default(level: str, message: str, colorfulMessage: Optional[str] = None, logger: Optional[Logger] = None):
    '''
    ## Args

    - colorfulMessage: 不满足于自动的色彩填充，可以选择自定义的控制台内容。它仅会改变消息内容，对消息等级以及时间的样式不会有影响。

    - logger: 应该不会用到...指定其他的日志实例输出消息。
    '''

    ''' Validate '''
    if level not in logger.levels:
        raise KeyError('no level with this key')

    ''' Filter '''
    if isinstance(logger.filter, list):
        for _level in logger.filter:
            if level == _level:
                return
    elif logger.levels[level].weight <= NonNegativeInt(logger.filter):
        return

    ''' Terminal '''
    now = datetime.datetime.now()
    message = f'{message}'
    if logger.colorful:
        if colorfulMessage is None:
            terminalMessage = (logger.levels[level].messageTemplate or logger.messageTemplate).replace('%level', f'\033[{logger.levels[level].color}m{level}\033[0m' if logger.levels[level].color else level).replace('%timer', f'\033[2m{now.strftime(logger.levels[level].timerTemplate or logger.timerTemplate)}\033[0m').replace('%content', message).replace('\n', '\n    ')
        else:
            terminalMessage = (logger.levels[level].messageTemplate or logger.messageTemplate).replace('%level', f'\033[{logger.levels[level].color}m{level}\033[0m' if logger.levels[level].color else level).replace('%timer', f'\033[2m{now.strftime(logger.levels[level].timerTemplate or logger.timerTemplate)}\033[0m').replace('%content', colorfulMessage).replace('\n', '\n    ')
    else:
        terminalMessage = (logger.levels[level].messageTemplate or logger.messageTemplate).replace('%level', level).replace('%timer', now.strftime(logger.levels[level].timerTemplate or logger.timerTemplate)).replace('%content', message).replace('\n', '\n    ')
    print(terminalMessage)

    ''' Log file writter '''
    if logger.filePath is not None:
        if not logger.is_alive():
            logger.start()
        logger._queue.put((level, now, message))

def debug(message: str, colorfulMessage: Optional[str] = None, logger: Optional[Logger] = logger):
    default('DEBUG', message, colorfulMessage, logger)

def info(message: str, colorfulMessage: Optional[str] = None, logger: Optional[Logger] = logger):
    default('INFO', message, colorfulMessage, logger)

def starting(message: str, colorfulMessage: Optional[str] = None, logger: Optional[Logger] = logger):
    default('STARTING', message, colorfulMessage, logger)

def ending(message: str, colorfulMessage: Optional[str] = None, logger: Optional[Logger] = logger):
    default('ENDING', message, colorfulMessage, logger)

def warning(message: str, colorfulMessage: Optional[str] = None, logger: Optional[Logger] = logger):
    default('WARNING', message, colorfulMessage, logger)

def danger(message: str, colorfulMessage: Optional[str] = None, logger: Optional[Logger] = logger):
    default('DANGER', message, colorfulMessage, logger)

def error(message: str, colorfulMessage: Optional[str] = None, logger: Optional[Logger] = logger):
    default('ERROR', message, colorfulMessage, logger)

def http(message: str, colorfulMessage: Optional[str] = None, logger: Optional[Logger] = logger):
    default('HTTP', message, colorfulMessage, logger)

def websocket(message: str, colorfulMessage: Optional[str] = None, logger: Optional[Logger] = logger):
    default('WEBSOCKET', message, colorfulMessage, logger)
