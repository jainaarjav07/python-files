input("Name Of The Student: ")
input("Roll No.: ")
a=int(input("Marks Obtained By The Student:"))
if(a>=90):
    print("The Student got the grade:'A+'")
elif(a<90 and a>=80):
    print("The Student got the grade:'A'")
elif(a<80 and a>=75):
    print("The Student Got The Grade:'B'")
elif(a<75 and a>=60):
    print("The Student Got The Grade:'C'")
elif(a<60 and a>=40):
    print("The Student got the grade:'D'")
elif(a<40):
    print("The Student got the grade:FAIL")