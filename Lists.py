parrot_list = ["non pinin", "s stiff", "bereft of live"]
parrot_list.append("A norwegian blue")

for strings in parrot_list:
    print("This parrot is "+ strings)

even = [2, 4, 6, 8]
odd =[1, 3, 5, 7, 9]
numbers = odd+even
numbers1 = odd+even
print(numbers)

# now you hva two ways to sort
# Option 1 will work
numbers.sort()
print(numbers)

# will not work, will print out none as in python objects work on same rather create one more
print(numbers.sort())

# Option 2, below both options work

sorted_numbers = sorted(numbers1)
print(sorted_numbers)
#or
print(sorted(numbers1))

if numbers == sorted_numbers:
    print("both lists are match")
else:
    print("both lists are not match")
