# global variable
num = 30

def add():
    # Local Variable
    global num_1
    num_1 = 60
    print("Addition : ", num+num_1)

def sub():
    # Local Variable
    num_2 = 60
    print("Subtraction : ", num_1-num_2)

# print("Addition : ", num+num_11)
add()
sub()