import sys
# import argparse
# parser = argparse.ArgumentParser()

# parser.add_argument("")

with open("arguments.txt") as fp:
    l = fp.read().split()

command = "sudo perf stat -x , -e"
for each in l:
    command += f"{each}:u,"

nums_args = len(sys.argv)
out_file = sys.argv[1]

print(len(sys.argv))
# mat_size = sys.argv[2]
# tile_size = sys.argv[3]

write_file = "output/V"

if nums_args >= 2:
    ver = sys.argv[2]
    write_file += f"{ver}"

if nums_args >= 3:
    mat_size = sys.argv[3]
    write_file += f"_{mat_size}"

if nums_args >= 4:
    pile_size = sys.argv[4]
    write_file += f"_{pile_size}"

command = command[:-1] + f" -o {write_file}.csv"
command +=   f' ./{out_file}'

with open("command.sh", "w") as fp:
    fp.write(command)
print(command)