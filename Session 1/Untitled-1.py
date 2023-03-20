class candidate: 
  region = '서울 성북 병'
  
  def _init_(self, name, gender, age, number, rating):
      self.name=name
      self.gender=gender
      self.age=age
      self.number=number
      self.rating=rating   
chae = candidate("채윤", "m", 47, 1, 2.5)
jo = candidate("조원경", "f", 50, 56, 20.5)
print(chae.gender)