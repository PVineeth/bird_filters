from flask import Flask
from waitress import serve

#proto_obj = prt.protocols(prt.Types.BGP, prt.Format.BIRD_1_x)

app = Flask(__name__)

@app.route('/')
def hello_world():
    #return proto_obj.list_protocol()
    pass

if __name__ == '__main__':
    serve(app, host="127.0.0.1", port=8080)