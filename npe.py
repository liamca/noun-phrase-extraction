import string
from nltk import word_tokenize, pos_tag, ne_chunk, sent_tokenize
from nltk import RegexpParser, Tree
from nltk.stem import WordNetLemmatizer  
from nltk.corpus import stopwords

# Defining a grammar & Parser
# This one seems to be quite good for medical content
# NP = "NP: {<NN.?>+<DT.?>+|<JJ.?>*<NN.?>+<IN.?|DT.?|JJ.?|NN.?>+<NN.?>{1}|<NN.?>+|<JJ.?>+<NN.?>+}"
# This one is for continuous nouns
NP = "NP: {<NN.?>+}"
# This one is for continuous nouns preceded by an adjective
# NP = "NP: {<JJ.?|NN.?>+}"

lemmatizer = WordNetLemmatizer()
stop = set(stopwords.words('english') + list(string.punctuation))
chunker = RegexpParser(NP)

must_contain_alphe = True
min_term_len = 3

def extract_noun_phrases(text):
    tokenized_content = []

    sentences = []
    for s in sent_tokenize(text):
        for ss in s.split('\n'):
            for sss in ss.split('     '):
                if len(sss.strip()) > 0:
                    sentences.append(sss.strip())


    for sentence in sentences:
        # print (sentence)
        tokenized = word_tokenize(sentence.lower())
        sent_stop = [i for i in  tokenized if i not in stop]
        # print ('sent_stop', sent_stop)
        cleaned_sent_stop = []
        for ss in sent_stop:
            if len(ss) >= min_term_len and any(c.isalpha() for c in ss):
                cleaned_sent_stop.append(ss)

        # print ('cleaned_sent_stop', cleaned_sent_stop)
        lemmatized = []
        if len(cleaned_sent_stop) > 0:
            lemmatized=[lemmatizer.lemmatize(word) for word in cleaned_sent_stop]
        # print ('lemmatized', lemmatized)
        continuous_chunk = []
        current_chunk = []
        if len(cleaned_sent_stop) > 0:
            chunked = chunker.parse(pos_tag(cleaned_sent_stop))
            for subtree in chunked:
                if type(subtree) == Tree:
                    for token, pos in subtree:
                        if token.isalnum() and len(token) > 1:
                            # print (token)
                            lemma_token = lemmatizer.lemmatize(token)
                            current_chunk.append(lemma_token)
                            # print (lemma_token)

                    if len(current_chunk) > 0:
                        continuous_chunk.append("_".join(current_chunk))
                        current_chunk = []

        # Remove the chnunks that are already in sentence
        continuous_chunk_cleaned = []
        for chunk in continuous_chunk:
            if chunk not in lemmatized:
                continuous_chunk_cleaned.append(chunk)
        continuous_chunk_cleaned = lemmatized + continuous_chunk_cleaned
        tokenized_content.append(list(set(continuous_chunk_cleaned)))            

    return tokenized_content
