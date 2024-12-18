
# parameterization inputs: [inlet temperature, inlet velocity, heat flux]
paraInList = [[438.15, 2.511048614, 458333.3333], # 1
              [458.15, 2.511048614, 458333.3333], # 3
              [478.15, 2.511048614, 458333.3333], # 5
              [458.15, 2.287844293,	458333.3333], # +8
              [438.15, 2.064639971, 458333.3333], # 11
              [458.15, 2.064639971, 458333.3333], # 13
              [478.15, 2.064639971, 458333.3333], # 15
              [458.15, 1.84143565,  458333.3333], # +18
              [438.15, 1.618231329, 458333.3333], # 21
              [458.15, 1.618231329, 458333.3333], # 23
              [478.15, 1.618231329, 458333.3333], # 25
              [458.15, 2.511048614, 375000.0   ], # +28 
              [438.15, 2.287844293, 375000.0   ], # +31
              [468.15, 2.287844293, 375000.0   ], # +34
              [448.15, 2.064639971, 375000.0   ], # +37
              [478.15, 2.064639971, 375000.0   ], # +40
              [458.15, 1.84143565,  375000.0   ], # +43
              [438.15, 1.618231329, 375000.0   ], # +46
              [468.15, 1.618231329, 375000.0   ], # +49
              [438.15, 2.511048614, 291666.6667], # 51
              [458.15, 2.511048614, 291666.6667], # 53
              [478.15, 2.511048614, 291666.6667], # 55
              [458.15, 2.287844293, 291666.6667], # +58
              [438.15, 2.064639971, 291666.6667], # 61
              [458.15, 2.064639971, 291666.6667], # 63
              [478.15, 2.064639971, 291666.6667], # 65
              [458.15, 1.84143565,  291666.6667], # +68
              [438.15, 1.618231329, 291666.6667], # 71
              [458.15, 1.618231329, 291666.6667], # 73
              [478.15, 1.618231329, 291666.6667], # 75
              [458.15, 2.511048614, 208333.3333], # +78
              [438.15, 2.287844293, 208333.3333], # +81
              [468.15, 2.287844293, 208333.3333], # +84
              [448.15, 2.064639971, 208333.3333], # +87
              [478.15, 2.064639971, 208333.3333], # +90
              [458.15, 1.84143565,  208333.3333], # +93
              [438.15, 1.618231329, 208333.3333], # +96
              [468.15, 1.618231329, 208333.3333], # +99
              [438.15, 2.511048614, 125000.], # 101
              [458.15, 2.511048614, 125000.], # 103
              [478.15, 2.511048614, 125000.], # 105
              [458.15, 2.287844293, 125000.], # +108
              [438.15, 2.064639971, 125000.], # 111
              [458.15, 2.064639971, 125000.], # 113
              [478.15, 2.064639971, 125000.], # 115
              [458.15, 1.84143565,	125000.], # 118
              [438.15, 1.618231329, 125000.], # 121
              [458.15, 1.618231329, 125000.], # 123
              [478.15, 1.618231329, 125000.]] # 125

lenParaIn = len(paraInList)

# normalize the input
for i in range(lenParaIn):
  paraInList[i][0] = (paraInList[i][0] - 400.0) / 100.0

for i in range(lenParaIn):
  paraInList[i][1] = paraInList[i][1] - 1.5

for i in range(lenParaIn):
  paraInList[i][2] = paraInList[i][2] / 1000000.0

if __name__=="__main__":
  print(lenParaIn)
  #for i in range(len(paraInList)):
  #  print(paraInList[i][0])
  #for i in range(len(paraInList)):
  #  print(paraInList[i][2])