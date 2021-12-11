
import pandas as pd
import string
import json

sheet_url = 'https://docs.google.com/spreadsheets/d/1il54YsQNfGxLOeMvG94PyymbKZ-JeddP/edit#gid=1921110563'
csv_export_url = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
pl_nosql = pd.read_csv(csv_export_url, header=None)
payload_nosql = pl_nosql.values.tolist()

sheet_url = 'https://docs.google.com/spreadsheets/d/1DudjjdnNl8A4O2bD5zD-uPnT6Ow-XQ_0/edit#gid=1846316042'
csv_export_url = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
pl_sql = pd.read_csv(csv_export_url, header=None)
payload_sql = pl_sql.values.tolist()

for i in range(len(payload_sql)):
  payload_sql[i][0] = payload_sql[i][0].translate(
      {ord(c): None for c in string.whitespace})

for i in range(len(payload_nosql)):
  payload_nosql[i][0] = payload_nosql[i][0].translate(
      {ord(c): None for c in string.whitespace})


def detect_malicious_sql(input):

  userInput = ''
  for i in input.values():
    userInput = userInput + \
        str(i).translate({ord(c): None for c in string.whitespace})

  #print(payload_sql)

  second_layer_check = True
  for i in payload_sql:

    if i[0] in userInput:
      second_layer_check = False

  return second_layer_check


def detect_malicious_nosql(input):

  userInput = ''
  for i in input.values():
    userInput = userInput + \
        str(i).translate({ord(c): None for c in string.whitespace})

  second_layer_check = True
  for i in payload_nosql:
    if i[0] in userInput:
      second_layer_check = False
  return second_layer_check
