import pandas as pd
import matplotlib.pyplot as plt

"""
#Задача1
# Load the dataset
df = pd.read_csv('GAMES.csv', delimiter=';', header=None, names=['Name', 'Genre', 'Link', 'Year'])

# Extract the year information
df['Year'] = pd.to_numeric(df['Year'], errors='coerce')

# Create a histogram of the number of games released per year
df['Year'].hist(bins=range(1980, 2001, 1), figsize=(10,5))
plt.title('Number of games released per year')
plt.xlabel('Year')
plt.ylabel('Number of games')
plt.show()
"""

#Задача 2
import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
games = pd.read_csv("GAMES.csv", sep=";", header=None, names=["Title", "Genre", "URL", "Year"])

# Convert the "Year" column to numeric type
games["Year"] = pd.to_numeric(games["Year"], errors="coerce")

# Filter out games with missing years
games = games.dropna(subset=["Year"])

# Group the games by year and genre, and count the number of games in each group
counts = games.groupby(["Year", "Genre"]).size().reset_index(name="Count")

# Pivot the counts table so that the rows are years and the columns are genres
pivot = counts.pivot(index="Year", columns="Genre", values="Count")

# Create a stacked bar chart showing the counts for each genre for each year
pivot.plot(kind="bar", stacked=True, figsize=(30, 10))

# Add labels and a title to the chart
plt.xlabel("Year")
plt.ylabel("Number of Games")
plt.title("Genres of Old Computer Games")
plt.legend(title="Genre", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.show()
