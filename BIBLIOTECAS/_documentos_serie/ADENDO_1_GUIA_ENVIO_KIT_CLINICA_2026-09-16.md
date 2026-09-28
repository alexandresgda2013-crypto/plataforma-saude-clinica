# ADENDO 1 ao GUIA DE ENVIO DO KIT CLÍNICA — atualizações verificadas após 2026-09-15

**Data:** 2026-09-16 · **Uso:** anexar ao pacote do kit junto com o guia original. **Trilhas:** 33 e 34 · **Ciência tocada:** 0.

---

## 1. Item 1º resolvido — `_ids_oficiais`/catálogo de IDs

O `1º IDS_OFICIAIS.md` enviado pelo operador em 15/09 é **byte a byte idêntico** ao catálogo oficial vigente das bibliotecas (`Ferramentas de geração e auditoria/01_norteadores/1º IDS_OFICIAIS.md`):

- sha256 `f3a74fbcda9aa0aa4b9e13d42321776c4b68a4928180d7245aa4c008400b0e16`
- **146 IDs válidos · 5 removidos** (marcados nas linhas 237/280/282)

A digital da casa vale como a digital do item 1º do kit para o projeto novo de claims — o COMO EXECUTAR v1.7 manda ler esse arquivo primeiro.

## 2. `CANDIDATOS_IDS_OFICIAIS` verificado

- Arquivo: `CANDIDATOS_IDS_OFICIAIS — v1.0.md` · sha256 `556bb82d4bbec8b42089ac709466c543dd2689c1e845a03e2078193e3772ae00`
- **12 candidatos · 0/12 presentes no catálogo** (regra do kit — "candidato não pode colidir com ID oficial" — confirmada na bancada).
- `exame_razao_neutrofilos_linfocitos` (NLR) e `exame_s100b` constam `em_avaliacao` — **acionáveis** pela régua; a categoria `C4_inflamatorios` existe no catálogo (7 itens).
- Divergência menor registrada: nome do arquivo diz v1.0, conteúdo diz v1.1 (documenta as 2 trilhas de claims: `B1.SM02.*` × `B1.MEC.BLOCO03.002`).

## 3. Ponteiro morto declarado

"Estudos que não foram escolhidos.md" — referência da última linha do próprio BLOCO v1.6 (`nao_escolhidos_arquivo_externo`, 17+ PMIDs). O operador não localizou o arquivo; a casa o registra como **ponteiro morto nomeado**, saneamento futuro do Bloco. Nada se perde em silêncio.

## 4. Decisões que seguem do lado do operador (não são da casa nem do senhor)

1. conflito de disposição **33339712 × 30696814** (rejeitado × realocar a B4);
2. disposição dupla **20132991** (rejeitado em .012 × corroborante de .012c);
3. ressincronização do BLOCO v1.6 (cabeçalho 13 × corpo 22 entries; incluir **.017**, que o COMO EXECUTAR v1.7 diz ter mudado de desfecho).

## 5. Estado da frente (declaração de escopo)

A produção de claims SM-02 está **pausada por decisão do operador**. Este envio é de **ancoragem e medida** — o senhor ancorará byte a byte o que medimos — não é sinal de retomada. A oferta da casa de um **validador executável do SCHEMA-CLAIM v1.2** (lint: TAB, chave duplicada, enum fora do valor exato, ressalva sem nota, comparador ausente) segue aberta aguardando o "vai" dele.

## 6. Anexos reproduzíveis

Trilhas **33** (medição kit × B1 V7, com o script de cruzamento) e **34** (IDS/CANDIDATOS) em `atuais/producao/` — comandos, chaves e regex gravados. Qualquer número do guia ou deste adendo pode ser reexecutado.

— a casa
