'''
    training9_2_scoretable_3layer.py
'''
class StudentInfo:
    '''
        학생( StudentInfo ) class

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
        str = '{0:<10} {1:3} {2:3} {3:3} {4:5} {5:6.2f} {6:<10}'.format( self.name,
                                                                         self.subject1,
                                                                         self.subject2,
                                                                         self.subject3,
                                                                         self.total,
                                                                         self.average,
                                                                         self.grade )
        return str

class ScoreTable:
    '''
        성적 일람표( ScoreTable ) class

        member : 성적일람표( scoretable ) - 학생 정보 저장

                 최대 학생수( MAX )
                 등록 학생수( count_student )

        method : 생성자( __init__() )
                 학생 정보를 읽는다.( readStudentInfo() )
                 학생 정보를 기록한다.( writeStudentInfo() )
                 성적 일람표를 출력한다.( printScoreTable() )
    '''
    MAX = 10
    count_student = 0

    def __init__( self ):
        self.scoretable = {}

    def readStudentInfo( self, key ):
        return self.scoretable[ key ].readStudentInfo()

    def writeStudentInfo( self, name, subject1, subject2, subject3 ):
        self.scoretable[ name ] = StudentInfo( name, subject1, subject2, subject3 )
        ScoreTable.count_student += 1
    
    def printScoreTable( self ):
        return list( self.scoretable.values() )

class ScoreTableUI:
    '''
        성적 일람표 UI( ScoreTableUI ) class

        member : 성적일람표( scoretable ) - 성적 일람표 class 연결
                 
                 프로그램 표제( question_str )
                 입력 학생수( count )
                 입력 학생 이름( name )
                 입력 점수 목록( subjects )
                 입력 점수( subject )
                 출력 학생 정보 목록( studentInfos )

        method : 생성자( __init__() )
                 학생 정보를 입력한다.( inputStudentInfo() )
                 성적일람표를 출력한다.( inputStudentInfo() )
    '''
    def __init__( self ):
        self.scoreTable = ScoreTable()

        self.question_str = '''
1. 다음과 같이 출력하는 프로그램을 class를 작성하여 완성하세요.
   ( 10명이내 이름이 'end'이면 결과 출력, 90이상 Excellent 60이하 Fail )
   ( boundary class와 control class와 Entity class 관계로 구성한다. )

   Hong 50 50 50 150 50.0 Fail
   Kim  90 90 90 270 90.0 Excellent
   Nam  70 70 70 210 70.0
        '''
        print( ''.center( 72, '=' ) )
        print( self.question_str )
        print( ''.center( 72, '=' ) )
        print()
        self.inputStudentInfo()

    def inputStudentInfo( self ):
        self.count = 0

        self.name = input( '학생 이름 입력 ( "end" : quit ) : ' )
        while self.name != 'end' and self.count < ScoreTable.MAX:
            self.count += 1
            self.subjects = []

            for x in range( StudentInfo.SUBJECT_MAX ):
                self.subject = int( input( '{0:2} 과목중 {1:2} 번째 과목 성적 입력 : '.format( StudentInfo.SUBJECT_MAX, x + 1 ) ) )
                while ( self.subject < 0 or self.subject > 100 ):
                    print( '\nError : 점수는 0 ~ 100 입니다...\n다시 입력 하십시요...\n' )
                    self.subject = int( input( '{0:2} 과목중 {1:2} 번째 과목 성적 입력 : '.format( StudentInfo.SUBJECT_MAX, x + 1 ) ) )

                self.subjects.append( self.subject )

            self.scoreTable.writeStudentInfo( self.name, self.subjects[ 0 ], self.subjects[ 1 ], self.subjects[ 2 ] )
        
            self.name = input( '\n학생 이름 입력 ( "end" : quit ) : ' )

    def printScoreTable( self ):
        print()
        self.studentInfos = self.scoreTable.printScoreTable()
        for studentInfo in self.studentInfos:
            print( studentInfo )
        print( '\ncount student : {0:2}'.format( ScoreTable.count_student ) )

        input( '\nPress any key to program stop...' ) 

def main():
    '''
        성적일람표 출력 프로그램 main()
    '''
    scoreTableUI = ScoreTableUI()
    scoreTableUI.printScoreTable()

if __name__ == '__main__':
    main() 