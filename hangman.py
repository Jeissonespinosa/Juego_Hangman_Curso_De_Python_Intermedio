import random
import os

image_hangman = ['''
   +---+
   |   |
       |
       |
       |
       |
 =========''', '''
   +---+
   |   |
   O   |
       |
       |
       |
 =========''', '''
   +---+
   |   |
   O   |
   |   |
       |
       |
 =========''', '''
   +---+
   |   |
   O   |
  /|   |
       |
       |
 =========''', '''
   +---+
   |   |
   O   |
  /|\  |
       |
       |
 =========''', '''
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
 =========''', '''
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
 =========''']

def random_word(): #defino la funcion random para que me escoga una palabra la azar
    words = [] # Creo un lista vacia llamada words
    with open("palabras.txt", "r", encoding="utf-8") as f: # Abro el archivo de texto con el metodo de solo lectura y lo llamo f
        for line in f: # Loe cada linea dentro del archivo que se llama f
            words.append(line.rstrip()) # La guardo en mi lista words con el metodo append con rstrip no me guarda los saltos de linea
    return random.choice(words) # utilizamos el metodo random para que sea al azar la selección de las palabras en la lista words

def saved_word(): # Creamos esta función para guardar la palabra en una solo variable
    word = random_word() # llamo como word a toda la función anterior
    unknown_word = "_"*len(word) # Ahora guardo la palabra como _ dependiendo cuanto mida esta palabra
    return word, unknown_word # retorna la palabra y la palbra desconocida

def replace_letters(word, unknown_word, letter): # Creamos esta función en donde tenemos 3 parametros, esta función evalua si la letra que se ingresa esta dentro de la palabra y la remplaza
    number_of_letters = word.count(letter) # evalua la palabra y cuenta cuantas letras tiene iguales a la ingresada
    beginning = 0 # Creamos un contador en 0
    for i in range(number_of_letters): # Me cuenta el numero de veces se encuentra la palabra
        position = word.find(letter, beginning) # creamos esta variable en donde me encuentra la letra y la cuenta desde el principi
        unknown_word = unknown_word[:position] + letter + unknown_word[position + 1 :] # Me actualiza la letra encontrada y concatenamos los caracteres faltantes
        beginning = position + 1 # Reiniciamos el contador
    return unknown_word # Retorna la palabra desconocida    

def hangman():
    print(
 '''    888
    888
    888
    88888b.   8888b. 88888b.   .d88b.  88888b.d88b.    8888b. 88888b.
    888  88b     88b 888 88b  88P  88b 888  888  88b      88b 888  88b
    888  888 d888888 888  888 888  888 888  888  888 .d888888 888  888
    888  888 888 888 888  888 Y88b 888 888  888  888 888  888 888  888
    888  888 Y888888 888  888  Y88888  888  888  888  Y888888 888  888
                                  888
                             Y8b d88P
                               Y88P''',  '''
    
    ''''''Presiona enter para iniciar''')
    input()
    os.system("cls")
    word, unknown_word = saved_word()
    fails = 0
    print(image_hangman[fails])
    while unknown_word != word and fails <= 5:
        print("palabra: " + unknown_word)
        guess = input("Ingresa una letra ")
        os.system("cls")
        if guess in word:
            unknown_word = replace_letters(word, unknown_word, guess)
            print(image_hangman[fails])
        else:
            fails += 1   
            print(image_hangman[fails]) 
    if unknown_word == word:
        print("Adivinaste la palabra, Ganaste. La palabra era " + unknown_word)
    else:
        print("Perdiste, la palabra era: " + word)

def run():
    hangman()

if __name__ == "__main__":
    run()    