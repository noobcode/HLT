import os
import pandas as pd

FILE_PATH = os.path.dirname(os.path.realpath(__file__)) #this file's path
ROOT_DIR = os.path.dirname(FILE_PATH) #Project root dir - '.../HLT'

print(ROOT_DIR)

raw_data = [["d519.s3", "this text contains drugs", "d519.s3.e0", "29-36", "brand", "plenaxis"],
            ["d519.s3", "this text contains drugs", "d519.s3.e1", "83-94", "drug", "testosterone"]]

# TODO maybe split field "offset" in "start" and "end" if it is easier to access later
columns = ["sentenceID", "sentenceText", "entityID", "offset", "type", "drugName"]
df = pd.DataFrame(data=raw_data, columns=columns)
print df
