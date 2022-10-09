from glob import glob
import os
import regex as re

out_files = glob("out2048/*")
for file in out_files:
    print(f"execuing... {file}")
    # command = f"sudo perf stat -x , -e cpu-clock:u,cycles:u,instructions:u,L1-dcache-load-misses:u,LLC-load-misses:u,LLC-store-misses:u,dTLB-load-misses:u,dTLB-store-misses:u,l2_rqsts.all_demand_miss:u,page-faults:u,context-switches:u -o csv/{file}.csv ./{file}"
    command = f"sudo ./perforator -e cpu-clock,cpu-cycles,dtlb-read-accesses,dtlb-read-accesses,dtlb-read-misses,dtlb-write-misses,l1d-read-accesses,l1d-read-misses,l1d-write-accesses,l1i-read-misses,ll-read-accesses,ll-read-misses,ll-write-accesses,ll-write-misses -r multiplication --csv ./{file} > csv/{file.split('/')[-1]}.csv"
    os.system(command)
    break