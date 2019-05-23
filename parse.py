from flask import Flask, jsonify, request
  
app = Flask(__name__)


@app.route('/processjson', methods=['POST'])
def processjson():
    data = request.get_json()
    #name = data['name']
    #location = data['location']
    #randomlist = data['randomlist']
    return jsonify(data)
  
if __name__ == "__main__":
    app.run(debug=True)