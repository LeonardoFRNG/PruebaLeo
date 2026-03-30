from servicios import(add_student, show_students, search_student, update_student, delete_student)
from archivos import (save_csv)
data = []

valido = False
while not valido:
    print("-" * 45)
    print("Student Management System ")
    print("OPTIONS MENU: \n")
    print("1. Register new student")
    print("2. Consult list of students")
    print("3. Search student by name")
    print("4. Update student information")
    print("5. Delete student")
    print("6. Save csv")
    print("7. Exit")
    print("-" * 45)
    
    
    opcion = input("Ingrese una opcion: \n")
    
    
    if opcion == "1":
        add_student(data)
    elif opcion == "2":
        show_students(data)
    elif opcion == "3":
        search_student(data)
    elif opcion == "4":
        update_student(data)
    elif opcion == "5":
        delete_student(data)
    elif opcion == "6":
        save_csv(data)
    elif opcion == "7":
        print("You're out, come back soon!")
        valido = True
    else:
        print("Invalid option, try again.")
    
    
    
    