num=int(input("Enter a year"))

def is_leap(num):
        if(num%4==0):
            if(num%100==0):
                if(num%400==0):
                    print('The year is a leap year')
                else:
                    print('The year is not a leap year')
            else:
                print('The year is a leap year')
        else:
            print('The year is not a leap year')
is_leap(num)