#Generar una contraseña que acepte cualquier tipo de caracter,
#y que sea de un rango de 4 a 16 caracteres
import random
import string
def generatePassword() :
    password = ''.join(random.choice(string.ascii_letters + string.digits
                                 + string.punctuation) for x in range(4,16))
    print (password)

generatePassword()


