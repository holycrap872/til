# Setup environment

1) Drop in ./.vimrc file into `~/.vimrc`

2) Setup Pathogen to handle plugins

  - `mkdir -p ~/.vim/autoload ~/.vim/bundle`
  
  - `curl -LSso ~/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim`

3) Get Vim Sensible

  - `cd ~/.vim/bundle`

  - `git clone git://github.com/tpope/vim-sensible.git`

4) Setup YouCompleteMe

  - `cd ~/.vim/bundle`

  - `git clone https://github.com/Valloric/YouCompleteMe.git`

  - `cd YouCompleteMe/`

  - `git submodule update --init --recursive`

  - `sudo apt-get install clang CMake python-dev mono-xbuild`

  - `./install.sh --clang-completer --omnisharp-completer`

  - `cp ~/workspace/klee/.ycm_extra_conf.py ~/.vim`

