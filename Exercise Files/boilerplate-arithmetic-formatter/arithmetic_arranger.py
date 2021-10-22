#created by Regina Citra Pesela (reginapasela@gmail.com)
import re

def arithmetic_arranger(problems, summary = False):    
    #CHECK if the input is least than 5, if not return error
    if len(problems) > 5:
        return "Error: Too many problems."
        
    #create list variable to store value
    firstnums, secondnums, separators, summarynums = str(), str(), str(), str()

    #do looping for each input given
    for i in range(len(problems)):
        #use regex module to split problem given into 3 variables: firstnum, operator and secondnum
        numbers = re.split("\s", problems[i])

        #CHECK if the numbers is less than four digits
        for j in range(3):
            if len(numbers[j]) > 4:
                return "Error: Numbers cannot be more than four digits."

        #assign the value from regex split into variables
        firstnum, operator, secondnum = numbers[0], numbers[1], numbers[2]

        #CHECK if first number and second number is a digit or not
        if not secondnum.isdigit() or not firstnum.isdigit():
            return "Error: Numbers must only contain digits."

        #calculate the result of problems and convert it into string
        #if the operator isnot + or - return error
        if operator == "+":
            summarynum = str(int(firstnum) + int(secondnum))

        elif operator == "-":
            summarynum = str(int(firstnum) - int(secondnum))

        else:
            return "Error: Operator must be '+' or '-'."

        #compare which is bigger, firstnum or second num (will be used as variable for right alignet format)
        biglen = len(secondnum)

        if len(firstnum) > len(secondnum):
            biglen = len(firstnum)

        #make the number in variables comply right alligned format by add space in strings
        firstnum = (" " * ((biglen + 2) - len(firstnum)) + firstnum)
        secondnum = operator + (" " * ((biglen + 1) - len(secondnum)) + secondnum)
        separator = "-" * (2 + biglen)
        summarynum = " " * (len(separator) - len(summarynum)) + summarynum

        if i == 0:
            firstnums, secondnums, separators, summarynums = firstnum, secondnum, separator, summarynum
        else:
            firstnums += (" " * 4 + firstnum)
            secondnums += (" " * 4 + secondnum)
            separators += (" " * 4 + separator)
            summarynums += (" " * 4 + summarynum)
    
    arranged_problems = (firstnums + "\n" + secondnums + "\n" + separators)

    if summary:
        arranged_problems += "\n"
        arranged_problems += summarynums

    # return arranged problems
    return arranged_problems