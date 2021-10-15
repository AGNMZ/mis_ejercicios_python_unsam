
import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)    
    return pasos.cumsum()

def mas_alejado(caminatas : list) -> int:
    maximo_caminatas = [max(np.abs(caminata)) for caminata in caminatas]
    pos = maximo_caminatas.index(max(maximo_caminatas))
    return pos

def menos_alejado(caminatas : list) -> int:
    maximo_caminatas = [max(np.abs(caminata)) for caminata in caminatas]
    pos = maximo_caminatas.index(min(maximo_caminatas))
    return pos


N = 100000
fig = plt.figure()
plt.subplot(2,1,1)
plt.title('12 Caminatas al azar')
plt.ylim((-1000, 1000))
plt.yticks([-500, 0, 500])
plt.xlabel('Tiempo')
plt.ylabel('Distancia al origen')
walks = [randomwalk(N) for _ in range(12)]
for walk in walks:
    plt.plot(walk)
abs_walks = [np.abs(walk) for walk in walks]
plt.subplot(2,2,3)
plt.ylim((-1000, 1000))
plt.yticks([-500, 0, 500])
plt.ylabel('Distancia al origen')
plt.xlabel('Tiempo')
plt.plot(walks[mas_alejado(walks)])
plt.title('La caminata que mas se aleja')
plt.subplot(2,2,4)
plt.ylim((-1000, 1000))
plt.yticks([])
plt.xlabel('Tiempo')
plt.title('La caminata que menos se aleja')
plt.plot(walks[menos_alejado(walks)])
plt.show()