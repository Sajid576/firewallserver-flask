from joblib import *

nosql_feature_extractor_model_path='storage/feature_extraction.joblib'


class NoSqlFeatureExtractor:
        def loadModel(self,feature_object_name):
            feature_object_name = load(feature_object_name)
            return feature_object_name
        def __init__(self,query):
            self.query = query
            print(self.query)
            feature_object =self.loadModel(nosql_feature_extractor_model_path)
            feature_object.setPayloadURL('https://docs.google.com/spreadsheets/d/1il54YsQNfGxLOeMvG94PyymbKZ-JeddP/edit#gid=1921110563')
            self.result = feature_object.extractFeature(query)
          
           
