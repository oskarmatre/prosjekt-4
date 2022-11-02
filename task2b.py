import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords
import json

text = "Intelligent behavior in people is a product of the mind. But the mind itself is more like what the human brain does"

def indexer(text):
    stop_words = stopwords.words('english')
    words = {}
    text = text.split(" ")
    i = 1
    for word in text:
        l = len(word) + 1
        word = word.strip("").lower()
        word = word.strip(":',.!?\n")
        if word in words:
            words[word].append(i)
        else:
            words[word] = [i]
        i+=l
    words_without_stopwords = {}

    for key, value in words.items():
        if key not in stop_words:
            words_without_stopwords[key] = value
            
    return words_without_stopwords

for i in range(1,7):
    f = open("./Texts/Text" + str(i) +".txt", "r")
    indexes = indexer(f.read())
    f.close()

    with open("./Texts/Result" + str(i) +".txt", "w") as file:
        json.dump(indexes, file)