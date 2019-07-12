'''
    Student.py

    학생 class

    member : 이름( name )
             과목1( subject1 )
             과목2( subject2 )
             과목3( subject3 )
             총점( total )
             평균( average )
             판정( grade )

    method : 생성자( __init__() )
             이름 읽기( getName() )
             과목1 점수 읽기( getSubject1() )
             과목2 점수 읽기( getSubject2() )
             과목3 점수 읽기( getSubject3() )
             성적 계산( calcScore() )
             학생 정보 읽기( readStudentInfo() )
'''
class StudentInfo:
    # class member
    SUBJECT_MAX = 3
    EXCELLENT_BASE = 90
    FAIL_BASE = 60

    obj_count = 0

    def __init__( self, name = None, subject1 = 0, subject2 = 0, subject3 = 0 ):
        StudentInfo.obj_count += 1 
        
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
        self.total = sum( ( self.subject1, self.subject2, self.subject3 ) )
        self.average = self.total / StudentInfo.SUBJECT_MAX
        if self.average >= StudentInfo.EXCELLENT_BASE:
            self.grade = 'Excellent'
        elif self.average < StudentInfo.FAIL_BASE:
            self.grade = 'Fail'
        else:
            self.grade = ''

    def readStudentInfo( self ):
        return self.name, self.subject1, self.subject2, self.subject3, self.total, self.average, self.grade
    
    def __eq__( self, other ):
        return self.total == other.total

    def __gt__( self, other ):
        return self.average > other.average
    
    def __repr__( self ):
        str = '{0:<10} {1:3} {2:3} {3:3} {4:5} {5:6.2f} {6:<10}'.format( self.name, self.subject1, self.subject2, self.subject3, self.total, self.average, self.grade )
        return str

class ScoreCard():
    MAX = 10
    count_person = 0

    def __init__( self ):
        self.scoreCard = {}
    
    def writeScoreCard( self, name = None, subject1 = 0, subject2 = 0, subject3 = 0 ):
        self.scoreCard[ name ] = StudentInfo( name, subject1, subject2, subject3 )
        ScoreCard.count_person += 1
    
    def readScoreCardInfo( self, key ):
        return self.scoreCard[ key ].readScoreCardInfo()
    
    def printScoreCard( self ):
        for key in self.scoreCard:
            print( self.scoreCard[ key ])
    
    def __repr__( self ):
        s = []
        for key in self.scoreCard:
            s.append( self.scoreCard[ key ] )
        return str( s )

    def inputprint( self ):
        return list( self.scoreCard.values() )


def main():
    scoreCard = ScoreCard()

    scoreCard.writeScoreCard( 'hong', 50, 50, 50 )
    scoreCard.writeScoreCard( 'kim', 90, 90, 90 )
    scoreCard.writeScoreCard( 'nam', 70, 70, 70 )

    scoreCardAll = str( scoreCard )
    for v in scoreCardAll:
        print( v, end = '' )
    print()
    scoreCard.printScoreCard()

def main2():
    scoreCard = ScoreCard()

    count = 0

    name = input( '학생 이름 입력 ( "end" : quit ) : ' )
    while name != 'end' and count < ScoreCard.MAX:
        count = count + 1
        subjects = []

        for x in range( StudentInfo.SUBJECT_MAX ):
            subject = int( input( '{0:2} 과목중 {1:2} 번째 과목 성적 입력 : '.format( StudentInfo.SUBJECT_MAX, x + 1 ) ) )
            while ( subject < 0 or subject > 100 ):
                print( '\nError : 점수는 0 ~ 100 입니다...\n다시 입력 하십시요...\n' )
                subject = int( input( '{0:2} 과목중 {1:2} 번째 과목 성적 입력 : '.format( StudentInfo.SUBJECT_MAX, x + 1 ) ) )

            subjects.append( subject )

        scoreCard.writeScoreCard( name, subjects[ 0 ], subjects[ 1 ], subjects[ 2 ] )
        
        name = input( '\n학생 이름 입력 ( "end" : quit ) : ' )

    print()
    studentInfo = scoreCard.inputprint()
    for student in studentInfo:
        print( student )
    print( '\ncount student : {0:2}'.format( ScoreCard.count_person ) )


if __name__ == '__main__':
    main()
    main2()