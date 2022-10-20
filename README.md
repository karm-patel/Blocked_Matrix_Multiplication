## What this repo contains

In this repo, we have analyzed 96 various versions of the blocked matrix multiplication programs on combinations of following factors.
1. Matrix size: 2048, 8192
2. Outer loop order (variants): ‘ijk’, ‘jik’, ‘jki’, ‘ikj’, ‘kij’, ‘kji’
3. Tile size: 4, 8, 16, 32, 64, 128, 256, 512

Analysis contains various performance counters including but not limited to cache-misses, TLB misses, cpu cycles, branch instructions, etc. We use perforator CLI tool for analysis.

### Analysis Summary
![image](https://user-images.githubusercontent.com/59387624/196910151-276b9615-5f6d-4ef3-9486-8ee5df1f5598.png)
![image](https://user-images.githubusercontent.com/59387624/196910286-791060e7-397a-4c09-bfc9-111da1b98b02.png)
![image](https://user-images.githubusercontent.com/59387624/196910349-919b21f1-1966-49b4-99f0-060f952f96ee.png)
![image](https://user-images.githubusercontent.com/59387624/196910403-a131ffa7-646c-4bee-bcdf-9d8bf4c7d646.png)


## How to use this code?
## Perforater installation 
```bash
curl https://zyedidia.github.io/eget.sh | sh ./eget zyedidia/perforator
```
```bash
pip3 install regex pandas
```

### DELETE FOLLOWING DIRECTORIES
out2048/ </br>
out8192/ </br>
csv/ </br>

### RUN FOLLOWING PYTHON FILES IN SEQUENCE

1.  genereate .out files in out2048/
```bash
python3 outgen2048.py
```

2. generate csv files in csv/
```bash
python3 execout2048.py
```

3. genereate .out files in out2048/
```bash
python3 outgen8192.py
```

4. generate csv files in csv/
```bash
python3 execout8192.py
```

### FOLLOWING COMMAND IS BEING EXECUTED

```bash
sudo ./perforator -e cpu-cycles,branch-misses,branch-instructions,cache-misses,dtlb-read-accesses,dtlb-read-accesses,dtlb-read-misses,dtlb-write-misses,l1d-read-accesses,l1d-read-misses,l1d-write-accesses,l1i-read-misses,ll-read-accesses,ll-read-misses,ll-write-accesses,ll-write-misses -r multiplication --csv ./out2048/v3_2048_32 > csv/v3_2048_32.csv
```
