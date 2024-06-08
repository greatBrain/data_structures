from abc import ABC, abstractmethod

# Data Processing Pipeline example using OOP and Interface concept.
# Formal Interface:

class DataProcessor(ABC):

      @abstractmethod
      def get_source(self) -> str:
          pass

      @abstractmethod
      def extract_data(self) -> str:
          pass

      @abstractmethod
      def transform_data(self, data) -> str:
          pass

      @abstractmethod
      def load_data(self, data):
          pass





# CSV Processor  in an example manner, just to show how clases implement interfaces and uses its methods.
# Overrides the DataProcessor Interface methods:

class CSVProcessor(DataProcessor):

      def get_source(self) -> str:
          data_source = "source_path"
          return data_source

      def extract_data(self) -> str:
          return f"data extracted from {self.get_source()}"

      def transform_data(self, data) -> str:
          return "Data transformed from the extracted method."

      def load_data(self, data):
          return "Loading data to any place (Cloud, data base,  data warehouse, etc you mean.)"








# JSON Processor  in an example manner, just to show how clases implement interfaces and uses its methods.
# Overrides the DataProcessor Interface methods. The same approach.:

import json

class JSONProcessor(DataProcessor):

      def get_source(self) -> str:
          data_source = "source_path"
          return data_source

      def extract_data(self) -> str:
          return f"data extracted from {self.get_source()}"

      def transform_data(self, data) -> str:
          return "Data transformed from the extracted method."

      def load_data(self, data):
          return "Loading data to any place (Cloud, data base,  data warehouse, etc you mean.)"





# To run the pipeline program and make the magic happen:
if __name__=="__main__":
   def run_pipeline(processor = DataProcessor):
       data = processor.extract_data()
       transformed_data = processor.transform_data(data)
       processor.load_data(transformed_data)


   csv_processor = CSVProcessor()
   json_processor = JSONProcessor()


   # Run the run_pipeline method, that's awating for DataProcessor type object.
   # with the csv and json processors objects.

   run_pipeline(csv_processor)
   run_pipeline(json_processor)
