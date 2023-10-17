'''Fizz Buzz problems who stands that if any number inside a collection of 
numbers is divisible for its Fizz, if it is divisible for 5 its Buzz.'''

nums = [1,2,3,4,5,6,7,8,9]
#i.e. here 3 is Fizz and 5 is Buzz

for num in range(len(nums)):
   if num%3==0:
      print("{} is fizz".format(nm))
   elif num%5==0:
      print("{} is buzz".format(num))
