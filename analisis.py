import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

# Generate data
x = np.arange(10).reshape(-1, 1)
y = 2 * x + 1 + np.random.randn(10, 1)

# Simpan dalam DataFrame
df = pd.DataFrame({"x": x.flatten(), "y": y.flatten()})

# Regresi
model = LinearRegression()
model.fit(x, y)
pred = model.predict(x)

# Plot dengan seaborn
sns.scatterplot(x="x", y="y", data=df, label="Data")
plt.plot(x, pred, color="red", label="Regression")
plt.legend()
plt.title("Linear Regression Example")
plt.savefig("plot.png")
print("Analysis complete, saved plot.png")
