

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

class MajorCom( StudentInfo ):
    SUBJECT_MAX = 2

    def __init__( self, name = None, majorname = None, subjects = 0, m_subjects = 0 ):
        
        super().__init__( name, majorname, subjects )
        self.m_subjects = [ v for v in m_subjects ]
        self.calcScore()

    def getM_Subjects( self ):
        return self.subject1

    def getAverage( self ):
        return self.average

    def setRank( self, rank ):
        self.rank = rank

    def calcScore( self ):
        self.total = super().calcScore()
        self.total = self.total + sum( [ v for v in self.m_subjects ] )
        self.average = self.total / ( StudentInfo.SUBJECT_MAX + MajorCom.SUBJECT_MAX )
        
        if self.average >= StudentInfo.EXCELLENT_BASE:
            self.grade = 'Excellent'
        elif self.average < StudentInfo.FAIL_BASE:
            self.grade = 'Fail'
        else:
            self.grade = ''

    def readStudentInfo( self ):
        return super().readStudentInfo, self.subjects, self.m_subjects, self.total, self.average, self.grade

    def __repr__( self ):
        s = super().__repr__()
        s = s + '{0:3} {1:3} {2:7} {3:3} {4:3} {5:5} {6:6.2f} {7:2} {8:<10}'.format( self.m_subjects[ 0 ],
                                                                                    self.m_subjects[ 1 ],
                                                                                    self.subjects[ 0 ],
                                                                                    self.subjects[ 1] ,
                                                                                    self.subjects[ 2 ],
                                                                                    self.total,
                                                                                    self.average,
                                                                                    self.rank,
                                                                                    self.grade )
        return s

class MajorElec( StudentInfo ):
    SUBJECT_MAX = 3

    def __init__( self, name = None, majorname = None, subjects = 0, m_subjects = 0 ):
        
        super().__init__( name, majorname, subjects )
        self.m_subjects = [ v for v in m_subjects ]
        self.calcScore()

    def getM_Subjects( self ):
        return self.subjects

    def getAverage( self ):
        return self.average

    def setRank( self, rank ):
        self.rank = rank

    def calcScore( self ):
        self.total = super().calcScore()
        self.total = self.total + sum( [ v for v in self.m_subjects ] )
        self.average = self.total / ( StudentInfo.SUBJECT_MAX + MajorElec.SUBJECT_MAX )
        
        if self.average >= StudentInfo.EXCELLENT_BASE:
            self.grade = 'Excellent'
        elif self.average < StudentInfo.FAIL_BASE:
            self.grade = 'Fail'
        else:
            self.grade = ''


    def readStudentInfo( self ):
        return super().readStudentInfo, self.subjects, self.m_subjects, self.total, self.average, self.grade

    def __repr__( self ):
        s = super().__repr__()
        s = s + '{0:3} {1:3} {2:3} {3:3} {4:3} {5:3} {6:5} {7:6.2f} {8:2} {9:<10}'.format( self.m_subjects[ 0 ],
                                                                                    self.m_subjects[ 1 ],
                                                                                    self.m_subjects[ 2 ],
                                                                                    self.subjects[ 0 ],
                                                                                    self.subjects[ 1] ,
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