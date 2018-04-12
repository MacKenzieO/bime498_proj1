# importing requests
import json
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import csv
import glob
import os
import re 

def main():
	df = pd.read_csv("discharge_diagnosis.csv")
	size = len(df.index)

	for x in range(0, size): 
		temp = df.iat[x, 0]
		temp = re.sub(r'[0-9]', '', temp)
		temp = re.sub(r'\.', '', temp)
		temp = re.sub(r'\[.*\]', '', temp)
		temp = re.sub(r'\A\s*', '', temp)
		temp = re.sub(r'primary:', '', temp)
		temp = re.sub(r'secondary:', '', temp)
		df.iat[x,0] = temp

	df.to_csv('discharge_diagnosis_CLEAN.csv', index=False, header=False)

if __name__ == "__main__":
	main()