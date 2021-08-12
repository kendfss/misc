import csv 
import json 
import pandas as pd
import glob

csv_file = pd.DataFrame(
    pd.read_csv(
        "raw_data/playlist_tracks/playlist_track_4.csv",
        header=0,
        index_col=False
    )
)

csv_file.to_json(
    "processedfile/playlist_tracksjson/playlist_track_4.json",
    orient = "records",
    double_precision=0,
    lines=True
)


result = ''
for f in glob.glob("*.json"):
    with open(f, "r") as infile:
        result += infile.read()
    with open("merged_file.json.gz", "w") as outfile:
        outfile.writelines(result)
