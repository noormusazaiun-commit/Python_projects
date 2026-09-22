students = []


passed=0
failed=0

for i in range(int(input("how many Students you want to add "))):
    print("\nstudent",i+1)
    name =input("Enter your name ")
    math=float(input("math : "))
    python=float(input("python : "))
    data=float(input("data : "))

    totalmarkes=math+python+data
    avg=totalmarkes/3
    
    if avg >90:
        Grade ="A"
    elif avg>80:
        Grade ="B"
    elif avg>70:
        Grade ="C"
    elif avg>55:
        Grade ="D"
    else:
        Grade="Z"



    if avg>55:
        states="Passed"
        passed +=1
    else:
        states="Failed"
        failed +=1

    student = {
    'name':name,
    'total':totalmarkes,
    'avrage':avg,
    'states':states,
    'Grade' :Grade
    }


    students.append(student)

    
cavg=0

print("==========================================Results========================================")
for student in students:
    print(student["name"])
    print("states : ",student['states'])
    print('Grade : ',student['Grade'])
    print('avrege : ',round (student["avrage"],2))
    print('total : ',student['total'],"\n")
    cavg +=student['avrage']

print(f"passed {passed} ")
print(f"failed {failed} ")
havg=0
lavg=100

for student in students:
    if student['avrage']<lavg:
        lavg=student['avrage']

for student in students:
    if student['avrage']>havg:
        havg=student['avrage']


print(f"hiest avrage is {havg: .2f}") 
print(f"loest avrage is {lavg: .2f}")
print(f"class avrage is {cavg:.2f}")
