class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
    def yell(self):
        print("아?")
    def introduce(self):
        print(f"내 이름은 {self.name}이고, 나이는 {self.age}이며, 키는 {self.height}입니다.")

class Developer(Person):
    def yell(self):
        print("어?")
        keyboard: "기계식"

class Designer(Person):
    def __init__(self, name, age, height, disease):
        super().__init__(name, age, height)
        self.disease=disease

class ProductManager(Person):
    def yell(self):
        print("개발자님 여기 오류있어요.")
    def aging(self):
        self.age+=2
        self.height-=5
        print("개발자를 새로 뽑아야하나...")
        Developer.keyboard: "멤브레인"

d1=Developer("채윤석",24, 170)
d2=Designer("오박사",77, 227,"포켓몬집착증")
p1=ProductManager("이박사", 66, 180)
d1.introduce()
d1.yell()
d2.introduce()
d2.yell()
p1.introduce()
p1.yell()
p1.aging()
p1.introduce()