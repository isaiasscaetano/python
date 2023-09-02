from datetime import datetime, timedelta

#data
hoje = datetime.now()
print(hoje.date())

#variaveis data 
amanha = hoje + timedelta(days=1)
print(amanha)

data_contrato = datetime(year=2023, month=9, day=2)
atraso = hoje - data_contrato
print(atraso)

#extrair datas em outra formatos
data_contrato = "02/09/2023"
data_contrato = datetime.strptime(data_contrato, "%d/%m/%Y")
print(data_contrato)

#formato brasileiro
print(hoje.strftime("%d/%m/%Y"))
print(hoje.strftime("%A"))

#fuso horario
hoje = hoje - timedelta(hours=1)
print(hoje)



