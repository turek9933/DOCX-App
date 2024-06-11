#!/bin/bash

script="window_main.py"

if [ -f "$script" ]; then
    echo "Uruchamianie skryptu: $script"
    "python" "$script"
else
    echo "Plik $script nie istnieje."
    exit 1
fi
