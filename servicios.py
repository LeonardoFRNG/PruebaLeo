def add_student(data):
    # add ID
    valid = False
    while not valid:
        try:
            identificator = int(input("Enter the ID: \n"))
            if identificator < 0:
                print("You can only enter positive values.")
            else:
                valid = True
        except:
            print("Invalid ID, try again.")

    # add name
    valid = False
    while not valid:
        name = input("Enter the student name: \n")
        if name.replace(" ", "").isalpha():
            valid = True
        else:
            print("You can only enter letters in the name, try again.")

    # add age
    valid = False
    while not valid:
        try:
            age = int(input("Enter the age: \n"))
            if age < 0:
                print("You can only enter a positive age value.")
            else:
                valid = True
        except:
            print("Invalid age, try again.")

    # add course or program
    course = input("Enter the course or program name: \n")
    
    #add state
    state = input("Enter the student state (Active/Inactive): \n")

    students = {
        "identificator": identificator,
        "name": name,
        "age": age,
        "course": course,
        "state": state,
    }
    data.append(students)
    print(f"The student: {name} wass added succesfully.")


def show_students(data):
    if len(data) == 0:
        print("there is no student.")
    else:
        print("current students: ")

        for students in data:
            print("-" * 45)
            print(f"ID: {students['identificator']}")
            print(f"Nombre: {students['name']}")
            print(f"Edad:  {students['age']}")
            print(f"Course or program: {students['course']}")
            print(f"State: {students['state']}")
            print("-" * 45)


def search_student(data):
    name = input("Enter the name of the student to search for: \n")

    for students in data:
        if students["name"].lower() == name.lower():
            print("-" * 45)
            print(f"ID: {students['identificator']}")
            print(f"Name: {students['name']}")
            print(f"Age:  {students['age']}")
            print(f"State: {students['state']}")
            print("-" * 45)
            return students
    print("-" * 45)
    print(f"The student: {name} is not in our database.")
    print("-" * 45)
    return None


def update_student(data):
    # ID, Name, age, program, state
    name = input("Enter the name of the student to update: \n")

    
    for students in data:
        if students["name"].lower() == name.lower():
            students = students
            break
        
        print(f"The student: {name} was not found.")
        return 

    #upload id
    valid = False
    while not valid:
        try:
            new_id = float(input(f"Enter the new ID (current: {students['identificator']}): \n"))
            if new_id< 0:
                print("The new id must be positive, try again.")
            else:
                students["identificator"] = new_id
                valid = True
        except ValueError:
            print("Invalid value, enter again.")
            
    #upload name
    valid = False
    while not valid:
        new_name = input(f"Enter the student's name (current: {students['name']}): \n")
        if new_name.replace(" ", "").isalpha():
            students['name'] = new_name
            valid = True
        else:
            print("You can only enter letters in the name, try again.")
        
    #update age
    valid = False
    while not valid:
        try:
            new_age = float(input(f"Enter the new age (current: {students['age']}): \n"))
            if new_age < 0:
                print("Enter the new age(current: new age must be positive, try again.")
            else:
                students["age"] = new_age
                valid = True
        except ValueError:
            print("Invalid value, enter again.")
            
    #update course
    valid = False
    while not valid:
        new_course = input(f"Enter the name of the new course or program (current: {students['course']}): \n")
        if new_course.replace(" ", "").isalpha():
            students['course'] = new_course
            valid = True
        else:
            print("You can only enter letters in the new course or program, try again.")  
            
    #update state
    valid = False
    while not valid:
     new_state = input(f"Enter the new status to change, active/inactive)(current: {students['state']}): \n")
     
     if new_state.lower() == "active":
        students['state'] = "active"
        valid = True
        
     elif new_state.lower() == "inactive":
         students['state'] = "inactive"
         valid = True
     else:
        print("Invalid option")    
    

def delete_student(data):
    name = input("Enter the student to delete: \n")
    
    for students in data:
        if students['name'].lower() == name.lower():
            data.remove(students)
            print(f"The student {name} was successfully deleted.")
            return
    print(f"The student: {name} is not in our database.")