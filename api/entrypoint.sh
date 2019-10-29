
echo "Iniciando serviço do mongodb ..."
service mongodb start

echo "Iniciando aplicação ..."
python3 /app/app.py
