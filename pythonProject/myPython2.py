# class / object

class Person:
    def __init__(self, person_name):
        self.person_name = person_name

    #person_name = "밍밍"
    def say_hello(self):
        print("안녕! "+self.person_name)

    def say_hello(self, to_name):
        print("안녕! 난 "+self.person_name)
        print("반가워, "+ to_name)

p = Person("밍밍")
p.say_hello("철수")

david = Person("데이빗")
tom = Person("톰")

david.say_hello("영희")
tom.say_hello("민수")

class Police(Person):
    def arrest(self, target_name):
        print(target_name + ", 널 체포한다")

class Programmer(Person):
    def program(self, target_program):
        print("나의 다음 프로젝트 : " + target_program)

rm = Police("RM")
jin = Programmer("Jin")

rm.say_hello("Peterson")
jin.say_hello("Harari")
rm.arrest("도둑놈아")
jin.program("Python")

