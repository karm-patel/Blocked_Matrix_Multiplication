from glob import glob
import os
import regex as re


tiles_8192 = [4,8,16,512]
# for file in c_files:    
#     
if not os.path.isdir("code8192"):
    os.system("mkdir code8192")

    tiles_8192 = [8,16,32,64,128]

mat_size = 8192
for tile_size in tiles_8192:
    for file in c_files:
        with open(file,"r") as fp:
            content = fp.read()
        
        content = content.replace("int N = 2048;", f"int N = {mat_size};")
        content = content.replace("float A[2048][2048];",f"float A[{mat_size}][{mat_size}];")
        content = content.replace("int array1[2048][2048];",f"int array1[{mat_size}][{mat_size}];")
        content = content.replace("int array2[2048][2048];",f"int array2[{mat_size}][{mat_size}];")
        content = re.sub(r"int B = [0-9]*;", f"int B = {tile_size};", content)
        
        fname = file.split("/")[-1]
        with open(f"code8192/{fname}", "w") as fp:
            fp.write(content)
        
        version = file.split("/")[-1].split("_")[0]

        # print(version)
        exec_file = f"code8192/{file.split('/')[-1]}"
        print(f"out8192/{version}_{mat_size}_{tile_size}", exec_file)
        print(exec_file)
        os.system(f"gcc -g -o out8192/{version}_{mat_size}_{tile_size} {exec_file}")

