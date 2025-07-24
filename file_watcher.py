#!/usr/bin/env python3
import time
import subprocess
import os
import sys
import threading


venv_path = "/Users/fk/Desktop/stream_of_me_7-23/numbers_env/lib/python3.*/site-packages"
sys.path.insert(0, venv_path)

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class NumbersFileHandler(FileSystemEventHandler):
    def __init__(self):
        self.timers = {}
        
    def on_modified(self, event):
        if not event.is_directory and event.src_path.endswith('.numbers'):
            print(f"Numbers file changed: {event.src_path}")
            
            
            if event.src_path in self.timers:
                self.timers[event.src_path].cancel()
           
            self.timers[event.src_path] = threading.Timer(30.0, self.rebuild_after_delay, [event.src_path])
            self.timers[event.src_path].start()
            print("Will rebuild in 30 seconds if no more changes...")
    
    def rebuild_after_delay(self, file_path):
        print(f"30 seconds passed, rebuilding for {file_path}...")
        try:
            result = subprocess.run(['bash', '-c', 'cd /Users/fk/Desktop/stream_of_me_7-23 && source numbers_env/bin/activate && python3 updateHtml.py && git add . && git commit -m "Auto-update - $(date)" && git push origin main'],
                                  capture_output=True, 
                                  text=True)
            print("Rebuild output:", result.stdout)
            if result.stderr:
                print("Rebuild errors:", result.stderr)
            print("Rebuild complete!")
        except Exception as e:
            print(f"Error running rebuild: {e}")

if __name__ == "__main__":
    watch_path = "/Users/fk/Desktop/stream_of_me_7-23"
    
    event_handler = NumbersFileHandler()
    observer = Observer()
    observer.schedule(event_handler, watch_path, recursive=True)
    observer.start()
    
    print(f"Watching {watch_path} for changes to .numbers files...")
    print("Will wait 30 seconds after last change before rebuilding...")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()