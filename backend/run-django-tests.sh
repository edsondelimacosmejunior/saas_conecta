#!/bin/bash

# Executa os testes do Django
python manage.py test

# Captura o status de saída do comando de teste
TEST_STATUS=$?

# Se os testes falharem, aborta o commit
if [ $TEST_STATUS -ne 0 ]; then
    echo "Testes falharam. Abortando o commit."
    exit 1
fi

# Se os testes passarem, permite o commit
exit 0
