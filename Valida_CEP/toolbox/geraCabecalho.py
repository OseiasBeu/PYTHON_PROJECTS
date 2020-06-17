import os, shutil
from datetime import datetime
import time

def header():
  log = open("logs/logs.txt", "a+")
  now = datetime.now()
  log.write('\n======================================================================================================================================================================\n')
  now = datetime.now()
  log.write('\n..................................................................................INICIO DO SCRIPT: {}.................................................................\n'.format(now.strftime("%H:%M:%S")))
  log.write('\n======================================================================================================================================================================\n')
  log.close()


def footer():
  log = open("logs/logs.txt", "a+")
  now = datetime.now()
  log.write('SCRIPT FINALIZADP {}' .format(now.strftime("%H:%M:%S")))
  now = datetime.now()
  log.write('\n======================================================================================================================================================================\n')
  log.write('\n..................................................................................FIM DO SCRIPT: {}.................................................................\n'.format(now.strftime("%H:%M:%S")))
  log.write('\n======================================================================================================================================================================\n')
  log.close()
  time.sleep(10)