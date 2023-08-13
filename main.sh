#! /bin/bash

chmod +x main.py

if ./main.py; then
    echo "Log file analysed successfully"
else
    echo "An error occured"
fi

