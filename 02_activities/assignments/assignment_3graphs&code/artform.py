import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "C:/Users/frach/Downloads/visualization/02_activities/assignments/assignment_3graphs&code/Public Art - 4326.csv"
art_df = pd.read_csv(file_path)

print(art_df.head())

art_form_counts = art_df['ArtForm'].value_counts()

plt.figure(figsize=(12, 6))
sns.barplot(x=art_form_counts.index, y=art_form_counts.values, palette="viridis")
plt.xticks(rotation=45)
plt.xlabel("Art Form")
plt.ylabel("Number of Artworks")
plt.title("Number of Public Artworks by Art Form")
plt.show()

installations_per_year = art_df['YEAR_INSTALLED'].value_counts().sort_index()

time_series_file = "C:/Users/frach/Downloads/visualization/02_activities/assignments/assignment_3graphs&code/installations_per_year.csv"
installations_per_year.to_csv(time_series_file, header=["Number of Artworks"])

time_series_file