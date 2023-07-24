def intinput(text, min, max):
    while True:
        try:
            num = int(input(text))
        except:
            print('Digite um número válido!')
        else:
            if max >= num >= min:
                return num
                break
            else:
                print('Digite um número valido!')
                continue


def floatinput(text, min=0, max=999999):
    while True:
        try:
            num = float(input(text))
        except:
            print('Digite um número válido!')
        else:
            if max >= num >= min:
                return num
                break
            else:
                print('Digite um número valido!')
                continue
