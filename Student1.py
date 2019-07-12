'''
Python 8일차 실습

1. 다음과 같이 출력하는 프로그램을 class를 작성하여 완성하세요
  ( 10명이내 이름이 'end;이면 결과 출력, 90 이상 Excellent 60이하 fail )

hong 50 50 50 150 50.0 3 Fail
kim   90 90 90 270 90.0 1 Excellent
nam  70 70 70 210 70.0 2
'''

class Student():
    def __init__( self, name = None, subject1 = None, subject2 = None, subject3 = None ):
        self.subjects = 3
        self.excellent= 90
        self.fail = 60

        self.name = name
        self.subject1 = subject1
        self.subject2 = subject2
        self.subject3 = subject3

        self.calcScore()

    def getName( self ):
        return self.name

    def getSubject1( self ):
        return self.subject1

    def getSubject2( self ):
        return self.subject2
    
    def getSubject3( self ):
        return self.subject3

    def calcScore( self ):
        self.total = sum( (self.subject1, self.subject2, self.subject3) )

        self.average = self.total / self.subjects
        
        if self.average >= self.excellent:
            self.grade = 'Excellent'
        elif self.average < self.fail:
            self.grade = 'Fail'
        else:
            self.grade = ''

    def readStudentInfo( self ):
        return self.name, self.subject1, self.subject2, self.subject3, self.total, self.average, self.grade

if __name__ == '__main__':
    student = Student( 'hong', 50, 50, 50)
 
    print( student.readStudentInfo() )