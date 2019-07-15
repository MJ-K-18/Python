'''
    11일차 실습 #1

    1. 다음과 같이 출력하는 프로그램을 class를 작성하여 완성하세요.
    ( 10명이내 이름이 'end'이면 결과 출력, 90이상 Excellent 60이하 Fail )
    ( 상속과 control/entity class 형태로 구성 )
    학생정보를 상속받는 클래스를 하나로 하고, 학과 정보를 별도의 클래스로
    관리한다.
   
                            전공       공통
        Hong  computer     50 50    50 50 50 250 50.0  3 Fail
        Kim   Electronic   90 90 90 90 90 90 540 90.0  1 Excellent
        Nam   computer     70 70    70 70 70 350 70.0  2
'''



class StudentInfo:
    SUBJECT_MAX = 3
    EXCELLENT_BASE = 90
    FAIL_BASE = 60

    obj_count = 0

    def __init__( self, name = None, majorname = None, subjects = 0 ):
        StudentInfo.obj_count += 1 
        
        self.name = name
        self.majorname = majorname
        self.subjects = [ v for v in subjects ]

    def getName( self ):
        return self.name

    def getSubjects( self ):
        return self.subjects

    def calcScore( self ):
        return sum( [ v for v in self.subjects ] )

    def readStudentInfo( self ):
        return self.name, self.majorname

    def __repr__( self ):
        s = '{0:<10} {1:<20}'.format( self.name, self.majorname )
        return s

class MajorInfo:
    
    def __init__( self, majorname, majorsubjectmax ):
        self.majorname = majorname
        self.majorsubjectmax = majorsubjectmax

    def getMajorName( self ):
        return self.majorname

    def getMajorSubjectMax( self ):
        return self.majorsubjectmax

    def readMajorInfo( self ):
        return self.majorname, self.majorsubjectmax

    def readMajorSubjectMax( self ):
        return self.majorsubjectmax

    def __repr__( self ):
        s = '{0:20} {1:2}'.format( self.majorname, self.majorsubjectmax )

        return s

class MajorTable:

    def __init__( self ):
        self.majors = {}
        self.majorCount = 0

    def getMajorCount( self ):
        return self.majorCount

    def isMajorInfo( self, key ):
        return self.majors.get( key, False )

    def readmajorInfo( self, key ):
        return self.majors[ key ].readmajorInfo()

    def readMajorSubjectMax( self, key ):
        return self.majors[ key ].readMajorSubjectMax()

    def writemajorInfo( self, major ):
        self.majors[ major.getmajorName() ] = major
        self.majorCount += 1 

    def printMajorInfos( self ):
        keys = self.major.keys()
        for key in keys:
            print( self.majors[ key ] )

class MajorStudentInfo( StudentInfo ):

     def __init__( self, name, major, majorsubjectmax, subjects, m_subjects ): 
        super().__init__( name, major, common_subjects )  
        self.majorsubjectmax = majorsubjectmax     
        self.major_subjects = [ v for v in major_subjects ]
        self.calcScore()

    def getMajorSubjectMax( self ):
        return self.majorsubjectmax

    def getComputerSubjects( self ):
        return self.m_subjects

    def getAverage( self ):
        return self.average

    def setRank( self, rank ):
        self.rank = rank

    def calcScore( self ):
        self.total = super().calcScore()
        self.total = self.total + sum( [ v for v in self.m_subjects ] )
        
        self.average = self.total / ( StudentInfo.SUBJECT_MAX + self.majorsubjectmax )
        
        if self.average >= StudentInfo.EXCELLENT_BASE:
            self.grade = 'Excellent'
        elif self.average < StudentInfo.FAIL_BASE:
            self.grade = 'Fail'
        else:
            self.grade = ''

    def readStudentInfo( self ):
        return super().readStudentInfo(), tuple( self.subjects ), tuple( self.m_ubjects ), self.total, self.average, self.grade

    def __repr__( self ):
        s = super().__repr__()
        spaces = '          '
        for i in range( self.majorsubjectmax ):
            s = s + '{0:3} '.format( self.major_subjects[ i ] )
        s = s + '\t\t' + spaces[ self.majorsubjectmax::self.majorsubjectmax ]        
        s = s + '{0:3} {1:3} {2:3} {3:5} {4:6.2f} {5:2} {6:<10}'.format( self.subjects[ 0 ],
                                                                         self.subjects[ 1 ],
                                                                         self.subjects[ 2 ],
                                                                         self.total,
                                                                         self.average,
                                                                         self.rank,
                                                                         self.grade )
        return s
        

class ScoreTable:

    MAX = 10
    count_student = 0

    def __init__( self ):
        self.scoretable = {}

    def readStudentInfo( self, key ):
        return self.scoretable[ key ].readStudentInfo()

    def writeStudentInfo( self, student ):
        self.scoretable[ ScoreTable.count_student ] = student
        ScoreTable.count_student += 1
        self.calcRank()
    
    def printScoreTable( self ):
        return list( self.scoretable.values() )

    def calcRank( self ):
        keys = self.scoretable.keys()
        for key in keys:
            rank = 1
            average = self.scoretable[ key ].getAverage()
            for k in self.scoretable:
                if average < self.scoretable[ k ].getAverage():
                    rank += 1
            self.scoretable[ key ].setRank( rank )

def main():
    scoreTable = ScoreTable()
    count = 0

    name = input( '학생 이름 입력 ( "end" : quit ) : ' )
    while name != 'end' and count < ScoreTable.MAX:
        count = count + 1
        subjects = []
        m_subjects = []

        majorname = (input( '전공 입력 : ' ))
        while ( majorname != 'computer' and majorname != 'electronic' ):
            print( '전공은 [ "computer" ] [ "electronic" ] 중 하나를 입력하세요' )
            majorname = input( '전공 [ "computer" ] [ "electronic" ] 중 입력하세요 : ' )
        
        if majorname == 'computer':
            for x in range( MajorCom.SUBJECT_MAX ):
                m_subject = int( input( '전공 {0:2} 과목중 {1:2} 번째 전공 과목 성적 입력 : '.format( MajorCom.SUBJECT_MAX, x + 1 ) ) )
                while ( m_subject < 0 or m_subject > 100 ):
                    print( '\nError : 점수는 0 ~ 100 입니다...\n다시 입력 하십시요...\n' )
                    m_subject = int( input( '전공 {0:2} 과목중 {1:2} 번째 전공 과목 성적 입력 : '.format( MajorCom.SUBJECT_MAX, x + 1 ) ) )    
                m_subjects.append( m_subject )

            for x in range( StudentInfo.SUBJECT_MAX ):
                subject = int( input( '공통 {0:2} 과목중 {1:2} 번째 과목 성적 입력 : '.format( StudentInfo.SUBJECT_MAX, x + 1 ) ) )
                while ( subject < 0 or subject > 100 ):
                    print( '\nError : 점수는 0 ~ 100 입니다...\n다시 입력 하십시요...\n' )
                    subject = int( input( '{0:2} 과목중 {1:2} 번째 과목 성적 입력 : '.format( StudentInfo.SUBJECT_MAX, x + 1 ) ) )
                subjects.append( subject )

            student = MajorCom( name, majorname, subjects, m_subjects )

        elif majorname == 'electronic':
            for x in range( MajorElec.SUBJECT_MAX ):
                m_subject = int( input( '전공 {0:2} 과목중 {1:2} 번째 전공 과목 성적 입력 : '.format( MajorElec.SUBJECT_MAX, x + 1 ) ) )
                while ( m_subject < 0 or m_subject > 100 ):
                    print( '\nError : 점수는 0 ~ 100 입니다...\n다시 입력 하십시요...\n' )
                    m_subject = int( input( '전공 {0:2} 과목중 {1:2} 번째 전공 과목 성적 입력 : '.format( MajorElec.SUBJECT_MAX, x + 1 ) ) )    
                m_subjects.append( m_subject )

            for x in range( StudentInfo.SUBJECT_MAX ):
                subject = int( input( '공통 {0:2} 과목중 {1:2} 번째 과목 성적 입력 : '.format( StudentInfo.SUBJECT_MAX, x + 1 ) ) )
                while ( subject < 0 or subject > 100 ):
                    print( '\nError : 점수는 0 ~ 100 입니다...\n다시 입력 하십시요...\n' )
                    subject = int( input( '{0:2} 과목중 {1:2} 번째 과목 성적 입력 : '.format( StudentInfo.SUBJECT_MAX, x + 1 ) ) )
                subjects.append( subject )

            student = MajorElec( name, majorname, subjects, m_subjects )

        scoreTable.writeStudentInfo( student )
    
        name = input( '\n학생 이름 입력 ( "end" : quit ) : ' )

    print()
    studentInfos = scoreTable.printScoreTable()
    for studentInfo in studentInfos:
        print( studentInfo )
    print( '\ncount student : {0:2}'.format( ScoreTable.count_student ) )





if __name__ == '__main__':
    main()