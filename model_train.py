import json
import pandas as pd

# from sklearn import svm
from sklearn.model_selection import train_test_split

with open('./train_data/sample_with_keywords.json') as f:
    laws = json.load(f)

matriz = []
for law in laws:
    matriz.append([law['tag'],law['text']])
      
df = pd.DataFrame(matriz, columns = ['tag','text'])

datos_y = df.tag
datos_X = df.text

X_train, X_test, y_train, y_test = train_test_split(
    datos_X,
    datos_y,
    test_size = 0.2,
    random_state=42,
    stratify=datos_y
)

# modelo_svm_lineal = svm.SVC(C=100, gamma=0.01).fit(X=tfidf_train, y= y_train)