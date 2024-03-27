# Colas de Prioridad:
import heapq

class Queue:
      def __init__(self):
          self.queue:list = []

      def _queue_is_empty(self):
          return len(self.queue)==0


      def push_to_queue(self, data:str, priority_value:int) -> None:
          heapq.heappush(self.queue, (data, priority_value))


      def pop_from_queue(self) -> None:
          if not self._queue_is_empty():
             heapq.heappop(self.queue)[-1]

          return False

      def get_queue(self):
          if not self._queue_is_empty():
             return self.queue

          return f"The queue list is empty: {self.queue}"



    """ For a fixed size queue, we may want to use -- heapq.heappushpop. ---
    This method pushes a new value and pops the minimun value from the queue."""


if __name__=="__main__":
   queue_instance = Queue()
   queue_instance.push_to_queue("Completar despliegue a produccion", 5)
   queue_instance.push_to_queue("Realizar cambios en el archivo de instalacion de
Skillet", 2)
   queue_instance.push_to_queue("Eliminar branches del anio pasado", 2)
   queue_instance.push_to_queue("Agregar tabla Customers_report a la base de datos", 5)
   queue_instance.push_to_queue("Realizar un kernel tracking por el fallo de la
aplicacion", 1)
   print(queue_instance.get_queue())