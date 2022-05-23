import requests
import pandas as pd
from dataf import datafra
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

'''Proposta de teste
1. Acesse o site: https://acordaos.economia.gov.br/solr/acordaos2/browse/ --> FEITO!
2. Pesquise por covid --> FEITO!
3. Altere a visualização da página para o formato json --> FEITO!
4. Percorra todos os resultados de todas as páginas --> ##########
5. Percorra o json, capturando de cada documento o id, ano_sessao_s e conteudo_txt
6. Construa um dataframe que armazene os dados coletados no item 5 para todos os
documentos
7. Após a montagem do dataframe, identifique todos os registros que possuem o
ano_sessao_s igual a 2021 e que possuem a palavra coronavirus nos registros
8. Em seguida crie um novo dataframe apenas com os resultados do item 7 e o coloque
como retorno da função
'''


class Tahech:

    def __init__(self):

        self.url_inicial = "https://acordaos.economia.gov.br/solr/acordaos2_shard11_replica_n60/browse?q=covid"
        self.formato_json = "&wt=json"
        self.paginas = 0

    def acesse_o_site(self):
        global ano, id_site, texto
        res = requests.get(f"{self.url_inicial}{self.formato_json}", verify=False)
        inicial_json = res.json()
        if res.status_code == 200:

            numero_pagina = int(inicial_json['response']['numFound'])

            for i in range(0, numero_pagina, 10):
                url = f"{self.url_inicial}{self.formato_json}&start={i}"
                resposta = requests.get(url, verify=False)
                resposta_json = resposta.json()
                teste = resposta_json['response']['docs']
                anos = []
                ids = []
                textos = []
                for t in teste:
                    check_ano = "ano_sessao_s" in t.keys()

                    check_texto = "decisao_txt" in t.keys()

                    check_id = "id" in t.keys()

                    if check_ano and check_texto and check_id:
                        ano = t["ano_sessao_s"]
                        texto = t["decisao_txt"]
                        id_site = t["id"]

                    else:
                        ano = 0
                        id_site = 0
                        texto = 'vazio'

                    anos.append(ano)
                    ids.append(id_site)
                    textos.append(texto)

                # dataframe
                resultados = datafra()
                resultados.frame(ano, id_site, texto)

        else:
            print("API Momentaneamente Indisponível, tente mais tarde por favor")


if __name__ == "__main__":
    run = Tahech()
    run.acesse_o_site()

