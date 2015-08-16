"""
Run.py - init
"""
from app import app
app.run(host='0.0.0.0', port=61555, debug=True, threaded=True)