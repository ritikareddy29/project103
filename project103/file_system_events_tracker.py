import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "/Users/sunilreddy/Desktop/downloaded_images"
to_dir = "/Users/sunilreddy/Desktop/document_files"

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print("Hey, {event.src_path} has been created!")
    def on_deleted(self, event):
        print("Oops! Someone deleted {event.src_path}!")
    def on_moved(self, event):
        print("{event.src_path} has been moved or renamed")
    def on_modified(self, event):
        print("{event.src_path} has been modified")


event_handler = FileMovementHandler()

observer = Observer()

observer.schedule(event_handler, from_dir, recursive=True)

observer.start()


try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("Stopped")
    observer.stop()