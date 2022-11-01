" UTF-8化
set fenc=utf-8

" バックアップファイルを作らない
set nobackup

" スワップファイルを作らない
set noswapfile

" when edit by other,it can read automatic.
set autoread

" バッファが編集中でもそのほかのファイルを開ける
set hidden

" 入力中のコマンドをステータスに表示する
set showcmd

" 行番号表示
set number

" カーソルラインの可視化
"set cursorline

" 対応する括弧の強調表示
set showmatch

" シンタックスハイライトの有効化
syntax on

" enable mouse
set mouse=a

" these make to find Capital and Small literal.
set ignorecase
"set sartcase

" インクリメントサーチ
set incsearch

" 行の折り返し
set wrapscan

" highlight search
set hlsearch

" escape hlsearch mode
nmap <Esc><Esc> :nohlsearch<CR><Esc>

" enable clipboard
set clipboard+=unnamed,unnamedplus


set autoindent
"set smartindent
set expandtab
set tabstop=4
set shiftwidth=4

" color scheme
augroup TransparentBG
"  	autocmd!
"	autocmd Colorscheme * highlight Normal ctermbg=none
"	autocmd Colorscheme * highlight NonText ctermbg=none
"	autocmd Colorscheme * highlight LineNr ctermbg=none
"	autocmd Colorscheme * highlight Folded ctermbg=none
"	autocmd Colorscheme * highlight EndOfBuffer ctermbg=none 
augroup END
color molokai
highlight lineNr ctermfg=229
hi Comment ctermfg=102
hi Visual ctermfg=255

set nocompatible
set wildmenu

set list
set listchars=tab:»-,trail:-,eol:↲,extends:»,precedes:«,nbsp:%

"key map <exe>
function! Pyfkey()
    let l:name=expand("%")
    let l:path=expand("%:p:h")
    :execute "!cd" l:path ";python" l:name
endfunction

function! Fortfkey()
    let l:name=expand("%")
    let l:path=expand("%:p:h")
    :execute "!cd" l:path ";gfortran" l:name "&& ./a.out"
endfunction

nmap <F5> :call Pyfkey() <Enter>
nmap <F6> :call Fortfkey() <Enter>
