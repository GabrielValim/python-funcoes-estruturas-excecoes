# 7. Você recebeu uma demanda para tratar 2 listas com os nomes e sobrenomes de cada estudante concatenando-as para apresentar seus nomes completos na forma Nome Sobrenome. As listas são:

nomes = ["joão", "MaRia", "JOSÉ"]
sobrenomes = ["SILVA", "souza", "Tavares"]

#  Função lambda que recebe duas listas e itera em cada uma concatenando seu nome e sobrenome
# na forma desejada
nome_completo = map(lambda nome, sobrenome: f'{nome.title()} {sobrenome.title()}', nomes, sobrenomes)

# Leitura do objeto mapa(iterável)
for n in nome_completo:
  print(f'Nome completo: {n}')