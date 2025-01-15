class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}, {self.age}岁"
    
    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

p = Person("小明", 20)

print(p)

print(str(p))   # 输出: 小明, 20岁

print(repr(p))  # 输出: Person('小明', 20)
