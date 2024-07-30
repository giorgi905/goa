#მომხმარებელს input-ის გამოყენებით შემოატანინეთ სახელი, გვარი, ასაკი და ქალაქი. როცა  შემოიტანს
#მომხმარებელი ყველაფერს მერე უნდა დაუპრინტოთ გრძელი წინადადება

first_name = input("what is your first name?: ")
last_name = input("what is you last name?: ")
city = input("in what city do you reside in?: ")
age = input("how old are you?: ")

print("hello! my name is", first_name + ",",
      "last name is", last_name + ",",
      "i am from the city of", city + ",",
       "i am", age + "." )