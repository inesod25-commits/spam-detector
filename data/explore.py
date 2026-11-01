import pandas as pd

df = pd.read_csv("data/SMSSpamCollection", sep="\t", header=None, names=["label", "text"])

print("Taille :", df.shape)
print()
print(df.head())
print()
print(df["label"].value_counts())
print()
print("Longueur moyenne des messages :")
print(df["text"].str.len().groupby(df["label"]).mean())
print()
print("Exemples de spam :")
print(df[df["label"] == "spam"]["text"].head(5).to_string())