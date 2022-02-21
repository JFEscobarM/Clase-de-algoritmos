"""
Datos de entrada
X, M-->int

Datos de salida
Y-->int
"""
while True:
  X, M=map(int, input().split())
  if X==0 and M==0:
      break
  Y=X*M
  print(Y)