student = {
    "Nabila" : {
        "Roll"  : "011",
        "Department" : "RME",
        "Faculty" : "Engineering and Technology"
        },
    "Tahwa" : {
        "Roll"  : "050",
        "Department" : "RME",
        "Faculty" : "Engineering and Technology"
        },
    "year" : 1987
}

print(student["Tahwa"])

x = student.get("Nabila")
print(x)

y = student.keys()
print(y)

z = student.values()
print(z)