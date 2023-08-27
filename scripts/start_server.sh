echo "Collecting static files"
python3 manage.py collectstatic --noinput

echo "Starting web app"
gunicorn -c gunicorn_config.py