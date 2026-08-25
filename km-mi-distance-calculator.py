kmd = float(input("enter distance in kilometers: "))
x = 0.621371
#one kilometer is equal to 0.621371 miles
md = kmd*x
print("distance in miles: ",md)

a = input("do you want to convert another distance? (yes/no)  ")
if a == "yes":
    # == checks if both the value and the data type are the same. ex. = "yes" needs to be str
    kmD = float(input("enter distance in kilometers: "))
    mD= kmD*x
    print("distance in miles: ",mD)
else: 
    print("program ended.")