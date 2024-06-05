"""Example of overloading arithmetic operators like:

+ : __add__(self, other)  - : __sub__(self, other) * : __mul__(self, other) / : __truediv__(self, other)
// : __floordiv__(self, other) % : __mod__(self, other) ** : __pow__(self, other) == : __eq__(self, other)
!= : __ne__(self, other) < : __lt__(self, other) <= : __le__(self, other) > : __gt__(self, other) >= : __ge__(self, other)
[] : __getitem__(self, key) []=: __setitem__(self, key, value) () : __call__(self, *args, **kwargs) len(): __len__(self) 
"""

"""It makes operations to be written in a clean, intuitive way, enhancing code readability and maintainability.""" 

class Money:
      def __init__(self, amount):
          self.amount = amount

      def __add__(self, other):
          return Money(self.amount + other.amount)

      def __repr__(self):
          return f"${self.amount}"

mon = Money(25)
mon_2 = Money(18)
total_mon = mon + mon_2
print(total_mon)
