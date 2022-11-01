my_file = open("nationsPop.txt", 'r')
lines = my_file.readlines()
country_pop_data = []
for file_line in lines:
    split_pop_line = file_line.split(',')
    country_data = {
        'name':split_pop_line[0],
        'pop': int(split_pop_line[1]),
        'change':float(split_pop_line[2])
    }
    country_pop_data.insert(0,country_data)

while True:
    print("========Please selection from the following:=======")
    print("[1] Find country with smallest Population")
    print("[2] Find country with the largest population")
    print("[3] Add a new Country")
    print("[4] End the program")
    print("====================================================")
    user_selection = input("Your choice 1-4:")
    if user_selection == '1':
        smallest_so_far = country_pop_data[0]
        for current_country in country_pop_data:
            if current_country['pop'] < smallest_so_far['pop']:
                smallest_so_far = current_country
        print(f"{smallest_so_far['name']} is the smallest country with population {smallest_so_far['pop']}")
    elif user_selection == '2':
        if user_selection == '2':
            largest_so_far = country_pop_data[0]
            for current_country in country_pop_data:
                if current_country['pop'] > largest_so_far['pop']:
                    largest_so_far = current_country
            print(f"The largest pop country is {largest_so_far['name']}")
    elif user_selection == '3':
        country_name = input("Please enter the name of the new country")
        country_pop = int(input(f"enter the population{country_name}:"))
        country_change = float(input(f"How much did {country_name}'s population change 2021-2022"))
        new_country = {
            "name": country_name,
            'pop': country_pop,
            'change': country_change
        }
        country_pop_data.append(new_country)
    elif user_selection == '4':
        exit(0)
        #you do this one
    else:
        print("Invalid Selection, please choose 1-4")