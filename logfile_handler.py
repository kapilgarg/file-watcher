"""
Module for log filehandler
"""
import logging

Logger = logging.getLogger(__name__)


class LogFileHandler():
    """
    TODO
    """

    def __init__(self):
        self.active_watch = {}

    def handle(self, log_file):
        """
        Handler function file change
        """
        data, position = self.get_file_contents(
            log_file, self.active_watch.get(log_file, 0))

        if data:
            # do some thing with data, send it to message queue...
            Logger.info('processed data- %s', data)
        self.active_watch[log_file] = position

        # do not forget to remove the entry from this active_watch once the job completes
        # and no longer required to be monitored otherwise active_watch  will grow indefinitely.
        # del(self.active_watch[log_file])

    def get_file_contents(self, file, position):
        """
        reads the contents of the file from last position and
        return contents with current position
        """
        with open(file, 'r') as f:
            f.seek(position)
            return f.read(), f.tell()
