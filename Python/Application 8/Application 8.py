# Application 8 by Ahmed Diaa
from sklearn.model_selection import train_test_split # type: ignore
from sklearn.linear_model import LinearRegression # type: ignore
from sklearn.preprocessing import PolynomialFeatures # type: ignore
from sklearn.metrics import mean_squared_error # type: ignore
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
X = 6 * np.random.rand(100, 1) - 3
Y = 0.5 * X ** 2 * X + 2 * np.random.randn(100, 1)  # Corrected formula

poly_features = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly_features.fit_transform(X)

poly_reg = LinearRegression()
poly_reg.fit(X_poly, Y)

X_new = np.linspace(-3, 3, 100).reshape(100, 1)
X_new_poly = poly_features.transform(X_new)
Y_new = poly_reg.predict(X_new_poly)

plt.scatter(X, Y, alpha=0.7, label='Original data')  # Fixed alpha spelling
plt.plot(X_new, Y_new, color='green', linewidth=2, label='Polynomial Regression')
plt.title('Polynomial Regression')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()