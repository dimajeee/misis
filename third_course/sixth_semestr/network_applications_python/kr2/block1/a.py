# Библиотека NumPy. Что означают отрицательные индексы в срезах массивов. Примеры.

import numpy as np

text = "Этот код шифрует слова задом наперёд"
words = np.array(text.split())

# Разворачиваем буквы в каждом слове, но сохраняем порядок слов
encrypted = np.array([word[::-1] for word in words])

print("Оригинал:", words)
print("Зашифровано:", ' '.join(encrypted))