"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => General
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
set history=700

"How to handle tabbing
filetype plugin indent on
set expandtab
set tabstop=4
set shiftwidth=4
set softtabstop=4

"GT's internal design doc's limit columns to 80
set colorcolumn=80
highlight ColorColumn ctermbg=darkgray

"Force vim to look for .vimrc in current directory (enables
"project specific files)
set exrc
"exrc opens up a potential security threat so secure limits
"which options can be set in the not root .vimrc file
set secure

"Highlight trailing spaces
"highlight ExtraWhitespace ctermbg=red guibg=red
"match ExtraWhitespace /\s\+$/

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => Plugin manager
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"Now any plugins you wish to install can be extracted to a sub
"directory under ~/.vim/bundle, and they will be added to the
"'runtimepath'.
"For example...
" - cd ~/.vim/bundle && \
" - git clone git://github.com/tpope/vim-sensible.git

execute pathogen#infect()
syntax on
filetype plugin indent on



"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => YouCompleteMe
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"
let g:ycm_global_ycm_extra_conf = "~/.vim/.ycm_extra_conf.py"
