# In this code we are evaluating the grade of a student based on their obtained marks out of hundred

marks = float(input("what's your obtained marks? "))

if(marks >= 85 and marks <= 100):
    print("Grade A")
elif(marks >= 60 and marks <=84):
    print("Grade B")
elif(marks >=40 and marks <=59):
    print("Grade C")
elif(marks >=33 and marks <=30):
    print("Grade D")
else:
    print("YOU HAVE FAILED THE TEST! STUDY THE FUCKING HARD.")




# we can shorten this logic also: 
marks = float(input("what's your obtained marks? "))

if(marks >= 85):
    print("Grade A")
elif(marks >= 60):
    print("Grade B")
elif(marks >=40):
    print("Grade C")
elif(marks >=33):
    print("Grade D")
else:
    print("YOU HAVE FAILED THE TEST! STUDY THE FUCKING HARD.")