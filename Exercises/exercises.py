'''
Escreva uma função em Python para verificar letras duplicadas. Ele deve aceitar uma string, ou seja, uma sentença. A função deve 
retornar True se a frase tiver alguma palavra com letras duplicadas, senão retornar False. 
'''

def repeated(text):
    letters = []
    for x in text:
        if x not in letters:
            letters.append(x)
        else:
            return True
    return False

print(repeated('Eu sou fodaa'))



'''
Escreva um código em Python para criar um tradutor de código Morse. Você pode pegar uma string com caracteres alfanuméricos em letras
minúsculas ou maiúsculas. A string também pode ter quaisquer caracteres especiais como parte do código Morse. Caracteres especiais podem incluir vírgulas,
dois pontos, apóstrofos, pontos de exclamação, pontos e pontos de interrogação. O código deve retornar o código Morse que é equivalente à string
'''

from itertools  import chain

def translator(text):
    dis = {
    'a' : '.-',
    'b' : '-...',
    'c' : '-.-.',
    'd' : '-..',
    'e' : '.',
    'f' : '..-.',
    'g' : '--.',
    'h' : '....',
    'i' : '..',
    'j' : '.---',
    'k' : '-.-',
    'l' : '.-..',
    'm' : '--',
    'n' : '-.', 
    'o' : '---',
    'p' : '.--.',
    'q' : '--.-',
    'r' : '.-.',
    's' : '...',
    't' : '-',
    'u' : '..-',
    'v' : '...-',
    'w' : '.--',
    'x' : '-..-',
    'y' : '-.--',
    'z' : '--..',
    '.' : '.-.-.-',
    ',' : '--..--',
    '?' : '..--..',
    '!' : '-.-.--',
    ' ' : ' ',
    }
    translator_text = []
    text = "".join(text).lower()
    for x in chain.from_iterable(text.strip("'")):
        translator_text.append(dis[x])
    return "".join(translator_text)

print(translator(["Eu sou foda"]))


''' 
Escreva uma função em Python para analisar uma string de forma que ela aceite um parâmetro - uma string codificada. Essa string codificada conterá um nome,
sobrenome e um id. Você pode separar os valores na string por qualquer número de zeros. O id não conterá zeros. A função deve retornar um dicionário Python
com os valores de nome, sobrenome e id. Por exemplo, se a entrada for "John000Doe000123". Então a função deve retornar: { "first_name": "John", "last_name": "Doe", "id": "123" }
'''

def treatment(data):
    data = data.split('000')
    return { f"first_name": data[0], "last_name": data[1], "id": data[2] }

print(treatment("John000Doe000123"))

'''
Inverta um número inteiro.
'''

def invert(data):
    return str(data)[::-1]

print(invert(100))


