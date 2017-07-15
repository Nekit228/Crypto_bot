Leet_EN = ['4', '8', 'see', 'cl', '3', 'ph',
           '6', 'auch', 'ai', 'gei', 'IX', '1',
           'IVI', 'en', '0', 'q', '9', 'l2',
           'z', '7', 'IJ', 'U', 'VV', 'eks', 'uai', '2']
NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
data = input('vvedi ')
crypted_pass = ''
for i in range(len(data)):
    for j in range(len(Leet_EN)):
        if (j == ord(data[i]) - 97) or (j == ord(data[i]) - 65):
            crypted_pass += Leet_EN[j]
        #else:
         #   crypted_pass = 'Ввод недопустимых символов'
    if(ord(data[i]) >= 48) and (ord(data[i]) <= 57):
        crypted_pass += data[i]
    #else:
     #   crypted_pass = 'Ввод недопустимых символов'
if crypted_pass == '':
    crypted_pass = 'Ввод недопустимых символов'
    
print (crypted_pass)

