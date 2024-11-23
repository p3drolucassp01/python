#trabalhando com Data e Hora

from datetime import datetime, timedelta, timezone, time
#data
hoje=datetime.now()
print(hoje)#Exibir data atual
hoje=datetime.now()
print(hoje.date())#Exibir apenas a data
#
hoje=datetime.now()
print(hoje.day)#Exibi o dia

amanha=hoje+timedelta(days=1)
print(amanha)#exibir a data de amanhã

amanha=hoje+timedelta(weeks=1)
print(amanha)#data da proxima semana weeks

#data do contrato
data_contrato=datetime(year=2024, month=9, day=5)
atraso=hoje-data_contrato
print(atraso)#quantos dias de atraso

hoje=datetime.now()#data no formato Brasileiro / /
print(hoje.strftime("%d/%m/%y"))

hoje=datetime.now()#em extenso
print(hoje.strftime("%A"))
#Fuso horario
hora=hoje-timedelta(hours=1)
print(hoje)#Exibir uma hora antes

horario=time(hour=6,minute=30, second=10,microsecond=500)
print(horario)#defini

horario_formato1=horario.replace(minute=59)
print(horario_formato1)#valor alterado

horario_formato2=horario.isoformat('minutes')
print(horario_formato2)#exibir hora e minutos

hora=timedelta(hours=-21)
fuso=timezone(hora)
print(fuso)
