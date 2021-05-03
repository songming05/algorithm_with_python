# dataType
# operators
# variable
# function

x=2
y=3
z=1.22

print(x + y)
print(x - y)
print(x * y)
print(x ** y)
print(x / y)
print(x % y)

s = "hello"
s2 = 'world'
s3 = """
안녕
파이선
!!
"""
print(s)
print(s2)
print(s3)
print(s + s2)
#print(str + 2)
print(s + str(22))

b = True
f = False
print(b)
print(f)

a = 3
if 1 > 2:
    print("1 > 2")
elif a == 3:
    print("a 는 3")
else:
    print("else")

if not 1 > 2:
    print("1 < 2")

if True or False :
    print("or")
else:
    print("or else")

if True and False:
    print("and")
else:
    print("and else")


def greet(name1, name2, curtime):
    print("안녕 %s 좋은 아침!" % name2)
    print("응, 안녕!! " + name1 +"! %d 시네!" % curtime)

greet("Ming", "Hong", 8)

def myAdd(num1, num2):
    result = num1+num2
    return result

res = myAdd(3, 21)
print(res)

#loop
for i in range (10):
    print("i :: "+str(i))

i=0
while i<3:
    print(i)
    i += 1


# DataStructure
# List
listX = [1,4,3,2]
listY = ["hello", 1,2,3]
print(listX+listY)
print(listX[2])
print((listX+listY)[4])
print("len : "+str(len(listX)))
print("sum : "+str(sum(listX)))
print("sorted : "+str(sorted(listX)))
print("sorted : "+str(sorted(listX)))
for n in listX:
    print(n)

print("index : "+str(listY.index(3)))
print("in : "+str("hello" in listY))
print("in : "+str("helloPy!" in listY))

# Tuple
tupleX = (1,5,4)
tupleY = ("world",2,3)
tupleZ = tuple()

print(tupleX)
print(tupleY)
print(tupleZ)

# Dictionary

dictX = {
    "name": "ming",
    "age": 25,
    15: 1500
}
dictY = dict()

print(dictX)
print(dictY)
print(dictX["name"])
print(dictX[15])

print("dict in : "+str("name" in dictX))
print("dict in : "+str("ming" in dictX))
print("dict keys : "+str(dictX.keys()))
print("dict values : "+str(dictX.values()))

dictX[15] = 3000
dictX["city"] = "Seoul"
for key in dictX:
    print(str(key)+" : "+str(dictX[key]))

# Q.과일의 숫자를 세주세요
fruit = ["사과", "사과", "바나나", "바나나", "바나나", "복숭아"]
dictCount = dict()
for fruitName in fruit:
    if fruitName not in dictCount:
        dictCount[fruitName] = 1
    else:
        dictCount[fruitName] = dictCount[fruitName] +1

print(dictCount)