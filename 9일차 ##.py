from Student2 import StudentInfo

student1 = StudentInfo( 'Hong', 50, 50, 50 )
student2 = StudentInfo( 'Kim', 90, 90, 90 )
student3 = StudentInfo( 'lee', 50, 50, 50 )

print( student1 )
print( student2 )
print( student3 )
print()

if student1 == student2:
    print( '{0} 학생과 {1} 학생은 동일한 총점을 갖는다!!!'.format( student1, student2 ))
else:
    print( '{0} 학생과 {1} 학생은 다른 총점을 갖는다!!!'.format( student1, student2 ))
print()

if student1 == student3:
    print( '{0} 학생과 {1} 학생은 동일한 총점을 갖는다!!!'.format( student1, student3 ))
else:
    print( '{0} 학생과 {1} 학생은 다른 총점을 갖는다!!!'.format( student1, student3 ))
print()

if student1 > student2:
    print( '{0} 학생이 {1} 학생보다 평균이 높다!!!'.format( student1, student2 ))
else:
    print( '{0} 학생이 {1} 학생보다 평균이 낮다!!!'.format( student1, student2 ))
print()
