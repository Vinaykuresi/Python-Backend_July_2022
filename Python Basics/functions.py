# def is used to define the function
# function definition
def add(num1, num2): # formal arguments or parameters
    sum = num1+num2
    # returning the sum result
    return sum

# here we are catching the result
# function calling
result = add(10, 20) # actual argument

print("The sum of Number : ", result)

def calculate_current_no_of_flights(initial_no_of_flights, take_off_flights, landed_flights):
    current_no_of_flights = initial_no_of_flights - take_off_flights + landed_flights
    return current_no_of_flights

current_no_of_flights = calculate_current_no_of_flights(100, 20, 13)
print("Current no of flights : ", current_no_of_flights)