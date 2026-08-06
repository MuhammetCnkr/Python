list = []

while True:
    try:
        data = input("Enter: ")
    except EOFError:
        break
    else:
        list.append(data)


if len(list) % 2 == 1:
    uzunluk = (len(list)-1)/2
else:
    uzunluk = int(len(list)/2)

for i in range(1,len(list)):
    tut = list[i-1]
    list[i-1] = list[-i]
    list[-1] = tut
print(list)


#asdfasldşjfkn as

muhammernasldfnalsf yazı aşldsnflasjdnf 
