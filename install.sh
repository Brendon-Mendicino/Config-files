#!/bin/sh

cp ./.vimrc ~/.vimrc

[ ! -d ~/.config ] && mkdir ~/.config ; mkdir ~/.config/fish
[ ! -d ~/.config/fish ] && mkdir ~/.config/fish
cp ./.config/fish/config.fish ~/.config/fish/config.fish

[ ! -d ~/latex ] && mkdir ~/latex
cp ./latex/notestyle.sty ~/latex/notestyle.sty


# Install Vim package-manager
curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim

# Istall YCM
apt install build-essential cmake vim-nox python3-dev
apt install mono-complete golang nodejs default-jdk npm
python3 ~/.vim/plugged/YouCompleteMe/install.py --all

apt install fonts-dejavu
apt install fonts-powerline

# Install fish and omf
apt install fish
curl https://raw.githubusercontent.com/oh-my-fish/oh-my-fish/master/bin/install | fish
omf install bobthefish
