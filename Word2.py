'''
    Word.py

    단어 클래스

    member : 단어 - wordname
             품사 - wordclass
             뜻 - wordmeaning

             단어 길이 - WORD_LENGTH = 20
             품사 길이 - CLASS_LENGTH = 10
             뜻 길이 - MEANING_LENGTH = 50
             단어수 - count_word
             
    method : 생성자( __init__() )
             단어 읽기( getWordName() )
             품사 읽기( getWordClass() )
             뜻 읽기( getWordMeaning() )
             단어 쓰기( writeWord() )
             단어 내용 읽기( readWord() )
'''
class Word:
    WORD_LENGTH = 20
    CLASS_LENGTH = 10
    MEANING_LENGTH = 50

    count_word = 0

    def __init__( self, wordname = None, wordclass = None, wordmeaning = None ):
        Word.count_word += 1
        
        self.wordname = wordname
        self.wordclass = wordclass
        self.wordmeaning = wordmeaning

    def getWordName( self ):
        return self.wordname

    def getWordClass( self ):
        return self.wordclass

    def getWordMeaning( self ):
        return self.wordmeaning

    def writeWord( self, wordname, wordclass, wordmeaning ):
        self.wordname = wordname
        self.wordclass = wordclass
        self.wordmeaning = wordmeaning

    def readWord( self ):
        return self.wordname, self.wordclass, self.wordmeaning

    def __repr__( self ):
        str =  '단어 : {0:<20} 품사 : {1:<10} 뜻 : {2:<50}'.format( self.wordname, self.wordclass, self.wordmeaning )
        return str

class WordDic:
    MAX = 50
    count_word = 0

    def __init__( self ):
        self.wordDic = {}

    def writeWordDic( self, wordname = None, wordclass = None, wordmeaning = None ):
        self.wordDic[ wordname ] = Word( wordname, wordclass, wordmeaning )
        WordDic.count_word += 1
    
    def readWordDicInfo( self, key ):
        return self.wordDic[ key ].readWordDicInfo()

    def printWordDic( self ):
        return tuple( self.wordDic.values())

def main():
    count = 0

    wordbook = WordDic()
    

    word_name = input( '최대 {0:2}글자의 단어를 입력 ( "end" : quit ) : '.format( Word.WORD_LENGTH ) )
    while len( word_name ) < 1 or len( word_name ) > Word.WORD_LENGTH:
        print( '\nError : 단어의 글자수는 최대 {0:2}글자 단어만 입력하세요...\n'.format( Word.WORD_LENGTH ) )
        word_name = input( '최대 {0:2}글자의 단어를 입력 ( "end" : quit ) : '.format( Word.WORD_LENGTH ) )
        
    while word_name != 'end' and count < WordDic.MAX:
        count = count + 1
        word_class = input( '"{0:<10}" 단어의 최대 {1:10}글자 품사 입력 : '.format( word_name, Word.CLASS_LENGTH ) )
        while len( word_class ) < 1 or len( word_class ) > Word.CLASS_LENGTH:
            print( '\nError : 단어의 글자수는 최대 {0:2}글자 단어만 입력하세요...\n'.format( Word.CLASS_LENGTH ) )
            word_class = input( '"{0:<10}" 단어의 최대 {1:10}글자 품사 입력 : '.format( word_name, Word.CLASS_LENGTH ) )

        word_meaning = input( '"{0:<10}" 단어의 최대 {1:10}글자 뜻 입력 : '.format( word_name, Word.MEANING_LENGTH ) )
        while len( word_meaning ) < 1 or len( word_meaning ) > Word.MEANING_LENGTH:
            print( '\nError : 단어의 글자수는 최대 {0:2}글자 단어만 입력하세요...\n'.format( Word.MEANING_LENGTH ) )
            word_meaning = input( '"{0:<10}" 단어의 최대 {1:10}글자 뜻 입력 : '.format( word_name, Word.MEANING_LENGTH ) )

        wordbook.writeWordDic( word_name, word_class, word_meaning ) 

        word_name = input( '\n최대 {0:2}글자의 단어를 입력 ( "end" : quit ) : '.format( Word.WORD_LENGTH ) )
        while len( word_name ) < 1 or len( word_name ) > Word.WORD_LENGTH:
            print( '\nError : 단어의 글자수는 최대 {0:2}글자 단어만 입력하세요...\n'.format( Word.WORD_LENGTH ) )
            word_name = input( '최대 {0:2}글자의 단어를 입력 ( "end" : quit ) : '.format( Word.WORD_LENGTH ) )

    print()
    print( ''.center( 78, '=' ) )
    print( '단어장'.center( 78, ' ' )  )
    print( ''.center( 78, '=' ) )
    for word in wordbook.printWordDic():
        print( word )

    print( ''.center( 78, '=' ) )
    print( '총 단어수 : {0:5}\n'.format( Word.count_word  ) )

    input( '\nPress any key to program stop...' )

if __name__ == '__main__':
    main()