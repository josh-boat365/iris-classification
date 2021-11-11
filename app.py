import pickle
import sys
import os
from sklearn.neighbors import KNeighborsClassifier
import  numpy as np
from flask import Flask, request

port = int(os.environ.get("PORT",500))

#loading trained model
with open('./python_docker_heroku/model.pkl','rb') as model_pkl:
    knn = pickle.load(model_pkl)

#initialise flask app

app = Flask(__name__)

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

    return 'Predicted result for observation ' + str(new_record) + ' is: '+ str(predict_result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)