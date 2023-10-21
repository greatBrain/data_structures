''' Understanding what Python Set data 
type is deeply and how to apply it into real world problems.
Author: Mr. Fana 2023 '''

#Finding common items of two sets by comparing 'em
def compare_users():

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


# Makin' a copy of a set:
def get_copy():
    set_1 = {1, 2, 3, 4}
    print("I'm the original set", " ", set_1)


    set_2 = set_1.copy()
    print("I'm the copy set", " ", set_2, "\n") 
    # As we can see here, is exactly the same data duplicated
    # and it's shown below throw the memory address in buffer of each variable:

    print("I am the memory address of the original set:", "",  id(set_1))
    print("I am the memory address of the copy set:", "", id(set_2))

#get_copy()

#Getting the difference of two sets:
def get_difference():
    set_a = {1, 22, 8, 4}
    set_b = {1, 2, 3, 4, 5, 6}
    set_c = set_b.intersection(set_a) 

    return set_c  # It should be '1 and 4'

#print(get_difference())







''' Practice '''
''' Checking for Anagrams: Use sets to check if two strings are anagrams of each other by comparing the sets of characters in each string. '''

def is_anagram(first_word=str, second_word=str):
    first_word = set(first_word)
    second_word = set(second_word)

    if (first_word ^ second_word):       
       return False    
    return True

print(is_anagram("ROMA", "OMZAR"), "\n")
print(is_anagram("IEVL", "LIVE"), "\n")

'''As we can see in the above code, the function 'is_anagram' is executed twice
the first one recives two str parameter, a little bit differents and should return False because we can not get a anagram.
The second function calling recives the same string twice just unordered, but they are the same. And the is_anagram function 
should return True.'''



