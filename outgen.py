from glob import glob
import os
import regex as re

c_files = glob("code/*.c")
print(c_files)

piles_2048 = [8,16,32,64,128]
piles_8192 = [32,64]
# for file in c_files:    
#     

mat_size = 2048
for pile_size in piles_2048:
    for file in c_files:
        with open(file,"r") as fp:
            content = fp.read()
        
        # content = content.replace("int N = 2048;", f"int N = {mat_size};")
        # content.replace("","")
        # content.replace("double A[2048][2048];",f"double A[{mat_size}][{mat_size}];")
        # content.replace("double array1[2048][2048];",f"double array1[{mat_size}][{mat_size}];")
        # content.replace("double array2[2048][2048];",f"double array2[{mat_size}][{mat_size}];")
        content = re.sub(r"int B = [0-9]*;", f"int B = {pile_size};", content)
        # content = content.replace(r"int B = [0-9]*;", f"int B = {pile_size};")
        with open(file, "w") as fp:
            fp.write(content)
        
        version = file.split("/")[-1].split("_")[0]
        print(version)
        os.system(f"gcc -o out/v{version}_{mat_size}_{pile_size} {file}")

