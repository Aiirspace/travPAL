studentList = []


def file_parse(fileName, deliminator):
    file = open(fileName, "r")
    fileData = file.readlines()
    file.close()
    for line in fileData:
        split_line = line.split(deliminator)
        studentName = split_line[0]
        studentNumber = int(split_line[1])
        studentCredits = int(split_line[2])
        studentGPA = float(split_line[3])

        studentList.append({
            "name": studentName,
            "id": studentNumber,
            "credits": studentCredits,
            "gpa": studentGPA
        })
def menu():
    option = input("""Please choose an option 1-4:
    [1] Add a student
    [2] Find masters students
    [3] Find probation students
    [4] Find honors students
    [5] Exit
    ?""").strip()
    if option == "1":
        add()
    elif option == "2":
        find_masters()
    elif option == "3":
        find_prob()
    elif option == "4":
        find_honors()
    elif option == "5":
        exit()
    else:
        print("Invalid Option!")
        menu()
if option == 1:
    smallest_so_far = country_pop_data[0]
    for current_country in country_pop_data:
        if current_country['pop'] < smallest_so_far['pop']:
            smallest_so_far = current_country
            print(f"{smallest_so_far['name']} is the smallest country with population {smallest_so_far['pop']")
        elif user_selection == '2':
else:
    print("Invalid Selection, please choose 1-4")
file_parse("students.txt", "|")
print(studentList)

