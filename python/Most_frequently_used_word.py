# solving the 4 kyu most frequently used word in a text kata
import re

def top_3_words(text):
    text = text.lower().strip()
    text = re.split('[/\\?\-\!:;,_\.\\n\s]', text)
    ex_chars = ["''", "'''", '']
    
    counter = {i:text.count(i) for i in text}
    for char in ex_chars:
        if char in counter:
            del counter[char]
    if counter.get("'") is not None:
        del counter["'"]    
    counter = dict(sorted(counter.items(), key=lambda x: x[1], reverse=True))
    return [*counter][:3] if len(counter) >= 3 else [*counter][:len(counter)]
