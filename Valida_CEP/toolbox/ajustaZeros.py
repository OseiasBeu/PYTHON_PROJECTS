import pandas as pd
import numpy as np
def  ajustaZeros():
  wb = pd.ExcelFile('baseCep.xlsx')
  df = pd.read_excel(wb)

  ceps = df['cep_corrigido']
  ceps = df['cep_corrigido'].values
  for  cep in ceps:
    cep = str(cep)

    if len(cep) < 8:
      cep_old = cep
      cep = cep.rjust(8,'0')
      df['cep_corrigido'] = np.where((df['cep_corrigido'] == cep_old),cep, df['cep_corrigido'])


   
  nomeArquivo = 'baseCep.xlsx'
  df.to_excel(nomeArquivo, index=False)
  print('Zeros ajustados!')


# ajustaZeros()