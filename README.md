# Flask-web-app
services:
  - type: web
    name: flask-web-app
    runtime: python
    buildCommand: ""
    startCommand: "python app.py"
    envVars:
      - key: FLASK_ENV
        value: production
