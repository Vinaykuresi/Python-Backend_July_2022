range(5)
range(0, 5)
>>> num = range(5)
>>> num
range(0, 5)
>>> num[0]
0
>>> num[len(num)-1]
4
>>> # 0,1,2,3,4
>>> num[(5-1)]
4
>>> ticket_1  = 1234
>>> ticket_100 =4321
>>> ticket_2 = 1235
>>> ticket_3 = 1236
>>> tickets = [1221, 1222, 1223, 1224, 1225]
>>> tickets[0]
1221
>>> tickets[1]
1222
>>> tickets[len(tickets)-1]
1225


sample_list = [] -> creating a list
sample_list = ["Vinay", "Naveen", "Kumar", 2, 3, 4] -> with known size and known elements, and heterogeneous
sample_list = [None]*5 -> with known size and unknown elements
len(sample_list) -> Length of List

sample_list = []
print(type(sample_list))

sample_list = ["Vinay", "Naveen", "Kumar", 2, 3, 4]
print(sample_list)

sample_list = [None]*10
print(sample_list)
sample_list[9] = "Vinay"
print(sample_list)
# sample_list[10] = "Kumar"
# print(sample_list)

print(len(sample_list))

sample_list = []
print(type(sample_list))

sample_list = ["Vinay", "Naveen", "Kumar", 2, 3, 4]
print(sample_list)

sample_list = [None]*10
print(sample_list)
sample_list[9] = "Vinay"
print(sample_list)
# sample_list[10] = "Kumar"
# print(sample_list)

print(len(sample_list))

# random read
print(sample_list[9])
print(sample_list[len(sample_list)-1])

# random write
sample_list[5] = "Kumar"
print(sample_list)

sample_list.append("Kuresi")
print(sample_list)

random = [12, 23, "Garuda"]
sample_list += random # sample_list = sample_list + random
print(sample_list)






