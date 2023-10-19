# Importando as bibliotecas necessárias
import pandas as pd
import win32com.client as win32

# Importar a base de dados (vendas.xlsx)
tabelaVendas = pd.read_excel('Dados\Vendas.xlsx')

# Visualizar a base de dados
pd.set_option('display.max_columns', None)
print(tabelaVendas)
print('-' * 50)

# Cálculo do faturamento por loja
faturamento = tabelaVendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
print(faturamento)
print('-' * 50)

# Cálculo da quantidade de produtos vendidos por loja
quantidade = tabelaVendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
print(quantidade)
print('-' * 50)

# Cálculo do ticket médio por produto em cada loja
ticketMedio = (faturamento['Valor Final'] / quantidade['Quantidade']).to_frame()    # vai transformar o resultado da divisão em uma tabela
ticketMedio = ticketMedio.rename(columns={0: 'Ticket Médio'})
print(ticketMedio)

# Enviar e-mail com o relatório
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'contato@gmail.com'
mail.Subject = 'Relatório de Vendas por Loja'
mail.HTMLBody = f'''
<p>Prezados,</p>
<p>Segue relatório de Vendas por cada loja.</p>

<p>Faturamento:</p>
{faturamento.to_html(formatters={'Valor Final': 'R${:,.2f}'.format})}

<p>Quantidade Vendida:</p>
{quantidade.to_html()}

<p>Ticket Médio dos produtos em cada loja:</p>
{ticketMedio.to_html(formatters={'Ticket Médio': 'R${:,.2f}'.format})}


<p>Qualquer dúvida, estamos à disposição.</p>
<p>Att,</p>
'''
mail.Send()

print('Email enviado!')