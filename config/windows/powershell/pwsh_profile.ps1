# Alias
Set-Alias vim nvim
Set-Alias vi nvim
Set-Alias grep findstr

Set-Alias ll Get-ChildItem
Set-Alias l myls
#Set-Alias ls lsltr
Set-Alias ls ll


Set-Alias python python.exe
Set-Alias gfortran gfortran.exe

# user experience
# bash-like TAB
Set-PSReadLineKeyHandler -Key Tab -Function Complete

# 履歴ベースの予測を有効化
Set-PSReadLineOption -PredictionSource History

# exit key map of Ctrl + D
Set-PSReadlineKeyHandler -Key ctrl+d -Function DeleteCharOrExit

# cancel beep sound
Set-PSReadlineOption -BellStyle None

# fuction
# ls color
filter lsColor{
    if($_.mode[0] -eq "d"){
        Write-Host $_.name -ForeGroundColor Green
    }
    elseif($_.get_Extension() -eq ".exe"){
        Write-Host $_.name -ForeGroundColor Yellow
    }
    else{
        Write-Host $_.name
    }
}
function myls{
    $c = "Get-ChildItem " + $args
    Invoke-Expression $c | lsColor
}

function lsltr{
    ls | Sort-object LastWriteTime
}

$env:DISPLAY="localhost:0.0"
