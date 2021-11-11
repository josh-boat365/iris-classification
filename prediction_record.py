import pickle 
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
#load the model into memory
with open ('model.pkl', 'rb') as model_pkl:
    knn = pickle.load(model_pkl)

#test data
new_record = np.array([[1.2,1.6,1.8,2.4]])
predict_result = knn.predict(new_record)

print('Predicted results for observation' + str(new_record) + 'is: ' + str(predict_result))

