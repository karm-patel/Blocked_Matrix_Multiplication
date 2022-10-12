from glob import glob
import os
import regex as re

def genOutFile2048():
    if not os.path.isdir("out2048"):
        os.system("mkdir out2048")

    c_files = glob("code2048/*.c")

    tiles_2048 = [2,4,8,16,32,64,128,256,512]

    mat_size = 2048
    for tile_size in tiles_2048:
        for file in c_files:
            with open(file,"r") as fp:
                content = fp.read()

            content = re.sub(r"int B = [0-9]*;", f"int B = {tile_size};", content)
            with open(file, "w") as fp:
                fp.write(content)
            
            version = file.split("/")[-1].split("_")[0]
            os.system(f"gcc -g -o out2048/{version}_{mat_size}_{tile_size} {file}")