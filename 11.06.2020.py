# 2.3 На вход программе поступает строка, состоящая как из заглавных так из строчных букв латинского алфавита. Ваша задача преобразовать строку так, чтобы все символы были только заглавными.
#
# Sample Input:
#
# ManY mUcH
# Sample Output:
#
# MANY MUCH
# s=input().upper()
# print(s)



# 2. 3. 2 На вход программе поступает строка, состоящая как из заглавных так из строчных букв латинского алфавита. Ваша задача преобразовать строку так, чтобы все символы были только строчными
#
# Sample Input:
#
# TheRe is NO spOOn
# Sample Output:
#
# there is no spoon

# a=input().lower()
# print(a)

# 2.3.3 На вход программе поступает строка, ваша задача подсчитать сколько раз в ней встречается латинская буква "e". При этом стоит учитывать как маленькие, так и заглавные буквы
#
# Sample Input:
#
# Helen
# Sample Output:
#
# # 2

b=input().lower()
print(b.count('e'))

# 4. На вход программе поступает строка, ваша задача удалить из нее все символы "w" и "z".
#
# Учитываем только маленькие буквы
#
# Sample Input:
#
# what's up?
# Sample Output:
#
# hat's up?
# d=input()
# print(d.find("a"))
#
#
# 5. На вход программе поступает строка, ваша задача вывести на экран индекс последней найденной латинской буквы "a"
#
# Если такого символа в введенной строке нет, выведите -1
#
# Sample Input 1:
#
# banana
# Sample Output 1:
#
# 5
# Sample Input 2:
#
# cat
# Sample Output 2:
#
# 1
# Sample Input 3:
#
# zoo
# Sample Output 3:
#
# -1

# 6. Программа получает на вход фразу, ваша задача посчитать из скольких слов состоит данная фраза. Для удобство будет считать словом любую последовательность символов.
#
# Sample Input 1:
#
# Hello my friend
# Sample Output 1:
#
# 3
# Sample Input 2:
#
# aa bbb ccc dddd
# Sample Output 2:
#
# 4
#
# g=input()
# print(len(g.split()))



# 7. Программа получает на вход фразу, состоящую из нескольких слов, разделенных пробелом.
#
# Ваша задача заменить все пробелы запятыми и вывести полученную строку.
#
# Sample Input:
#
# Smells Like Teen Spirit
# Sample Output:
#
# Smells,Like,Teen,Spirit
#
# h=input()
# print(h.replace(" ",","))

# 8. Петя записался в кружок по программированию. На первом занятии Пете задали написать простую программу. Программа должна делать следующее: в заданной строке, которая состоит из прописных и строчных латинских букв, она:
#
# удаляет все гласные буквы,
# перед каждой согласной буквой ставит символ ".",
# все прописные согласные буквы заменяет на строчные.
# Гласными буквами считаются буквы "A", "O", "Y", "E", "U", "I", а согласными — все остальные. На вход программе подается ровно одна строка, она должна вернуть результат в виде одной строки, получившейся после обработки.
#
# r=input().lower()
# r=r.replace('a','')
# r=r.replace('o','')
# r=r.replace('y','')
# r=r.replace('e','')
# r=r.replace('u','')
# r=r.replace('i','')
# r='.'.join(r)
# print('.' + r)






