# Multiple functions output
def scores(student_grades):
   min = student_grades[0]
   max = student_grades[0]
   for g in student_grades:
      if (g < min):
         min = g
   for g in student_grades:
      if(g >  max):
         max = g
   return(min, max)
     
grades = [87,100,99,72]

worst, best = scores(grades)
print('highest score is :', best)
print('lowest score is : ', worst)