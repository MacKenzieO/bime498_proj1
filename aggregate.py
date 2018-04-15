import pandas as pd
import numpy as np

def main():
    conditions = pd.read_csv("final.csv")
    conditions = conditions.apply(lambda x: x.astype(str).str.lower())
    conditions = conditions.sort_values("diagnosis")
    counts = conditions.diagnosis.value_counts()
    counts.to_csv('counts.csv')

    squarify.plot(sizes=counts, alpha=.8 )
	plt.axis('off')
	plt.show()


if __name__ == "__main__":
    main()
