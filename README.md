#Web2py Boilerplate UNIRIO

Applicação *Web2py* pronta para ser usada como base para futuros projetos.

### Como usar

1. Clone o repositorio, lembrando de usar o parametro `--recursive`.
2. Crie uma pasta `private/` e copie o arquivo `appconfig.example.ini` para ela, renomeando o arquivo para `appconfig.ini`.
3. Dentro da pasta web2py_common, execute o script para criar os links simbolicos nas pastas `static` e `views`
  - `symlinks.bat` para Windows
  - `symlinks.sh` para Linux/Mac
4. (Opcional) Edite o arquivo `appconfig.ini` (dentro da pasta `private`) de acordo com as configurações do projeto (BD, email, etc)

#### Colocando no GIT

1. Remova os arquivos de repositorio atuais.
  - Apage a pasta .git
  - Ou use `git checkout-index -a -f --prefix=/caminho/destino/`. No diretorio `/caminho/destino/` vai ter o projeto sem os arquivos de git.
  - Ou use `git archive --format zip --output /caminho/destino/arquivo.zip master`. No arquivo `/caminho/destino/arquivo.zip master` vai ter o projeto (compactado) sem os arquivos de git.
2. Inicie um repositorio git na pasta do projeto.
  - `git init`
3. Adicione os arquivos do projeto
  - `git add .`
4. (Opcional) Adicione o repositorio remoto e envie.
  - `git remote add origin endereco_do_repositorio` para adicionar o remoto
  - `git push origin master` para enviar para o remoto
  
#### Observações
* Evite colocar o arquivo `private/appconfig.ini` no versionamento se ele conter senhas ou chaves.
  