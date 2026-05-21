

# Exercise 1: Perform basic dictionary operations

# d1={"First Name":"Prathik","Last name":"Patel","Gender":"Male","age": 30}
# print(d1)
# print(d1["Last name"])
# d1["city"]="Banglore"
# print(d1)
# d1["age"]=20
# print(d1["age"])

# Exercise 2: Perform dictionary operations

# del d1["Gender"]
# print(d1)

# Exercise 3: Dictionary from Lists

# a=["Prathik","Patel","Banglore"]
# b=["name","last name","City"]
# d2=dict(zip(a,b))
#print(d2)

# Exercise 4: Clear Dictionary

#d2.clear()
#print(d2)

# Exercise 5: Merge two Python dictionaries into one

# d3=(d1,*d2)
# print(d3)

# Exercise 6: Count Character Frequencies

name="Prathik"

# Exercise 7: Access Nested Dictionary

nested_student_dict = {
    "class": {
        "student": {
            "name": "Jessa",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
print(nested_student_dict["class"]["student"]["name"])

# Exercise 8: Print the value of key ‘history’ from nested dict

print(nested_student_dict["class"]["student"]["marks"]["history"])

# Exercise 9: Modify Nested Dictionary

nested_student_dict["class"]["student"]["marks"]["physics"]=100
print(nested_student_dict)

# Exercise 10: Initialize dictionary with default values

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
# Expected output:
var=dict.fromkeys(employees,defaults)
print(var)
# {'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}