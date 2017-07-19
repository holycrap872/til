# Setup environment

1) Drop in ./.vimrc file into `~/.vimrc`

2) Setup Pathogen to handle plugins

  - `mkdir -p ~/.vim/autoload ~/.vim/bundle`
  
  - `curl -LSso ~/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim`

3) Get Vim Sensible

  - `cd ~/.vim/bundle`

  - `git clone git://github.com/tpope/vim-sensible.git`

4) Install needed junk

  - `sudo apt-get install git tmux hexedit vim curl python-pip python-dev build-essential python3-pip libtool-bin libtool automake libboost-all-dev g++ scons subversion gcc-multilib g++-multilib clang`

5) Setup YouCompleteMe

  - `cd ~/.vim/bundle`

  - `git clone https://github.com/Valloric/YouCompleteMe.git`

  - `cd YouCompleteMe/`

  - `git submodule update --init --recursive`

  - `sudo apt-get install clang CMake python-dev mono-xbuild`

  - `./install.py --clang-completer --system-libclang --system-boost`

