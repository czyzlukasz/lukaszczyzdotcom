echo "Migrating database"
python3 manage.py makemigrations logbook landing_page &&
python3 manage.py migrate
python3 manage.py collectstatic --noinput

echo "Starting web app"
gunicorn -c gunicorn_config.py