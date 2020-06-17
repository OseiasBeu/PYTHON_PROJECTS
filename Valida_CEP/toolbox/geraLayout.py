import pandas as pd
import numpy as np
import os, shutil



def  extractKaique():
  log = open("logs/logs.txt", "a+")
  wb = pd.ExcelFile('baseCep.xlsx')
  df = pd.read_excel(wb)
  pedidos = df['pedido']
  ceps = df['cep_corrigido'].values
  ceps = np.asarray(ceps)
  # print (ceps)
    
  for  cep in ceps:
    cep = str(cep)
    cep_old = cep.replace(r'(?:\.|,|[A-Za-z]|-||/|)*','')
    # print('antes:{}' .format(cep_old))
    cep = cep.rjust(8,'0')
    cep = '{}-{}'.format(cep[:5],cep[5:8])
    # print(cep)
    df['cep_corrigido'] = np.where((df['cep_corrigido'] == cep_old),cep, df['cep_corrigido'])
    # print('depois:{}'.format(cep))
  
  df['Tipo Do erro'] = ''
  df['Tratado?'] = ''
  df_kaique = df[['pedido','Tipo Do erro','Tratado?','cep_corrigido','cep_api','uf_corrigida']]
  
  df_arr = np.asarray(df)
  for item in df_arr:
     pedido = item[0]
    #  print(pedido)
     if item[20] == 'S'and item[21] == 'S':  
       df_kaique['Tipo Do erro'] = np.where((df_kaique['pedido'] == pedido),'CEP|UF', df_kaique['Tipo Do erro'])      
     elif item[21] == 'S':  
      df_kaique['Tipo Do erro'] = np.where((df_kaique['pedido'] == pedido),'UF', df_kaique['Tipo Do erro'])
     elif item[20] == 'S':
      df_kaique['Tipo Do erro'] = np.where((df_kaique['pedido'] == pedido),'CEP', df_kaique['Tipo Do erro'])
      
  
  # print(df_kaique['Tipo Do erro'])
  log.write('\n ----------------------------------------------------------------------------------- \n')
  log.write('\n Resumo da planilha baseCep.xlsx: {}\n'.format(df.head()))
  log.write('\n ----------------------------------------------------------------------------------- \n')
  log.write('\n Descrição da planilha baseCep.xlsx: {}\n'.format(df.describe()))
  log.write('\n ----------------------------------------------------------------------------------- \n')
  log.write('\n Resumo da planilha baseKaique.xlsx: {}\n'.format(df_kaique.head()))
  log.write('\n ----------------------------------------------------------------------------------- \n')
  log.write('\n Descrição da planilha baseKaique.xlsx: {}\n'.format(df_kaique.describe()))
  log.write('\n ----------------------------------------------------------------------------------- \n')
  
  nomeArquivo = 'baseKaique.xlsx'
  df_kaique.to_excel(nomeArquivo, index=False)
  print('Arquivo Layout final gerado!')

# extractKaique()