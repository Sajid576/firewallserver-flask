
from flask import *
from second_layer.NoSql.feature_extractor import NoSqlFeatureExtractor
from second_layer.NoSql.nosql_injection_classifier import NoSqlInjection
from second_layer.Sql.feature_extractor import SqlFeatureExtractor
from second_layer.Sql.sql_injection_classifier import SqlInjection
from first_layer.common_malicious_payload_detector import *

app = Flask(__name__)

@app.route("/",methods=['GET'])
def  mainRoute():
  return "<h1>Welcome to the SQL and NoSQL Injection Detection Microservice</h1>"


@app.route("/malicious_payloads", methods=['POST'])
def detect_malicious_payloads_for_sql():
    try:
      payload_type = request.get_json()['payload_type']
      if(payload_type == 'sql'):
        print("SQL")
        second_layer_check = detect_malicious_sql(request.get_json()['data'])
        print(second_layer_check)
        res = {
            'message': "Successful",
            'error': 'NULL',
            'body': {
                'result': second_layer_check
            }
        }
        return res
      else:
        print("NoSQL")
        second_layer_check = detect_malicious_nosql(request.get_json()['data'])
        res = {
            'message': "Successful",
            'error': 'NULL',
            'body': {
                'result': second_layer_check
            }
        }
        return res

    except Exception as e:
        print(e)
        res = {"message": "Internal server error occurred"}
        return res
# Route for detecting SQL Injection by 2nd level
@app.route("/sql_injection",methods=['POST'])
def detectSqlInjection():
    try:
        SqlFeatureExtractor(request.get_json() )
        predictedClass=SqlInjection().predict()
        res={
                  'message':"SQL injection prediction successfully performed",
                  'error':'NULL',
                  'body':{
                    'result': predictedClass
                  }
                }
        return res
    except Exception as e:
        print(e)
        res = {"message": "Internal server error occurred"}
        return res


# Route for detecting NoSQL Injection by 2nd-level
@app.route("/nosql_injection", methods=['POST'])
def detectNoSqlInjection():
    try:
          feature_extractor_obj= NoSqlFeatureExtractor(request.get_json()['query'] )
          predictedClass=NoSqlInjection(feature_extractor_obj).predict()
          print("Predicted class:  "+str(predictedClass))
        
          res={
              'message':"NoSQL injection prediction successfully performed",
              'error':'NULL',
              'body':{
                'result':predictedClass
              }
            }
          return res
    except Exception as e:
        print(e)
        res = {"message": "Internal server error occurred"}
        return res
  

if __name__ == "__main__":
    app.run(port='8080',debug=True)