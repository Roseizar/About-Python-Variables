
numbers = [1,3,5,4,7,9,11,13,15,17,19,21,23,25,27,29,31]
letters=['a','b','c','g','s','y','h','u']
val = min(numbers)
val = max(numbers)
val = max(letters)
print(val)
val = numbers[3:17]
val = numbers[:19]
val = numbers[15:]
 
numbers.append(49)
numbers.append('selam') #eklemek için
numbers.insert(3,79) #üçüncü elemandan sonraya 79 ekler
numbers.insert(-1,55) # -1 yazdığımız için listenin en sonuna ekler
numbers.pop() #silmek için pop kullanılabilir belirtmediğimiz için en sonu siler
numbers.pop(0) #ama 0 dediğimizde soldan sağa ilk eleman 0 dan baslar en bastakini siler 
numbers.pop(-1) # -1 dediğimizde ise en sondaki elemanı siler cunku eksi bir en sonkidir
#numbers.remove(21) aynı sekilde remove ile de istenilen eleman veya elemanlar silinir. 
numbers.sort #liste sayısal olarak sıralanır
letters.sort #alfabe olarak sıralanır.
print(letters) 
print(numbers)


print(val)

names= ['Ali','deniz','serra','meva']
years=[1997,1996,1995,1994]
index = names.index('deniz')


print(index)