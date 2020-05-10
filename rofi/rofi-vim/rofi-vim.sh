#!/bin/bash

vim_run()
{
  command=$1
  [[ $2 = "" ]] && time=.150 || time=$2
  sleep $time
  xdotool type $command
  sleep $time
  xdotool key Return
}

list()
{
  echo "fzf_files Pesquisar arquivos na pasta local"
  echo "fzf_buffers Listar arquivos abertos"
  echo "fzf_search_in_files Busca palavras dentro do arquivos"
  echo "vim_help Abre a ajuda do vim em nova aba"
}

fzf_files()
{
  vim_run ":Files"
}

fzf_buffers()
{
  vim_run ":Buffers"
}

fzf_search_in_files()
{
  vim_run ":Rg"
}

vim_help()
{
  vim_run ":tabnew | help | only"
}

handler()
{
  function_name=$(echo $@ | cut -d " " -f1)
  #echo $function_name
  case $function_name in
    vim_help) vim_help;;
    fzf_buffers) fzf_buffers;;
    fzf_files) fzf_files;;
    fzf_search_in_files) fzf_search_in_files;;
  esac
}

main()
{
  user_choice=$(list | rofi -dmenu -i -p "Vim" -matching regex)
  handler $user_choice  
}

main
