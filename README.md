# Base26-to-Base10-and-vice-versa-
Base26 to Base10 and base10 to base26 converter using python

Consider a base 26 system wherein the letters of the alphabets are the digits.

That is A=0, B=1, C=2….Z=25 in base 10

Write a program that will take an input string of alphabets, use the first half of the string as a number in the base26 system and the other half as another number in the base26 system.
Now, add these two numbers to obtain a sum in base10.
Accept the string only if it contains even number of characters otherwise, return 0.

As the second part of the program, write a function to convert the base10 number you have obtained back to base 26.

Example, first function: - If your input string is “Petpan”, then first split it into PET26 and PAN26.
And show the sum in base10.

Example, second function:- Pass both base10 numbers 10263(PET) and 10153(PAN). The output should be PETPAN.

First Function
------------------
Sample Input
“Petpan”
Sample Output
20416

Second Function
-----------------------
Sample Input
10263, 10153
Sample Output
“PETPAN”

Here Base26 table for the program
 A=0,B=1,....Z=26
