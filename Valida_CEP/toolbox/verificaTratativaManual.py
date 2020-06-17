import pandas as pd
import numpy as np


def tratativaManual():
  wb = pd.ExcelFile('./baseCep.xlsx')
  df = pd.read_excel(wb)
  df_arr = np.asarray(df)
  
  # print(df_arr[0][0])
  for item in df_arr:
    if item[20] == 'N' and item[21] == 'N':  
      # print('Antes: {}{}{}'.format(item[20],item[21],item[22]))
      item[22] = 'S'
      # print('Depois: {}{}{}'.format(item[20],item[21],item[22]))
      df['tratativa_manual'] = np.where((df['pedido'] == item[0]),'S', df['tratativa_manual'])
  
  
  nomeArquivo = 'baseCep.xlsx'
  df.to_excel(nomeArquivo, index=False)
  print('Coluna ajustada!')

# tratativaManual()