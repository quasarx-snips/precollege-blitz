from io_cleaner import DataCleaner
import json

class Tokenizer:
  def __init__(self):
    self.stoi = {}
  
  def fit(self, text):
    for i in sorted(list(set(text))):
      if i not in self.stoi:
        self.stoi[i]=(len(self.stoi)+1)
      else:
        pass
    return self.stoi

  def save_vocab(self, path):
    with open("../../assets/datasets/vocabulary.json", "w") as f:
      json.dump(self.stoi, f)
    
  def encode(self, char):
      encoded =[]
      for i in char:
        try:
          encoded.append(self.stoi[i.lower()])
        except KeyError:
          encoded.append(0)
      return encoded  
    
  def decode(self, idx):
      inv = {value:key for key, value in self.stoi.items()}
      decoded=[]
      for i in idx:
        try:
          decoded.append(inv[i])  
        except KeyError:
          decoded.append("<?>")

      return "".join(decoded)
  def load_vocab(self, path):
    with open(path, "r") as f:
        self.stoi = json.load(f)

  def get_training_pairs(self,text,block_size=5):
    data = self.encode(text)
    inputs = []
    targets =[]
    for i in range(len(data)-block_size):
      inputs.append(data[i:block_size+i])
      targets.append(data[i+block_size])

    return inputs,targets
      
if __name__ == "__main__":
  tokenizer = Tokenizer()
  cleaner = DataCleaner()

  tokenizer.fit(cleaner.load_and_clean("../../assets/datasets/raw_text.txt"))
  tokenizer.save_vocab("../../assets/datasets/vocabulary.json")
  sample_text = "Bibhab"
  inputs, targets = tokenizer.get_training_pairs(sample_text, block_size=2)

  print("\n--- Training Pairs ---")
  for inpt, tgt in zip(inputs, targets):
      print(f"Input: {inpt} -> Target: {tgt}")


        
      