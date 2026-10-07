import pandas as pd

scores = pd.read_csv("scores.csv")
scores["score"] = pd.to_numeric(scores["score"], errors="coerce")
result = scores.groupby("category")["score"].mean().round(2)
print(result)

