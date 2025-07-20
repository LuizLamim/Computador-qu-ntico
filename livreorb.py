import numpy as np
import matplotlib.pyplot as plt

 def calcular_orbita_com_tempo(tempo_total=10 * 2 * np.pi, passo_tempo=0.005):
     
     G = 1.0
     M_sol = 1.0

     posicao_x_inicial = 1.0
     posicao_y_inicial = 0.0
     velocidade_x_inicial = 0.0
     velocidade_y_inicial = np.sqrt(G * M_sol / posicao_x_inicial)

     num_passos = int(tempo_total / passo_tempo)

     posicoes_x = np.zeros(num_passos)
     posicoes_y = np.zeros(num_passos)
     deslocamentos = np.zeros(num_passos) # Para armazenar a distância da Terra ao Sol
     tempos = np.zeros(num_passos)        # Para armazenar o tempo correspondente

     posicao_atual_x = posicao_x_inicial
     posicao_atual_y = posicao_y_inicial
     velocidade_atual_x = velocidade_x_inicial
     velocidade_atual_y = velocidade_y_inicial

     for i in range(num_passos):
         
         distancia_ao_sol = np.sqrt(posicao_atual_x**2 + posicao_atual_y**2)
         deslocamentos[i] = distancia_ao_sol
         tempos[i] = i * passo_tempo 

         forca_gravitacional_modulo = (G * M_sol) / (distancia_ao_sol**2)
         forca_x = -forca_gravitacional_modulo * (posicao_atual_x / distancia_ao_sol)
         forca_y = -forca_gravitacional_modulo * (posicao_atual_y / distancia_ao_sol)

         aceleracao_x = forca_x
         aceleracao_y = forca_y

         velocidade_atual_x += aceleracao_x * passo_tempo
         velocidade_atual_y += aceleracao_y * passo_tempo

         posicao_atual_x += velocidade_atual_x * passo_tempo
         posicao_atual_y += velocidade_atual_y * passo_tempo

         posicoes_x[i] = posicao_atual_x
         posicoes_y[i] = posicao_atual_y

     return tempos, deslocamentos

 
 def plotar_deslocamento(tempos, deslocamentos):
     """
     Plota o gráfico do deslocamento (distância da Terra ao Sol) em função do tempo.
     """
     plt.figure(figsize=(10, 6))
     plt.plot(tempos, deslocamentos, color='red')
     plt.title('Deslocamento da Terra em Relação ao Sol ao Longo do Tempo')
     plt.xlabel('Tempo')
     plt.ylabel('Distância da Terra ao Sol')
     plt.grid(True)
     plt.show()

 if __name__ == "__main__":
     
     tempos_orbita, deslocamentos_orbita = calcular_orbita_com_tempo()

     plotar_deslocamento(tempos_orbita, deslocamentos_orbita)