# 1. Variables in Python
name = "Codelearn"
date_of_birth = 2
pi = 3.14
print(type(name))
print(type(date_of_birth))
print(type(pi))

# 2. Data types
message = "Hello" + " " +  "Codelearn"
print(message)

# 3. Concatenate string and integer
age = 19
print("Age: " + str(age))

a = 438
b = 636
print("a + b = " + str(a + b))
print("a - b = " + str(a - b))
print("a * b = " + str(a * b))
print("a / b = " + str(a / b))

length = 7.8
width = 3.5
print("Area: " + str(length * width))
print("Perimeter: " + str((length + width) *2))

# 4. Function
# input()
name = input()
print("Hello " + name)

# int()
name = input()
age = int(input())
print("In 15 years, age of " + name + " will be " + str(age + 15))

# Operator %
a = int(input())
b = int(input()) 
print("a % b = " + str(a % b))

# Excersice: Calculate the total of sum + ; difference - ; product * ; quotient / ; remainder %
a = int(input())
b = int(input())
print("a + b = " + str(a + b))
print("a - b = " + str(a - b))
print("a * b = " + str(a * b))
print("a / b = " + str(a / b))
print("a % b = " + str(a % b))

# After swap
a = int(input())
b = int(input())
c = a
a = b
b = c
print("after swap a = " + str(a) + ", b = " + str(b))

# Calculate the circumference of that circle knowing that π = 3.14
r = float(input())
print("Circumference = " + str(2 * 3.14 * r))

# 5. Python Operator
# 5.1 Arithmetic Operator
Calculate the area of triangle: A = 1/2*a*h

a = int(input())
h = int(input())
area = 1/2 * a * h
print("The area of triangle is " + str(area))

# Operator ** (a mũ b)
a = int(input())
b = int(input())
print(a ** b)

# 5.2 Comparison (Relational) Operator
Print result True if x > y

x = int(input())
y = int(input())
print("x > y:", x > y)

# 5.3 Assignment Operator
Print result of Total

a = int(input())
Total = int(input())
Total += a # Using += Operator
print("The Value of the Total after using += Operator is:", Total)
Total -= a # Using -= Operator
print("The Value of the Total after using -= Operator is:", Total)
Total *= a # Using *= Operator
print("The Value of the Total after using *= Operator is:", Total)
Total //= a # Using //= Operator
print("The Value of the Total after using //= Operator is:", Total)
Total **= a # Using **= Operator
print("The Value of the Total after using **= Operator is:", Total)
Total /= a # Using /= Operator
print("The Value of the Total after using /= Operator is:", Total)
Total %= a # Using %= Operator
print("The Value of the Total after using %= Operator is:", Total)

# 5.4 Membership Operator
x = input()
print('H' in x)

# 5.5  Identity Operator
a = int(input())
b = int(input())
print(a is b)

# 5.6 Logical Operator
x = int(input())
y = int(input())
z = int(input())
t = int(input())
print("Result evaluation is", (x > y) and (z < t))

# 6.1 if-else statements
age = int(input())
if age < 5:
    print("Your cat is young")
else:
    print("Your cat is old")

# 6.2 Using Ternary Operators
age = int(input())
print("Your cat is young") if age < 5 else print("Your cat is old")

# 6.3 if-else statements shortened
temperature = int(input())

if temperature >= 100:
    print("Stay at home and enjoy a good movie")
elif temperature >= 92:
    print("Stay at home")
elif temperature == 75:
    print("Go outside and enjoy the weather")
elif temperature <= 0:
    print("It's cool outside")
else:
    print("Let's go to school")

# 6.4 Excersise if-else comparison 3 numbers
x = int(input())
y = int(input())
z = int(input())

if x % 2 == 0:
    if y >= 20:
        print("y is greater than or equal to 20")
    else:
        print("y is less than 20")
else:
    if z >= 30:
        print("z is greater than or equal to 30")
    else:
        print("z is less than 30")

# 6.5 
a = int(input())
b = int(input())
c = int(input())
avg = (a + b + c) / 3

if avg > a and avg > b:
    print("The average value is greater than both a and b")
elif avg > a and avg > c:
    print("The average value is greater than both a and c")
elif avg > b and avg > c:
    print("The average value is greater than both b and c")
elif avg > a:
    print("The average value is greater than a")
elif avg > b:
    print("The average value is greater than b")
elif avg > c:
    print("The average value is greater than c")

# 6.6
age = int(input())

if age <= 0:
    print("This can hardly be true")
elif age == 1:
    print("About 1 human year")
elif age == 2:
    print("About 2 human years")
elif age > 2:
    print("Over 5 human years")