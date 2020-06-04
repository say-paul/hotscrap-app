from flask import jsonify, make_response

msg = {401 : "Unauthorized",
    203 : "Request Successful",
    400 : "Bad Request",
    404 : "Not Found"}

def styler (status,body = None):
    if (status in msg.keys()):
        body = {"body": msg[status]}
        return make_response(jsonify(body),status)
    body = {"body": body}
    return make_response(jsonify(body), status)
