emp_details = {
    "name" : "Vinay",
    "education" : "MCA",
    "emp_id" : "115661",
    "profession" : "SSE",
    "other_details" : {
        "location" : "Mysore",
        "address" : "Hebbal"
    }
}

print("Employee Details : ", emp_details)

print("Employee name : ", emp_details["name"])

print("Employee details : ", emp_details["other_details"])

print("Address : ", emp_details["other_details"]["address"])
