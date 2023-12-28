# solving the 4 kyu Vigenere Cipher Helper kata
class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alph = alphabet
    
    def encode(self, text):
        return self._doWork(text, 'e')
    
    def decode(self, text):
        return self._doWork(text, 'd')
        
    def _doWork(self, text, mode):
        new_key = self.key * len(text)
        ret = ''
        
        for i in range(len(text)):
            key_index = self.alph.find(new_key[i])
            text_index = self.alph.find(text[i])
            
            if text_index == -1:
                ret += text[i]
                continue
                
            if mode == 'e':
                ret += self.alph[(text_index + key_index) % len(self.alph)]
            elif mode == 'd':
                ret += self.alph[(text_index - key_index) % len(self.alph)]
        
        return ret
