def paginacao(self, pagina=0, estados="", chaves=""):
    url = f'''{self.url}?data_insercao={self.ultimo_dia_util}&uf={estados}
    &palavra_chave={chaves}
    &pagina={pagina}'''

    payload = {}
    headers = {
        "Token": self.token,
        "Content-Type": "application/json",
    }

    response = requests.request("GET", url, json=payload, headers=headers)

    dados = response.text
    conteudo = json.loads(dados)

    # print("Conteúdo: ")
    # print(conteudo)

    total_licitacoes = conteudo['totalLicitacoes']
    print("Quantidade de licitações: ", total_licitacoes)

    paginas = conteudo['paginas']
    print("Quantidade de páginas: ", paginas)

    print("Data Limite: ", self.data_prazo)
    dados = conteudo['licitacoes']
    return dados, paginas