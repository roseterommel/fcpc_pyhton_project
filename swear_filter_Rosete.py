
foulwords = ['bobo', 'tanga', 'bakla', 'tarantado', 'gago', 'tangina', 'putangina', 'pakyu', 'fuck','gay', 'ulol',
              'bading', 'bakla', 'supot', 'nigga','anal','pak','yu','anus']

sentence = input('Enter your sentence: ')

new = [x for x in sentence.lower().split()]

text = ''
for word in new:
    if word in foulwords:
        a = len(word)

        text += '*' * a + ' '

    else:
        text += word + ' '

print(text)
