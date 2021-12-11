from joblib import *

nosql_model_path='storage/Adaboost.joblib'

class  NoSqlInjection():

        def __init__(self,feature_extractor):
            print(nosql_model_path)
            self.feature_extractor=feature_extractor

        def loadModel(self,nosql_model_path):
            model_object= load(nosql_model_path)
            return model_object

        def predict(self):
                features_val= self.feature_extractor.result
                adaboost=self.loadModel(nosql_model_path)
                result = adaboost.best_estimator_.predict([features_val])
                #converting numpy array to list
                result=result.tolist()
                # converting list to integer
                result=result[0]
                return result
        