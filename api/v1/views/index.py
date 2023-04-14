#!/usr/bin/python3 
"""comments"""

from flask import jsonify
from models import storage
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'])
def status():
    """comments"""
    return jsonify({'status': 'OK'})


@app_views.route('/api/v1/stats', methods=['GET'], strict_slashes=False)
def count_objects():
    """comments"""
    classes = ["Amenity", "City", "Place", "Review", "State", "User"]
    counts = {cls: storage.count(cls) for cls in classes}
    return jsonify(counts)
