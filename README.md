# Noun Phrase Extraction of Text (Key Phrase Extraction)

This code will extract all of the single word nouns along with any noun phrases that can be found. 
These words and phrases are lemmatized and any stop words are removed.

It is based primarily on Spacy and NLTK libraries.

## Extract Noun Phrase split by Sentence
```
import npe
text = "The quick brown foxes jumped over the lazy dogs. This is a second sentence with the phrase Azure Cognitive Search. "
npe.noun_phrase_by_sentence(text)
```

Output:

```
[['dog', 'fox', 'quick', 'quick_brown_fox', 'brown', 'lazy', 'lazy_dog'],
 ['azure_cognitive_search',
  'search',
  'azure',
  'second',
  'cognitive',
  'phrase',
  'sentence',
  'second_sentence']]
```

## Extract Noun Phrase split by Passage
```
import npe
text = "The quick brown foxes jumped over the lazy dogs. This is a second sentence with the phrase Azure Cognitive Search. "
npe.noun_phrase_by_passage(text)
```

Output:

```
[['second',
  'quick_brown_fox',
  'lazy_dog',
  'lazy',
  'second_sentence',
  'azure_cognitive_search',
  'sentence',
  'dog',
  'brown',
  'quick',
  'azure',
  'cognitive',
  'fox',
  'search',
  'phrase']]
```

