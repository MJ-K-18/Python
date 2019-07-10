
def Insert_word( ):
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


        word = ( word_name, word_class, word_meaning )

        wordbook[ word_name ] = word    
    
        word_name = input( '\n최대 {0:2}글자의 단어를 입력 ( "end" : quit ) : '.format( WORD_LENGTH ) )
        while len( word_name ) < 1 or len( word_name ) > WORD_LENGTH:
            print( '\nError : 단어의 글자수는 최대 {0:2}글자 단어만 입력하세요...\n'.format( WORD_LENGTH ) )
            word_name = input( '최대 {0:2}글자의 단어를 입력 ( "end" : quit ) : '.format( WORD_LENGTH ) )
    return 


def Search_word( ):
    search_word_name = input( '\n최대 {0:2}글자의 검색할 단어를 입력 ( "end" : quit ) : '.format( WORD_LENGTH ) )
    while len( search_word_name ) < 1 or len( search_word_name ) > WORD_LENGTH:
        print( '\nError : 단어의 글자수는 최대 {0:2}글자 단어만 입력하세요...\n'.format( WORD_LENGTH ) )
        word_name = input( '최대 {0:2}글자의 단어를 입력 ( "end" : quit ) : '.format( WORD_LENGTH ) )

    while search_word_name != 'end':
        search_result = wordbook.get( search_word_name, () )

        if search_result:
            print( '\n{0:<10} ( {1:<5} ) : {2:<20}'.format( search_result[ 0 ],
                                                        search_result[ 1 ],
                                                        search_result[ 2 ]))
        else:
            print( '\n{0:<10} 단어는 등록되어 있지 않습니다...ㅠㅠ'.format( search_word_name ) )

        search_word_name = input( '\n최대 {0:2}글자의 검색할 단어를 입력 ( "end" : quit ) : '.format( WORD_LENGTH ) )
        while len( search_word_name ) < 1 or len( search_word_name ) > WORD_LENGTH:
            print( '\nError : 단어의 글자수는 최대 {0:2}글자 단어만 입력하세요...\n'.format( WORD_LENGTH ) )
            word_name = input( '최대 {0:2}글자의 단어를 입력 ( "end" : quit ) : '.format( WORD_LENGTH ) )

    return 


MAX = 50
WORD_LENGTH = 10
CLASS_LENGTH = 5
MEANING_LENGTH = 20

wordbook = {}

Insert_word( )
Search_word( )