#start
import sys
print("Hello Welcome to CGPA Calculator")

#takesinputfromuser(i.e his marks)
ordinalNumber = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eight', 'ninth', 'tenth']

#chooseWhatYouWantToDo
choice = int(input("Enter your choice for the following task to perform:\n 0.Exit\n 1.CGPA Calculator \n 2.Desired CGPA\n 3.Semester Marks\n"))

def main(choice):
    if choice == 1:
        cgpacalculator()
    elif choice == 2:
        desirecgpa()
    elif choice == 3:
        semmarks()
    elif choice == 0:
        sys.exit(0)

#setting up the condtion for calculating cgpa as per semester in academic year
def cgpacalculator():
    totalSem = int(input("Enter the number of semester in your academic year: "))
    validNumberOfSem = [2, 4, 6, 8, 10] #one, two, three, four, five years respectively
    #oneyearcourse
    if totalSem in validNumberOfSem:
        semSum = 0
        for i in range(0, totalSem):
            semSum += float(input("Enter your SGPA in "+ ordinalNumber[i] +" sem: "))
        cgpa = float(semSum/totalSem)
        print(f"Your CGPA Is {cgpa}")
    else:
        print("You entered wrong number of semesters.")

#avergaeCgpaRequiredToAttainTheGoal
def desirecgpa():
    totalSem = int(input("Enter the number of semester in your academic year: "))
    validNumberOfSem = [2, 4, 6, 8, 10]
    if totalSem in validNumberOfSem:
        cgpa = input("Enter the desired CGPA you want to get: ")
        print(f"The averaga SGPA you need to get every sem is {cgpa}")
    else:
        print("You entered the wrong number of semesters")

#calcuateMarksOfIndividualSemseter
def semmarks():
    totalSem = int(input("Enter the semester marks you want to find out: "))
    validNumberOfSem = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    if totalSem in validNumberOfSem:
        semSum = 0
        for i in range(0, totalSem-1):
            semSum += float(input("Enter your SGPA in "+ ordinalNumber[i] +" sem: "))
        cgpa = float(input("Enter the desired CGPA you want to get: "))
        semTarget = (totalSem*cgpa) - semSum
        if semTarget > 10:
            print(f"You cannnot get this desried CGPA as you cannot score {semTarget}.")
        else:
            print(f"You need to score {semTarget} to attain your desired CGPA")

main(choice)
#end

