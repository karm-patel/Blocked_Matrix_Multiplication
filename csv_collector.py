from pathlib import Path
import shutil
import os
 
def csvCollector():
    if not os.path.isdir("csv"):
        os.system("mkdir csv")

    source = ['./csv2048','./csv8192']
    target = './csv'
    for src in source:
        try:
            files=os.listdir(src)
        except:
            print("No csv dump found")
            continue
        for fname in files:
            shutil.copy2(os.path.join(src,fname), target)