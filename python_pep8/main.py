# from fila_normal import FilaNormal
# from fila_prioritaria import FilaPrioritaria
from fabrica_fila import FabricaFila

# fila_teste = FilaNormal()
# fila_teste.atualiza_fila()
# fila_teste.atualiza_fila() 
# fila_teste.atualiza_fila() 
# print(fila_teste.chama_cliente(5))
# print(fila_teste.chama_cliente(10))

# fila_teste2 = FilaPrioritaria()
# fila_teste2.atualiza_fila()
# fila_teste2.atualiza_fila()
# fila_teste2.atualiza_fila()
# print(fila_teste2.chama_cliente(20))
# print(fila_teste2.chama_cliente(15))
# print(fila_teste2.estatistica('12/11/2022', 198, 'detail'))

teste_fabrica = FabricaFila.pega_fila('normal')
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
print(teste_fabrica.chama_cliente(5))
