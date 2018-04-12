# importing requests
import json
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import csv
import glob
import os

def main():
    files = glob.glob("DischargeNotes-05/*.txt")

    conditions = []
    diagnosis = False

    for file in files:
        f = open(file)
        text = f.read().lower()
        lines = text.strip().splitlines();
        for line in lines:
            line = line.strip()
            if diagnosis:
                if line != '' and line != '.':
                    conditions.append(line)
                else:
                    diagnosis = False
            if line == 'discharge diagnosis:':
               diagnosis = True


    
    df_conditions = pd.DataFrame(conditions)
    df_conditions.to_csv('discharge_diagnosis.csv', index=False, header=False)


if __name__ == "__main__":
    main()
