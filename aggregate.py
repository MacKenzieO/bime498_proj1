import pandas as pd

def main():
    conditions = pd.read_csv("final.csv")
    conditions = conditions.sort_values("diagnosis")
# 
#counts = conditions.value_counts()

if __name__ == "__main__":
    main()
