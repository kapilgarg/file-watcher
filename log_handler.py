"""
Module for Handler class for watchdog handler
"""
import logging
from logfile_handler import LogFileHandler
from watchdog.events import FileSystemEventHandler

Logger = logging.getLogger(__name__)


class LogHandler(FileSystemEventHandler):
    """
    Handler class, provides implementation for file / directory change event
    """

    def __init__(self):
        self.log_file_handler = LogFileHandler()

    def on_modified(self, event):
        """
        invoked when a file is modified.
        """
        Logger.info('on modified %s', str(event))
        log_file = event.src_path
        try:
            self.log_file_handler.handle(log_file)
        except Exception as ex:
            Logger.exception("Error while handling the message", ex)
