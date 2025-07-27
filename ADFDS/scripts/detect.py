
import pandas as pd
import pickle
import sys

# Load the model
with open('ADFDS/models/ensemble_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Load test data (replace or adapt this as needed)
test_data = pd.read_csv(sys.argv[1])  # Input test file

# Predict
predictions = model.predict(test_data)
print("Predictions:", predictions)
