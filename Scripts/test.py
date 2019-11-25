import redeHibrida as rn
import dinoClasse as dn

dino = []

for i in range(32):
    dino.append(dn.DinoClasse())

#for i in range(32):
#    print(f'I: {i} - Cerebro: {dino[i].cerebro.nos_s}')

#print(type(dino[0].cerebro.pesos_eo))

print(dino[0].cerebro.pesos_eo)
print(dino[0].cerebro.pesos_eo[0][0])