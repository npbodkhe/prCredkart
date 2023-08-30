import inspect
import logging


class LogGenerator:
    @staticmethod
    def loggen():
        name = inspect.stack()[1][3]
        logger = logging.getLogger()
        file = logging.FileHandler(
            "C:\\Users\\npbod\\Videos\\Captures\\revision\\prCredkart\\Logs\\Automation_Cart.log")
        format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(funcname)s : %(lineno)s : %(massage)s")
        file.setFormatter(format)
        logger.addHandler(file)
        logger.setLevel(logging.DEBUG)
        return logger
