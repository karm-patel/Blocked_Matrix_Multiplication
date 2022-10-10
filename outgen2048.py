from glob import glob
import os
import regex as re


if not os.path.isdir("out2048"):
    os.system("mkdir out2048")

c_files = glob("code2048/*.c")
print(c_files)

tiles_2048 = [8,16,32,64,128,256,512]
# for file in c_files:    
#     

mat_size = 2048
for tile_size in tiles_2048:
    for file in c_files:
        if "v2" not in file:
            continue
        
        with open(file,"r") as fp:
            content = fp.read()
        
        # content = content.replace("int N = 2048;", f"int N = {mat_size};")
        # content.replace("","")
        # content.replace("double A[2048][2048];",f"double A[{mat_size}][{mat_size}];")
        # content.replace("double array1[2048][2048];",f"double array1[{mat_size}][{mat_size}];")
        # content.replace("double array2[2048][2048];",f"double array2[{mat_size}][{mat_size}];")
        content = re.sub(r"int B = [0-9]*;", f"int B = {tile_size};", content)
        # content = content.replace(r"int B = [0-9]*;", f"int B = {pile_size};")
        with open(file, "w") as fp:
            fp.write(content)
        
        print(file)
        version = file.split("/")[-1].split("_")[0]
        print(version)
        os.system(f"gcc -o out2048/{version}_{mat_size}_{tile_size} {file}")

