#Challenge7

#1
l = ['ウォーキング・デッド','アントラージュ','ザ・ソプラノズ','ヴァンパイア・ダイアリーズ']
for i in l:
    print(i)

#2
for i in range(25,51):
    print(i)
    
#3
for i,title in enumerate(l):
    print(str(i)+':'+title)

#4
correct = [2,3,5,7,11,13,17,19,23]

while True:
    input_key = input('type a prime number')
    if input_key == 'q':
        print('end...')
        break
    elif int(input_key) in correct:
        print('correct answer!')
    else:
        print('incorrect!')
#5
list1 = [8,19,148,4]
list2 = [9,1,33,83]
for p in list1:
    for q in list2:
        print(p*q)

list3 = []
for p in list1:
    for q in list2:
        l = p*q
        list3.append(l)
print(list3)
