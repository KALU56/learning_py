###1
# class person():
#   def __init__(self,name,age):
#     self.name=name
#     self.age=age
#   def introduction(self):
#     return f"hi {self.name}"
# class student(person):
#   def __init__(self,name,age,course):
#     super().__init__(name,age)             
#     self.course=course
#   def intro(self):
#     return f"hi{self.name}
#     "     
# p1=person("kal",22)     
# print(p1.intro())  
# s1=student("kal",23,"eng")
# print()                                                                                                                                             
###2
class person():
  def __init__(self,name,phone_no):
    self.name=name
    self.phone_no=phone_no
  def stu(self):
    
    return f"the student name is {self.name}.{self.phone_no} "
class student(person):
  def __init__(self,name,phone_no,id):
      super().__init__(name,phone_no) 
      self.id=id
  # def stu(self):
  #   pass
      # return f"the student name is {self.name}.{self.phone_no} and id {id}"
p1=person("kal",9233409)
print(p1.stu())
s1=student("kal",9090,"dbu1601212")
print(s1.stu())
# ###3
# class vechice():
#   def __init__(self):
#    "car1","bike1"
#   def v1(self):
 
#     return f"the list of vechice {self.car}.{self.bike} "
# class ful(vechice):
#   def __init__(self,car,bike):
    
#       self.car=car
#       self.bike=bike
#   def v2(self):
#       return f"the list of vechice {self.car}.{self.bike} "
# v=vechice("car1","bike1")
# print(v.v1())
# v=ful("car1","bike1")
# print(v.v2())
    

  
   

  