'''
Write a program using a function called compute_grade that takes a score
between 0.0 and 1.0 as its parameter and returns a grade as a string. If the
score is out of range, print an error message. If the score is between 0.0
and 1.0, print a grade using the following table.
Score Grade
> 0.9 A
> 0.8 B
> 0.7 C
> 0.6 D
<= 0.6 F
Program Execution:
Enter score: 0.95
A
Enter score: perfect
Bad score
Enter score: 10.0
Bad score
Enter score: 0.75
C
Enter score: 0.5
F
Run the program repeatedly to test the various different values for input
'''
def compute_grade(score):
    try:
        if(float(score)>0.9 and float(score)<=1.0):
            return 'A'
        elif(float(score)>0.8 and float(score)<=0.9):
            return 'B'
        elif(float(score)>0.7 and float(score)<=0.8):
            return 'C'
        elif(float(score)>0.6 and float(score)<=0.7):
            return 'D'
        elif(float(score)<=0.6 and float(score)>=0):
            return'F'
        else:
            return'Bad Score'
    except:
        return'Bad Score'

n=input("Enter the score:")
grade=compute_grade(n)
print(grade)