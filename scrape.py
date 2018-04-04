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

    for file in files:
        f = open(file)
        text = f.read()

        if 'Discharge Diagnosis:' in text: 
            a, b = text.split("Discharge Diagnosis:", 1)
            c, d = b.split("Discharge Condition:", 1)

            if c:
                conditions.append(c)


    df_conditions = pd.DataFrame(conditions)
    df_conditions.to_csv('discharge_diagnosis.csv', index=False, header=False)

        

if __name__ == "__main__":
    main()