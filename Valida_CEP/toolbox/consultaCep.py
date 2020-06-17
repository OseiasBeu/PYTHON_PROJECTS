import requests
import pandas as pd
import difflib
import numpy as np
import toolbox.trataArquivo as trataArquivo
# import trataArquivo as trataArquivo
import time
from datetime import datetime


def consultaCep():
    # log.write('-------------------------------------------------------')
    # print('consulta por cep:')
    wb1 = pd.ExcelFile('./baseCep.xlsx')
    df = pd.read_excel(wb1)
    cep_input = df['cep_corrigido']
    for cep in cep_input:
        time.sleep(2)
        cep = str(cep)
        try:
            request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
            address_data = request.json()
            
            if 'erro' not in address_data:
                bairroOms = df['bairro_corrigido'].where(df['cep_corrigido']== int(cep))
                ruaOms = df['rua_corrigida'].where(df['cep_corrigido']== int(cep))
                bairroOms = np.asarray(bairroOms)
                bairroOms = trataArquivo.trataBairro(bairroOms)
                bairroViaCep = address_data['bairro'].lower()
                CepViaCep = address_data['cep'].replace("-","")
                if bairroViaCep == "":
                    # print('---------------------------------------------------------------------------------')
                    # print('cep bairro vazio:'.format(cepVia))
                    # print('rua bairro vazio:'.format(ruaVia))
                    df['cep_api'] = np.where((df['rua_corrigida'] == ruaOms),CepViaCep, df['cep_api'])
                    # print('cep incluido:{}'.format(CepViaCep))
                    # print('---------------------------------------------------------------------------------')
                # df.loc[df['cep_corrigido'] == int(cep), 'bairro_api'] = address_data['bairro']    
                # if difflib.SequenceMatcher(None,bairroOms,bairroViaCep).ratio() > 0.6 and (np.array_equal(sorted(str(cep)),sorted(str(CepViaCep)))):
                if difflib.SequenceMatcher(None,bairroOms,bairroViaCep).ratio() > 0.6:
                    df.loc[df['cep_corrigido'] == int(cep), 'bairro_api'] = address_data['bairro']
                else:
                    df.loc[df['cep_corrigido'] == int(cep), 'bairro_api'] = 'verificação manual'
            else:
                print('Sem retorno na API para o cep: {} '.format(cep))

        except ValueError:
            print("Cep não localizado: {} ERRO 404.".format(cep))
            df.loc[df['cep_corrigido'] == int(cep), 'cep_errado'] = 'S'
    # print(df[['bairro_api', 'cep_api']])

    nomeArquivo = 'baseCep.xlsx'
    df.to_excel(nomeArquivo, index=False)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print('Consulta por cep finalizada {}!'.format(current_time))
     
# consultaCep()
