user = int(input("Enter your age: "))
driving_license = input("Do you have a driver's license? ")
if user >= 21 and driving_license == "yes" or "Yes" :
    print("You are able to drive this vehicle")
else:
    print("You are not able to drive this vehicle")