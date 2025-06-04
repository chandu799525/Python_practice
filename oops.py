class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def greet(self):
        print(f"hi {self.name} your age is {self.age}")


p1=person("chandu",23)
p1.greet()            