# Objetivo
Extrair as tabelas 30, 31 e 32 do pdf da Tarefa 1, salvar seus dados em arquivos .csv e zipar todos os arquivos csv.
 
# Como executar
 O algoritmo utiliza as dependências pathlib, tabula e e zipfile. Para instalar, execute
 
 ```
 pip install pathlib
 pip install tabula-py
 pip install zipfile
 ```
Então execute o comando 
 ```
 python dataextraction.py
 ```
 O algoritmo lerá o arquivo padrao-tiss_componente-organizacional_202111.pdf presente no diretório da tarefa 1 e irá extrair os arquivos csv.
 Em seguida, incluirá todos eles num único zip, com o nome assim como solicitado.
 Os arquivos gerados também foram upados neste repositório, caso seja necessário.
