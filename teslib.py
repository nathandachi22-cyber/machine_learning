# test_libraries.py

print("=== Testing Installed Libraries ===")

# 1. NumPy
try:
    import numpy as np
    arr = np.array([1, 2, 3])
    print("NumPy OK:", arr)
except Exception as e:
    print("NumPy ERROR:", e)

# 2. Pandas
try:
    import pandas as pd
    df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
    print("Pandas OK:\n", df)
except Exception as e:
    print("Pandas ERROR:", e)

# 3. Matplotlib
try:
    import matplotlib.pyplot as plt
    plt.plot([1, 2, 3], [1, 4, 9])
    plt.title("Matplotlib Test")
    plt.close()
    print("Matplotlib OK")
except Exception as e:
    print("Matplotlib ERROR:", e)

# 4. scikit-learn
try:
    from sklearn.linear_model import LinearRegression
    model = LinearRegression()
    model.fit([[0], [1], [2]], [0, 1, 2])
    print("Scikit-learn OK, coef:", model.coef_)
except Exception as e:
    print("Scikit-learn ERROR:", e)

# 5. Seaborn
try:
    import seaborn as sns
    import matplotlib.pyplot as plt
    sns.set()
    sns.lineplot(x=[0, 1, 2], y=[0, 1, 4])
    plt.close()
    print("Seaborn OK")
except Exception as e:
    print("Seaborn ERROR:", e)

# 6. PyQt5
try:
    from PyQt5.QtWidgets import QApplication, QLabel
    app = QApplication([])
    label = QLabel("Hello PyQt5")
    label.setWindowTitle("PyQt5 Test")
    # tidak menjalankan app.exec_() biar tidak blocking
    print("PyQt5 OK (GUI not shown)")
except Exception as e:
    print("PyQt5 ERROR:", e)

# 7. pygame
try:
    import pygame
    pygame.init()
    screen = pygame.display.set_mode((200, 100))
    pygame.display.set_caption("Pygame Test")
    pygame.quit()
    print("Pygame OK")
except Exception as e:
    print("Pygame ERROR:", e)

# 8. Flask
try:
    from flask import Flask
    app = Flask(__name__)

    @app.route("/")
    def home():
        return "Hello Flask!"

    print("Flask OK (app created)")
except Exception as e:
    print("Flask ERROR:", e)

# 9. Django
try:
    import django
    from django.conf import settings
    settings.configure()
    django.setup()
    print("Django OK, version:", django.get_version())
except Exception as e:
    print("Django ERROR:", e)

print("=== Testing Complete ===")
