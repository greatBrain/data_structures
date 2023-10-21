# Small program to delete duplicate data. This using sets.
def set_data():
    numbers = [5, 5, 25, 10, 1, 2, 2]
    return numbers


def clean_data():
    return list(set(set_data()))


def get_data():
    return clean_data()

#print(get_data())


'''   '''

def compare_users():
    #Compare data of two sets to find common items
    sytem_users_2022 = {"Bobby", 
                        "Ramon", 
                        "Julieta", 
                        "Sabrina", 
                        "Meredith"
                        }

    sytem_users_2023 = {"Lisa", 
                        "Ramona", 
                        "Julieta", 
                        "George", 
                        "Maritza", 
                        "Sabrina",
                        }
    
    users = list(sytem_users_2022 & sytem_users_2023)
    return users

#print(compare_users())



'''   '''

# Makin' a copy of a set:
def copy_set():
    set_1 = {1, 2, 5}
    print("I am the original set:", " ", set_1)
    
    set_2 = set_1.copy()
    print("I am the copy set:", " ", set_2)

copy_set()
