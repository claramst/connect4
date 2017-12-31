#!flask/bin/python

from app import app
from socket import gethostname

if gethostname().find('astoddart') != -1:
    app.run(debug=True)
else:
    app.run(host='0.0.0.0', debug=False)