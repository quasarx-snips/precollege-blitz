
data_set = [[1.0, 3.2], [2.0, 5.3], [3.0, 7.1]]
multiplier = 0
step_speed = 0.01
bias = 0
for i in range(10000):
  for x,y in data_set:
    prediction = (x*multiplier)+bias
    error = y-prediction
    multiplier += step_speed*error*x
    bias += step_speed*error



print(multiplier,bias)
