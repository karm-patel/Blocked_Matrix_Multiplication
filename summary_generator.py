import pandas as pd
import glob

def summaryGenerator():
    path = r'./csv/'
    all_files = glob.glob(path + "/*.csv")
    if(len(all_files)==0):
        print("There is no csv trace found at ./csv/.........\n")
        return
    summ = list()
    for filename in all_files:
        version, matrix_size, tile_size = filename.split('_')
        version = version.split('/')[-1]
        tile_size = tile_size.split('.')[0]
        # print(filename)
        try:
            df = pd.read_csv(filename)
        except:
            print(filename)
            continue
        df.columns = [''] * len(df.columns)
        # print(df)
        data = dict()
        data["version"] = version
        data["matrix_size"] = matrix_size
        data["tile_size"] = tile_size
        for index, row in df.iterrows():
            data[row[0]] = row[1]
        data["page_fault"] = 0
        summ.append(data)

    df = pd.DataFrame.from_dict(summ)
    df.to_csv("summary.csv")

