from bs4 import BeautifulSoup
import urllib.request
import nltk
from nltk.corpus import stopwords

# Stopwords package
nltk.download('stopwords')

# Web crawling
response = urllib.request.urlopen('https://www.nobelprize.org/prizes/literature/1990/paz/25350-octavio-paz-nobel-lecture-1990/')
html = response.read()

# Clean text
soup = BeautifulSoup(html, "html5lib")
text = soup.get_text(strip=True)

# Tokenize / Splitting text 
tokens = [t for t in text.split()]

# Remove stopwords
clean_tokens = tokens[:]
sr = stopwords.words('spanish')
for token in tokens:
    if token in stopwords.words('spanish'):
        clean_tokens.remove(token)

# Count word frequency
freq = nltk.FreqDist(tokens)
for key,val in freq.items():
    print(str(key) + ':' + str(val))

# Plot
freq.plot(20, cumulative=False)