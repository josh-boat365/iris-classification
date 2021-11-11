#training resource - https://atrium.ai/resources/build-and-deploy-a-docker-containerized-python-machine-learning-model-on-heroku/
#loading datasets from sklearn
from sklearn import datasets
#to build accuracy we split the dataset into train and text
from sklearn.model_selection import train_test_split
#build model using KNeighbors
from sklearn import neighbors
from sklearn.metrics import accuracy_score
import  pickle


iris = datasets.load_iris()

#separating features and target lables in different data frames

x = iris.data
y= iris.target

#spliting data into train and test
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size= 0.3)

knn = neighbors.KNeighborsClassifier()

#training model for prediction on test dataset to calculate accuracy

knn.fit(x_train,y_train)

predictions = knn.predict(x_test)

#testing for the accuracy of the predictions on the data 'x' 
print(accuracy_score(y_test,predictions))

#exporting the ml model coefficients into a pickle 'pkl' file - we do this so that we don't have to retrain the model when we want to make future predictions.
with open('model.pkl', 'wb') as model_pkl:
    #store classification model into pickle file
    pickle.dump(knn, model_pkl)


