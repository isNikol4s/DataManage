from prettytable import PrettyTable

tabela = PrettyTable()
tabela.field_names = ["Codigo", "Níveis", "Tentativas"]

# Adicionando dados a tabela
tabela.add_row(["1", "Fácil", 7])
tabela.add_row(["2", "Médio", 5])
tabela.add_row(["3", "Difícil", 3])

#Tabela com niveis, e as tentativas que terão.

