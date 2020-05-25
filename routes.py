from flask import Flask,request,jsonify
app = Flask(__name__)

@app.route('/test')
def hello_world():
    return '<!DOCTYPE html > \
    <html > \
    <body > \
    <h1> Mockup for hotscrap test </h1> \
    <p> Authored by - sayan paul </p> \
    </body> \
    </html>'   


@app.route('/test/validatemobile')
def validate_mobile():
    num = request.args.get('phone',type = str)
    if len(num) == 10 and num.isdigit():
        return jsonify({'description':'default otp is 1234'}),200
    else:
        return jsonify({'description': 'invalid ph no'}), 401


@app.route('/test/checkotp')
def check_otp():
    otp=request.args.get('otp',type=str)
    if otp == '1234': 
        return jsonify({'description': 'authenticated'}), 200
    else:
        return jsonify({'description': 'unauthorized'}), 403
