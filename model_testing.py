#test the 3 models in deision_tree


import joblib

model = joblib.load("CART")
pred = model.predict([[40,1]])
print(pred)

model = joblib.load("RF")
pred = model.predict([[40,1]])
print(pred)

model = joblib.load("GB")
pred = model.predict([[40,1]])
print(pred)