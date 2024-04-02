class TagCloud:
  def __init__(self):
    self.tags={} #declare dictionary
  def add(self,tag):
    self.tags[tag] = self.tags.get(tag,0)+1

cloud=TagCloud()
cloud.add("Pthon")
cloud.add("Pthon")      
cloud.add("Pthon")      
print(cloud.tags)      

cloud=TagCloud()
cloud.add("pthon")
cloud.add("Pthon")      
cloud.add("Pthon")      
print(cloud.tags) 

# to prevent case sensitive

class TagCloud:
  def __init__(self):
    self.tags={} #declare dictionary
  def add(self,tag):
    self.tags[tag.lower()] = self.tags.get(tag.lower(),0)+1

cloud=TagCloud()
cloud.add("pthon")
cloud.add("Pthon")      
cloud.add("Pthon")      
print(cloud.tags) 

# like we can make customer container

class TagCloud:
  def __init__(self):
    self.tags={} #declare dictionary
  def add(self,tag):
    self.tags[tag.lower()] = self.tags.get(tag.lower(),0)+1
  def __getitem__(self,tag):
    return self.tags.get(tag.lower(),0)
  def __setitem__(self,tag,count):
    self.tags[tag.lower()] = count  

  def __len__ (self):
    return len(self.tags) 

  def __iter__(self):
    iter(self.tags) # it iterates each items at a time

cloud=TagCloud()
cloud["python"] # reading
cloud["python"] =10 #setting data
cloud.add("pthon")
cloud.add("Pthon")      
cloud.add("Pthon")      
print(cloud.tags) 

print(cloud.tags["python"]) # we will get correct output because everthing stored lower case if you read upper case got error
# print(cloud.tags["Python"]) # got error because all are lower case  to prevent this use private members we cannot acess outside

# private memebers

class TagCloud:
    def __init__(self):
        self.__tags = {}  # declare dictionary __tags represent private memeber

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count  

    def __len__(self):
        return len(self.__tags) 

    def __iter__(self):
        return iter(self.__tags)
    
cloud=TagCloud()
cloud["python"] # reading
cloud["python"] =10 #setting data
cloud.add("pthon")
cloud.add("Pthon")      
cloud.add("Pthon")      
     
# print(cloud.tags["Python"]) # now it shows not defined means we cannot acess outsides
# technically we can access it
print(cloud.__dict__) # python reads the code gives some data like class name along with attrribute
print(cloud._TagCloud__tags) # based providing that data we can print this one  even if the attribute private