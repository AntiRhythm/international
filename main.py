import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import keybert
from keybert import KeyBERT
from CSESearch import CSESearch
from MaxURL import TopFiveCommon
kw_model = KeyBERT()


def filter_stopwords(text: str) -> str:
    text = text.lower()
    word_tokens = word_tokenize(example_sent)
    filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]

    filtered_sentence = []

    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)
    return filtered_sentence

def find_frequency(input: list):
    dictionary = {}
    for word in input:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    return dictionary


stop_words = set(stopwords.words('english'))
stop_words_array = [",", ".", "ok", ".", "introduction", "textbook", "lecture", "lectures", "textbooks", "courses", "lectures of"]
for i in stop_words_array:
    stop_words.add(i)


with open("transcript.txt") as f:
    transcript = f.read()
example_sent = transcript.lower()
to_sort = find_frequency(filter_stopwords(example_sent))
keywords = kw_model.extract_keywords(example_sent)
words = kw_model.extract_keywords(example_sent, keyphrase_ngram_range=(1, 3), stop_words=None)

searchquotes = []
for i in words:
    searchquotes.append(i[0])
    print(i[0])
language = "en"

urls = CSESearch(searchquotes, language)
URLOutput = TopFiveCommon(urls)


print(URLOutput)
