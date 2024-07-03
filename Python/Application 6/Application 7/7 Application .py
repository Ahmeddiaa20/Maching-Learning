#Assignment 7 by Ahmed Diaa
from sklearn.model_selection import train_test_split # type: ignore
from sklearn.linear_model import LinearRegression # type: ignore
from sklearn.metrics import mean_squared_error # type: ignore
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)

X = 2 * np.random.rand(100, 1)

Y = 4 * 3 * X + np.random.randn(100, 1)  # Corrected generation of Y with noise

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

model = LinearRegression()  # Correct instantiation of LinearRegression

model.fit(X_train, Y_train)

Y_pred = model.predict(X_test)

plt.scatter(X, Y, alpha=0.7, label='Original Data')

plt.plot(X_test, Y_pred, color='red', linewidth=2, label='Linear Regression')  # Corrected linewidth argument
plt.title('Linear Regression in Python')

plt.xlabel('X')

plt.ylabel('Y')

plt.legend()

plt.show()

mse = mean_squared_error(Y_test, Y_pred)

print(f'Mean Squared Error: {mse}')