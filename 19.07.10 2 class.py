'''
    최대 50명 사람의 이름, 전화번호, 이메일 정보를 기록하는 전화번호부를
    컴퓨터로 관리하고자 한다.

    개인 정보 : member - 이름(name), 전화번호(tel), 이메일(email)
    (person)   method - 이름을 기록한다 - setName()
                        이름을 읽는다 - getName()
                        전화번호를 기록한다 - setTel()
                        전화번호를 읽는다 - getTel()
                        이메일을 기록한다 - setEmail()
                        이메일을 읽는다 - getEmail()
                        개인정보를 기록한다 - writePersonInfo()
                        개인정보를 읽는다 - readPersonInfo()
'''
# class를 이용한 사용자 정의 자료형 생성

import Person


def main():
    MAX = 50
    count = 0
    telephone_book = []
    name = input( '이름입력 "end" : quit ) : ')
    while name != 'end' and count < MAX:
        tel = input( '전화 번호 입력 : ' )
        email = input( ' e-mail 입력 : ' )
        count += 1
        telephone_book.append( Person.Person( name, tel, email ) )
        name = input( '이름입력 "end" : quit ) : ')
    print()
    for i, v in enumerate( telephone_book ):
        print( '[{0}] : '.format( i ), end = '' )
        print( v.readPersonInfo() )
        print()



if __name__ == '__main__':
    main()