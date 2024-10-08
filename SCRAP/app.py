from flask import Flask, request
import pandas as pd
import json

app = Flask(__name__)

@app.route('/')
def index():
  return 'Hello...'


@app.route('/wine/list.json') #테스트:http://192.168.0.98:5000/wine/list.json?page=1
def wine():
  args = request.args
  page = int(args.get('page'))
  start = (page-1) * 10
  end = page * 10

  df = pd.read_csv('data/WineInfo_Red_detail.csv')
  df['rating'] = 3.4
  total = len(df)

  df = df[start:end]
  list = df.to_json(orient='records')
  list = json.loads(list)

  data = {'total':total, 'list':list}
  return data


if __name__ == '__main__':
  app.run(port=5000, debug=True, host='192.168.0.98')