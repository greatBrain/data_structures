# Patient care using Prioriry Queues:

"""
REQUERIMENTS
============

Let's say you are developing a Patient Management System for a medical clinic.
At this clinic, patients may have different levels of severity in their medical conditions,
and it is crucial to see the most critical patients first.

The system should allow doctors to add new patients with their medical information and severity level,
and then, based on severity priority, decide which patient should be seen next.

The task is to implement this system using a Priority Queue.
Patients will be represented as objects with attributes such as "name", "age", "medical condition" and "severity level".
"""


class Patient:
      def __init__(self, name:str, age:int, medical_condition:str, severity_level:int):
          self.name:str = name
          self.age:int = age
          self.medical_condition:int = medical_condition
          self.severity_level:int = severity_level

      def get_patient(self):
          return (self.name, self.age, self.medical_condition, self.severity_level)



import heapq

class Patient_Attention:
      def __init__(self, patient_name:str, age:int, medical_condition:int, severity_level:int):
          self.patient_name:str = patient_name
          self.age:int = age
          self.medical_condition:str = medical_condition
          self.severity_level:int = severity_level
          self.patient_data = (self.patient_name, self.age, self.medical_condition, self.severity_level)

          self.queue = []
          self.patient_instance = Patient(self.patient_name, self.age, self.medical_condition, self.severity_level)


      def patient_exists(self) -> bool:
          if self.patient_data == self.patient_instance.get_patient():
             return True
          return False


      def queue_is_empty(self):
           return len(self.queue)==0


      def push_queue(self):
          if self.patient_exists():
             heapq.heappush(self.queue, (-self.severity_level, self.patient_name))

          new_patient = Patient(self.patient_name, self.age, self.medical_condition, self.severity_level)


      def pop_queue(self):
          if not self.queue_is_empty():
             heapq.heappop(self.queue)[-1]


if __name__=="__main__":
   patient = Patient_Attention("Mercy", 24, "Bonquitis", 1)
   patient = Patient_Attention("Holy", 32, "Cancer", 4)
   patient.push_queue()

