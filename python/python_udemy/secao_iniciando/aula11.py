velocidade = 61  # Velocidade atual do carro
local_carro = 100  # km em que o carro está na estrada

RADAR_1 = 60  # Velocidade máxima do radar.
LOCAL_1 = 100  # km aonde está o 1° radar.
RADAR_RANGE = 1  # Circunferência do radar.

velocidade_carro_pass_radar1 = velocidade > RADAR_1
carro_multa_radar1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
   local_carro <= (LOCAL_1 + RADAR_RANGE)


if velocidade_carro_pass_radar1:
  print('Velocidade acima do limite no radar 1')

if carro_multa_radar1 and velocidade_carro_pass_radar1:
  print('Carro multado em radar 1')
