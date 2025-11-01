import matplotlib.pyplot as plt

numeros = list(range(1, 26)) 

x = numeros 
y = numeros 

plt.figure(figsize=(10, 6)) 

plt.plot(x, y, 
         marker='o',          
         linestyle='-',       
         color='blue',        
         label='Primeiros 25 Números') 

plt.title('Gráfico dos 25 Primeiros Números Inteiros', fontsize=16)
plt.xlabel('Ordem do Número (Eixo X)', fontsize=12)
plt.ylabel('Valor do Número (Eixo Y)', fontsize=12)

