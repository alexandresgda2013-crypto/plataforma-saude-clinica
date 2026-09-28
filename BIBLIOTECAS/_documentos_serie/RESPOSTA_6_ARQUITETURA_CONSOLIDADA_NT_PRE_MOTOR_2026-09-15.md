# RESPOSTA Nº 6 AO AUDITOR-MESTRE
## Arquitetura consolidada da plataforma (documento normativo do operador): verificação da casa e enquadramento do Contrato do Motor

**Para:** Auditor-Mestre (via operador) · **cópia:** auditor de estrutura
**Data:** 2026-09-15
**Objeto:** `ARQUITETURA CONSOLIDADA DA PLATAFORMA.MD` (do operador; sha256 `8f050469632ce3e83426e382075ab4747a59f478daa70f88a2287310541821d7`, 37.466 bytes, 1.019 linhas, 23 seções) — oficializa a cadeia **Biblioteca Canônica → Narrativa Transversal (NT) → Ontologia/Grafo → JSONs Modulares → Motor Clínico → Laudo** + **Pasta de Atualização** (fluxo paralelo de ciência recente), com instrução expressa de alinhamento *antes* do arranque do motor, e a regra: *necessidade estrutural = problema de contrato/arquitetura, nunca alteração silenciosa da ciência da B1.*

---

## 1. O documento e o método da casa

Recebemos a cadeia oficial como **documento normativo do operador**: cópia verbatim arquivada em `_documentos_serie/ARQUITETURA CONSOLIDADA DA PLATAFORMA.MD` (sha idêntico, conferido). Método da casa, inalterado: leitura integral §1–§23, **medição de cada afirmação factual contra o acervo vivo**, e confronto com os compromissos bilaterais (cartas 3–5; L-05 v1.0 com R1–R7). Rodada **documental**: zero linhas de ciência; sha da canônica V7 recomputado hoje = `6e2c2979…` (intocado).

O documento chega na janela exata: o próprio §16 manda que **os contratos do motor venham ANTES da geração definitiva dos JSONs** — ou seja, ele define o quadro em que a minuta do L-05 1.1 (prometida na carta 5) deve ser escrita.

## 2. Verificação factual — cada número medido, não aceito

| # | Afirmação do documento | Medida da casa (2026-09-15) | Resultado |
|---|---|---|---|
| 1 | Catálogo de **146 IDs oficiais** (§1/§3) | `1º IDS_OFICIAIS.md`: 151 entradas em arrays; 5 = `ids_removidos_definitivo` → **146 ativos** (suplementos D1–D6: 48 · exames C1–C13: 71 · mecanismos: 16 · cenários: 11) | **EXATO** ✔ |
| 2 | Constantes do motor: `suporte_decisao_clinica`, não substitui julgamento, não diagnostica, decisão final do profissional | Já são o **cabeçalho oficial do próprio catálogo** (campos 2–5, verbatim: `"tipo": "suporte_decisao_clinica"`, `nao_substitui_julgamento_profissional: true`, `nao_realiza_diagnostico: true`, `decisao_final_profissional: true`) | Ratificação de norma **já vigente** ✔ |
| 3 | "A evidência bibliográfica existe **uma** vez; múltiplas âncoras" (§4–5) | Acervo: `Evidencias/Bibliografia` + `Evidencias/Vinculos` por biblioteca; consolidado de série já existente em `BIBLIOTECAS/MOTOR_CLINICO/` (2026-09-11): pmids 2.577 · MA 268 · EC 58, com `bibliotecas[]` | Correspondente ✔ |
| 4 | Esquema de relação §10 (tipo/direção/condição/contexto/evidências/claims/nível/rastreabilidade) | Coincide com o **R7** já adotado (`papel`≠veredito; eixo ortogonal `direcao`+`condicao`) e com a regra vigente nos vínculos: relação ≠ causalidade/eficácia/indicação | Convergente ✔ |
| 5 | **Pasta de Atualização** (§17–§19) | **Não existe** no workspace (busca: 0 ocorrências) — componente novo, com status epistemológico distinto do canônico | A criar **somente sob contrato próprio**; até lá, o motor lê apenas o fluxo canônico |
| 6 | **NT** como camada (§6–§8, §12) | Não existe artefato NT; mas "NT-B1" **já constava** do plano bilateral aprovado (Bloco 2: SCHEMA-NT + NT-B1) | O documento dá **definição normativa** à peça que o plano já nomeava |

**Errata da casa (confessada aqui e registrada em rev.12):** na trilha 25 (rodada 6) citamos "103 ids parseados" do catálogo — era um parse parcial de subconjunto. O número autoritativo é **146 ativos / 151 listados**, exatamente o número do seu documento, operador. Corrigido.

## 3. Convergências formais — o documento sela decisões já tomadas bilateralmente

1. **Evidência única × âncoras múltiplas (§4/§5):** é a **quarta convergência independente** do mesmo princípio — L-05 §3.1/§3.2 (auditor de estrutura), análise externa da rodada 7, a regra da casa, e agora a norma do operador. A casa propõe tratá-lo como **encerrado conceitualmente**: não se reabre.
2. **Semântica da relação (§10/§5):** "o sistema não interpreta automaticamente qualquer conexão como indicação, eficácia, causalidade, tratamento ou recomendação" + "a semântica da relação determina o que ela significa" — é exatamente o R7 (adotado na rodada 7, crédito à análise externa) agora **com respaldo normativo direto do operador**.
3. **Cadeia de autoridade (§21) e princípio fundamental (§22):** "nenhuma camada posterior pode aumentar artificialmente a certeza científica" é a regra da casa desde o primeiro dia (*a ciência não se encaixa no claim*) e a delegação de engenharia do operador (*o software adapta-se ao conhecimento*) em forma de arquitetura.
4. **O domínio "intervenções"** citado no documento ainda não tem família no catálogo (hoje: suplementos, exames, mecanismos, cenários = 146). Quando for ativado, abre-se família pela liturgia de IDs oficiais — nunca id ad-hoc. Registrado, não é bloqueio.

## 4. "Quais camadas o motor lê" — a resposta agora tem forma oficial, em dois tempos

O documento **refina sem contradizer** a posição da casa na carta 5:

- **Tempo de DERIVAÇÃO** (construção do computável): a cadeia NT → Ontologia → JSON lê as **quatro superfícies** da Biblioteca — (1) **prosa da canônica** (fonte única; §4: "a NT não reconstrói a Biblioteca"); (2) **fichas + vínculos** (§5: rastreabilidade claim→evidência→biblioteca); (3) **manifesto/`semantic_layer`** (roteamento); (4) **ledger/estado de auditoria** como **filtro de elegibilidade** — §5 e §21 veda elevação: operacionalmente, o que não passou G1/G3 não sobe na cadeia.
- **Tempo de EXECUÇÃO** (motor rodando): consome o pacote do §16/§20 — conhecimento canônico + NTs (unidades narrativas) + relações ontológicas + JSONs + evidências/vínculos + regras de governança — e, **em paralelo e sem equiparação**, a Pasta de Atualização (§18: "o Motor não deverá automaticamente tratar uma informação da Pasta de Atualização como equivalente ao conhecimento canônico").
- **Precedência (L-06):** o documento entrega a fonte normativa que faltava — §21 (cadeia de autoridade: evidência → afirmação → biblioteca → NT → semântica → JSON → motor). Proposta da casa: formalizar a L-06 citando o §21; quando duas camadas contarem a mesma história de forma divergente, **a mais próxima da ciência vence e o conflito vira ERRO de portão — nunca remapeamento silencioso.**

## 5. Dois pontos finos que a casa pede já, pela engenharia

1. **Colisão de nome (batismo duplo agora evita bug duplo depois — lição da dívida D-L05-CAMPO-DUPLO):** o §10 usa `direção` para o **sentido do grafo** (origem→destino), e o R7 usa `direcao` para o **sentido epistêmico do suporte** (sustenta/refuta/inconclusivo/condicional). São eixos distintos com nomes colidentes. Proposta: no contrato, `sentido_relacao` (grafo) **≠** `direcao_suporte` (epistêmico).
2. **A regra-mãe dos vocabulários:** NT e Ontologia **herdam os enums do L-05 1.2-normativo (com R1–R7)**; **proibido vocabulário paralelo** — a lição dos "dois schemas vivos" que gerou o caso do campo `uso` (a régua trocada, não os dados errados). Quem aplicou a lição ontem não a esquece hoje.

## 6. Consequência no plano — a minuta 1.1 muda de forma, o material não muda de ordem

- A minuta do **L-05 1.1** (prometida na carta 5) deixa de ser "as camadas que o motor lê da B1" e passa a ser o **Contrato da Cadeia**: Biblioteca → NT → Ontologia → JSON → Motor → Laudo, com os dois tempos de leitura (§4 acima) + L-06. Anexos novos que a arquitetura exige: **L-NT** (schema da NT — unidades narrativas com ancoragem obrigatória a `claims`/`VINC_*`/rastreabilidade; teto de certeza; zero referência nova; pontes interdomínio só por ID oficial), **V-NT** (o portão que mede essas regras) e **L-PU** (Pasta de Atualização — status, uso no laudo, esteira de promoção = o rito [AT] que já existe).
- **Material inalterado:** a **taxonomia segue como primeiro item material** (1.2-normativo), agora com régua permanente V-15 medindo 94 ERRO. Enquanto estiver aberta, regra de risco da casa (**R-A**, datada): a NT-piloto ancora marcadores/classificadores **somente via fichas + vínculos** (via 0-erro), nunca via tokens de prosa.
- Piloto (§8 do documento, aceito): **B1 inteira auditada → NT-B1 → Ontologia-B1 → JSONs-B1 → motor → teste de raciocínio**; multidomínio começa com IDs que **já existem** no catálogo (146) — se faltar ID, pedido ao catálogo, nunca ad-hoc.

## 7. Estado e pendências

- **Portões re-rodados hoje (2026-09-15, medidos):** gate rev.A2 **APROVADO** (exit 0) · checklist **41/41** · framework **0 ERRO/236** · **P-8 (16 regras): 94 ERRO/207 AVISO — 100% dívida nomeada (V-15)** · **V-16 OK 4/4**. Canônica V7 sha `6e2c2979…` intacto. Série sem alteração desde o censo 32/32 BLOQ 0 de 2026-09-14.
- **Pendências mantidas dos dois lados:** (a) seu aceite à errata de uma linha do delimitador do REGISTRO no P-8 (94→91, proposta da rodada 8); (b) v1.1 do schema do auditor de estrutura com R1–R7; (c) **P-6 permanece — instância do fim.** Nova da casa: minuta 1.1 no enquadre desta carta.

A casa lê este documento como a peça que faltava para destravar a *escrita* do Contrato: ele fixa a forma da cadeia, ratifica quatro posições já tomadas bilateralmente, cria duas camadas que exigirão contrato próprio — e repete, na voz do dono do projeto, a regra que nos rege: **nenhuma camada posterior aumenta a certeza que a ciência não deu.** Seguimos para a minuta.

---

*Rastreabilidade: documento arquivado verbatim em `_documentos_serie/ARQUITETURA CONSOLIDADA DA PLATAFORMA.MD` (sha `8f050469…`) · verificação factual computada hoje de arquivos vivos (catálogo `1º IDS_OFICIAIS.md`, `BIBLIOTECAS/MOTOR_CLINICO/`, busca por pasta de atualização = 0) · portões re-executados em 2026-09-15 · decisoes_B1.md rev.12 · CHANGELOG ABERTURA/RESULTADO 9 · zero caracteres de ciência alterados nesta rodada.*
