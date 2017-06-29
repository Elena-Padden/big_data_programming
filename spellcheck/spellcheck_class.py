class SpellChecker:

    def load_words(self, file_name):
        words = open(file_name).readlines()
        words = map(lambda x: x.strip(), words)
        return words

    def check_word(self, words, word):
        return word in words
    
    def check_words(self, words, sentence):
        words_to_check = sentence.split(' ')
        for word in words_to_check:
            if not self.check_word(words, word):
                print ('Word is misspelt: ' + word)
                return False
        return True
        
spell_check = SpellChecker()
words = spell_check.load_words('spell.words')
print words[0]   
print spell_check.check_word(words, 'zygotic')
print spell_check.check_word(words, 'mistasdas')
print spell_check.check_words(words, 'zygotic mistasdas elelmentary')
