from prettytable import PrettyTable

tabela = PrettyTable()
tabela.field_names = ["Codigo", "Níveis", "Segundos"]

# Adicionando dados a tabela
tabela.add_row(["1", "Fácil", 50])
tabela.add_row(["2", "Médio", 25])
tabela.add_row(["3", "Difícil", 15])

#Tabela com niveis, e as tentativas que terão.

