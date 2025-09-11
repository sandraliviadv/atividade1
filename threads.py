# Importação de biblioteca 
import threading  
import time    

#  Definição da função que será executada por cada thread
def estruturathread (nome, inicio, fim): # A função recebe um nome para identificar a thread, e os números de início e fim do laço
    for i in range(inicio, fim +1): # Estrutura de repetição que vai do valor 'inicio' até 'fim' 
        print(f"{nome} - > {i}")# Exibe o nome da thread e o número atual do laço
        time.sleep(0.5) # Pausa a thread por 0.5 segundos entre cada numero
        
# Aqui criamos dois objetos de thread, indicando:
# - qual função elas devem executar (estruturathread)
# - quais argumentos essa função receberá (nome da thread, valor inicial e final do laço)
thread1 = threading.Thread(target=estruturathread,args=("thread1", 1, 10))# Vai imprimir de 1 a 10        
thread2 = threading.Thread(target=estruturathread, args=("thread2", 50, 60))# Vai imprimir de 50 a 60

# Iniciamos a execução das threads em paralelo
thread1.start() # Inicia a execução da primeira thread
thread2.start() # Inicia a execução da segunda thread

# Faz o programa principal esperar até que cada thread termine
thread1.join()
thread2.join()

print('Threands finalizadas com sucesso!')