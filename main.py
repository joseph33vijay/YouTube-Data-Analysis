import pandas as pd

print("Loading Dataset...")

df = pd.read_csv("INvideos.csv", encoding="utf-8", low_memory=False)

print("Loaded Successfully")
print("Shape:", df.shape)

print("\nColumns:")
print(df.columns)

print("\nFirst 5 rows loaded succesfully")

print("\nChecking Missing Values:")
print(df.isnull().sum())

print("\nRemoving Duplicates...")
df = df.drop_duplicates()
print("New Shape After Removing Duplicates:", df.shape)

import json

# Load category JSON
with open("IN_category_id.json") as f:
    categories = json.load(f)

# Create dictionary: id → title
category_dict = {}

for item in categories["items"]:
    category_dict[int(item["id"])] = item["snippet"]["title"]

# Convert category_id to numeric
df["category_id"] = pd.to_numeric(df["category_id"], errors="coerce")

# Map category names
df["category_name"] = df["category_id"].map(category_dict)

print("\nCategory Mapping Successful ")
print(df[["category_id", "category_name"]].head())

# Convert numeric columns properly
df['views'] = pd.to_numeric(df['views'], errors='coerce')
df['likes'] = pd.to_numeric(df['likes'], errors='coerce')
df['dislikes'] = pd.to_numeric(df['dislikes'], errors='coerce')
df['comment_count'] = pd.to_numeric(df['comment_count'], errors='coerce')

print("\nTotal Videos:", len(df))

print("\nMost Viewed Video:")
most_viewed = df.loc[df['views'].idxmax()]
print("Title:", most_viewed['title'])
print("Views:", most_viewed['views'])

print("\nAverage Likes:", df['likes'].mean())

print("\nTop 5 Categories by Total Views:")
top_categories = df.groupby('category_id')['views'].sum().sort_values(ascending=False).head()
print(top_categories)

import matplotlib.pyplot as plt

top_categories = df.groupby("category_name")["views"].sum().sort_values(ascending=False).head(5)

print("\nTop 5 Categories by Total Views:")
print(top_categories)

plt.figure(figsize=(8,5))
top_categories.plot(kind="bar")

plt.title("Top 5 Categories by Total Views")
plt.xlabel("Category Name")
plt.ylabel("Total Views")

plt.xticks(rotation=30)
plt.tight_layout()
plt.show()