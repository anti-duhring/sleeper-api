const request = new Request(
    'https://sleeper.com/graphql',
    { 
        headers: {
               'authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdmF0YXIiOiJmOWNiMDhhNjI0Mjc1YTAzNmY0NjljNmY2MWIwZDFiNCIsImRpc3BsYXlfbmFtZSI6IkJyYWR5Q29tdW5pc3RhIiwiZXhwIjoxNjgyMDM1NjE5LCJpc19ib3QiOm51bGwsImlzX21hc3RlciI6bnVsbCwicmVhbF9uYW1lIjpudWxsLCJ1c2VyX2lkIjo1NzMwMzc3Mjc3NDM2NDM2NDh9.rrqvvqTQBH1gAOLWO9qsjpgdz8qv8xEIL-zrUYqwfR4',
               'Content-Type': 'application/json' 
        },
        body: {
            "operationName": "update_matchup_leg",
            "variables": {},
            "query": "mutation update_matchup_leg($starters_games: Map) {\n        update_matchup_leg(league_id: \"858869440463376384\",roster_id: 7,leg: 1,round: 1,starters: [\"4881\",\"4199\",\"4018\",\"3321\",\"2309\",\"2251\",\"1479\",\"1339\",\"1264\",\"TEN\"],starters_games: $starters_games){\n          league_id\n          leg\n          matchup_id\n          roster_id\n          round\n          starters\n          players\n          player_map\n          points\n          starters_games\n          custom_points\n          proj_points\n          max_points\n        }\n      }"
        }
    },
  );

  fetch(request).then(response =>{
    console.log(response)
  })
  
  