import math

emp_ids = []

employee_strength = 100

id = 1000

for employee in range(employee_strength):
    id += 1
    emp_ids.append(id)

print(emp_ids)

emp_ids[0] += 1
emp_ids[1] += 2
emp_ids[2] += 3


for index in range(4, employee_strength):
    boolean = True
    # print(math.ceil(math.sqrt(index+1)))
    for num in range(2, index+1):  O nsquare
    for num in range(2, int(index+1)/2): On(logn)
    for num in range(2, (math.ceil(math.sqrt(index+1)))+1): On
        if((index+1)%num == 0):
            boolean = False
            break

    if(boolean == True):
        emp_ids[index] += index+1

print(emp_ids)
    
    


