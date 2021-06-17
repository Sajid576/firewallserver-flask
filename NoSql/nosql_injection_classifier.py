from joblib import *

nosql_model_path='storage/Adaboost.joblib'

class  NoSqlInjection():

        def __init__(self):
            print(nosql_model_path)
            self.loadModel(nosql_model_path)


        def loadModel(self,nosql_model_path):
            self.model_object= load(nosql_model_path)
           
        
        def predict(self):
                result= self.model_object.best_estimator_.predict([[1,1,0,1,0,0,0,0,0,	0]])
                #converting numpy array to list
                result=result.tolist()
                # converting list to integer
                result=result[0]
                return result
        