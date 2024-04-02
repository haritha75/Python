# if you want custom exception then we can extend the exception class
class InvalidOperationError(Exception):
  pass
class Stream:
  def __init__(self):
    self.opened = False
  def open(self):
    if self.opened:
      raise InvalidOperationError("stream  already open")  
    self.opened = True 
  def close(self):
    if not self.opened:
      raise InvalidOperationError("stream  already close")  
    self.opened = False    

class FileStream(Stream):
  def read(self):
    print("read the data from a file")    
class NetowrkStream(Stream):
  def read(self):
    print("read the data from a network")        

# if more than one subclass inherite the parent class called hierachical inheritance    