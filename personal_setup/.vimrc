"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => General
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
set history=700
set whichwrap=h,l
syntax on
filetype indent plugin on

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

