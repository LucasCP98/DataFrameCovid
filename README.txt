1. Acesse o site: https://acordaos.economia.gov.br/solr/acordaos2/browse/
2. Pesquise por covid
3. Altere a visualização da página para o formato json
4. Percorra todos os resultados de todas as páginas
5. Percorra o json, capturando de cada documento o id, ano_sessao_s e conteudo_txt
6. Construa um dataframe que armazene os dados coletados no item 5 para todos os documentos
7. Após a montagem do dataframe, identifique todos os registros que possuem o
ano_sessao_s igual a 2021 e que possuem a palavra coronavirus nos registros
8. Em seguida crie um novo dataframe apenas com os resultados do item 7 e o coloque
como retorno da função
