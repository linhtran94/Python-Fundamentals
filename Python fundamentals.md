# Python Fundamentals

## Table of Contents
1. [Variables in Python](#variables)
2. [Data types](#datatypes)
3. [Concatenate string and integer](#concatenate)
4. [Functions](#functions)
5. [Python Operator](#pythonOperator)
    1. [Python Arithmetic Operator](#arithmetic)
    2. [Python Comparison (Relational) Operator](#comparison)
    3. [Python Assignment Operator](#assignment)
    4. [Python Membership Operator](#membership)
    5. [Python Identity Operator](#identity)
    6. [Python Logical Operator](#logical)
    7. [Python Bitwise Operator](#bitwise)


## 1. Variables in Python <a name="variables"></a>
Variables are containers for storing data values. Values, which are stored in variables, can change while the program is running.

In Python, you do not need to declare explicitly variables before using them or declare their type. 
A variable is created the moment you first assigned value to it.

## 2. Data types <a name="datatypes"></a>
Variable stores a different type in Python. Python has the following data types built-in by default
- int represents integer values (e.g: 1, 2, 3, 4, etc.).
- float represents float values (e.g: 1.43, 5.34, etc.).
- bool represents 2 values True or False
- str represents string values  (e.g: "Viet Nam", "Codelearn", etc.)

In addition, there are some other data types such as list, set, dict, tuple, complex. 
To check the data type of a variable, use type() function

## 3. Concatenate string and integer <a name="concatenate"></a>
In Python, you can only concatenate two strings but cannot concatenate a string and integer. 

If you try to combine a string and a number, Python will give you an error.
So, if you want to merge the two, you will need to use str() function to convert the integer to a string
> To check type: print(type(str(19))) -> <class 'str'>

## 4. Functions <a name="functions"></a>
- input(): that values from the keyboard are always <class 'str'> type even if you enter a number.
- int(): In Python, input from the keyboard is always str type ( input() functions always return str type)  so we can not do calculations with it. Therefore, we need to convert age to the appropriate type, int here. 
To convert, use the built-in function int()
- operator '%' : the division operator to get remainder
- after swap: swap value a and b using a temporary variable c
- circumference: the radius of a circle could be a real number so we need to convert str to float. 
- operator ** : to calculate ab 

## 5. Python Operator <a name="pythonOperator"></a>

### 5.1. Python Arithmetic Operator <a name="arithmetic"></a>
We can do various arithmetic operations like addition, subtraction, multiplication, division, modulus, exponent, etc.

Python provides multiple ways for arithmetic calculations like eval function, declare variable & calculate, or call functions.

**Examples:**

    x = 15
    y = 4
    print('x + y =', x+y)
    print('x - y =', x-y)
    print('x * y =', x*y)
    print('x / y =', x/y)
    print('x % y =', x % y)
    print('x // y =', x//y)
    print('x ** y =', x**y)


### 5.2. Python Comparison (Relational) Operator <a name="comparison"></a>
Comparison operators are used for comparing values. It either returns True or False according to the condition.

Comparison operators allow us to determine whether two values are equal or if one is greater than the other and then make a decision based on the result. 

**Examples:**

    x = 10
    y = 12

    print('x > y is', x > y) => False
    print('x < y is', x < y) => True
    print('x == y is', x == y) => False
    print('x != y is', x != y) => True 
    print('x >= y is', x >= y) => False 
    print('x <= y is', x <= y) => True


### 5.3. Python Assignment Operator <a name="assignment"></a>
Learn how to use assignment operators to assign values to variables in Python. 

Python assignment operators are used for assigning the value of the right operand to the left operand.

## Assignment Operator:

  <table>
    <thead>
      <tr>
        <th>Operator</th>
        <th>Purpose</th>
        <th>Usage</th>
      </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>=<code></td>
            <td>Assign value of right side of expression to left side operand</td>
            <td><code>x = y + z</code></td>
        </tr>
        <tr>
            <td><code>+=</td>
            <td>Add AND: Add right side operand with left side operand and then assign to left operand</td>
            <td><code>a+=b a=a+b</code></td>
        </tr>
                <tr>
            <td><code>-=<code></td>
            <td>Subtract AND: Subtract right operand from left operand and then assign to left operand</td>
            <td><code>a-=b a=a-b</code></td>
        </tr>
                <tr>
            <td><code>*=<code></td>
            <td>Multiply AND: Multiply right operand with left operand and then assign to left operand</td>
            <td><code>a*=b a=a*b</code></td>
        </tr>
                <tr>
            <td><code>/=<code></td>
            <td>Divide AND: Divide left operand with right operand and then assign to left operand</td>
            <td><code>a/=b a=a/b</code></td>
        </tr>
                <tr>
            <td><code>%=<code></td>
            <td>Modulus AND: Takes modulus using left and right operands and assign result to left operand</td>
            <td><code>a%=b a=a%b</code></td>
        </tr>
                <tr>
            <td><code>//=<code></td>
            <td>Divide(floor) AND: Divide left operand with right operand and then assign the value(floor) to left operand</td>
            <td><code>a//=b a=a//b</code></td>
        </tr>
                <tr>
            <td><code>**=<code></td>
            <td>Exponent AND: Calculate exponent(raise power) value using operands and assign value to left operand</td>
            <td><code>a**=b a=a**b</code></td>
        </tr>
                <tr>
            <td><code>&=<code></td>
            <td>Performs Bitwise AND on operands and assign value to left operand</td>
            <td><code>a&=b a=a&b</code></td>
        </tr>
                <tr>
            <td><code>|=<code></td>
            <td>Performs Bitwise OR on operands and assign value to left operand</td>
            <td><code>a|=b a=a|b</code></td>
        </tr>
                <tr>
            <td><code>^=<code></td>
            <td>Performs Bitwise xOR on operands and assign value to left operand</td>
            <td><code>a^=b a=a^b</code></td>
        </tr>
                <tr>
            <td><code>>>=<code></td>
            <td>Performs Bitwise right shift on operands and assign value to left operand</td>
            <td><code>a>>=b     a=a>>b</code></td>
        </tr>
                <tr>
            <td><code><<=<code></td>
            <td>Performs Bitwise left shift on operands and assign value to left operand</td>
            <td><code>a <<= b a= a << b</code></td>
        </tr>
    </tbody>
  </table>


**Examples:**

    x = 15
    y = 4

    print('x + y =', x + y) => 19
    print('x - y =', x - y) => 11
    print('x * y =', x * y) => 60
    print('x / y =', x / y) => 3.75
    print('x // y =', x // y) =>3
    print('x ** y =', x ** y) => 50625


### 5.4. Python Membership Operator <a name="membership"></a>
Learn how to use membership operators to check if a value or variable is found in a sequence.

**in** and **not in** are the membership operators in Python. You can test if a string is found in another string as below:

    print("Code" in "Codelearn") => True
    print("Py" not in "Python") => False


### 5.5. Python Identity Operator <a name="identity"></a>
The identity operators in Python are used to determine whether a value is of a certain class or type. 

We can use both == operator and identity operator to compare variables of type **int, str, float, etc**. The difference between these operators will be explained in the next lessons. 

Two identity operators are available in Python are is and is not. Example:


    a = 5
    b = 7
    print(a is b)
    print(a is not b)

    When the above code is compiled and executed, it produces the following result:
    False
    True


### 5.6. Python Logical Operator <a name="logical"></a>

The logical operators **not, or, and** modify and combine **Boolean** expressions to create more complex conditions.

## Logical Operator

  <table>
    <thead>
      <tr>
        <th>Operator</th>
        <th>Purpose</th>
        <th>Usage</th>
      </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>and<code></td>
            <td>If both expressions are True then return True. Otherwise, it returns False</td>
            <td><code>a and b</code></td>
        </tr>
        <tr>
            <td><code>or</td>
            <td>If at least one expression is True then return True. Otherwise, it returns False</td>
            <td><code>a or b</code></td>
        </tr>
                <tr>
            <td><code>not<code></td>
            <td>If the expression is True then return False and vise versa</td>
            <td><code>a not b</code></td>
        </tr>
        </tbody>
  </table>


### 5.7. Python Bitwise Operator <a name="bitwise"></a>
N/A

## 6. Selection statements

### 6.1. If-Else statements

- **if-else** statements are used to check whether a condition is correct or not. If a statement is used to check if a condition is correct, the statement block inside it will be executed, otherwise, if the condition is incorrect, the block inside the else statement will be executed

An example of a program that checks whether a given number is even or odd using an if-else statement:

    n = int(input())
    if n % 2 == 0:
        print("n is an even number")
    else:
        print "n is an odd number"
        print("n is an odd number")


### 6.2. Ternary Operators in Python

Ternary operators are used for evaluating something based on a condition being true or false as if-else statements do. However, they simply allow testing a condition in a single line. Therefore, they can be used as a substitute for if-else statements when we want to check simple conditions.

An example of a program that compares two given number using the ternary operator

Python program to demonstrate nested ternary operator: 

    a, b = 10, 20

    print ("Both a and b are equal" if a == b else "a is greater than b"
            if a > b else "b is greater than a")
      

If we use if-else statement to compare the two given numbers, do the following:

    a, b = 10, 20

    if a != b:
        if a > b:
            print("a is greater than b")
        else:
            print("b is greater than a")
    else:
        print("Both a and b are equal")

### 6.3. If-Else statements shortened 
If there is an if statement is present inside the body of an else statement as below:

    a = int(input())
    b = int(input())
    if a == b:
        print("a = b")
    else:
        if a > b:
            print("a > b")
        else:
            print("a < b")

The above program can be shortened as below:

    a = int(input())
    b = int(input())
    if a == b:
        print("a = b")
    elif a > b:
        print("a > b")
    else:
        print("a < b")

### 6.4. Excersise if-else comparison 3 numbers
**Excersise:**
Write a program that takes 3 integers x, y, z from the user and checks If x is even or odd.

If x is an even number, check whether y is greater than or equal to 20. If y >= 20, print "y is greater than or equal to 20", print "y is less than 20" otherwise.
If x is an odd number, check whether z is greater than or equal to 30. If z >= 30, print "z is greater than or equal to 30", print "z is less than 30" otherwise. 

Example:
For x = 20, y = 33, z = 15, the output should be "y is greater than or equal to 20".
Because x % 2 = 0 and y > 20
For x = 15, y =23, z = 20, the output should be "z is less than 30". 
Because x % 2 != 0 and z < 30

### 6.5. Excersise if-else calculates the average (avg) of numbers

The 'and' keyword is a logical operator, which is used to combine conditional statements. An example of a program using 'and' to check whether a given number is in range [10, 20] as below:

    n = int(input())
    if n >= 10 and n <= 20:
        print("n is in the range [10, 20]")
    else:
        print("n is not in the range [10, 20]")

**Excersise:**

Write a program that accepts 3 natural numbers a, b, c from the user and calculates the average (avg) of those numbers. Check the avarage for the following conditions:

    If avg > a and avg > b, print The average value is greater than both a and b on the screen.
    If avg > a and avg > c, print The average value is greater than both a and c on the screen.
    If avg > b and avg > c, print The average value is greater than both b and c on the screen.
    If avg is greater than a and only a, print The average value is greater than a on the screen.
    If avg is greater than b and only b, print The average value is greater than b on the screen.
    If avg is greater than c and only c, print The average value is greater than c on the screen.

Example:

If a = 10, b = 20, c = 20, the output should be The average is greater than a
Because avg = (10+20+20)/3 = 20 so that the avg is greater than a and only a.

### 6.6. Excersise if-else to compare your pet's age to a human's age

    If age <= 0, print "This can hardly be true" on the screen.
    If age == 1, print "About 1 human year" on the screen.
    If age == 2, print "About 2 human years" on the screen.
    If age > 2, print "Over 5 human years" on the screen.

Example:

If age = 3, the output should be "Over 5 human years"
If age = 1, the output should be "About 1 human year"

