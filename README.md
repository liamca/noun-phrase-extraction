# Noun Phrase Extraction of Text (Key Phrase Extraction)

This code will extract all of the single word nouns along with any noun phrases that can be found. It is based primarily on Spacy and NLTK libraries.

## Extract Noun Phrase split by Sentences
```
import npe
text = """
The quick brown fox jumped over the lazy dog. This is a second sentence with the phrase Azure Cognitive Search.
"""
npe.noun_phrase_by_sentence(text)
```

Output:

```
[['quick_brown_fox', 'brown', 'lazy', 'fox', 'lazy_dog', 'dog', 'quick'],
 ['second',
  'phrase',
  'sentence',
  'azure_cognitive_search',
  'second_sentence',
  'azure',
  'cognitive',
  'search']]
```

## Extract Noun Phrase split by Passage
```
import npe
text = """
The quick brown fox jumped over the lazy dog. This is a second sentence with the phrase Azure Cognitive Search.
"""
noun_phrase_by_passage(text)
```

Output:

```
[['second',
  'phrase',
  'quick_brown_fox',
  'brown',
  'sentence',
  'azure_cognitive_search',
  'lazy',
  'fox',
  'quick',
  'lazy_dog',
  'second_sentence',
  'dog',
  'azure',
  'cognitive',
  'search']]
```

