#Employee little system, for showing the concept of inheritance

# Base class, works as an interface:
class Employee:
      def __init__(self, name, emp_id, salary):
          self._name = name
          self._id = emp_id
          self.salary = salary

      
      # Common method implemented for ervery type of employee and will be overwrited.
      def get_employee_work(sef):
          pass


# Manager employee
class Manager(Employee):
      pass

