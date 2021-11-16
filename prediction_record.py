import pickle 
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris

iris_dataset = load_iris()
#load the model into memory
with open ('./python_docker_heroku/model.pkl', 'rb') as model_pkl:
    knn = pickle.load(model_pkl)

#test data
new_record = np.array([[2.0,2.8,2.1,2.0]])
predict_result = knn.predict(new_record)
pred_name = iris_dataset['target_names'][predict_result]
print('Predicted results for observation' + str(new_record) + 'is: ' + str(predict_result), pred_name)



