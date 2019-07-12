'''
Python 8일차 실습

1. 다음과 같이 출력하는 프로그램을 class를 작성하여 완성하세요
  ( 10명이내 이름이 'end;이면 결과 출력, 90 이상 Excellent 60이하 fail )

hong 50 50 50 150 50.0 3 Fail
kim   90 90 90 270 90.0 1 Excellent
nam  70 70 70 210 70.0 2
'''

class Student():
    def __init__( self, name = None, subject1 = None, 
                    subject2 = None, subject3 = None,
                    total = None, average = None,
                    rank = None, grade = None ):
        self.name = name
        self.subject1 = subject1
        self.subject2 = subject2
        self.subject3 = subject3
        self.total = total
        self.average = average
        self.rank = rank
        self.grade = grade
    
    def setName( self, name ):
        self.name = name
    
    def getName( self ):
        return self.name
    
    def setSubject1( self, subject1 ):
        self.subejct1 = subject1

    def getSubject1( self ):
        return self.subject1
    
    def setSubject2( self, subject2 ):
        self.subejct2 = subject2

    def getSubject2( self ):
        return self.subject2

    def setSubject3( self, subject3 ):
        self.subejct3 = subject3

    def getSubject3( self ):
        return self.subject3

    def setTotal( self, total ):
        self.total = total
    
    def getTotal( self ):
        return self.total
    
    def setAverage( self, average ):
        self.average = average
    
    def getAverage( self ):
        return self.average
    
    def setRank( self, rank ):
        self.rank = rank

    def getRank( self ):
        return self.rank
    
    def setGrade( self, grade ):
        self.grade = grade
    
    def getGrade( self ):
        return self.grade

    def writeStudentInfo( self, name, subject1, 
                            subject2, subject3,
                            total, average,
                            rank, grade ):
        self.name = name
        self.subejct1 = subject1
        self.subejct2 = subject2
        self.subejct3 = subject3
        self.total = total
        self.average = average
        self.rank = rank
        self.grade = grade

    def readStudentInfo( self ):
        return self.name, self.subejct1, self.subejct2, self.subejct3, self.total, self.average, self.rank, self.grade

if __name__ == '__main__':
    student = Student()
    student.setName( 'hong' )
    student.setSubject1( '50' )
    student.setSubject2( '50' )
    student.setSubject3( '50' )
    student.setTotal( '150' )
    student.setAverage( '50.0' )
    student.setRank( '3' )
    student.setGrade( 'Fail' )
    print( student.readStudentInfo() )