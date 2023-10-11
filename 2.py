List1 = [0,1,2,3,4,5,6,7,8,9]
List2 = [9,8,7,6,5,4,3,2,1,0]

nov = []

for i in range(len(List1)):
    nov.append(List1[i] + List2[i])

print (nov)