# listCase1 = 1 2 3 4 5 6 7 8
# listCase2 = 8 7 6 5 4 3 2 1
# listCase3 = 8 1 7 2 6 3 5 4
# print("Start")
# if int("1") == 1 :
#     print("true")
# else:
#     print("false")

desc = [8, 7, 6, 5, 4, 3, 2, 1]
asc = [1, 2, 3, 4, 5, 6, 7, 8]

p = list(map(int, input().split(" ")))
# print(p[1])
isAsc = True
isDesc = True

for i in range(len(p)):
    if isAsc:
        if p[i] != asc[i]:
            isAsc = False
    if isDesc:
        if p[i] != desc[i]:
            isDesc = False

if isAsc:
    print("ascending")
elif isDesc:
    print("descending")
else:
    print("mixed")