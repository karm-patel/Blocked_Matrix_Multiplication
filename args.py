# REQUIRED INPUT FORMAT: v1_2048_32
import sys

with open("arguments.txt") as fp:
    l = fp.read().split()

command = "sudo perf stat -x , -e"
for each in l:
    command += f"{each}:u,"

nums_args = len(sys.argv)
out_file = sys.argv[1]

print(len(sys.argv))

command = command[:-1] + f" -o output/{out_file}.csv"
command +=   f' ./{out_file}'

with open("command.sh", "w") as fp:
    fp.write(command)
print(command)