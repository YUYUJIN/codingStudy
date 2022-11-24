n = int(input())
age_list = []

for i in range(n):
    age, name = input().split()
    age_list.append([int(age), name])

#age_list.sort(key = lambda x: x[0])
sort_list = sorted(age_list, key = lambda x : x[0])

for i in sort_list:
    print(i[0], i[1])