#!/usr/bin/env python3
import time
import subprocess
import os
import sys
import threading

# Add the virtual environment to Python path
venv_path = "/Users/sophiawood/Desktop/streamof/myenv/lib/python3.*/site-packages"
sys.path.insert(0, venv_path)

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class NumbersFileHandler(FileSystemEventHandler):
    def __init__(self):
        self.timers = {}
        
    def on_modified(self, event):
        if not event.is_directory and event.src_path.endswith('.numbers'):
            print(f"Numbers file changed: {event.src_path}")
            
            # Cancel any existing timer for this file
            if event.src_path in self.timers:
                self.timers[event.src_path].cancel()
            
            # Set a new timer to rebuild after 30 seconds of no changes
            self.timers[event.src_path] = threading.Timer(30.0, self.rebuild_after_delay, [event.src_path])
            self.timers[event.src_path].start()
            print("Will rebuild in 30 seconds if no more changes...")
    
    def rebuild_after_delay(self, file_path):
        print(f"30 seconds passed, rebuilding for {file_path}...")
        try:
            result = subprocess.run(['bash', '-c', 'cd /Users/sophiawood/Desktop/streamof && source myenv/bin/activate && python3 updateHtml.py && git add . && git commit -m "Auto-update - $(date)" && git push origin main'], 
                                  capture_output=True, 
                                  text=True)
            print("Rebuild output:", result.stdout)
            if result.stderr:
                print("Rebuild errors:", result.stderr)
            print("Rebuild complete!")
        except Exception as e:
            print(f"Error running rebuild: {e}")

if __name__ == "__main__":
    # Update this path to where your Numbers file is stored
    watch_path = "/Users/sophiawood/Desktop/streamof"
    
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