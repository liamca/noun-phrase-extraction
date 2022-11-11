# Noun Phrase Extraction of Text (Key Phrase Extraction)

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

