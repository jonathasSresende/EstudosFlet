# n (next): Executa a proxima linha do codigo.
# s (step): Entra em uma funçao chamada na linha atual.
# c (continue): Continue a execução ate o proximo breakpoint.
# q (quit): Sai do Depurador.
# p nome_variavel: Imprime o valor de nome_variavel
# l (list): Lista o codigo ao redor da linha atual
def soma(a,b):
    import pdb;pdb.set_trace() #depuraçao começa aqui
    variavel="Carlos"
    return a + b

resultado=soma(2,3)
print(resultado)

#python -m pdb seu script.py

