# Setup enviroment

1) Drop in .vimrc file into `~/.vimrc`

2) mkdir -p ~/.vim/autoload ~/.vim/bundle && curl -LSso ~/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim

3) cd ~/.vim/bundle

4) git clone https://github.com/Valloric/YouCompleteMe.git 
ls
cd YouCompleteMe/
git submodule update --init --recursive

sudo apt-get install clang CMake python-dev mono-xbuild
./install.sh --clang-completer  --omnisharp-completer
cp ~/workspace/klee/.ycm_extra_conf.py ~/.vim
