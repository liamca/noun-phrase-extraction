# Noun Phrase Extraction of Text (Key Phrase Extraction)

```
import npe
text = """
The quick brown fox jumped over the lazy dog. This is a second sentence.
"""
npe.extract_noun_phrases(text)
```

Output:

```
[['lazy', 'fox', 'jumped', 'brown_fox', 'quick', 'dog', 'brown'],
 ['sentence', 'second']]```
```

