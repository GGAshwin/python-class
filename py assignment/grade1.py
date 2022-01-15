#Exercise 7: Rewrite the grade program from the previous chapter using a function 
#called computegrade that takes a score as its parameter and returns a grade as a 
#string.

#Here is my original grade program (Chapter 3, Exercise 3):
# score=input("Please type a score between 0.0 and 1.0:")
# try:
#   float(score)
#   if float(score) >= 0.9 and float(score) <= 1.0:
#     print("A")
#   elif float(score) >= 0.8 and float(score) <= 0.9:
#     print("B")
#   elif float(score) >= 0.7 and float(score) <= 0.8:
#     print("C")
#   elif float(score) >= 0.6 and float(score) <= 0.7:
#     print("D")
#   elif float(score) > 0 and float(score) <= 0.6:
#     print("F")
#   else:
#     print("Bad score.  Please run the program again.")  
# except: 
#     print("Bad score.  Please run the program again.")

score=input("Please type a score between 0.0 and 1.0:")
try:
  def computegrade(score):
    if float(score) > 0.9 and float(score) <= 1.0:
      print("A")
    elif float(score) > 0.8 and float(score) <= 0.9:
      print("B")
    elif float(score) > 0.7 and float(score) <= 0.8:
      print("C")
    elif float(score) > 0.6 and float(score) <= 0.7:
      print("D")
    elif float(score) > 0 and float(score) <= 0.6:
      print("F")
    else:
      print("Bad score.  Please run the program again.")  
  computegrade(score)
except: 
    print("Bad score.  Please run the program again.")