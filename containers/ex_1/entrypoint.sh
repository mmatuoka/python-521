
echo "Inciando serviço do Apache ...";
service apache2 start

echo 'Container iniciado com sucesso ...'
service apache2 status
tail -f /dev/null