import hashlib
flag = 0
# hash para su posterior comparacion
md5_hash = input("Hash: ")
# lista de contraseñas sin hash
wordList = input("Lista.txt: ")
# leer el archivo y almacenarlo en file_list
try:
    file_list = open(wordList,"r")
except:
    print("El archivo "+wordList+" no fue encontrado")
    exit()
# recorrer la lista
for word in file_list:
    word_enc = word.encode('utf-8').strip()
    # palabla lista para comparar
    digest = hashlib.md5(word_enc).hexdigest()
    if(digest == md5_hash):
        # contraseña encontrada
        print('Contraseña encontrada: '+word)
        flag = 1
if flag == 0:
    print('Contraseña no encontrada en la lista')