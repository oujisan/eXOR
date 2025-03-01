#!/bin/bash
chmod +x ./exor.py
sudo cp exor.py /usr/local/bin/exor
sudo sed -i 's/\r$//' "/usr//local/bin/exor"
echo "eXOR has been successfully installed! You can run it using: exor"
