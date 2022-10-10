from glob import glob
import os
import regex as re

c_files = glob("code2048/*.c")
print(c_files)

piles_8192 = [128]
# for file in c_files:    
#     
if not os.path.isdir("code8192"):
    os.system("mkdir code8192")

if not os.path.isdir("out8192"):
    os.system("mkdir out8192")

mat_size = 8192
for pile_size in piles_8192:
    for file in c_files:
        with open(file,"r") as fp:
            content = fp.read()
        
        content = content.replace("int N = 2048;", f"int N = {mat_size};")
        content = content.replace("double A[2048][2048];",f"double A[{mat_size}][{mat_size}];")
        content = content.replace("double array1[2048][2048];",f"double array1[{mat_size}][{mat_size}];")
        content = content.replace("double array2[2048][2048];",f"double array2[{mat_size}][{mat_size}];")
        content = re.sub(r"int B = [0-9]*;", f"int B = {pile_size};", content)
        
        fname = file.split("/")[-1]
        with open(f"code8192/{fname}", "w") as fp:
            fp.write(content)
        
        version = file.split("/")[-1].split("_")[0]
        # print(version)
        exec_file = f"code8192/{file.split('/')[-1]}"
        print(f"out8192/{version}_{mat_size}_{pile_size}", exec_file)
        os.system(f"gcc -o out8192/{version}_{mat_size}_{pile_size} {exec_file}")

