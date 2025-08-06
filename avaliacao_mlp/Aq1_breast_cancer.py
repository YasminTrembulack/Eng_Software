from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, accuracy_score

# Carregar dados
data = load_breast_cancer()
X, y = data.data, data.target

# Dividir dados
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Função para avaliar e imprimir resultados
def avaliar_modelo(modelo, nome):
    modelo.fit(X_train_scaled, y_train)
    y_pred = modelo.predict(X_test_scaled)
    print(f"\n== {nome} ==")
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred, target_names=data.target_names))

# Normalização
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Cenário 1: Perceptron
modelo_1 = Perceptron(max_iter=1000, random_state=42)
avaliar_modelo(modelo_1, "Perceptron (baseline)")

# Cenário 2: MLP com 1 camada oculta
modelo_2 = MLPClassifier(hidden_layer_sizes=(30,), activation='relu', max_iter=1000, random_state=42)
avaliar_modelo(modelo_2, "MLP (30,) - relu")

# Cenário 3: MLP com 2 camadas ocultas
modelo_3 = MLPClassifier(hidden_layer_sizes=(50, 30), activation='relu', max_iter=1000, random_state=42)
avaliar_modelo(modelo_3, "MLP (50, 30) - relu")

# Cenário 4: MLP com ativação tanh
modelo_4 = MLPClassifier(hidden_layer_sizes=(30,), activation='tanh', max_iter=1000, random_state=42)
avaliar_modelo(modelo_4, "MLP (30,) - tanh")

# Cenário 5: MLP sem normalização (para comparação)
modelo_5 = MLPClassifier(hidden_layer_sizes=(30,), activation='relu', max_iter=1000, random_state=42)
modelo_5.fit(X_train, y_train)
y_pred_5 = modelo_5.predict(X_test)
print("\n== MLP (30,) - relu - sem normalização ==")
print("Accuracy:", accuracy_score(y_test, y_pred_5))
print(classification_report(y_test, y_pred_5, target_names=data.target_names))