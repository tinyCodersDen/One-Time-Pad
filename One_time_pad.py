import random
import string
alphabet = list(string.ascii_letters+'1234567890')
text = input('Enter text here: ')
encrypted_text,l = '',[]
for t in text:
    if t!=' ':
        s = random.randint(1,26)
        if alphabet.index(t)+s>=len(alphabet):
            l.append(s)
            s-=(len(alphabet)-alphabet.index(t)-1)
            encrypted_text+=alphabet[s]
        else:
            encrypted_text+=alphabet[alphabet.index(t)+s]
            l.append(s)
    else:
        encrypted_text+=' '
print('')
print('Original text:',text); print('')
print('Encrypted text:',encrypted_text); print('')
print('List of random dice rolls:',l); print('')
print('Number of Trials to break:',str(26**len(text))); print('')
print('Fun facts about the One time Pad:') ;print('')
print('The one time pad was invented by Gilbert S. Vernam and Joseph O. Mauborgne.')
print('But it was thought to be created 35 years earlier by Frank Miller')
print('It was created in 1882, and this was an unbreakable technique during WW2')
print('This was used for militaries to send messages')
print('The one time pad is unbreakable because it will require you to take a maximum of 26**n trials to solve')
print('This encryption algorithm is paired with random keys, so this will take a stack of 26**n papers(taller than the highest tower on Earth)')
print('We have reached perfect secrecy :)')