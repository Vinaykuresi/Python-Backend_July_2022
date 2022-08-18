
# while loops : 
# total_no_of_bags = 50

# while(total_no_of_bags > 0):
#     picked_up_bags = int(input("Enter the Number of Bags : "))
#     if(picked_up_bags <= total_no_of_bags):
#         total_no_of_bags -= picked_up_bags
#         print("Remaining No of Bags : ", total_no_of_bags)
#     else:
#         print("The Given value ", picked_up_bags, " is greater than the remaining bags : ", total_no_of_bags)


# example of Infinte Loop
# num = 10
# count = 0

# while(count < num):
#     print("Count Value : ", count)
#     count -= 1

# for loops : 
# list, tuple, dictionary, set, string or a range

# c, c++, java, javascript, go : 
# for(var i=0; i<limit; i++){

# }

# Queue : first in first out
# passanger_count = 1
# print("€first passanger completed : ", passanger_count)
# passanger_count += 1
# print("€first passanger completed : ", passanger_count)
# passanger_count += 1
# print("€first passanger completed : ", passanger_count)
# passanger_count += 1
# print("€first passanger completed : ", passanger_count)

# for loop
# for passanger in 1,2,3,4,5:
#     print("€first passanger completed : ", passanger)

# for passanger in range(5):
#     print("€first passanger completed : ", passanger+1)

# Triangle and Pyramid : 
'''
*
**
***
****
*****
'''

rows = int(input("Enter the No. of Rows : "))

for row in range(rows):
    for col in range(row+1):
        print("*", end="")
    print()

'''
    *
   **
  ***
 ****
***** 
'''

for row in range(rows):
    for col in range(rows-row-1):
        print(" ", end="")
    for col in range(row+1):
        print("*", end="")
    print()

star = "**********"
for row in range(rows):
    for col in range(rows-row-1):
        print(" ", end="")
    print(star[0:row+1])

# Assignment : 

'''
*****
****
***
**
*
'''
