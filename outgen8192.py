from glob import glob
import os
import regex as re


def genOutFile8192():
    c_files = glob("code8192/*.c")

    tiles_8192 = [8,16,32,64,128]

    if not os.path.isdir("out8192"):
        os.system("mkdir out8192")

    mat_size = 8192
    for tile_size in tiles_8192:
        for file in c_files:
            with open(file,"r") as fp:
                content = fp.read()

            content = re.sub(r"int B = [0-9]*;", f"int B = {tile_size};", content)
            with open(file, "w") as fp:
                fp.write(content)
            
            version = file.split("/")[-1].split("_")[0]
            os.system(f"gcc -g -o out8192/{version}_{mat_size}_{tile_size} {file}")

