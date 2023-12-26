# key - value,

# 41 => kocaeli 34 =>istanbul

#sehirler= ['kocaeli','istanbul']
#plakalar=[41,34]

#print(plakalar[sehirler.index('istanbul')])


#print(plakalar['kocaeli'])
#print(plakalar['istanbul'])
#plakalar['kocaeli'] = 'new value'
#plakalar['ankara']=6 #yeni bir key olarak ankara plakalara eklenmiş olur bu şekilde

#print(plakalar)
users={
    'gulizaronder' : {
        'age': 26,
        'email':'ondergulizar54',
        'address' : 'sakarya',
        'phone ': '05445417401'
    },
    
    'dilaraonder': {
        'age':29,
        'email': 'onderdafda@',
        'address': 'sdfdsfsdfasd'
    }
}
print(users['dilaraonder']['age']) #dilaraonderin alt bilgilerinden birine ulasmak icin ayrı bir köşeli acıp bilgi istenebilir
print(users['gulizaronder'])

