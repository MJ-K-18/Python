

class StudentInfo:
    # class member
    SUBJECT_MAX = 3
    EXCELLENT_BASE = 90
    FAIL_BASE = 60

    obj_count = 0

    def __init__( self, name = None, subject4 = 0, subject5 = 0, subject6 = 0 ):
        StudentInfo.obj_count += 1 
        
        self.name = name
        self.subject4 = subject4
        self.subject5 = subject5
        self.subject6 = subject6

    def getName( self ):
        return self.name

    def getSubject4( self ):
        return self.subject4

    def getSubject5( self ):
        return self.subject5

    def getSubject6( self ):
        return self.subject6

    def readStudentInfo( self ):
        return self.name, self.subject4, self.subject5, self.subject6

class MajorCom( StudentInfo ):
    SUBJECT_MAX = 6

    def __init__( self, name = None, majorname = None, subject1 = 0, subject2 = 0, subject3 = None ):
        
        super().__init__( name )
        self.majorName = majorname
        self.subject1 = subject1
        self.subject2 = subject2
        self.subject3 = subject3
        super().__init__( subject4 )
        super().__init__( subject5 )
        super().__init__( subject6 )
        self.calcScore()

    def getMajorName( self ):
        return self.majorName

    def getSubject1( self ):
        return self.subject1

    def getSubject2( self ):
        return self.subject2

    def calcScore( self ):
        self.total = sum( ( self.subject1, self.subject2, self.subject3, self.subject4, self.subject5, self.subject6 ) )
        self.average = self.total / MajorCom.SUBJECT_MAX
        if self.average >= StudentInfo.EXCELLENT_BASE:
            self.grade = 'Excellent'
        elif self.average < StudentInfo.FAIL_BASE:
            self.grade = 'Fail'
        else:
            self.grade = ''

    def readStudentInfo( self ):
        return self.name, self.majorName, self.subject1, self.subject2, self.subject3, self.subject4, self.subject5, self.subject6,self.total, self.average, self.grade

    def __repr__( self ):
        str = '{0:<10} {1:15} {2:3} {3:8} {4:3} {5:3} {6:3} {7:3} {8:5} {9:6.2f} {10:<10}'.format( self.name,
                                                                                                    self.majorName,
                                                                                                    self.subject1,
                                                                                                    self.subject2,
                                                                                                    self.subject3,
                                                                                                    self.subject4,
                                                                                                    self.subject5,
                                                                                                    self.subject6,
                                                                                                    self.total,
                                                                                                    self.average,
                                                                                                    self.grade )
        return str

class MajorElec( StudentInfo ):
    SUBJECT_MAX = 6

    def __init__( self, name = None, majorname = None, subject1 = 0, subject2 = 0, subject3 = 0 ):
        
        super().__init__( name )
        self.majorName = majorname
        self.subject1 = subject1
        self.subject2 = subject2
        self.subject3 = subject3
        super().__init__( subject4 )
        super().__init__( subject5 )
        super().__init__( subject6 )
        self.calcScore()

    def getMajorName( self ):
        return self.majorName

    def getSubject1( self ):
        return self.subject1

    def getSubject2( self ):
        return self.subject2

    def getSubject3( self ):
        return self.subject3


    def calcScore( self ):
        self.total = sum( ( self.subject1, self.subject2, self.subject3, self.subject4, self.subject5, self.subject6 ) )
        self.average = self.total / MajorElec.SUBJECT_MAX
        if self.average >= StudentInfo.EXCELLENT_BASE:
            self.grade = 'Excellent'
        elif self.average < StudentInfo.FAIL_BASE:
            self.grade = 'Fail'
        else:
            self.grade = ''


    def readStudentInfo( self ):
        return self.name, self.majorName, self.subject1, self.subject2, self.subject3, self.subject4, self.subject5, self.subject6,self.total, self.average, self.grade

    def __repr__( self ):
        str = '{0:<10} {1:15} {2:3} {3:3} {4:3} {5:3} {6:3} {7:3} {8:5} {9:6.2f} {10:<10}'.format( self.name,
                                                                                                    self.majorName,
                                                                                                    self.subject1,
                                                                                                    self.subject2,
                                                                                                    self.subject3,
                                                                                                    self.subject4,
                                                                                                    self.subject5,
                                                                                                    self.subject6,
                                                                                                    self.total,
                                                                                                    self.average,
                                                                                                    self.grade )

class ScoreTable:

    MAX = 10
    count_student = 0

    def __init__( self ):
        self.scoretable = {}

    def readStudentInfo( self, key ):
        return self.scoretable[ key ].readStudentInfo()

    def writeStudentInfo( self, name, majorname, subject1, subject2, subject3, subject4, subject5, subject6 ):
        self.scoretable[ name ] = StudentInfo( name, subject1, subject2, subject3, subject4, subject5, subject6 )
        ScoreTable.count_student += 1
    
    def printScoreTable( self ):
        return list( self.scoretable.values() )

def main():
    scoreTable = ScoreTable()
    count = 0

    name = input( '학생 이름 입력 ( "end" : quit ) : ' )
    while name != 'end' and count < ScoreTable.MAX:
        count = count + 1
        subjects = []
        x = 0
        y = 0
        majorname = str(input( '전공 입력 : ' ))
        for y in range( MajorCom.SUBJECT_MAX, y + 1 ):
            subjectm = int( input( '전공 {0:2} 과목중 {1:2} 번째 과목 성적 입력 : '.format( MajorCom.SUBJECT_MAX, y + 1 ) ) )
            subjects.append( subjectm )
        
        for x in range( StudentInfo.SUBJECT_MAX ):
            subject = int( input( '공통 {0:2} 과목중 {1:2} 번째 과목 성적 입력 : '.format( StudentInfo.SUBJECT_MAX, x + 1 ) ) )
            while ( subject < 0 or subject > 100 ):
                print( '\nError : 점수는 0 ~ 100 입니다...\n다시 입력 하십시요...\n' )
                subject = int( input( '{0:2} 과목중 {1:2} 번째 과목 성적 입력 : '.format( StudentInfo.SUBJECT_MAX, x + 1 ) ) )
            subjects.append( subject )

        scoreTable.writeStudentInfo( name, majorname, subjects[ 0 ], subjects[ 1 ], subjects[ 2 ], subjects[ 3 ], subjects[ 4 ], subjects[ 5 ], subject[ 6 ] )

        
        name = input( '\n학생 이름 입력 ( "end" : quit ) : ' )

    print()
    studentInfos = scoreTable.printScoreTable()
    for studentInfo in studentInfos:
        print( studentInfo )
    print( '\ncount student : {0:2}'.format( ScoreTable.count_student ) )





if __name__ == '__main__':
    main()