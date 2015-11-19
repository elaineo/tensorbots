import nltk

GARBAGE = [",", "--", "\'s", ".", "``","n\'t","\'\'",")","(","%","!","\'","?","percent",":"]

# semantic tools
def remove_stopwords(document):
    tokens = nltk.word_tokenize(document.decode('utf-8').lower())
    tokens = [t for t in tokens if t not in nltk.corpus.stopwords.words('english')]
    tokens = [t for t in tokens if t not in GARBAGE]
    return " ".join(tokens).encode('ascii', 'ignore')

def tokenize_text(document):
    sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
    sents_all = sent_detector.tokenize(document.decode('utf-8').strip())
    sent_generator = nltk.bigrams(sents_all)
    # sent_generator = nltk.bigrams(sent_detector.tokenize(page.strip()))
    sents = [" ".join(s) for s in sent_generator]
    return sents
