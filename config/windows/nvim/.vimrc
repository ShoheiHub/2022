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

" シンタックスハイライトのテーマ設定
highlight Normal ctermbg=none
highlight NonText ctermbg=none
highlight LineNr ctermbg=none
highlight Folded ctermbg=none
highlight EndOfBuffer ctermbg=none

" enable mouse
set mouse=a

" these make to find Capital and Small literal.
set ignorecase
set smartcase

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


set smartindent
" オートインデント
set tabstop=4
set autoindent
set expandtab
set shiftwidth=4

" color scheme
augroup TransparentBG
  	autocmd!
	autocmd Colorscheme * highlight Normal ctermbg=none
	autocmd Colorscheme * highlight NonText ctermbg=none
	autocmd Colorscheme * highlight LineNr ctermbg=none
	autocmd Colorscheme * highlight Folded ctermbg=none
	autocmd Colorscheme * highlight EndOfBuffer ctermbg=none 
augroup END
color molokai
hi Comment ctermfg=102
hi Visual ctermfg=255

set nocompatible
set wildmenu

"テキスト
"highlight Normal ctermbg=none
"テキスト下の余白
"highlight NonText ctermbg=none
"行番号
"highlight LineNr ctermbg=none
"コマンドの折りたたみ
"highlight Folded ctermbg=none
"ファイルの終わり以降の空白
"highlight EndOfBuffer ctermbg=none
"
set list
set listchars=tab:»-,trail:-,eol:↲,extends:»,precedes:«,nbsp:%
