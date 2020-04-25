liste = [0,1,2,3,4,5,6,7,8,9,2]
search = input('Which value are you looking for ? ')

if str.isdigit(search) == False:
    print('Enter a number')
    
while str.isdigit(search) != True:
    search = input('Which value are you looking for ? ')

search = int(search)

for i in range(0,len(liste)):
    if liste[i] == search:
        print('found ! rank : ', i)
        break

if liste[i] != search:
    print('Sorry, anything for you here...')
