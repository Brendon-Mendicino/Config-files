"" vimrc by Brendon

set nocompatible


call plug#begin('~/.vim/plugged')

Plug 'morhetz/gruvbox'
Plug 'ycm-core/YouCompleteMe'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'preservim/nerdtree'
Plug 'tpope/vim-fugitive'  " CVS
Plug 'lervag/vimtex'

call plug#end()


" Colors
syntax on
set termguicolors
colorscheme gruvbox
set background=dark
"filetyepe indent on
filetype plugin on
hi Normal ctermbg=none
hi Terminal ctermbg=none

set encoding=utf-8


" Improve performance
"set lazydrawer

"" UI
set noerrorbells
set number
set relativenumber
set cursorline
set showcmd
set splitbelow splitright


"" Backup
set noswapfile
"set nobackup
set undodir=~/.vim/undodir
set undofile


" Highlight search patters
set hlsearch
set incsearch
set showmatch

" Tab
set cindent
set tabstop=4
set softtabstop=0
set expandtab
set shiftwidth=4
set smarttab

" No auto-comment
autocmd FileType * setlocal formatoptions-=c formatoptions-=r formatoptions-=o

" Status bar
"set laststatus=2

" Copy-paste inside vim
set clipboard=unnamed


""FINDING FILES
" Search down into subfolders
" Provides tab-completion for all file-related tasks
set path+=**
" Display all matching files when tab-complete
set wildmenu


let mapleader = " "

"" YCM
nnoremap <silent> <Leader>gd :YcmCompleter GoTo<CR>
set completeopt-=preview


"" Airline
" Buffers tab
let g:airline#extensions#tabline#enabled = 1

if !exists('g:airline_symbols')
    let g:airline_symbols = {}
endif

" powerline symbols
" to use these fonts: sudo apt install fonts-powerline
let g:airline_left_sep = ''
let g:airline_left_alt_sep = ''
let g:airline_right_sep = ''
let g:airline_right_alt_sep = ''
let g:airline_symbols.branch = ''
let g:airline_symbols.colnr = ' :'
let g:airline_symbols.readonly = ''
let g:airline_symbols.linenr = ' :'
let g:airline_symbols.maxlinenr = '☰ '
let g:airline_symbols.dirty='⚡'


"" Nerdtree
map <C-n> :NERDTreeToggle<CR>

