class Employee:
    def __init__( self, name ):
        self.name = name
    def doWork( self ):
        print( 'Employee {0}는 '.format( self.name ), end ='' )

# class명의 옆에 ( ) 안에 super class의 이름을 넣어주면 상속됨

class RegularEmployee( Employee ):
    def __init__( self, name, age ):
        super().__init__( name )
        self.age = age
    def doWork( self ):
        super().doWork()
        print( '일반적인 사무업무 수행' )
        #self.name = name
    
    #def doWork( self ):
        #print( 'Employee {0}는 일반적인 사무업무 수행'.format( self.name ) )


class SalesEmployee( Employee ):
    def __init__( self, name, age ):
        super().__init__( name )
        self.age = age
    def doWork( self ):
        super().doWork()
        print( '영업 업무를 수행' )
        #self.name = name
    
    #def doWork( self ):
        #print( 'Eomployee {0}는 영업 업무를 수행'.format( self.name ) )


def main():
    regularEmployee = RegularEmployee( 'Hong', 21 )
    salesEmployee = SalesEmployee( 'Kim', 33 )
    regularEmployee.doWork()
    salesEmployee.doWork()

if __name__ == '__main__':
    main()