
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from xgboost import XGBClassifier
from sklearn.naive_bayes import GaussianNB

# Load your dataset (replace with actual path)
data = pd.read_csv('dataset/processed_features.csv')  # placeholder

X = data.drop(columns=['label'])
y = data['label']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Ensemble classifiers
clf1 = RandomForestClassifier(n_estimators=100, random_state=42)
clf2 = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
clf3 = SVC(probability=True)
clf4 = KNeighborsClassifier()
clf5 = GaussianNB()

ensemble = VotingClassifier(estimators=[
    ('rf', clf1), ('xgb', clf2), ('svc', clf3),
    ('knn', clf4), ('gnb', clf5)
], voting='soft')

ensemble.fit(X_train, y_train)

# Save the model
with open('ADFDS/models/ensemble_model.pkl', 'wb') as f:
    pickle.dump(ensemble, f)

print("Model trained and saved to ADFDS/models/ensemble_model.pkl")
