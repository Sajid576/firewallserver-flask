
from flask import *
from NoSql.feature_extractor import NoSqlFeatureExtractor
from NoSql.nosql_injection_classifier import NoSqlInjection
from Sql.feature_extractor import  SqlFeatureExtractor
from Sql.sql_injection_classifier import  SqlInjection

app = Flask(__name__)

@app.route("/",methods=['GET'])
def  mainRoute():
  return "<h1>Welcome to the SQL/NoSQL Injection Detection Machine Learning Model API</h1>"
  
# Route for detecting SQL Injection
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
                  print("Oops!", e.message, "occurred.")
                  res={
                        'message':e.message,
                        'error':"Err",
                        'body':{
                          'result':""
                        }
                      }
                  return res



# Route for detecting NoSQL Injection
@app.route("/nosql_injection",methods=['POST'])
def detectNoSqlInjection():
    try:
          NoSqlFeatureExtractor(request.get_json() )
          predictedClass=NoSqlInjection().predict()
          print(predictedClass)
        
          res={
              'message':"NoSQL injection prediction successfully performed",
              'error':'NULL',
              'body':{
                'result':predictedClass
              }
            }
          return res
    except Exception as e:
        print("Oops!", e.message, "occurred.")
        res={
              'message':e.message,
              'error':"Err",
              'body':{
                'result':""
              }
            }
        return res
  

if __name__ == "__main__":
    app.run(port='8080',debug=True)