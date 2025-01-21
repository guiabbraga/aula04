idade: int = 31
altura: float = 1.75
nome: str = "Guilherme"
estudante: bool = True


# # 1. Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
# number_list = list(range(1, 10))
# for num in number_list:
#     print(num**2)


# # 2. Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".
# language_list = ["Python", "Java", "C++", "JavaScript"]
# language_list.remove("C++")
# language_list.append("Ruby")
# print(language_list)


# # 3. Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.
# books_dict = {
#     "livro01": {"título": "Engenharia de Dados",
#                 "autor": "Luciano Vasconcelos",
#                 "ano de publicação": "2020"
#                 },
#     "livro02": {"título": "Game of Thrones",
#                 "autor": "Estagiario",
#                 "ano de publicação": "2018"
#                 },
# }
# for books in books_dict:
#     print(books, "-", books_dict[books])


# 4.Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
string = "contar os caracteres dessa frase usando um dicionario"

print({e: string.count(e) for e in set(string)})
