@echo off

:: List wymaganych bibliotek Python
set required_packages=customtkinter darkdetect docx2pdf chardet pdfkit


:: Sprawdzamy i instalujemy każdą bibliotekę
for %%p in (%required_packages%) do (
    call:check_and_install %%p
)

:: Pominiecie funcji, aby nie wywoływać jej bez argumentów
goto :after_check

:: Funkcja do sprawdzania i instalowania bibliotek Python
:check_and_install
python -c "import %1" 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo Pakiet %1 nie jest zainstalowany. Instalowanie...
    pip install %1
)
exit /b 0

:after_check

:: Nazwa skryptu do uruchomienia
set script=window_main.py

:: Sprawdzenie istnienia skryptu i uruchomienie go
if exist "%script%" (
    echo Uruchamianie skryptu: %script%
    start "" pythonw "%script%"
) else (
    echo Plik %script% nie istnieje.
    exit /b 1
)