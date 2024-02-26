#!/bin/bash
venv/Scripts/activate

pip install -r requeriments.txt

export FLASK_APP=main.py
export FLASK_DEBUG=1
export FLASK_ENV=development

flask run