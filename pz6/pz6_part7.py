# -*- coding: utf-8 -*-
# Прочитайте статью и выполните действия, которые в ней прописаны
# https://pythonist.ru/vvedenie-v-mnozhestvennoe-nasledovanie-i-super/

class Tokenizer:
    """Tokenize text"""
    def __init__(self, text):
        print('Start Tokenizer.__init__()')
        self.tokens = text.split()
        print('End Tokenizer.__init__()')


class WordCounter(Tokenizer):
    """Count words in text"""
    def __init__(self, text):
        print('Start WordCounter.__init__()')
        super().__init__(text)
        self.word_count = len(self.tokens)
        print('End WordCounter.__init__()')


class Vocabulary(Tokenizer):
    """Find unique words in text"""
    def __init__(self, text):
        print('Start init Vocabulary.__init__()')
        super().__init__(text)
        self.vocab = set(self.tokens)
        print('End init Vocabulary.__init__()')


class TextDescriber(WordCounter, Vocabulary):
    """Describe text with multiple metrics"""
    def __init__(self, text):
        print('Start init TextDescriber.__init__()')
        super().__init__(text)
        print('End init TextDescriber.__init__()')


td = TextDescriber('row row row your boat')
print('--------')
print(td.tokens)
print(td.vocab)
print(td.word_count)

print('--------class a1')
class a1:
    """Tokenize text"""
    def __init__(self, text):
        print('Start a1')
        self.tokens = text.split()
        print('End a1')


class b1(a1):
    """Count words in text"""
    def __init__(self, text):
        print('Start b1')
        super().__init__(text)
        self.word_count = len(self.tokens)
        print('End b1')


class b2(a1):
    """Find unique words in text"""
    def __init__(self, text):
        print('Start b2')
        super().__init__(text)
        self.vocab = set(self.tokens)
        print('End b2')


class c1(b1, b2):
    """Describe text with multiple metrics"""
    def __init__(self, text):
        print('Start c1')
        super().__init__(text)
        print('End c1')

test1 = c1('row row row your boat')
print('--------')
print(test1.tokens)
print(test1.vocab)
print(test1.word_count)