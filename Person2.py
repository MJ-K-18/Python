
'''
    Person.py

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
# class 명은 첫글자 대문자로 - programmer들 간의 관행
# class의 method의 첫번째 인수는 무조건 self를 넣어야한다.
class Person:           #Entity Class ( data 성격 )
    def __init__( self, name, tel, email = '' ):  
        self.name = name                                          
        self.tel = tel
        self.email = email
    
    def getName( self ):
        return self.name
 
    def getTel( self ):
        return self.tel

    def getEmail( self ):
        return self.email
    
    def writePersonInfo( self, name, tel, email ):
        self.name = name
        self.tel = tel
        self.email = email
    
    def readPersonInfo( self ):
        return self.name, self.tel, self.email
    
    def __repr__( self ):
        str = '{0:10} {1:<13} {2:<30}'.format( self.name, self.tel, self.email )
        return str


class TelephoneBook:  # Control Class( 관리 성격 )
    MAX = 50
    count_person = 0

    def __init__( self ):
        self.telephoneBook = {}

    def writePersonInfo( self, name, tel, email = '' ):
        self.telephoneBook[ name ] = Person( name, tel, email )
        TelephoneBook.count_person += 1

    def readPersonInfo( self, key ):
        return self.telephoneBook[ key ].readPersonInfo()    

    def printTelephoneBook( self ):
        for key in self.telephoneBook:
            print( self.telephoneBook[ key ] )

    def __repr__( self ):
        s = []
        for key in self.telephoneBook:
            s.append( self.telephoneBook[ key ] )
        return str( s )

def testMain():
    telephoneBook = TelephoneBook()

    telephoneBook.writePersonInfo( 'hong', '010-1234-5678', 'Hong@korea.com' )
    telephoneBook.writePersonInfo( 'kim', '010-2345-6789' )
    telephoneBook.writePersonInfo( 'lee', '010-5678-1234', 'lee@korea.com' )

    telephoneBookAll = str( telephoneBook )
    for v in telephoneBookAll:
        print( v, end= '' )

    print()
    telephoneBook.printTelephoneBook()

    name = input( 'input name : ' )
    tel = input( 'input tel : ' )
    email = input( 'input email : ' )
    telephoneBook.writePersonInfo( name, tel, email )
    telephoneBook.printTelephoneBook()

if __name__ == '__main__':
    testMain()