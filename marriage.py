#Given the age of a person and gender determine the eligibility for marriage
gender=input("Enter gender (male/female)")
age=int(input("Enter your age"))
if(gender=="male" and age>=21):
    print('You are eligible for marriage')
elif (gender=="female" and ahe>=18):
    print('You are eligible for marriage')
else:
    print('You are not eligible')