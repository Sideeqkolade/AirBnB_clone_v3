#!/usr/bin/python3
"""
import app_views from api.v1.views
create a route /status on the object app_views that returns
a JSON: "status": "OK" (see example)
"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'])
def status():
    """status of API"""
    return jsonify({"status": "OK"})