_auther_ = "bhavani"

#Program1

name = input("please enter your name :")
age = int(input("how old are you, {0}?".format(name)))
if age >=18:
    print("you are old enough to vote")
    print("please mark X in box")
else:
    print("please come back in {0} years".format(18-age))

# program 2
#  end="" will make print next item in smae line rather in new line , other wise default value is "\n"
number = "+1 (201) 360 -1218"
clean_number = ""
for i in range(0, len(number)):
    if number[i] in "0123456789":
        print(number[i],end="")

# Program 3
# clean phone number and print as integear

number = "+1 (201) 360 -1218"
clean_number = ""
for i in range(0, len(number)):
    if number[i] in "0123456789":
        clean_number = clean_number + number[i]

clean_number = int(clean_number)
print ("new number is :{}".format(clean_number))


