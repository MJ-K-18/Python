'''
    Python 9일차 실습#1

    1. 50개 이내의 단어, 품사, 뜻을 저장한 단어장을 구성한 후
        단어장을 출력하는 프로그램을 class를 이용하여 작성한다.
        ( 단어가 '0'이면 단어 입력 종료 )
        ( 단어는 최대 20자, 품사는 최대 10자, 뜻은 최대 50자 )
'''

class Wordbook1():
    def __init__( self, word_name = None, word_class = None, word_meaning = None ):
        self.word_name = word_name
        self.word_class = word_class
        self.word_meaning = word_meaning

    def getWord_name( self ):
        return self.word_name 

    def getWord_class( self ):
        return self.word_class

    def getWord_meaning( self ):
        return self.word_meaning
    
    def writeWordbook( self, word_name, word_class, word_meaning ):
        self.word_name = word_name
        self.word_class = word_class
        self.word_meaning = word_meaning

    def readWordbookInfo( self ):
        return self.word_name, self.word_class, self.word_meaning