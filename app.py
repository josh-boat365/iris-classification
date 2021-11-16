import pickle
import sys
import os
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
import  numpy as np
from flask import Flask, request


port = int(os.environ.get("PORT",5000))
iris_dataset = load_iris
#initialise flask app
app = Flask(__name__) 

#loading trained model
pickle_file = open('./python_docker_heroku/model.pkl','rb')

knn = pickle.load(pickle_file)

@app.route('/')
def home():
    return "This is a Test Page for Docker Containerization!!!!"

#creating an API endpoint - a route 
@app.route('/predict')
def predict_iris():
    #read all necessary request parameters - sl= sepal length, sw= sepal width, pl= petal length, pw= petal width
    sl = request.args.get('sl')
    sw = request.args.get('sw')
    pl = request.args.get('pl')
    pw = request.args.get('pw')
    
    #get the prediction for unseen data
    new_record = np.array([[sl, sw, pl, pw]])
    predict_result = knn.predict(new_record)
    pred_name = iris_dataset['target_names'][predict_result]
    return 'Predicted result for observation ' + str(new_record) + ' is: '+ str(predict_result), pred_name

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)