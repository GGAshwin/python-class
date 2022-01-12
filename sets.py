def average(array):
    # your code goes here
    x=arr
    sum=0
    for i in x:
        sum +=i
    return (sum/len(arr))


arr = {161,182,161,154,176,170,167,171,170,174}
result = average(arr)
print(result)