import pandas as pd
import requests
import difflib
import toolbox.trataArquivo as trataArquivo
import numpy as np
from datetime import datetime
import time 
import os, shutil




def consultaEnd():
  log = open("logs/logs.txt", "a+")
  log.write('\n-------------------------------------------------------\n')
  log.write('consulta por endereco:----')
  # print('consulta por endereco:----')
  wb =  pd.ExcelFile("./baseCep.xlsx")
  df = pd.read_excel(wb)
  # df = df.drop_duplicates()
  arr = df.to_numpy()
  for item in range(len(df)):
  
    cidadeOms = arr[item][15]
    ruaOms = arr[item][12]
    ufOms = arr[item][16]
    cepOms = arr[item][17]
    cepOms_v = cepOms
    bairroOms = arr[item][14]

    # print('item: {}  - Requisicao::|{}/{}/{} |'.format(item,ufOms,cidadeOms,ruaOms))
    log.write('\n-------------------------------------------------------\n')
    log.write('\nitem: {}  - Requisicao::|{}/{}/{} |\n'.format(item,ufOms,cidadeOms,ruaOms))
    log.write('\n-------------------------------------------------------\n')
    # time.sleep(5)
    df1 = df
    try:
      address_data = requests.get('https://viacep.com.br/ws/{}/{}/{}/json'.format(ufOms,cidadeOms,ruaOms)).json()
      log.write('\n-------------------------------------------------------\n')
      log.write('\nRequisicao:: Dados:{}/{}/{}\n'.format(ufOms,cidadeOms,ruaOms))
      log.write('\n-------------------------------------------------------\n')
      if address_data != []:
        log.write('\n{}\n'.format(address_data))
        tamArr = []
        if len(address_data) > 1:
          for item in address_data:
            bairroVia = item['bairro']
            simil = difflib.SequenceMatcher(None, bairroVia, bairroOms).ratio()
            tamArr.append(simil)
          simil = max(tamArr)
          indice = tamArr.index(max(tamArr))
          # print('Indice simil:{}'.format(indice))  
          log.write('\n-------------------------------------------------------\n')
          log.write('\nIndice simil:{}\n'.format(indice))  
          # print('Maior similadade:{}'.format(simil))
          log.write('\nMaior similadade:{}\n'.format(simil))
          end =  address_data[indice]
          # print('Vencedor:{}'.format(end))
          log.write('\nVencedor:{}\n'.format(end))
          log.write('\n-------------------------------------------------------\n')
          cepVia = end['cep']
          ruaVia = end['logradouro']
          ruaVia = ruaVia.lower()
          bairroVia = end['bairro']
          bairroVia = bairroVia.lower()
          ruaVia = trataArquivo.remover_acentos(ruaVia)
          ruaVia = trataArquivo.trataResApi(ruaVia)
          ruaVia = trataArquivo.remover_acentos(ruaVia)
          bairroVia = trataArquivo.remover_acentos(bairroVia)
          bairroVia = trataArquivo.trataResApi(bairroVia)
          if bairroVia == "":
            df1['cep_api'] = np.where((df1['cep_corrigido'] == cepOms_v),cepVia, df1['cep_api'])
            
          # print('Requisicao:: Dados:{}/{}/{}'.format(ufOms,cidadeOms,ruaOms))
          log.write('\n-------------------------------------------------------\n')
          log.write('\nRequisicao:: Dados:{}/{}/{}\n'.format(ufOms,cidadeOms,ruaOms))
          # print('Dados Via: rua: {} | bairro: {} | cep: {} \nDados Oms: rua: {} | bairro: {} | cep: {} '.format(ruaVia,bairroVia,cepVia,ruaOms,bairroOms,cepOms))
          log.write('\nDados Via: rua: {} | bairro: {} | cep: {} \nDados Oms: rua: {} | bairro: {} | cep: {} \n'.format(ruaVia,bairroVia,cepVia,ruaOms,bairroOms,cepOms))
          log.write('\n-------------------------------------------------------\n')
          ###############################################################################################################
          df1['cep_api'] = np.where((df1['rua_corrigida'] == ruaVia),cepVia, df1['cep_api'])
          df1['bairro_api'] = np.where((df1['rua_corrigida'] == ruaVia),bairroVia, df1['bairro_api'])
          df1['cep_errado'] = np.where((df1['rua_corrigida'] == ruaVia),'S', df1['cep_errado'])      
        else:
          cepVia = address_data[0]['cep']
          ruaVia = address_data[0]['logradouro']
          ruaVia = ruaVia.lower()
          bairroVia = address_data[0]['bairro']
          bairroVia = bairroVia.lower()
          ruaVia = trataArquivo.trataResApi(ruaVia)
          ruaVia = trataArquivo.remover_acentos(ruaVia)
          bairroVia = trataArquivo.remover_acentos(bairroVia)
          bairroVia = trataArquivo.trataResApi(bairroVia)
          cepOms = df['cep_corrigido'].where(df['rua_corrigida'] == ruaVia)
          cepOms = trataArquivo.trataBairro(cepOms)
          # print('check')
          # print('RUA VIACEP.:{}'.format(ruaVia))
          # print('RUA OMS....:{}'.format(ruaOms))
          # print('CEP OMS....:{}'.format(cepOms))
          log.write('\n-------------------------------------------------------\n')
          log.write('\nRUA VIACEP.:{}\n'.format(ruaVia))
          log.write('\nRUA OMS....:{}\n'.format(ruaOms))
          log.write('\nCEP OMS....:{}\n'.format(cepOms))
          log.write('\n-------------------------------------------------------\n')
          if bairroVia == "" :
              df1['cep_api'] = np.where((df1['cep_corrigido'] == cepOms_v),cepVia, df1['cep_api'])
              

          df1['cep_api']    = np.where((df1['rua_corrigida'] == ruaVia),cepVia, df1['cep_api'])
          df1['bairro_api'] = np.where((df1['rua_corrigida'] == ruaVia),bairroVia, df1['bairro_api'])
          df1['cep_errado'] = np.where((df1['rua_corrigida'] == ruaVia),'S', df1['cep_errado'])
      else:
        # print('Retorno Vazio tratamento manual para o item: /{}/{}/{}/ |'.format(item,ufOms,cidadeOms,cepOms))
        log.write('\n-------------------------------------------------------\n')
        log.write('\nRetorno Vazio tratamento manual para o item: /{}/{}/{}/ |\n'.format(item,ufOms,cidadeOms,cepOms))
        log.write('\n-------------------------------------------------------\n')
    except ValueError:
      # print('{}/{}/{}'.format(ufOms,cidadeOms,ruaOms))
      # print(requests.get('https://viacep.com.br/ws/{}/{}/{}/'))
      # print('Endereco nao localizado /{}/{}/{}/: ERROR 404'.format(ufOms,cidadeOms,ruaOms))
      log.write('\n-------------------------------------------------------\n')
      log.write('\nEndereco nao localizado /{}/{}/{}/: ERROR 404\n'.format(ufOms,cidadeOms,ruaOms))
      log.write('\n-------------------------------------------------------\n')

  df1['uf_corrigida']  = df1['uf_corrigida'].str.upper()
  nomeArquivo = 'baseCep.xlsx'
  df1.to_excel(nomeArquivo, index=False)
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  # print('Consulta por enderecos finalizada:{}!'.format(current_time))
  log.write('\n-------------------------------------------------------\n')
  log.write('\nConsulta por enderecos finalizada:{}!\n'.format(current_time))
  log.write('\n-------------------------------------------------------\n')
  
# consultaEnd()    
