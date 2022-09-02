import math
e = 1
x = 10
i = 1000000                 # Numero de iteraciones
n = math.exp(x)
while i > 0:
    e = 1 + (1 / i) * x * e # 1 + x (1 + x / 2 (1 + x / 3 (...(1 + 1 / n)...)))
    i = i - 1                # b_{i} = 1 + x / i (b_{i + 1}); b_{n} = 1 + x / n
print("Propio:", e)
print("Python:", n)
print("Error:", n - e)
