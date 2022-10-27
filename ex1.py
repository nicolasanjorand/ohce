import datetime

now = datetime.datetime.now()
if(now.hour<18):
    print('Bonjour !')
else:
    print('Bonsoir !')

while(1):
    text = input('Saisissez un texte : ')
    if(text == 'quit'):
        if(now.hour<18):
            print('Au revoir !')
        else:
            print('Bonne soirée !')
        break
    reverse_text = text[::-1]
    print(reverse_text)
    if(reverse_text == text):
        print('Bien dit !')
