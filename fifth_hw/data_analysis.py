import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score, RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, roc_auc_score

seed = 17

df = pd.read_csv('/Users/micheleatzeni/Desktop/python course/fifth_hw/PokemonResult.csv', delimiter=';')
## outcome
y = pd.read_csv('/Users/micheleatzeni/Desktop/python course/fifth_hw/RefactoredOutcomePokemonResult.csv', delimiter=',')
y = y.astype(int)

## independent variables
x = pd.read_csv('/Users/micheleatzeni/Desktop/python course/fifth_hw/RefactoredPokemonResult.csv', delimiter=',')


training_data, test_data, training_labels, test_labels = train_test_split(x, y, test_size=0.3, random_state = seed, stratify=y)

# rf does not accept nans
rf = RandomForestClassifier().fit(training_data, training_labels)
y_pred = rf.predict_proba(test_data)

accuracy = accuracy_score(test_labels, rf.predict(test_data))
auc = roc_auc_score(test_labels, rf.predict(test_data))
probs = rf.predict_proba(test_data)

# tuning

#scores = cross_val_score(regr, training_data, training_labels, cv = 5)
print("Scores (accuracy):", str(accuracy))
print("Scores (auc):", str(auc))
print("Scores (probabilities):", str(probs))









