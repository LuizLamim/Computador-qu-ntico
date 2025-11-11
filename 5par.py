import matplotlib.pyplot as 

numeros_pares = [2, 4, 6, 8, 10]

ordem = [1, 2, 3, 4, 5]

plt.figure(figsize=(8, 5)) 
plt.plot(ordem, numeros_pares, 
         marker='o',          
         linestyle='-',       
         color='blue',        
         label='Primeiros 5 Pares') 

plt.title('Plotagem dos 5 Primeiros Números Pares')
plt.xlabel('Ordem do Número Par')
plt.ylabel('Valor do Número Par')

plt.yticks(numeros_pares) 

# Adiciona a legenda
plt.legend() 

plt.grid(True, linestyle='--', alpha=0.6) 

plt.show()