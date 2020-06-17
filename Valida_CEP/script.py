import toolbox.mengagem as mengagem
import toolbox.selectOms as selectOMs
import toolbox.ajustaZeros as ajustaZeros
import toolbox.corrigeUF as corrigeUF
import toolbox.consultaCep as consultaCep
import toolbox.consultaEnd as consultaEnd
import toolbox.geraLayout as geraLayout
import toolbox.verificaTratativaManual as tratativa_manual
import toolbox.geraCabecalho as geraCabecalho
import time


mengagem.mensagem()
geraCabecalho.header()
selectOMs.selectOMs()
ajustaZeros.ajustaZeros()
corrigeUF.corrigeUF()
consultaEnd.consultaEnd()
consultaCep.consultaCep()
tratativa_manual.tratativaManual()
geraLayout.extractKaique()
geraCabecalho.footer() 