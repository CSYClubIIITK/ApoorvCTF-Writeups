echo "127.0.0.1 get-price.internal" >> /etc/hosts
python3 -m gunicorn --workers=3 app:app --bind=0.0.0.0:5001 --daemon
python3 -m gunicorn --workder=3 price_app:app --bind=127.0.0.1:5000 --daemon
python3 -m gunicorn --workers=3 admin_app:app --bind=127.0.0.1:5002
