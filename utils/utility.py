import sys
import os
from threading import Lock
from utils.logger import get_logger as logging
import datetime

DateFormat = '%Y-%m-%d %H:%M:%S'


def get_time_stamp_str() -> str:
    """Returns timestamp as string"""
    return datetime.datetime.now().strftime(DateFormat)


def get_datetime_from_timestamp(timestamp: str) -> datetime.datetime:
    """Returns datetime object from string"""
    return datetime.datetime.strptime(timestamp, DateFormat)


def get_timestamp_from_datetime(dt: datetime.datetime) -> str:
    """Returns string from datetime object."""
    return dt.strftime(DateFormat)


def timedelta_to_string(td: datetime.timedelta) -> str:
    """Returns string from time delta."""
    return str(td)


class MovingAvg:
    """Helps with creating a simple moving average."""

    def __init__(self, frame_size: int):
        """Initializes moving average object.

        Args:
            frame_size (int): The number of averaging frames to use.
        """
        self._sum = 0.0
        self._cur_elem_count = 0
        self._buffer = []
        self._frame_size = frame_size
        self._mtx = Lock()

    def add_value(self, val: float):
        """Adds a value to the buffer.

        Args:
            val (float): Value to add into buffer.
        """
        self._mtx.acquire()
        self._buffer.append(val)
        self._sum += val

        if self._cur_elem_count < self._frame_size:
            self._cur_elem_count += 1
        else:
            self._sum -= self._buffer[0]
            self._buffer.pop(0)
        self._mtx.release()

    def set_frame_fount(self, frame_count: int):
        """Sets the frame count

        Args:
            frame_count (int): Frame count to set averager to.
        """
        self._mtx.acquire()
        self._frame_size = frame_count
        self._buffer.clear()
        self._cur_elem_count = 0
        self._sum = 0.0
        self._mtx.release()

    def get_avg(self) -> float:
        """Returns the average value."""
        if self._cur_elem_count < 1:
            return 0
        self._mtx.acquire()
        avg = self._sum / float(self._cur_elem_count)
        self._mtx.release()
        return avg


SharesDirectory = ""


def get_cur_directory(file_name: str=__file__) -> str:
    """Returns the current directory of the file.

    Args:
        file_name (str):
    """
    if hasattr(sys, 'frozen') and sys.frozen:
        path, filename = os.path.split(sys.executable)
        directory = path
    else:
        directory = os.path.dirname(os.path.realpath(file_name))
    return directory


def get_root_directory() -> str:
    """Returns root directory, useful for storing data."""
    return "{}/../".format(get_cur_directory(__file__))


def file_exists(file_name: str) -> bool:
    """
    Args:
        file_name (str):
    """
    if os.path.isfile(file_name) and os.access(file_name, os.R_OK):
        return True
    else:
        return False


def make_directory(directory: str) -> bool:
    """ Creates supplied directory and checks to make sure it exists.

    Args:
        directory (str): Directory to create.

    Return:
        True on success.
    """
    if not os.path.exists(directory):
        # Try to make directory
        try:
            os.mkdir(str(directory))
        except Exception as e:
            logging("Utility").error("Could not create directory:\n\t> {}\n\t> Exception: {}"
                                     .format(directory, str(e)))
            return False
        if not os.path.exists(directory):
            logging("Utility").error("Could not create directory:\n\t> {}".format(directory))
            return False

    return True