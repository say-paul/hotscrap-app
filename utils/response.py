from flask import jsonify, make_response

msg = {404 : "Not Found",
    401 : "Unauthorized"}

def styler (status,body = None):
    if (status in msg.keys()):
        body = {"body" : msg[status]}
        return make_response(jsonify(body),status)
    body = {"body": body}
    return make_response(jsonify(body), status)
