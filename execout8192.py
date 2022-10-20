from glob import glob
import os
import time

def executeOutFiles8192():
    if not os.path.isdir("csv8192"):
        os.system("mkdir csv8192")

    out_files = glob("out8192/*")
    for ind, file in enumerate(out_files):
        print(f"execuing... {file}")
        # command = f"sudo perf stat -x , -e cpu-clock:u,cycles:u,instructions:u,L1-dcache-load-misses:u,LLC-load-misses:u,LLC-store-misses:u,dTLB-load-misses:u,dTLB-store-misses:u,l2_rqsts.all_demand_miss:u,page-faults:u,context-switches:u -o csv/{file}.csv ./{file}"
        command = f"echo peng1998 | sudo -S ./perforator -e instructions,cpu-cycles,branch-misses,branch-instructions,cache-references,cache-misses,dtlb-read-accesses,dtlb-read-misses,dtlb-write-misses,dtlb-write-accesses,l1d-read-accesses,l1d-read-misses,l1d-write-accesses,ll-read-accesses,ll-read-misses,ll-write-accesses,ll-write-misses -r multiplication --csv ./{file} > csv8192/{file.split('/')[-1]}.csv"
        seconds = time.time()
        os.system(command)
        print(f"{(time.time() - seconds)/60} mins")