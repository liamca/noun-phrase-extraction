# !python -m spacy download en_core_web_sm
import string
import spacy
nlp = spacy.load("en_core_web_sm")
from nltk.stem import WordNetLemmatizer  
from nltk.corpus import stopwords
from nltk import word_tokenize, sent_tokenize
lemmatizer = WordNetLemmatizer()
stop = set(stopwords.words('english') + list(string.punctuation))

must_contain_alphe = True
min_term_len = 3

def noun_phrase_by_sentence(text):
    tokenized_content = []

    sentences = []
    for s in sent_tokenize(text):
        for ss in s.split('\n'):
            for sss in ss.split('     '):
                if len(sss.strip()) > 0:
                    sentences.append(sss.strip())


    np_list = []
    for sentence in sentences:
        np_sentence_list = []
        doc = nlp(sentence)
        for noun_chunk in doc.noun_chunks:
            sent_stop = [i for i in word_tokenize(noun_chunk.text.lower()) if i not in stop]
            # print ('sent_stop', sent_stop)
            cleaned_sent_stop = []
            for ss in sent_stop:
                if len(ss) >= min_term_len and any(c.isalpha() for c in ss):
                    cleaned_sent_stop.append(ss)

            # print ('cleaned_sent_stop', cleaned_sent_stop)
            lemmatized = []
            if len(cleaned_sent_stop) > 0:
                lemmatized=[lemmatizer.lemmatize(word) for word in cleaned_sent_stop]

            if len(lemmatized) > 0:
                # print ('lemmatized', lemmatized)
                for n in lemmatized:
                    np_sentence_list.append(n)
                np_sentence_list.append("_".join(lemmatized))

        if len(np_sentence_list) > 0:
            np_list.append(list(set(np_sentence_list)))
            # print('np_sentence_list', np_sentence_list)
    return np_list
