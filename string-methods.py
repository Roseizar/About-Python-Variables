message= ' Hello There. My name is Theodora'
#message= message.upper() "harfleri büyütmek isityorsak bunu kullanıcaz upper
message=message.lower() #harfleri kücültmek icin 
message=message.title() #harflerin basını büyütmek için
message=message.capitalize() #sadece ilk harf buyur
message=message.strip() #bu parametreyle kullanıcın girdiği karakterlerin basındaki ya da sonudaki bosluklar gider
# message=message.split() #bu parametre ile her bir bosluktan sonraki karakterleri bölünür öyle ifade eder
message=message.split('.') #noktadan itibaren ayırır 
print(message)
#print(message[2]) ikinci ifadeyi yazar
message='*'.join(message) #ayrı olan bilgileri birleştirmek istenirse ya da araya yıldız vs konulmak istenirse
print(message)
#index= message.find('hello') #hello itibari ile geri kalan her seyle beraber ifadeleri ekrana yazar
#print(index)
#print(message)
#isFound = message.startswith('h')
#isFound=message.endswith('g')
#print(isFound)
#message = message.replace('guli ','onder')

message =message.center(100)
print(message)

