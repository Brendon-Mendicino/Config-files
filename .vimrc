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


filetype plugin indent on

" Colors
syntax enable
set termguicolors
colorscheme gruvbox
set background=dark
"filetyepe indent on
filetype plugin on
hi Normal ctermbg=none
hi Terminal ctermbg=none

set encoding=utf8


" Improve performance
"set lazydrawer

"" UI
set noerrorbells
set belloff=all
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

let g:ycm_complete_in_comments_and_strings=1
let g:ycm_key_list_select_completion=['<C-n>', '<Down>']
let g:ycm_key_list_previous_completion=['<C-p>', '<Up>']
let g:ycm_autoclose_preview_window_after_completion = 1

"This assumes your kernel directory has the word 'kernel'
if getcwd() =~ "kernel"
    let g:ycm_global_ycm_extra_conf='~/ycm_extra_conf_kernel.py'
else
    let g:ycm_global_ycm_extra_conf='~/ycm_extra_conf.py'
endif



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


"" VimTex
" for text concealing ~> replaces expressions with unicode symbols
set conceallevel=2
