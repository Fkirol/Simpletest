#!/usr/bin/env bash
# Exit on error
set -o errexit
pip install --upgrade pip setuptools wheel 
pip install "pyyaml==5.4.1" --no-build-isolation
pip install "cython<3.0.0" wheel 

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt


python manage.py collectstatic --no-input


python manage.py migrate

python database_inizializer.py