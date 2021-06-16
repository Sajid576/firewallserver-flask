
from flask import *
from NoSql.feature_extractor import NoSqlFeatureExtractor
from NoSql.nosql_injection_classifier import NoSqlInjection
from Sql.feature_extractor import  SqlFeatureExtractor
from Sql.sql_injection_classifier import  SqlInjection

app = Flask(__name__)

@app.route("/",methods=['GET'])
def projectRoot():
  return "<h1>Welcome to the SQL/NoSQL Injection Detection Machine Learning Model API</h1>"

@app.route("/sql_injection",methods=['POST'])
def detectSqlInjection():
    SqlFeatureExtractor(request.get_json() )
    SqlInjection().predict()
    res={
              'message':"SQL injection prediction successfully performed",
              'error':'NULL',
              'body':{
                'result':'true'
              }
            }
    return res


@app.route("/nosql_injection",methods=['POST'])
def detectNoSqlInjection():
    NoSqlFeatureExtractor(request.get_json() )
    NoSqlInjection().predict()
    res={
        'message':"NoSQL injection prediction successfully performed",
        'error':'NULL',
        'body':{
          'result':'true'
        }
      }
    return res

if __name__ == "__main__":
    app.run(port='8080',debug=True)