import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from preprocess import load_and_prepare_data

print("Loading dataset...")

X, y, encoder = load_and_prepare_data()

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

print("Training Random Forest model...")

model = RandomForestClassifier(
    n_estimators=200,
    max_depth=6,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("Model accuracy:", round(accuracy * 100, 2), "%")

print("Confusion Matrix:")
print(confusion_matrix(y_test, predictions))

print("Saving trained model...")

pickle.dump((model, encoder), open("model.pkl", "wb"))

print("Model trained successfully")