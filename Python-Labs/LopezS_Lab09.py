#LopezSLab09.py
"""
Name: Santiago Lopez

Class: CSEC 1436

Purpose: Generate the value of pi for a number of litgerations indicatged by the user and write results to a file


English Steps:
    Ask user input for the number of iterations
    Ask user input for amount of decimal places
    Check if the number is valid
    If number not valid ask user to input another number with specifiec instructions
    Calcualge Pi using the Leibniz formula 
    Calculate Pi using pythons math.pi and 22/7
    Indicate the difference between Leibniz formula and values from math libary & 22/7
    Display the results in a nice tabulated format
    Ask user for file name with written reusults in a nice tabulated way
    Ask if user wants to repeat 
    If repeat ask to append file or create mew
    If yes repeat same calculations
    if no end Program

Test:    
    Test 1. Iterations- 17  Decimal Places- 8  Filename- PiT1.txt  Repeat: No   
    Expected Results- 17 rows of Pi calculations, All 6 collumns, and 8 decimal places format

    Test 2. Iterations- 1  Decimal Places- 7  Filename- PiT2.txt  Repat: No 
    Expected Result- 1 iteration is accpedted, Leibniz Pi= 4.0000000, One row written

    Test 3. Iterations- 0 and then 100000001 and then 9  Decimal Places- 6  Filename- PiT3.txt  Repeat: No 
    Expected Result- 0 and 100000001 are not accepted, Program then asks for another input, and then 9 is acceptedt wich writes 9 rows after

    Test 4. Iterations- 13  Decimal places- 0 and then 1  Filename- PiT4.txt Repeat: No
    Expected Result- 0 is not accpeted, 1 is accepted, and 13 rows with 1 decimal place are written

    Test 5. Iterations- 7  Decimal places- 51, and after 50  Filename- PiT5 Repeat: No
    Expected Result- 51 is not accepted, then 50 is accepted, creates 7 rows with 50 decimal places

    Test 6. Iterations- hello, then 11    Decimal Places- yoo, then 4   Filename- PiT6.txt  Repeat: No
    Expected Result- hello and yoo are not accepted, and then ask for valid inputs as in numbers, creates 11 rows with 4 decimal places

    Test 7.  Iterations- 8   Decimal Places- 9  FileName- PiT7.txt  Repeat: yes append   After append - 6 iterations, 9 decimal places, and repeat no
    Expected Result- Same File has 14 data rows

    Test 8. Iterations- 12  Decimal Places- 3  FileName- PiT8.txt  Repeat: yes and then new   After new- 5 iterations, 10 decimal places, and Filename- PiT82.txt Repeat: no
    Expected Result- 2 seperate files one with 12 and the other 5 rows


Psuedo Code:

import math

RightSideVal<== 1.0
Denominator <= 1.0
Repeat<== True
FileName<== ""
FileM= "w"

While Repeat == True
    RightSideVal<== 1.0
    Denominator <== 1.0

    NumIters<== Input from user(integer)

While NumIters is invalid or outside of 1 to 100000000
    Print "That is not a valid number of iterations"
    And ask user to enter another value 
End Whie

NumD<== Input from user (integer)

While NumD is invalid or outside 1 to 50
    print "That value for the decimal places is invalid"
    And asl user to eneter another value
End While

If FileName= ""
    FileName<== Input from user
End If

While FileName is not valid
    Print"File name not valid"
    Ask user to enter another name
End While

ApproximateVal<= 22/7
MathPi <== math.pi

Open the output file
Write the table headers to the file

For index <== 0 to NumIters -1

    if index > 0
    Denominator <== Denominator +2

    if index % 2 == 0
        RightSideVal<== RightSideVal+1 / Denominator
    Else
        RightSideVal <== RightSideVal -1 / Denominator
    End If

End If

PiVal <== 4.0 * RightSideVal

MathDiff <== difference between the PiVal and MathPi
AproxDiff <== difference between Pi Val and AproximateVal

Write the iteration number
Write the Pi Val
Write the Math Pi
Write the AproximateVal
Write the MathDiff 
Write the ApproxDiff 

All to the file using NumD Decimal places indicated

End For

Close Output File

Ask uer if they want to repeat

While answer is not "yes" or "no"
    Print"Invalid answer, please enter ("Yes or No")
    Ask user for another input
End While
If answer == "no"
    Repeat <== False
Else
    Ask user to append the file or create new one

While answer is not "append" or "new"
    Print "Invalid input, please enter ("append" or "new)
    Ask user for another input
End While

if answer == "append"
    FileM <== "a"
Else 
    FileName <== ""
    FileMode <== "w"
End if

End While
Print "The Pi Calculations have come to an end"

"""

import math

RightSideVal= 1.0
Denominator= 1.0
Repeat= True
FileName= ""
FileM= "w"

RightSideVal= 1.0
Denominator= 1.0

while Repeat == True:
    RightSideVal= 1.0
    Denominator= 1.0

    while True:
        try:
            NumIters= int(input("Enter the number of iterations between ( 1 & 100000000):"))
            
            if NumIters >= 1 and NumIters <= 100000000:
                break
            else:
                print("Inavlid value, Enter a correct one")
        except ValueError:
            print("Invalid input. Enter a whole number.")

    while True:
        try:
            NumD= int(input("Enter a number of decimal places between 1 and 50:"))

            if NumD >= 1 and NumD <= 50:
                break
            else:
                print("Value entered is not valid, try again")
        except ValueError:
            print("Value entered is not valid, Enter a whole number")
    if FileName== "":
        FileName= input("Enter the output filename: ")
    try:
        OutputFile= open(FileName, FileM)
        FormatSpecifier= f".{NumD}f"
        if FileM== "w":
            OutputFile.write("Iteration | Leibniz Pi | Math Pi | 22/7 | Math Difference | 22/7 Difference\n")
        for index in range(NumIters):
            if index >0:
                Denominator +=2

                if index % 2 == 0:
                    RightSideVal +=1/Denominator
                else:
                    RightSideVal -=1/Denominator
            PiVal= 4.0 * RightSideVal

            MathPi= math.pi
            ApproxVal= 22/7

            if PiVal >= MathPi:
                MathDiff= PiVal- MathPi
            else:
                MathDiff= MathPi- PiVal
            if PiVal>= ApproxVal:
                ApproxDiff= PiVal- ApproxVal
            else:
                ApproxDiff= ApproxVal- PiVal

            OutputFile.write(f"{index + 1} | {PiVal:{FormatSpecifier}} | {MathPi:{FormatSpecifier}} | {ApproxVal:{FormatSpecifier}} | {MathDiff:{FormatSpecifier}} | {ApproxDiff:{FormatSpecifier}}\n")

        OutputFile.close()
        print(f"Results recorded in {FileName}")

    except:
        print("There was a probelm recording results to the file")

    Answer= input("Would you like to repeat the test again?(yes or no): ")

    while True:
        if Answer == "yes":
            break
        elif Answer == "no":
            break
        else:
            print("Invalid input please enter yes or no.")
            Answer= input("Would you like to repeat the test again? (yes or no): ")

    if Answer== "no":
        Repeat= False
    else:
        Repeat=True

        FileChoice= input("Do you want to append or new file? ( Enter append or new): ")

        while True:
            if FileChoice== "append" :
                break
            elif FileChoice== "new" :
                break
            else:
                print("Invalid input, enter append or new")
                FileChoice= input("Enter append or new")
        if FileChoice== "append": 
            FileM= "a"
        else:
            FileName= ""
            FileM= "w"





        
        
        
       

