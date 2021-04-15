import time
import os
if os.name == "nt":
    os.system("pip install -r requirements.txt") #Windows Only
else:
    os.system("python3 -m pip install -r requirements.txt")
