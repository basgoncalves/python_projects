import pandas as pd
import os
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

print (os.getcwd())
current_file = __file__
music_data = pd.read_csv(os.path.join(current_file,'..\\music.csv'))
X = music_data.drop(columns=['genre'])
y = music_data['genre']
X_train, X_test, y_train,y_test = train_test_split(X,y,test_size=0.2)

model = DecisionTreeClassifier()
model.fit(X_train,y_train)
predictions = model.predict(X_test)
score = accuracy_score(y_test, predictions)
print('test accuracy = ', score)