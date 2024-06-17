#!/bin/bash

# List wymaganych bibliotek Python
required_packages=("customtkinter" "darkdetect" "docx2pdf" "chardet" "pdfkit")


check_and_install() {
    package=$1
    python -c "import $package" &> /dev/null
    if [ $? -ne 0 ]; then
        echo "Pakiet $package nie jest zainstalowany. Instalowanie..."
        pip install $package
        if [ $? -ne 0 ]; then
            echo "Nie udało się zainstalować pakietu $package."
            exit 1
        fi
    fi
}

# Sprawdzamy i installujemy każdą bibliotekę
for package in "${required_packages[@]}"; do
    check_and_install $package
done

script="window_main.py"

if [ -f "$script" ]; then
    echo "Uruchamianie skryptu: $script"
    nohup python "$script" &
else
    echo "Plik $script nie istnieje."
    exit 1
fi
