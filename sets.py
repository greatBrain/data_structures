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





# Unifying two or more sets:
def get_union():
    set_x = {"Perla", "Lucas", "George", "Maria"}
    set_y = {"Arlinna", "Andrea", "Mirabal", "Jose"}
    print("Set x:", set_x, " ", "set_y:", set_y, "\n")

    '''In some cases, we may need to unify two or more sets for some purpose, 
    As the others operations there are two ways to do that: Using Python set built-in method named union (just like mathematics) 
    or by operators:'''
    
    #Union by method.
    set_Z = set_x.union(set_y)
    print("Conjunto unificado por metodo:", set_Z)


    #Union by operator:
    set_op = set_x | set_y
    print("Conjunto unificado por operador:", set_op)

#get_union()





''' Practice '''
''' Checking for Anagrams: Use sets to check if two strings are anagrams of each other by comparing the sets of characters in each string. '''

def is_anagram(first_word=str, second_word=str):
    first_word = set(first_word)
    second_word = set(second_word)

    if (first_word ^ second_word):       
       return False    
    return True

#print(is_anagram("ROMA", "OMZAR"), "\n")
#print(is_anagram("IEVL", "LIVE"), "\n")

'''As we can see in the above code, the function 'is_anagram' is executed twice
the first one recives two str parameter, a little bit differents and should return False because we can not get a anagram.
The second function calling recives the same string twice just unordered, but they are the same. And the is_anagram function 
should return True.'''






''' Diving deeper'''
''' ============'''


'''There's another built-in type of sets in Python named 'frozenset' (sounds like an horror movie, right? :V ) 
which is in all respects exactly like a set, except that a frozenset is immutable (indeed). 
What can u do with it? You can perform non-modifying operations on a frozenset:
'''

def get_frozenset():

    f = frozenset(['foo', 'bar', 'baz'])

    ''' Without any operation that attempt to modify the set object, we can do every operation on it, like a normal set:'''
    print(len(f))

    #Compare with other:
    n = {'bird', 'block', 'bass'}
    print(f & n)

    '''Frozensets are useful in situations where we want to use a set, but we need an immutable object'''



#Set comprehension.
#As lists, sets can be comprehenssed:

def set_comprehension():
    p = {a+a for a in range(10)}
    print(p)

set_comprehension()   