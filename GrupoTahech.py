import requests
import pandas as pd
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Tahech:
    def __init__(self):
        self.url_inicial = "https://acordaos.economia.gov.br/solr/acordaos2_shard11_replica_n60/browse?q=covid"
        self.formato_json = "&wt=json"
        self.paginas = 0
        self.dicionario = []

    def acesse_o_site(self):
        res = requests.get(f"{self.url_inicial}{self.formato_json}", verify=False)
        inicial_json = res.json()
        if res.status_code == 200:
            numero_pagina = int(inicial_json['response']['numFound'])
            for i in range(0, numero_pagina, 10):
                url = f"{self.url_inicial}{self.formato_json}&start={i}"
                resposta = requests.get(url, verify=False)
                resposta_json = resposta.json()
                teste = resposta_json['response']['docs']
                for t in teste:
                    check_ano = "ano_sessao_s" in t.keys()
                    check_texto = "conteudo_txt" in t.keys()
                    check_id = "id" in t.keys()
                    if check_ano and check_texto and check_id:
                        ano = t["ano_sessao_s"]
                        texto = t["conteudo_txt"]
                        id_site = t["id"]
                        data = {
                            "id_site": id_site,
                            "ano": ano,
                            "texto": texto
                        }
                        self.dicionario.append(data)
                    else:
                        ano = 0
                        id_site = 0
                        texto = 'vazio'
                print("Página", i)
            df = pd.DataFrame(self.dicionario)
            df.to_excel("planilha.xlsx")
            df_corona = df[df.ano == '2021']
            df_corona = df_corona[df_corona.texto.str.contains("coronavírus")]
            df_corona.to_excel("planilha corona.xlsx")

            return df_corona

        else:
            print("API Momentaneamente Indisponível, tente mais tarde por favor")


if __name__ == "__main__":
    run = Tahech()
    df_corona = run.acesse_o_site()

    print(f"\nExistem {len(list(df_corona.id_site))} registros contendo a palavra coronavírus!!!")


