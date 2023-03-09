pip3 install typer
pip3 install typing
pip3 install colorama
pip3 install prettytable
pip3 install secrets
pip3 install pyinstaller
git clone "https://github.com/UltronTheAI/productivePy.git"
pyinstaller -F ./productivePy/productivePy.py
chmod +x ./dist/productivePy
mkdir -p ~/bin/productivePy
cp ./dist/productivePy ~/bin/productivePy
echo 'export PATH="$HOME/bin/productivePy:$PATH"' >> ~/.zshrc
source ~/.zshrc
echo "Installation completed!"
