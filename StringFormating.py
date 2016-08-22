_author_ = "Bhavani Bheemanadham"

age = 24
print("My Age is " + str(24) + " years")

print("My age is {0} years".format(age))

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}".format(31, "Jan", "Mar", "May", "jul", "Aug", "Oct",
                                                                          "Dec"))

# 2 format
for i in range(1, 12):
    print("Number %2d squire root %4d Qubed %4d" % (i, i ** 2, i ** 3))

# 3 format  {1:4} represents second item alocate 4 spaces and  < represent left alone
for i in range(1, 12):
    print("Number {0:2} sqire root {1:4} Qubed {2:<4}".format(i, i ** 2, i ** 3))
