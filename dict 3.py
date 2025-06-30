# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.
marks_dict = {}

x = int(input("Enter marks for subject 1: "))
marks_dict.update({"subject1": x}) 

x = int(input("Enter marks for subject 2: "))
marks_dict.update({"subject2": x})

x = int(input("Enter marks for subject 3: "))
marks_dict.update({"subject3": x})

print("Marks Dictionary:", marks_dict) # {'subject1': 85, 'subject2': 90, 'subject3': 78}
