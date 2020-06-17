import pandas as pd
from unidecode import unidecode
import unicodedata
import numpy as np

def trataString(column_df):
  column_df = column_df.str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
  column_df = column_df.str.replace(r'(?:\.|,|[0-9])*','')
  column_df = column_df.str.replace(r'(?:\.|,||-|)*','')
  column_df = column_df.str.replace("'", "",)
  column_df = column_df.str.lower()
  return column_df

def repRua(column_df):
  column_df = column_df.str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
  column_df = column_df.str.replace(r'(?:\.|,|[0-9])*','')
  column_df = column_df.str.replace(r'(?:\.|,||-|)*','')
  column_df = column_df.str.replace("'", "",)
  column_df = column_df.str.lower()
  column_df = column_df.str.replace("rua","",)
  # column_df = column_df.str.replace("av ","",)
  column_df = column_df.str.strip()
  column_df = column_df.str.lstrip()
  
  return column_df

def trataNumber(column_df):
  column_df = column_df.str.replace(r'(?:\.|,|[A-Za-z]|-||/|)*','')
  column_df = column_df.str.replace("'", "",)
  return column_df

def trataBairro(column_df):
  column_df = np.asarray(column_df)
  column_df = str(column_df)
  column_df = column_df.replace("nan","")
  column_df = column_df.replace("[","")
  column_df = column_df.replace("]","")
  column_df = column_df.replace("'","")
  column_df = column_df.replace(".","")
  column_df = column_df.strip()
  return column_df
# trataArquivo()

def trataResApi(column_df):
  column_df = column_df.replace(r'(?:\.|,|[0-9])*','')
  column_df = column_df.replace(r'(?:\.|,||-|)*','')
  column_df = column_df.replace("'", "",)
  column_df = column_df.lower()
  column_df = column_df.replace("rua","",)
  # column_df = column_df.replace("av","",)
  # # column_df = column_df.replace("avenida","",)
  return column_df

def remover_acentos(txt):
  txt = unicodedata.normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')
  txt = txt.strip()
  return txt

def trataUf(column_df):
  column_df = column_df.str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
  column_df = column_df.str.replace(r'(?:\.|,|[0-9])*','')
  column_df = column_df.str.replace(r'(?:\.|,||-|)*','')
  column_df = column_df.str.replace("'", "",)
  # column_df = column_df.str.lower()
  return 

