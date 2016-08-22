# Program 4
# clean phone number and print as integear, just much better way

number = "+1 (201) 360 - 1218"
clean_number = ""
for i in number:
    if i in "0123456789":
        clean_number = clean_number + i

clean_number = int(clean_number)
print("new number is :{}".format(clean_number))

# Program 5

for i in ("one", "two", "three", "four"):
    print("this is i value at presnt :" + i)

# Program 6

for i in range (0, 100, 5):
     print("this is i value at presnt :" + str(i))
     # or
     print("this is i value at presnt :{}".format(i))