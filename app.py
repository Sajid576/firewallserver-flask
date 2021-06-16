from flask import *
app = Flask(__name__)

@app.route("/",methods=['GET'])
def projectRoot():
  return "Root project"

@app.route("/sql_injection",methods=['POST'])
def detectSqlInjection():
  return "SQL"


@app.route("/nosql_injection",methods=['POST'])
def detectNoSqlInjection():
  return "NoSQL"

if __name__ == "__main__":
    app.run(port='8080',debug=True)