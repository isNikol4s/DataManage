import pandas as pd

data = {
    "Nome": ["Alice", "Bob", "Carol"],
    "Idade": [25, 30, 22],
    "Cidade": ["Nova York", "Los Angeles", "Chicago"]
}

tabela = pd.DataFrame(data)

# Para acessar os dados da tabela:
print(tabela)