@echo off
title SISTEMA CANTINA FATEC 2026
mode con: cols=100 lines=30
cls
echo Aguarde... Ativando ambiente virtual e iniciando o sistema.

:: Ativa a venv (ajuste o nome se a sua pasta for diferente de 'venv')
call venv\Scripts\activate

:: Executa o programa principal
python main.py

echo.
echo O sistema foi encerrado.
pause