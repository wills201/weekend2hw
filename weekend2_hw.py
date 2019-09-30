class HashTable:

  def __init__(self, hash_size):
    self.hash_size = hash_size
    self.table = [None] * hash_size
  def __len__(self):
    count = 0
    for i in self.table:
      if not(i is None):
        count += len(i)
    return count

  def insert(self, val):
    index = id(val) % self.hash_size
    if self.table[index] == None:
      self.table[index] = [val]
    else:
      if not(val in self.table[index]):
        self.table[index].append(val)
        
  def search(self, val):
    index = id(val) % self.hash_size
    if self.table[index] == None:
      return False
    return val in self.table[index]
    
  def traverse(self):
    trav_lst = []
    for i in self.table:
      if i is not None:
        trav_lst.append(i)
    return trav_lst
    
  def delete(self, val):
    index = id(val) % self.hash_size
    for val in self.table:
      if val 
    




table = HashTable(10)
table.insert(15)
table.insert(25)
table.insert(35)
table.insert(30)
table.insert(33)
print(table.traverse())