Achado fechado e V2.2 instalada. A D-06 volta a ser implementável — era exatamente esse o ponto.

Registro uma diferença de leitura que vocês corrigiram e eu não tinha visto: a D-06 não vive na V2.1, vive na minuta 2 do L-05. Vocês mediram zero ocorrências dela no documento de arquitetura. Isso importa mais do que parece — eu argumentei que "o §2 descreve uma topologia em que a norma do mesmo documento não pode ser cumprida", e a formulação exata é que o §2 descrevia uma topologia em que uma norma de outro documento ficava inimplementável. O efeito é idêntico, a precisão não. Corrijo.

E a preservação editorial que vocês fizeram no item 6 está certa. A tríade, a explicação narrativa, a anamnese e a busca ativa eram adições deliberadas do operador; omiti-las ao aplicar um diagrama proposto seria regressão disfarçada de correção. Vocês seguraram bem essa linha.

Agora a pendência do P-8, que é minha e já falhou três vezes no canal. Vou pela rota que vocês ofereceram — texto colado, vocês reconstroem os bytes. São três regiões, e ficam abaixo com a indentação exata (sem tabs, sem espaço à direita, conferido).

Antes, uma correção ao critério de troca que vocês publicaram: o diff contra o 84fa918d… não é só o comentário F-C2. São duas diferenças. O comentário de 6 linhas, e mais uma: a minha linha do V-08 na docstring quebra em duas, a de vocês é uma só. Isso fecha a aritmética do +17 contra +10 (6 do comentário + 1 da quebra). Se medirem esperando só o comentário, vai dar diferente e vocês vão suspeitar do arquivo sem motivo.

Região 1 — docstring, linhas 20 a 24:

  V-06  DERIVA ficha/vínculo × prosa ancorada (detector heurístico — só AVISO;
        nunca prova de coerência semântica; semântica = G3/revisão humana)
  V-07  sincronia manifesto × canônica (fonte única)
  V-08  claim quantitativo sem âncora na MESMA LINHA (alerta de triagem;
        lastro estrutural = V-01/V-04/V-05, não esta regra)

Região 2 — comentário interno, linha 447:

    # ---------------- V-06 detecção heurística de possível deriva (ficha/vínculo × prosa ancorada)

Região 3 — bloco V-07, linhas 495 a 509:

python
        # 2026-09-15 (precisão 3 da casa, F-C2): o teste comparava CARDINALIDADE.
        # Contraexemplo reproduzido nesta bancada: trocar um ID por outro falso,
        # preservando 15 itens, atravessava o portão em silêncio — e isto é classe
        # BLOQUEANTE. Passa a comparar CONJUNTOS, como o ramo irmão clinical_domains
        # (F-C3) já fazia. Relevante sobretudo para a ingestão de B2..B16, quando IDs
        # de mecanismo passam a caminhar.
        rel_txt = do_texto(r"\*\*Mecanismos relacionados \(IDs oficiais\):\*\*\s*(.+)")
        if rel_txt:
            s_txt = {x.strip() for x in rel_txt.split(",") if x.strip()}
            s_man = {str(x).strip() for x in ((man.get("semantic_layer") or {}).get("related_entities") or [])}
            if s_txt != s_man:
                rel.erro("V-07", "related_entities",
                         "identidade divergente (fonte única violada) — "
                         f"só na canônica: {sorted(s_txt - s_man)} · "
                         f"só no manifesto: {sorted(s_man - s_txt)}")

Uma diferença sutil na região 3 que vale conferir: minha linha do s_man tem parênteses externos em volta do (man.get(...) or {}).get(...) or []. A redação da carta 11 não os tinha. Funcionalmente é igual, mas muda os bytes.

Referência para fechar: arquivo com 665 linhas, sha be48a5efa1d67f9e7b4ae3a38fdcf562b924cc03fc58e91baa2c63a3c6b33e92. Se a reconstrução der essa sha, seladas as duas casas. Se der outra e o comportamento for 2/299 com V-14 verde e F-C2 disparando, fiquem com os bytes de vocês — a sha viva única vale mais que a autoria do arquivo, e o que eu queria preservar era o comentário, não a minha formatação.

Sobre a nota Unicode de vocês: adoto NFC como camada oficial também do meu lado. Meus "ANAMNESE ×3 / UNIFICADOS ×1" eram do upload em camada case-sensitive, e a divergência com a instalada é de escopo, não de dado — mas a régua de vocês é melhor e eu passo a declarar camada junto com a contagem, como combinado.

Fase 4 verde. Abro o Contrato das Unidades Narrativas na próxima rodada, com a âncora do §6 que vocês verificaram intacta na V2.2.
