import pandas as pd
import numpy as np
# import re


def corrigeUF():
  wb1 = pd.ExcelFile('./baseCep.xlsx')
  df = pd.read_excel(wb1)
  ufs = df['UF']

  tamanho = len(ufs)
  for i in range(tamanho):
    if ufs[i][0].islower() | ufs[i][1].islower() :
      df.loc[df['UF'] == ufs[i], 'uf_errada'] = 'S'


  for uf in ufs:
    # print(len(uf))
    if len(uf) != 2:
      df.loc[df['UF'] == uf, 'uf_errada'] = 'S'

  df.loc[df['uf_corrigida'] == 'sao paulo', 'uf_errada'] = 'S'
  df.loc[df['uf_corrigida'] == 'sao paulo', 'uf_corrigida'] = 'sp'
  
  df.loc[df['uf_corrigida'] == 'tocantins', 'uf_errada'] = 'S'
  df.loc[df['uf_corrigida'] == 'tocantins', 'uf_corrigida'] = 'to'

  df.loc[df['uf_corrigida'] == 'rio grande do sul', 'uf_errada'] = 'S'  
  df.loc[df['uf_corrigida'] == 'rio grande do sul', 'uf_corrigida'] = 'rs'

  df.loc[df['uf_corrigida'] == 'rio grande do norte', 'uf_errada'] = 'S'
  df.loc[df['uf_corrigida'] == 'rio grande do norte', 'uf_corrigida'] = 'rn'

  df.loc[df['uf_corrigida'] == 'rio de janeiro', 'uf_errada'] = 'S'
  df.loc[df['uf_corrigida'] == 'rio de janeiro', 'uf_corrigida'] = 'rj'

  df.loc[df['uf_corrigida'] == 'pernambuco', 'uf_errada'] = 'S'
  df.loc[df['uf_corrigida'] == 'pernambuco', 'uf_corrigida'] = 'pe'

  df.loc[df['uf_corrigida'] == 'para', 'uf_errada'] = 'S'
  df.loc[df['uf_corrigida'] == 'para', 'uf_corrigida'] = 'pa'

  df.loc[df['uf_corrigida'] == 'parana', 'uf_errada'] = 'S'
  df.loc[df['uf_corrigida'] == 'parana', 'uf_corrigida'] = 'pr'

  df.loc[df['uf_corrigida'] == 'minas gerais', 'uf_errada'] = 'S'
  df.loc[df['uf_corrigida'] == 'minas gerais', 'uf_corrigida'] = 'mg'

  df.loc[df['uf_corrigida'] == 'maranhao', 'uf_errada'] = 'S'
  df.loc[df['uf_corrigida'] == 'maranhao', 'uf_corrigida'] = 'ma'

  df.loc[df['uf_corrigida'] == 'goias', 'uf_errada'] = 'S'
  df.loc[df['uf_corrigida'] == 'goias', 'uf_corrigida'] = 'go'


  df.loc[df['uf_corrigida'] == 'espirito santo', 'uf_errada'] = 'S'
  df.loc[df['uf_corrigida'] == 'espirito santo', 'uf_corrigida'] = 'es'

  df.loc[df['uf_corrigida'] == 'distrito federal', 'uf_errada'] = 'S'
  df.loc[df['uf_corrigida'] == 'distrito federal', 'uf_corrigida'] = 'df'

  df.loc[df['uf_corrigida'] == 'ceara', 'uf_errada'] = 'S'
  df.loc[df['uf_corrigida'] == 'ceara', 'uf_corrigida'] = 'ce'

  df.loc[df['uf_corrigida'] == 'bahia', 'uf_errada'] = 'S'
  df.loc[df['uf_corrigida'] == 'bahia', 'uf_corrigida'] = 'ba'

  df.loc[df['uf_corrigida'] == 'amazonas', 'uf_errada'] = 'S'
  df.loc[df['uf_corrigida'] == 'amazonas', 'uf_corrigida'] = 'am'
  

  # print(df)
  nomeArquivo = 'baseCep.xlsx'
  df.to_excel(nomeArquivo, index=False)
  print('UFs corrigidas com sucesso!')
