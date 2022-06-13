alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#alphabet_2 = ['v', 'k', 'h', 'w', 'y', 'f', 'e', 'x', 'j', 'z', 'n', 'p', 'i', 'c', 'q', 'u', 'd', 's', 'g', 'm', 'a', 'o', 'r', 'l', 't', 'b']
alphabet_2 = ['x', 'u', 'm', 'z', 'q', 'w', 'v', 'p', 't', 's', 'r', 'o', 'n', 'g', 'l', 'k', 'j', 'i', 'h', 'y', 'f', 'e', 'd', 'c', 'b', 'a']
text = input("Введите текст: ")

text_list = []

for i in text:
    text_list.append(i)



#Функция шифрования по ключу
#text - list символов текста
#key - list с перестановкой на алфавите
def encrypt(text, key):
    result = []
    for i in range(len(text)):
        if(text[i]!=" "):
            result.append(key[alphabet.index(text[i])])
        else:
            result.append(" ")
    return result


# Функция дешифрования по ключу
# code - list символов шифра
# key - list с перестановкой на алфавите
def decrypt(code, key):
    result = []
    for i in range(len(code)):
        if code[i] != " ":
            result.append(alphabet[key.index(code[i])])
        else:
            result.append(" ")
    return result

list_of_symbols = encrypt(text_list, alphabet_2)

aa = decrypt(list_of_symbols, alphabet_2)

tt = ""
for i in aa:
    tt += i

print("Шифровка: ", list_of_symbols )
print("Дешифровка: ", tt)