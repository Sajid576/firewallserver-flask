from joblib import *
import pandas as pd
import string

nosql_feature_extractor_model_path='storage/feature_extraction.joblib'

class NoSQL_Feature_Extraction:
  

  def setPayloadURL(self,payloadurl):
      self.payloadurl = payloadurl
  
  def extractFeature(self, query):
    #sheet_url='https://docs.google.com/spreadsheets/d/1il54YsQNfGxLOeMvG94PyymbKZ-JeddP/edit#gid=1921110563'
    csv_export_url = self.payloadurl.replace('/edit#gid=', '/export?format=csv&gid=')
    pl = pd.read_csv(csv_export_url)

    tempQuery = query.translate({ord(c): None for c in string.whitespace}) #removing all whitespace
    # Feature 1
    # Detect if query has $ne

    def containsCondition(query):
      condition = ["find(", "$selector", "find.sort("]
      condition2 = ["$eq", "$gt", "$gte" , "$ne", "$lt", "$lte", "$in", "$nin"]
      for i in condition:
        if i in query:
          return 1
      for i in condition2:
        if i in query:
          return 0
      return 0  

    # Feature 2
    # Detects piggy back query

    def isNewQuery(query):
      if ";db.(" in query:
        return 1
      else:
        return 0

    # Feature 3
    # Detect if query contains empty string

    def containsEmptyString(query):
      if "\"\"" in query or "''" in query:
        return 1
      else:
        return 0  

    # Feature 4
    # Detect if query has $ne

    def containsNotEqual(query):
      if "$ne" in query:
        return 1
      else:
        return 0

    # Feature 5
    # Detect if query contains payload

    def containsPayload(tempQuery):
      try:
        for i in range(32):
          temp = df.loc[i].values[0]
          temp = temp.translate({ord(c): None for c in string.whitespace})
          if temp in tempQuery:
            return 1 
      except:
        print("Error")
      return 0   

    # Feature 6
    # Detect if query contains return

    def containsReturn(query):
      returnlist = [";return", "return 1", "return true" , "return(true)"]
      for i in returnlist:
        if i in query:
          return 1
      return 0       

    # Feature 7
    # Detect if query is always true

    def containsRegexTrue(tempQuery):
      if "/.*/" in tempQuery or "/./" in tempQuery or "/." in tempQuery:
        return 1
      return 0


    # Feature 8
    # Detect if query contains evaluation operators

    def evalQueryOperations(tempQuery):
      evalop = ["$mod", "$regex", "$text" , "$where"]
      for i in evalop:
        if i in tempQuery:
          return 1
      return 0  

    # Feature 9
    # Detect if query contains logical operators

    def containsLogicalOp(query):
      logop = ["$or", "$and", "$not" , "$nor"]
      for i in logop:
        if i in query:
          return 1
      return 0


    # Feature 10
    # Detect if query contains element operation

    def elementQueryOperations(tempQuery):
      if "$exists" in tempQuery or "$type" in tempQuery:
        return 1
      return 0

  
    features = []
    features.append(containsCondition(query))
    features.append(isNewQuery(query))
    features.append(containsEmptyString(query))
    features.append(containsNotEqual(query))
    features.append(containsPayload(tempQuery))
    features.append(containsReturn(query))
    features.append(containsRegexTrue(tempQuery))
    features.append(evalQueryOperations(tempQuery))
    features.append(containsLogicalOp(query))
    features.append(elementQueryOperations(tempQuery))
    return features 


class NoSqlFeatureExtractor:
        def loadModel(self,feature_object_name):
            feature_object_name = load(feature_object_name)
            return feature_object_name
        def __init__(self,query):
            self.query = query
            print(self.query)
            
            #feature_object = self.loadModel(nosql_feature_extractor_model_path)
            feature_object = NoSQL_Feature_Extraction()
            feature_object.setPayloadURL("https://docs.google.com/spreadsheets/d/1il54YsQNfGxLOeMvG94PyymbKZ-JeddP/edit#gid=1921110563")
            self.result = feature_object.extractFeature(query)
            print(self.result)
           
