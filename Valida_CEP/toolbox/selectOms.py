import toolbox.engine as engine
import toolbox.connection as conn
import toolbox.trataArquivo as trataArquivo
import pandas as pd
import numpy as np
from datetime import datetime
import os, shutil



def selectOMs():
  log = open("logs/logs.txt", "a+")
  try:
    
    conection = conn.getConnection('Domain','user','password','database')
    print('Connected!')
    wb1 = pd.ExcelFile('./tratativaCEP.xlsx')
    df_pedidos = pd.read_excel(wb1)
    pedidos = np.asarray(df_pedidos['pedido'])
    ped = []
    for pedido in pedidos:
      ped.append(pedido)
    
    ped =str(ped).replace("[","").replace("]","")
  

    query = 'SELECT Sequence as pedido,ClientDocument as cpf,Street as rua,Number as numero,Neighborhood as bairro,City as cidade,UF,PostalCode as cep,SellerName,dominio FROM oms.oms2 where CREATIONDATE >  "2019-09-25 00:00:00"  and Sequence IN({});'.format(ped)
    select = engine.queryReturn(conection,query)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    log.write('\n ----------------------------------------------------------------------------------- \n')
    log.write('Extração do banco realizada com sucesso! {}'.format(current_time))
    print('Extração do banco realizada com sucesso! {}'.format(current_time))
    log.write('\n ----------------------------------------------------------------------------------- \n')

    df = pd.DataFrame(select)
    
    df['cpf_corrigido'] = trataArquivo.trataNumber(df['cpf'])
    df['uf_corrigida'] = trataArquivo.trataString(df['UF'])
    df['rua_corrigida'] = trataArquivo.repRua(df['rua'])
    df['numero_corrigido'] = trataArquivo.trataNumber(df['numero'])
    df['bairro_corrigido'] = trataArquivo.trataString(df['bairro'])
    df['cep_corrigido'] = trataArquivo.trataNumber(df['cep'])
    df['cidade_corrigida'] = trataArquivo.trataString(df['cidade'])
    df['Escritório de vendas'] = ''
    df['bairro_api'] = '-'
    df['cep_api'] = '-'
    df['cep_errado'] = 'N'
    df['uf_errada'] ='N'
    df['tratativa_manual'] = 'N'
    print(df.head())
    log.write('\n ----------------------------------------------------------------------------------- \n')
    log.write('DESCRIÇÃO DO ARQUIVO EXTRAÍDO: {}'.format(df.head()))
    log.write('DESCRIÇÃO DO ARQUIVO EXTRAÍDO: {}'.format(df.describe()))
    log.write('\n ----------------------------------------------------------------------------------- \n')

    df = df[['pedido','cpf','rua','numero','bairro','cidade','UF','cep','SellerName','dominio','Escritório de vendas','cpf_corrigido','rua_corrigida','numero_corrigido','bairro_corrigido','cidade_corrigida','uf_corrigida','cep_corrigido','cep_api','bairro_api','cep_errado','uf_errada','tratativa_manual']]
    nomeArquivo = 'baseCep.xlsx'
    df.to_excel(nomeArquivo, index=False)
    log.write('\n ----------------------------------------------------------------------------------- \n')
    print('Arquivo inicial gerado com sucesso!')
    log.write('Arquivo inicial gerado com sucesso!\n')
    log.write('\n ----------------------------------------------------------------------------------- \n')
  except ValueError:
    print('Erro na conexão com o banco de dados!!')
    log.write('\n ----------------------------------------------------------------------------------- \n')
    log.write('Erro na conexão com o banco de dados!!\n')
    log.write('\n ----------------------------------------------------------------------------------- \n')

  return
# selectOMs() 