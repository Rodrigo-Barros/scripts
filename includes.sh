#!/bin/bash

root=/var/www/html
#provider="http://177.234.151.251/~"
function PrintUsage(){
  echo "
  -g Altera para https

  -h imprime essa lista de comandos

  -l verifica a existencia dos seguintes arquivos: artigo.php, artigo.js categoria.php  categorias.js. 
     e se não existirem o script os cria.

  -m verifica a existencia dos seguintes arquivos: artigo.php, artigo.js, categorias.php, categorias.js,
     produtos.php, produtos.js.

  -f verifica a existencia dos seguintes arquivos: artigo.php, artigo.js, categorias.php, categorias.js,
     produtos.php, produtos.js, produto.php, produto.js.

  -a nome da pasta a ser criada no diretório /var/www/html/nomepasta

  -s nome do site exemplo 177.234.151.251/~nomesite, aqui o script irá tratar nos arquivo de scripts para 
     fazer a inclusão dos scripts automaticamente

  Dica Útil:

  Você irá desenvolver um site em HTTP ou HTTPS? Caso Seja em HTTPS Especifique a opção -g na linha de comandos

  Script para automatizar o desenvolvimento de sites feito por: Rodrigo Gabrie, 2018 Todos os direitos Reservados
  "
  exit 0
}
while getopts ghlmfp:s: OPCAO; do
  case "${OPCAO}" in
    s) site=${OPTARG};;
    h) PrintUsage ;;
    p) p="${OPTARG}";;   
    l) l=1;;#low
    m) m=1;;#medium
    f) f=1;;#full
    g) g=1;;#change to https
  esac
done

shift $((OPTIND-1))

if [ "$g" == 1 ];then
  provider="https://177.234.151.251/~"
else
  provider="http://177.234.151.251/~"
fi

projectPath=$root/$p

#---------------- print help--------------------------
if [ -z "$site" ] && [ -z "$p" ] && [ -z "$l" ] && [ -z "$m" ] && [ -z "$f" ]; then
   PrintUsage
fi
#make Path
if [ "$site" ] && [ "$p" ];then
projectPath=$root/$p
find $projectPath/$p/includes 2> /dev/null
if [[ $? -ne 0 ]];then
  mkdir  $projectPath/includes -p
  echo "" > $projectPath/includes/head.php
  echo "" > $projectPath/includes/header.php
  echo "
  <script src=\"$provider${site}/goupsistema/assets/js/consumers.js\"></script>
  <script src=\"$provider${site}/goupsistema/assets/js/application.js\"></script>
" > $projectPath/includes/footer.php
fi
  find $projectPath/goupsistema/assets/js 2> /dev/null
  if [[ $? -ne 0 ]];then
    mkdir $projectPath/goupsistema/assets/js -p
    #verifica se consumers.js e application.js estão criados senão estiverem os cria
    find $projectPath/goupsistema/assets/js/consumers.js
    if [[ $? -ne 0 ]];then
      echo "" > $projectPath/goupsistema/assets/js/consumers.js
    fi

    find $projectPath/goupsistema/assets/js/application.js
    if [[ $? -ne 0 ]];then
      echo "" > $projectPath/goupsistema/assets/js/application.js
    fi
  fi
else
  echo "é necessário fornecer o nome do site para prosseguir"
  exit 1
fi

#low
if [ "$l" == 1 ];then

  find $projectPath/artigo.php 2> /dev/null
  if [[ $? -ne 0 ]]; then
    echo "
  <?php include(\"includes/head.php\") ?>
  <?php include(\"includes/header.php\") ?>
  <?php include(\"includes/footer.php\") ?>
  <script src=\"$provider${site}/goupsistema/assets/js/artigo.js\"></script>
" > $projectPath/artigo.php
  fi

  find $projectPath/categorias.php 2> /dev/null
  if [[ $? -ne 0 ]];then
    echo "
  <?php include(\"includes/head.php\") ?>
  <?php include(\"includes/header.php\") ?>
  <?php include(\"includes/footer.php\") ?>
  <script src=\"$provider${site}/goupsistema/assets/js/categoria.js\"></script>
  " > $projectPath/categoria.php
  fi

  find $projectPath/goupsistema/assets/js/artigo.js
  if [[ $? -ne 0 ]]; then
    echo "artigo.js" > $projectPath/goupsistema/assets/js/artigo.js
  fi

  find $projectPath/goupsistema/assets/js/categoria.js
  if [[ $? -ne 0 ]];then
      echo "categoria.js" > $projectPath/goupsistema/assets/js/categoria.js
  fi
fi

#medium
if [[ "$m" == 1 ]]; then
  find $projectPath/artigo.php
  if [[ $? -ne 0 ]]; then
    echo "
    <?php include(\"includes/head.php\") ?>
    <?php include(\"includes/header.php\") ?>
    <?php include(\"includes/footer.php\") ?>
    <script src=\"$provider${site}/goupsistema/assets/js/artigo.js\"></script>
    " > $projectPath/artigo.php
  fi

  find $projectPath/goupsistema/assets/js/artigo.js
  if [[ $? -ne 0 ]]; then
    echo "" > $projectPath/goupsistema/assets/js/artigo.js
  fi

  find $projectPath/categoria.php
  if [[ $? -ne 0 ]]; then
    echo "
  <?php include(\"includes/head.php\") ?>
  <?php include(\"includes/header.php\") ?>
  <?php include(\"includes/footer.php\") ?>
  <script src=\"$provider${site}/goupsistema/assets/js/categoria.js\"></script>
    " > $projectPath/categoria.php
  fi

  find $projectPath/goupsistema/assets/js/categoria.js
  if [[ $? -ne 0 ]]; then
    echo "" > $projectPath/goupsistema/assets/js/categoria.js
  fi

  find $projectPath/produtos.php
  if [[ $? -ne 0 ]]; then
  echo "
    <?php include(\"includes/head.php\") ?>
    <?php include(\"includes/header.php\") ?>
    <?php include(\"includes/footer.php\") ?>
    <script src=\"$provider${site}/goupsistema/assets/js/produtos.js\"></script> 
  " > $projectPath/produtos.php
  fi

  find $projectPath/goupsistema/assets/js/produtos.js
  if [[ $? -ne 0 ]]; then
    echo "" > $projectPath/goupsistema/assets/js/produtos.js
  fi
fi

#full
if [[ "$f" == 1 ]]; then
  find $projectPath/artigo.php
  if [[ $? -ne 0 ]]; then
    echo "
    <?php include(\"includes/head.php\") ?>
    <?php include(\"includes/header.php\") ?>
    <?php include(\"includes/footer.php\") ?>
    <script src=\"$provider${site}/goupsistema/assets/js/artigo.js\"></script>
    " > $projectPath/artigo.php
  fi

  find $projectPath/goupsistema/assets/js/artigo.js
  if [[ $? -ne 0 ]]; then
    echo "" > $projectPath/goupsistema/assets/js/artigo.js
  fi

  find $projectPath/categoria.php
  if [[ $? -ne 0 ]]; then
    echo "
  <?php include(\"includes/head.php\") ?>
  <?php include(\"includes/header.php\") ?>
  <?php include(\"includes/footer.php\") ?>
  <script src=\"$provider${site}/goupsistema/assets/js/categoria.js\"></script>
    " > $projectPath/categoria.php
  fi

  find $projectPath/goupsistema/assets/js/categoria.js
  if [[ $? -ne 0 ]]; then
    echo "" > $projectPath/goupsistema/assets/js/categoria.js
  fi

  find $projectPath/produtos.php
  if [[ $? -ne 0 ]]; then
  echo "
    <?php include(\"includes/head.php\") ?>
    <?php include(\"includes/header.php\") ?>
    <?php include(\"includes/footer.php\") ?>
    <script src=\"$provider${site}/goupsistema/assets/js/produtos.js\"></script> 
  " > $projectPath/produtos.php
  fi

  find $projectPath/goupsistema/assets/js/produtos.js
  if [[ $? -ne 0 ]]; then
    echo "" > $projectPath/goupsistema/assets/js/produtos.js
  fi  

  find $projectPath/produto.php
  if [[ $? -ne 0 ]]; then
    echo "
    <?php include(\"includes/head.php\") ?>
    <?php include(\"includes/header.php\") ?>
    <?php include(\"includes/footer.php\") ?>
    <script src=\"$provider${site}/goupsistema/assets/js/produto.js\"></script> 
    " > $projectPath/produto.php
  fi

  find $projectPath/goupsistema/assets/js/produto.js
  if [[ $? -ne 0 ]]; then
    echo "" > $projectPath/goupsistema/assets/js/produto.js
  fi
fi
exit 0
#----------------------end script -----------------------------------------------------
