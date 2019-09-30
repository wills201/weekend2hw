class Node:
  def __init__(self, first, next = None):
    self.first = first
    self.next = next
  def __len__(self):
    if self.next == None:
      return 1
    else:
      return 1 + len(self.next)
   def __eq__(self, other):
    while self != None or other != None:
      if self.first != other.first:
        return False
      self = self.next
      other = other.next
    return True if self == None and other == None else False
      
  def insert(self, index, num):
    if index == 0:
      new_node = Node(num)
      new_node.next = self
      self = new_node
    elif index == 1:
      new_node = Node(num)
      new_node.next = self.next
      self.next = new_node
    else:
      self.next.insert(index - 1, num)
      
  def delete(self, num):
    pass
  def search(self, num):
    pass
  def traverse(self):
    pass

    