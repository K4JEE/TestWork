import itertools
r={"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, 
"seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, 
"fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen":18, "nineteen": 19, "twenty": 20}
r=[r[i] for i in input().split()]
print(r)
#избавляемся от повторений и сотрировка
r=[r[0]for r in itertools.groupby(sorted(r))]
print("без повторений",r)
#произведение и сумма
for i in range(len(r)-1):
    if i % 2 == 0:
        print("проивзедение",r[i]*r[i+1])
    else:
        print("сумма",r[i]+r[i+1])
#сумма всех нечетных
print("суммавсех",sum([x for x in r if x%2==1]))

