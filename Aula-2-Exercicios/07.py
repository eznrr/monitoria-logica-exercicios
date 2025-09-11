# Exercício 7: Pré-Análise de Crédito Bancário
# Complete usando and, or e not

"""
    - O programa deve solicitar ao usuário sua renda mensal, idade e se possui
    - o nome negativado (respondendo com "sim" ou "nao").

Regras para ser considerado apto ao empréstimo é:
    - Ter renda mensal de R$ 2.000,00 ou mais.
    E
    - Atender a pelo menos uma das seguintes condições:
        - Ter mais de 21 anos.
        OU 
        - NÃO possuir nome negativado.

O desafio é obter os dados, aplicar a lógica e imprimir o resultado
(True ou False) indicando se o cliente está apto.
"""

print("--- Análise de Crédito Simplificada ---")
renda = float(input("Qual a sua renda mensal? (digite apenas números): "))
idade = int(input("Qual a sua idade? "))
negativado = input("Você possui nome negativado? (s/n): ")

# --- Crie a expressão lógica aqui ---
nome_negativado = ...

tem_renda_suficiente = ...

atende_condicao_extra = ...

apto_para_emprestimo = ...

print("\nApto para próxima fase do empréstimo?")
if apto_para_emprestimo == True:
    print("Sim!")
else:
    print("Não.")