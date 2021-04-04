#start
import sys
print("Hello Welcomme to CGPA Calculator")
#takesinputfromuser(i.e his marks)
cgpa = 0 
desiredcgpa = 0
totalsem = 0
#choosewhatyouwanttodo
choice = int(input("Enter your choice for the following task to perform:\n 0.Exit\n 1.CGPA Calculator \n 2.Desired CGPA\n"))
def main(choice):
    if choice == 1:
        cgpacalculator(totalsem)
    elif choice == 2:
        desirecgpa(totalsem,cgpa)
    elif choice == 0:
        sys.exit(0)
#setting up the condtion for calculating cgpa as per semester in academic year
def cgpacalculator(totalsem):
    totalsem = int(input("Enter the number of semester in your academic year: "))
    #oneyearcourse
    if totalsem == 2:
        sem1 = input("Enter your sgpa in first sem: ")
        sem1 = float(sem1)
        sem2 = input("Enter your sgpa in second sem: ")
        sem2 = float(sem2)
        cgpa = (sem1+sem2)/2
        cgpa = float(cgpa)
        print(f"Your CGPA Is {cgpa}")
    #twoyearcourse
    elif totalsem == 4:
        sem1 = input("Enter yur sgpa in first sem: ")
        sem1 = float(sem1)
        sem2 = input("Enter your sgpa in second sem: ")
        sem2= float(sem2)
        sem3 = input("Enter your sgpa in third sem: ")
        sem3 = float(sem3)
        sem4 = input("Enter your sgpa in fourth sem: ")
        sem4 = float(sem4)
        cgpa = (sem1+sem2+sem3+sem4)/4
        cgpa = float(cgpa)
        print(f"Your CGPA Is {cgpa}")
    #threeyearcourse
    elif totalsem == 6:
        sem1 = input("Enter yur sgpa in first sem: ")
        sem1 = float(sem1)
        sem2 = input("Enter your sgpa in second sem: ")
        sem2 = float(sem2)
        sem3 = input("Enter your sgpa in third sem: ")
        sem3 = float(sem3)
        sem4 = input("Enter your sgpa in fourth sem: ")
        sem4 = float(sem4)
        sem5 = input("Enter your sgpa in fifth sem: ")
        sem5 = float(sem5)
        sem6 = input("Eneter your sgpa in sixth sem: ")
        sem6 = float(sem6)
        cgpa = (sem1+sem2+sem3+sem4+sem5+sem6)/6
        cgpa = float(cgpa)
        print(f"Your CGPA Is {cgpa}")
    #fouryearcourse
    elif totalsem == 8:
        sem1 = input("Enter yur sgpa in first sem: ")
        sem1 = float(sem1)
        sem2 = input("Enter your sgpa in second sem: ")
        sem2 = float(sem2)
        sem3 = input("Enter your sgpa in third sem: ")
        sem3 = float(sem3)
        sem4 = input("Enter your sgpa in fourth sem: ")
        sem4 = float(sem4)
        sem5 = input("Enter your sgpa in fifth sem: ")
        sem5 = float(sem5)
        sem6 = input("Eneter your sgpa in sixth sem: ")
        sem6 = float(sem6)
        sem7 = input("Enter your sgpa in seventh sem: ")
        sem7 = float(sem7)
        sem8 = input("Enter your sgpa in eighth sem: ")
        sem8 = float(sem8)
        cgpa = (sem1+sem2+sem3+sem4+sem5+sem6+sem7+sem8)/8
        cgpa = float(cgpa)
        print(f"Your CGPA Is {cgpa}")
    #fiveyearcourse  
    elif totalsem == 10:
        sem1 = input("Enter yur sgpa in first sem: ")
        sem1 = float(sem1)
        sem2 = input("Enter your sgpa in second sem: ")
        sem2 = float(sem2)
        sem3 = input("Enter your sgpa in third sem: ")
        sem3 = float(sem3)
        sem4 = input("Enter your sgpa in fourth sem: ")
        sem4 = float(sem4)
        sem5 = input("Enter your sgpa in fifth sem: ")
        sem5 = float(sem5)
        sem6 = input("Eneter your sgpa in sixth sem: ")
        sem6 = float(sem6)
        sem7 = input("Enter your sgpa in seventh sem: ")
        sem7 = float(sem7)
        sem8 = input("Enter your sgpa in eighth sem: ")
        sem8 = float(sem8)
        sem9 = input("Enter your sgpa in ninth sem: ")
        sem9 = float(sem9)
        sem10 = input("Enter your sgpa in tenth sem: ")
        sem10 = float(sem10)
        cgpa = (sem1+sem2+sem3+sem4+sem5+sem6+sem7+sem8+sem9+sem10)/10
        cgpa = float(cgpa)
        print(f"Your CGPA Is {cgpa}")
    else:
        print("You entered wrong number of semesters.")

#avergaecgparequiredtoattainthegoal
def desirecgpa(totalsem,cgpa):
    totalsem = int(input("Enter the number of semester in your academic year: "))
    if totalsem == 2:
        cgpa = input("Enter the desired CGPA you want to get: ")
        cgpa = float(cgpa)     
        desiredcgpa = cgpa/2
        print(f"The averaga sgpa you need to get every sem is {2*desiredcgpa} ")
    elif totalsem == 4:
        cgpa = input("Enter the desired CGPA you want to get: ")
        cgpa = float(cgpa)     
        desiredcgpa = cgpa/4
        print(f"The averaga sgpa you need to get every sem is {4*desiredcgpa} ")
    elif totalsem == 6:
        cgpa = input("Enter the desired CGPA you want to get: ")
        cgpa = float(cgpa)     
        desiredcgpa = cgpa/6
        print(f"The averaga sgpa you need to get every sem is {6*desiredcgpa} ")
    elif totalsem == 8:
        cgpa = input("Enter the desired CGPA you want to get: ")
        cgpa = float(cgpa)     
        desiredcgpa = cgpa/8
        print(f"The averaga sgpa you need to get every sem is {8*desiredcgpa} ")    
    elif totalsem == 10:
        cgpa = input("Enter the desired CGPA you want to get: ")
        cgpa = float(cgpa)     
        desiredcgpa = cgpa/10
        print(f"The averaga sgpa you need to get every sem is {10*desiredcgpa} ")
    else:
        print("You entered the wrong number of semesters")

main(choice)
#end  

