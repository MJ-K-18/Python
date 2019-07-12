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
class Person:
    def __init__( self, name = None, tel = None, email = None ):  # 생성자( constructor ) → __init__ 
        self.name = name                                          # instance 생성 시 자동 호출되는 method
        self.tel = tel
        self.email = email
    '''
    def __del__( self ):                                          # 소멸자( destructor ) 
        print( '{0} Good bye...^^'.format( self.__dir__ ) )       # instance가 memory에서 소멸될 때 자동 호출되는 method
    '''
    def setName( self, name ):
        self.name = name
    
    def getName( self ):
        return self.name
    
    def setTel( self, tel ):
        self.tel = tel
    
    def getTel( self ):
        return self.tel
    
    def setEmail( self, email ):
        self.email = email

    def getEmail( self ):
        return self.email
    
    def writePersonInfo( self, name, tel, email ):
        self.name = name
        self.tel = tel
        self.email = email
    
    def readPersonInfo( self ):
        return self.name, self.tel, self.email
    
if __name__ == '__main__':
    person = Person()           # instance 생성 - class명() - / member들은 생성된 상태가 아님
    print( 'Name : {0}'.format( person.getName() ) )
    print( 'Tel : {0}'.format( person.getTel() ) )
    print( 'Email : {0}'.format( person.getEmail() ) )


    person.setName( 'hong' )    # 이런표현을 message라 한다.
    person.setTel( '010-1234-5678' )
    person.setEmail( 'Hong@korea.com' )
    print( 'Name : {0}'.format( person.getName() ) )
    print( 'Tel : {0}'.format( person.getTel() ) )
    print( 'Email : {0}'.format( person.getEmail() ) )


    # person2 ~ 4 까지 상단처럼 생성자를 따로 만들지않으면 class 생성 안에 변수 넣기 안됨
    person2 = Person( 'kim', '010-2345-6789', 'kim@korea.com' )
    print( 'Name : {0}'.format( person2.getName() ) )
    print( 'Tel : {0}'.format( person2.getTel() ) )
    print( 'Email : {0}'.format( person2.getEmail() ) )

    person3 = Person( 'lee', '010-9431-6789' )
    print( 'Name : {0}'.format( person3.getName() ) )
    print( 'Tel : {0}'.format( person3.getTel() ) )
    print( 'Email : {0}'.format( person3.getEmail() ) )

    person4 = Person( 'park' )
    print( 'Name : {0}'.format( person4.getName() ) )
    print( 'Tel : {0}'.format( person4.getTel() ) )
    print( 'Email : {0}'.format( person4.getEmail() ) )
