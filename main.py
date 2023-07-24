import functions as func
import json
data = '/home/l4ndrade/Documentos/Repositórios/Meus-projetos/Organizador-de-notas/data.json'
user = '/home/l4ndrade/Documentos/Repositórios/Meus-projetos/Organizador-de-notas/user.json'

while True:
    opt = func.intinput('''Escolha uma ação:
    [1] - Mudar/adicionar notas
    [2] - Alterar lista de cursos
    [3] - Mostrar resumo de dados
-''', 1, 3)
    
#Mudar/Adicionar notas
    if opt == 1:
        with open(user) as user_json:
            user_dict = json.load(user_json)
        areadict = {'red': 'Redação', 'cnt': 'Ciências da Natureza e suas Tecnologias', 'cht': 'Ciências Humanas e suas Tecnologias', 'lct': 'Linguagens, Códigos e suas Tecnologias', 'mt': 'Matemática e suas Tecnologias'}
        for cod, area in areadict.items():    
            user_dict[cod] = func.floatinput(f'Digite a sua nota em {area}: ', 0, 1000)
        user_dumps = json.dumps(user_dict, separators=(',', ':'))
        with open(user, 'w') as user_json:
            user_json.write(user_dumps)
        print('Notas alteradas com sucesso!')

#Alterar lista de cursos
    elif opt == 2:
        opt2 = func.intinput('''Escolha uma ação:
    [1] - Adicionar uma curso à lista
    [2] - Retirar um curso da lista
    [3] - Mostrar lista de cursos
-''', 1, 3)
        with open(data) as data_json:
            data_lst = json.load(data_json)

    #Adicionar um curso à lista
        if opt2 == 1:

            pesos = {"red":'',"cnt":'',"cht":'',"lct":'',"mt":''}
            nome = input('Digite o nome da universidade do curso desejado: ')
            sigla = input('Digite a sigla referente a essa mesma universidade: ').upper()
            uf = input('Digite a sigla da UF onde está localizada essa universidade: ').upper()
            pesos['red'] = func.floatinput('Digite o peso para Redação referente ao seu curso nessa universidade: ')
            pesos['cnt'] = func.floatinput('Digite o peso para Ciências da Natureza e suas Tecnologias referente ao seu curso nessa universidade: ')
            pesos['cht'] = func.floatinput('Digite o peso para Ciências Humanas e suas Tecnologias referente ao seu curso nessa universidade: ')
            pesos['lct'] = func.floatinput('Digite o peso para Linguagens, Códigos e suas Tecnologias referente ao seu curso nessa universidade: ')
            pesos['mt'] = func.floatinput('Digite o peso para Matemática e suas Tecnologias referente ao seu curso nessa universidade: ')
            corte = func.floatinput('Digite a nota de corte para o ingresso nesse curso em 2021 para ampla concorrência: ', 0, 1000)

            data_lst.append({"nome": nome, "sigla": sigla, "uf": uf, "pesos": pesos, "corte": corte})
            data_dumps = json.dumps(data_lst, separators=(',', ':'))
            with open(data, 'w') as data_json:
                data_json.write(data_dumps)
        
    #Retirar um curso da Lista
        elif opt2 == 2:
            print('Os cursos cadastrados são os seguintes:')
            with open(data) as data_json:
                data_lst = json.load(data_json)
            for item in data_lst:
                print(f'[{data_lst.index(item)}] - {item["nome"]}({item["uf"]}) - Ciência da Computação')
            index = func.intinput('Digite o número correspondente ao curso que será removido: ', 0, len(data_lst) - 1)
            del data_lst[index]
            data_dumps = json.dumps(data_lst, separators=(',', ':'))
            with open(data, 'w') as data_json:
                data_json.write(data_dumps)
                print('Curso removido com sucesso!')

    #Mostrar Lista
        elif opt2 == 3:
            for item in data_lst:
                print(f'[{data_lst.index(item)}] - {item["nome"]}({item["uf"]}) - Ciência da Computação')
    
#Mostrar Resumo de dados
    elif opt == 3:
        with open(user) as user_json:
            user_dict = json.load(user_json)
        with open(data) as data_json:
                data_lst = json.load(data_json)
        
        for curso in data_lst:
            nota = round((user_dict["red"] * curso["pesos"]["red"] + user_dict["cnt"] * curso["pesos"]["cnt"] + user_dict["cht"] * curso["pesos"]["cht"] + user_dict["lct"] * curso["pesos"]["lct"] + user_dict["mt"] * curso["pesos"]["mt"])/(curso["pesos"]["red"] + curso["pesos"]["cnt"] + curso["pesos"]["cht"] + curso["pesos"]["lct"] + curso["pesos"]["mt"]), 2)

            if nota >= curso["corte"]:
                status = "\033[0;32mAPROVADO!\033[0;0m"
            else:
                status = "\033[1;31mREPROVADO!\033[0;0m"
            
            diferença = round(nota - curso["corte"], 2)
            if diferença >=0:
                diferença = f'\033[0;32m+{diferença}\033[0;0m'
            else:
                diferença = f'\033[1;31m{diferença}\033[0;0m'

            print(f'''
    \033[1;3m{curso["nome"]}({curso["uf"]})'\033[0m
    Nota de corte: {round(curso["corte"], 2)}
    Sua nota: {nota}
    Status: {status}
    Diferença: {diferença}
            ''')

# Alguns cursos tem o termo de adesão desatualizadso (2022.1 e não 2023.1), são eles: UFU