# streamlit_yolov8_detect

---

# deploy error

ImportError: This app has encountered an error. The original error message is redacted to prevent data leaks. 
Full error details have been recorded in the logs 
(if you're on Streamlit Cloud, click on 'Manage app' in the lower right of your app).

Traceback:

File "/home/adminuser/venv/lib/python3.11/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 600, in _run_script
    exec(code, module.__dict__)
    
File "/mount/src/streamlit_yolov8_detect/app.py", line 2, in <module>
    from ultralytics import YOLO
    
File "/home/adminuser/venv/lib/python3.11/site-packages/ultralytics/__init__.py", line 5, in <module>
    from ultralytics.data.explorer.explorer import Explorer
    
File "/home/adminuser/venv/lib/python3.11/site-packages/ultralytics/data/__init__.py", line 3, in <module>
    from .base import BaseDataset
    
File "/home/adminuser/venv/lib/python3.11/site-packages/ultralytics/data/base.py", line 12, in <module>
    import cv2

---
