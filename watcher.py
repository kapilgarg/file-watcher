import argparse
import time
import logging
from log_handler import LogHandler
from watchdog.observers import Observer

SLEEP_TIME = 5  # seconds
logging.basicConfig(format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d:%H:%M:%S', level=logging.INFO)
Logger = logging.getLogger(__name__)


def watch(target_dir, handler):
    observer = Observer()
    observer.schedule(handler, target_dir, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(SLEEP_TIME)
    except:
        observer.stop()
    observer.join()


def main(target_dir):
    handler = LogHandler()
    Logger.info(f"starting watch on {target_dir}")
    watch(target_dir, handler)


if __name__ == "__main__":
    argParser = argparse.ArgumentParser()
    argParser.add_argument("--dir", help="directory to monitor")
    args = argParser.parse_args()
    Logger.info(args)
    main(args.dir)
