import requests
import json
from flask import Flask
from flask import request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

url = "https://sleeper.com/graphql"
s = requests.Session()

@app.route('/chageStarters')
def change_starters():
  username = request.args.get('username')
  password = request.args.get('pw')
  league_id = request.args.get('league')
  roster_id = request.args.get('roster_id')
  league_round = request.args.get('round')
  starters = request.args.get('starters').replace('"','\"')

  print(starters)
  print(request.args.get('starters'))

  payload_login = json.dumps({
    "operationName": "login_query",
    "variables": {
      "email_or_phone_or_username": username,
      "password": password
    },
    "query": "query login_query($email_or_phone_or_username: String!, $password: String) {\n        login(email_or_phone_or_username: $email_or_phone_or_username, password: $password){\n          token\n          avatar\n          cookies\n          created\n          display_name\n          real_name\n          email\n          notifications\n          phone\n          user_id\n          verification\n          data_updated\n        }\n      }"
  })
  headers_login = {
    'Content-Type': 'application/json'
  }

  response_login = s.request("POST", url, headers=headers_login, data=payload_login)
  response_login_json = json.loads(response_login.text)
  token = response_login_json['data']['login']['token']

  payload = json.dumps({
    "operationName": "update_matchup_leg",
    "variables": {},
    "query": "mutation update_matchup_leg($starters_games: Map) {\n        update_matchup_leg(league_id: \""+league_id+"\",roster_id: "+roster_id+",leg: 1,round: "+league_round+",starters: ["+starters+"],starters_games: $starters_games){\n          league_id\n          leg\n          matchup_id\n          roster_id\n          round\n          starters\n          players\n          player_map\n          points\n          starters_games\n          custom_points\n          proj_points\n          max_points\n        }\n      }"
  })
  headers = {
    'authorization': token,
    'Content-Type': 'application/json'
  }

  response = s.request("POST", url, headers=headers, data=payload)

  return json.loads(response.text)

app.run()