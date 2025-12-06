info = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
    ("Charlie", "English"),
]

# unique_courses = set()

# for i in info:
#     unique_courses.add(i[1])


# print(unique_courses)


for name, course in info:
    if(course == "English"):
        print(name)
