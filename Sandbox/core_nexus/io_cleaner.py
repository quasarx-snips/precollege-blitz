import re
class DataCleaner:

      def load_and_clean(self, path):
          with open(path, 'r', encoding='utf-8') as file:
            text = file.read()
            text = re.sub(r'\s+', ' ', text)
            text = text.lower()
            text = text.encode('ascii', 'ignore').decode('ascii')
            text = text.strip()
          
          return text

if __name__ == "__main__":
  cleaner = DataCleaner()
  print(cleaner.load_and_clean("../../assets/datasets/raw_text.txt")[:100])