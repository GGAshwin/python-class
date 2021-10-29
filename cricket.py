#program to read cricketer's achievements during his carrer interms of year,
# runs scored and wickets. Sort the achievement of a cricket in the order of runs scored and wickets
#cricket=[['ms',2001,69,0],['abc',2005,100,5],['fg',2007,67,15],['jbd',2004,10,30]]
cricket=[]
n=int(input("Enter the no.of cricketers"))
for i in range(n):
    year=input("Enter year")
    runs=input("Enter runs")
    wickets=input("Enter wickets")
    cricket.append((year,runs,wickets))
cricket.sort(reverse=True)
print(cricket)