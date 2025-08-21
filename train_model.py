import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, accuracy_score
import shap
import numpy as np
import pickle

df = pd.read_csv("sorted_file.csv")

if 'error' in df.columns:
    df = df[df['error'].isna()].drop(columns=['error'])

# Drop rows with any remaining NaNs
df = df.dropna()


# Separate features and labels
X = df.drop(columns=["filename", "label"])
y = df["label"]

# Optionally scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state = 1)

# Train model
clf = RandomForestClassifier(random_state=1)
clf.fit(X_train, y_train)

# Predict and evaluate
y_pred = clf.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Cross-validation
scores = cross_val_score(clf, X_scaled, y, cv=5)
print("\nCross-validated accuracy:", scores.mean())
# Feature Importance
importances = clf.feature_importances_
features = X.columns
plt.figure(figsize=(10, 6))
plt.barh(features, importances)
plt.xlabel("Importance")
plt.title("Feature Importance (Random Forest)")
plt.tight_layout()
plt.savefig("feature_importance.png")

pickle.dump(clf,open("model.pkl","wb")) #freezes trained model so no need to retrain
pickle.dump(scaler, open("scaler.pkl", "wb"))
model = pickle.load(open('model.pkl','rb')) #deploy