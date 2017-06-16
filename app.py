import os
from flask import Flask

app = Flask(__name__)

respondents = {}

respondents['jon.doe@abc.com'] = '{"firstname": "Jon", "surname": "Doe", "telephone": "+441678673864", "status": "ACTIVE"}'
respondents['jane.doe@abc.com'] = '{"firstname": "Jane", "surname": "Doe", "telephone": "+441678673864", "status": "ACTIVE"}'

ids = {}
ids['a34b'] = '{"firstname": "Jon", "surname": "Doe", "email": "jon.doe@abc.com", "telephone": "+441678673864", "status": "ACTIVE"}'
ids['a23b'] = '{"firstname": "Jane", "surname": "Doe", "email": "jane.doe@abc.com", "telephone": "+441678673864", "status": "ACTIVE"}'

headers = {'Content-Type': 'application/json',
           'Authorization': 'eyJhbGciOiJSU0EtT0FFUCIsImVuYyI6IkEyNTZHQ00ifQ.GXOO8DQItBlk9hO2Lve2G7vjD1AoEdmzrJVn6_woPhPGddNk9dtfUgbHDuCVoQrteTC8ux1zbKnn0VSCSaSIEF8kM-8WQirDTxWtm8F5i339dJk7eM3Bk6-BxQgMcgrSUrGDwjPuQBYaHEvRGPZccB4576JXX4zhBjaqKDYzD_57St5bC1Ve7k_N-97W3w2VqT33OtQdwS6qeDqXFc6DHCgJsvLMFztmJ1BTWzab9PejmWhLup5uBb9s0XWRyx12KcNXJtNuFxFM2z4FMJ2sWPeNqLbgcg8ECfJ0IrO-Cy4JuitphnWegaujpcFnuoZl-FQvHszZF6uoGsjOQUII5w.ll-4VbmGRJL-ROgi.41hFWh6SLlp-y6ZrquxSeNkABGQp_4E6Y5gVkTogTNMbXkDJ2Dd3PRcsp_heGTzD6DEygIW_fAqR4ekfpuLYb4oj5Iax5fUYJfhp1b-FyKIqOExuQoaDCWaisDrIglfLQQYtSsXF49mvRVapIzD9YtSW4FyEJVwYsS6YVykezkk._xidxqOPvdqGocscjyi2wQ'}


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/respondent/email/<email>", methods=['GET'])
def get_email(email):
    details = respondents[email]
    return details


@app.route("/respondent/id/<id>", methods=['GET'])
def get_id(id):
    details = ids[id]
    return details


PORT = int(os.environ.get('PORT', 5004))
app.run(host='0.0.0.0', port=PORT, debug=True)
