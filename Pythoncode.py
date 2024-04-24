import sys
import subprocess
# install nltk, pandas, matplotlib using pip
subprocess.check_call([sys.executable, "-m", "pip", "install", "matplotlib",'pandas','nltk'])
import nltk
import matplotlib.pyplot as plt
import pandas as pd
from nltk.corpus import stopwords
from collections import Counter
# download stopwords
nltk.download("stopwords")
# read file
data=open('paragraphs.txt')
new_data=data.read()
new_data


# get english stopwords
stop_words = set(stopwords.words("english"))
cleaning_data = new_data.replace(",", "").replace(".", "").replace('(',"").replace('[',"").replace('-','').replace(';','').strip()
cleaning_data
words = cleaning_data.split()
# Remove stopwords 
cleaning_words = [word for word in words if word.lower() not in stop_words]
# Count of each word
word_counts = Counter(cleaning_words)
# Print the most common words
print("Most Common Words:")
for word, count in word_counts.most_common():
    print(word, ": ", count)
# Get the top 20 most common words
top_words = word_counts.most_common(20)
labels, values = zip(*top_words)

# Plot 
plt.figure(figsize=(8,8))
plt.bar(labels, values, color='purple',edgecolor='black')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title('Top 20 Words')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()