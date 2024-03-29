import Wordbook1

def main():
    WORD_LENGTH = 20
    CLASS_LENGTH = 10
    MEANING_LENGTH = 50
    MAX = 50
    wordbook = {}
    count = 0

    word_name = input( '최대 {0:2}글자의 단어를 입력 ( "end" : quit ) : '.format( WORD_LENGTH ) )
    while len( word_name ) < 1 or len( word_name ) > WORD_LENGTH:
        print( '\nError : 단어의 글자수는 최대 {0:2}글자 단어만 입력하세요...\n'.format( WORD_LENGTH ) )
        word_name = input( '최대 {0:2}글자의 단어를 입력 ( "end" : quit ) : '.format( WORD_LENGTH ) )
        
    while word_name != 'end' and count < MAX:
        count = count + 1
        word_class = input( '"{0:<10}" 단어의 최대 {1:10}글자 품사 입력 : '.format( word_name, CLASS_LENGTH ) )
        while len( word_class ) < 1 or len( word_class ) > CLASS_LENGTH:
            print( '\nError : 단어의 글자수는 최대 {0:2}글자 단어만 입력하세요...\n'.format( CLASS_LENGTH ) )
            word_class = input( '"{0:<10}" 단어의 최대 {1:10}글자 품사 입력 : '.format( word_name, CLASS_LENGTH ) )

        word_meaning = input( '"{0:<10}" 단어의 최대 {1:10}글자 뜻 입력 : '.format( word_name, MEANING_LENGTH ) )
        while len( word_meaning ) < 1 or len( word_meaning ) > MEANING_LENGTH:
            print( '\nError : 단어의 글자수는 최대 {0:2}글자 단어만 입력하세요...\n'.format( MEANING_LENGTH ) )
            word_meaning = input( '"{0:<10}" 단어의 최대 {1:10}글자 뜻 입력 : '.format( word_name, MEANING_LENGTH ) )


        word = Wordbook1.Wordbook1( word_name, word_class, word_meaning )

        wordbook[ word_name ] = word    
    
        word_name = input( '\n최대 {0:2}글자의 단어를 입력 ( "end" : quit ) : '.format( WORD_LENGTH ) )
        while len( word_name ) < 1 or len( word_name ) > WORD_LENGTH:
            print( '\nError : 단어의 글자수는 최대 {0:2}글자 단어만 입력하세요...\n'.format( WORD_LENGTH ) )
            word_name = input( '최대 {0:2}글자의 단어를 입력 ( "end" : quit ) : '.format( WORD_LENGTH ) )
    #keys = list(wordbook.keys())
    #for word_name in keys:
        #print( '단어 : {0:5} 품사 : {1:5} 명사 : {2:5}'.format( Wordbook1.Wordbook1[ word_name ][0], Wordbook1.Wordbook1[ word_name ][1], Wordbook1.Wordbook1[ word_name ][2] ))
    for v in wordbook:
        print( '단어 : {0:5} 품사 : {1:5} 명사 : {2:5}'.format( wordbook[ v ].getWord_name(), wordbook[ v ].getWord_class(), wordbook[ v ].getWord_meaning() ))

if __name__ == '__main__':
    main()