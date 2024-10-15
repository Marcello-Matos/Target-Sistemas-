def inverter_string(s):
    string_invertida = ''

    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]

    return string_invertida

def main():

    string_original = "Meu nome é Marcello, prazer!"
    resultado = inverter_string(string_original)

    print(f'String original: "{string_original}"')
    print(f'String invertida: "{resultado}"')


if __name__ == "__main__":
    main()
