''' Необходимо написать программу, которая будет принимать на вход строку, разбивать строку на слова по пробелу. Далее нужно из всех слов убрать следующие пунктуационные знаки: 

!,.?;:#$%^&*(),

а также привести слова к нижнему регистру. В итоге нужно вывести в алфавитном порядке слова, которые состоят как минимум из 5 символов, а также имеют как минимум 4 уникальных символа, 
и которые встретились в исходном тексте более 2х раз.
 '''

line = input()
new_line = line.lower()

symbols_to_remove = "!,.?;:#$%^&*()"

for symbol in symbols_to_remove:
    new_line = new_line.replace(symbol, "")
    
words = dict()

for word in new_line.split():
    if len(word) >= 5 and len(set(word)) >= 4:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
final_words = [word for word, val in words.items() if val > 2]

final_words.sort()
print("\n".join(final_words))
