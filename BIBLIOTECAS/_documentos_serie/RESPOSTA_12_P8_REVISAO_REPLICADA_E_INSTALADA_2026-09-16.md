# RESPOSTA 12 — P-8: revisão do senhor replicada na bancada e instalada como oficial (+ kit clínica nesta leva)

**Data:** 2026-09-16 · **Ref.:** sua revisão dos 3 pontos da carta nº 11 (sha `be48a5ef…`, conforme informado) · **Trilha:** 36 · **Ciência tocada:** 0

---

## 0. Arquivo recebido e método

Sua mensagem foi arquivada **verbatim** antes de qualquer resposta: `_documentos_serie/P8_revisao_mestre_3pontos_recebida_2026-09-16/RESPOSTA_MESTRE_REVISAO_P8_3PONTOS_2026-09-16.md` · sha256 `0cfe820b4ff67a36a6e1da71572c0e679ff0a7dba9c36d72a5033a35a66cb0bd`. (O sha `be48a5ef…` da revisão chegou truncado; se o senhor o passar por extenso, conferimos com a cópia arquivada.)

Como sempre: **replicamos empiricamente antes de aceitar** — inclusive cada afirmação da sua revisão. Comandos, chaves e saídas na **trilha 36** (`producao/TRILHA36_verificacao_instalacao_P8_3pontos_2026-09-16.json` + script reexecutável).

## 1. Réplica ponto a ponto da sua revisão — tudo confere

| # | Afirmação do senhor | Réplica da bancada | Resultado |
|---|---|---|---|
| 1 | Baseline: 2 ERRO / 299 AVISO / exit 1 na V7 | rodamos o oficial `76e526cf…` na V7 (`6e2c2979…`) | **confere** — 2/299/exit 1 |
| 2 | F-C2 no script antigo: V-07 muda com 15 itens e ID trocado | mesmo contraexemplo (`mecanismo_B16_neurogenese`→`mecanismo_B99_inexistente`) | **confere** — 2/299/exit 1, V-07 silente; o furo era real |
| 3 | Com o reforço, dispara e nomeia os dois lados | mesmo contraexemplo no candidato | **confere** — `ERRO V-07 related_entities: identidade divergente (fonte única violada) — só na canônica: ['mecanismo_B16_neurogenese'] · só no manifesto: ['mecanismo_B99_inexistente']`; placar sob adulteração 3 ERRO/exit 1 |
| 4 | Placar inalterado no dado limpo | candidato na V7 | **confere** — 2/299/exit 1, V-07 segue muda (agora por identidade) |
| 5 | V-14 verde com 16 regras | leitura do relatório | **confere** — `docstring x implementação coerentes: 16 regras anunciadas, todas executadas` |

Manifesto restaurado e sha `79d1309a…` conferido **após cada** adulteração de teste. Canônica `6e2c2979…` intacta do início ao fim.

**Uma divergência de superfície, declarada:** o senhor mediu o diff em **24 linhas / 5 hunks**; a nossa aplicação da redação da carta 11 mede **17 linhas tocadas (+10/−7) em 3 hunks**. A diferença é de contagem, não de escopo: com contexto 3, as duas linhas do docstring (V-06 e V-08, a 2 linhas de distância) colapsam num único hunk, e as linhas compartilhadas do bloco V-07 (`rel.erro("V-07", …)`) caem como contexto. Se a sua redação formatou o bloco de outro modo, o número sobe sem mudar comportamento. O vinculante da carta 11 — **escopo = só os 3 pontos · placar idêntico · V-14 verde** — está verde dos dois lados. Se o senhor anexar o seu arquivo revisado, a bancada confronta byte a byte e publica o diff funcional (esperamos equivalência exata de comportamento).

## 2. Instalação — novo oficial

- **Novo oficial:** sha256 `84fa918d09899d54995ae41d65b0787a7a52888ba6177ce77583483b1124fe8b`
- **Anterior:** `76e526cf…` aposentado **com backup** `validar_coerencia_camadas.py.bak_oficial_pre_3pontos_R16_2026-09-16` (cadeia completa de `.bak_*` preservada)
- Execução pós-instalação pela invocação de sempre: **2 ERRO / 299 AVISO / exit 1** — os 2 ERRO por desenho (`natureza_evidencia`, `trilha`) seguem exatamente como estão, aguardando taxonomia/migração
- B/A gravado na trilha (primeira comparação marcou falso por rótulos de cabeçalho do diff; correção datada no passo 7b: **conteúdo idêntico**, era artefato dos nomes dos arquivos)

## 3. Sobre o julgamento do senhor — aceito e registrado

Registramos com agrado a confissão da F-08-em-escala-menor no próprio portão; é a mesma classe e a bancada a tinha nomeado como "superfície". E **concedemos o ponto**: o senhor tem razão em dizer que o ponto 3 supera o 1 — honestidade de rótulo ensina, mas o furo executável na classe bloqueante **mordia**. A V-07 deixa de ser o único teste do portão que comparava cardinalidade onde devia comparar identidade (F-C3 permanece: alinhado ao irmão `clinical_domains`).

## 4. Notas finas da carta 10 — replicadas antes de concordar

- `condicao`: preenchida em **0/274** vínculos — confirmado: **ausente**, não esparso. O schema v1.1 tem a exigência condicional; o acervo não tem o dado.
- `verification_status = extrapolado`: **62/274** — confirmado. Degrau 5 da L-06 com meia perna ("gatilho + degraus 1, 6 e metade do 5") anotado para a minuta 2.

(Enum completo do rodapé, para o §4B da 1.2: verificado 140 · preclinico 63 · extrapolado 62 · pendente 7 · pendente_fulltext 1 · emergente 1 — 274/274.)

## 5. Kit clínica — nesta mesma leva, no arranjo que o senhor descreveu

O operador repassa: **9 arquivos byte a byte** os arquivados aqui (7 do kit + `1º IDS_OFICIAIS.md` + `CANDIDATOS_IDS_OFICIAIS — v1.0.md`), tabela de digitais (`DIGITAIS_KIT_2026-09-15.txt` + `_ADENDO1`), o **GUIA** (a leitura medida da bancada: cobertura 10/49 PMIDs = 20,4%, wiring formal zero, material dos 2 ERRO e da D-08, §5 com os defeitos internos do kit) e o **ADENDO 1** (item 1º resolvido — sha `f3a74fbc…` = catálogo oficial; CANDIDATOS 0/12 no catálogo; ponteiro morto nomeado; decisões do operador). Trilhas 33/34 disponíveis para reprodução. O que o senhor ancorar é byte a byte o que medimos — incluindo as arestas internas medidas, para não ancorar às cegas.

## 6. Fila

**Eixo P-8: pendência zero dos dois lados — confirmado pela bancada.** Registrada como próxima do seu eixo a **Fase 4 — Contrato das Unidades Narrativas** (D-05 como critério funcional; NT-B1 aguardando). Em paralelo e sem colisão, a bancada segue com: taxonomia (destrava os 2 ERRO: 197 leituras de desenho, 30 fichas `review`/Decisão 2, 24 `forca_biologica`), derivador IDS-JSON (dívida D-L05-IDS-JSON) e proposta rev.A3-E2. Ordem de emissão é sua.

## 7. Crédito e registro

Os 3 pontos são do **comentador externo** (crédito integral, carta 11); os reforços F-C1/F-C2/F-C3 são da **bancada**; a revisão é **sua**; a instalação é da **casa**. Trilha 36 · decisoes **rev.24** · CHANGELOG rodada 20. **Ciência tocada: 0** (0 campos, 0 fichas, 0 vínculos; V7 `6e2c2979…` e manifesto `79d1309a…` verificados por sha ao fim).

— a casa
