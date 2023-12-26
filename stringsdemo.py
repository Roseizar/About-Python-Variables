website="http://www.ondsfsasdasdsafasfas.com"
coursee= "python kursu: bastan sona phtyon programlama rehberiniz "
result = len(coursee)
length=len(website)
print(result)
"kelime uzunlukları"
g="gulizar"
result=len(g)
print(result)
s="selma"
result=len(s)
print(result)
h="halime"
result=len(h)
print(result)
"kactan kaca kadar istenilen kelime sayısı,sağdan baslarsak 0 dan sayılır sondan baslarsak -1"
result=website[7:10]
print(result)
result=website[10:13]
print(result)
"website cumle son uc harfleri"
result=website[length -3:length]
print(result)
result=coursee[0:15]
print(result)
"courseee nin sondan 11inci harfinden 15 incisine kadarkilerin sonucu"
result=coursee[-11:15]
print(result)
"coursee deki ifadeleri tersten yazdırmak için"
result=coursee[::1]
print(result)
s="12345" *5
print(s[::5])
name , surname , age , job = "bora","yilmaz", 32 ,"muhendis"
"yukardakiler ile ekrana asagıdaki ifadeyi terminale yazdirin"
"benim adım bora yılmaz,yaşım 32 ve mesleğim mühendis"
result="benim adim" + name + "  " + surname + "yaşim" + " "  + str(age) + "ve meslegim"+ job 
print(result)
result="benim adim {1} yaşım 36 {2} ve meslegim muhendis".format(name,surname,age,job)
result= "benim adım {name} {surname},{age} 32 ve mesleğim {job}"

"hello world  ifadesindeki w nun harfini W ile değiştirin"
s= 'hello world'
s= s[0:6] + "W" + s[-4:]
s.replace('w', 'w')
print(s)
"abc karakterlerini 3 defa yan yana yazdırın"
result= 'abc' *3
print(result)
 

'hello world karakterlerindeki baş ve sonundaki boşlukları silin'
result=' hello world '.split()
print(result)




