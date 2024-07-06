import pyexcel
from flask import Flask, request

app = Flask(__name__)

@app.get("/convert")
def format_convert():
    from_file = request.args.get('from', '')
    to_file = request.args.get('to', '')
    pyexcel.save_as(file_name=from_file, dest_file_name=to_file)
    return "ok"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)
