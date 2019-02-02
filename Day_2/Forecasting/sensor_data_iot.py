import pandas as pd

from sklearn.metrics import mean_squared_error
from math import sqrt
import matplotlib.pyplot as plt

df = pd.read_csv('feeds.csv')

train = df[0:110]
test = df[110:]


y_hat_avg = test.copy()
y_hat_avg['moving_avg_forecast'] = train['field2'].rolling(60).mean().iloc[-1]
rms = sqrt(mean_squared_error(test.field2, y_hat_avg.moving_avg_forecast))
print(rms)

plt.figure(figsize=(12, 8))
plt.grid(True)
plt.title('temperature')
plt.plot(train.created_at, train.field2, color='blue')
plt.plot(test.created_at, test.field2, color='red')
plt.plot(y_hat_avg.created_at, y_hat_avg['moving_avg_forecast'], label='Naive Forecast')
plt.show()
