import json
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import joblib

# train
train_df = pd.read_csv("transactions_labeled.csv")
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1, 2), min_df=1)),
    ("clf", LogisticRegression(max_iter=1000)),
])

# fit
pipeline.fit(train_df["description"], train_df["category"])
with open("db.json") as f:
    real_data = json.load(f)["transactions"]

real_df = pd.DataFrame(real_data.values())
real_df = real_df.rename(columns={"note": "description"})

preds = pipeline.predict(real_df["description"])
print(classification_report(real_df["category"], preds))

joblib.dump(pipeline, "categorizer_model.pkl")



# fit
pipeline.fit(train_df["description"], train_df["type"])
with open("db.json") as f:
    real_data = json.load(f)["transactions"]

real_df = pd.DataFrame(real_data.values())
real_df = real_df.rename(columns={"note": "description"})

preds = pipeline.predict(real_df["description"])
print(classification_report(real_df["type"], preds))

joblib.dump(pipeline, "type_model.pkl")


mismatches = real_df[preds != real_df["type"]]
print(mismatches[["description", "type"]])
print("predicted:", preds[preds != real_df["type"]])