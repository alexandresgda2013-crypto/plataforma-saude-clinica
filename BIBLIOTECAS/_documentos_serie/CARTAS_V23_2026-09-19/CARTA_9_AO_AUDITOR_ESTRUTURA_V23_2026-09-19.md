CARTA 9 AO AUDITOR-ESTRUTURA (auditor-2) — Atualização documental da arquitetura: V2.2 → V2.3
=============================================================================================
Casa (bancada de verificação) → via OPERADOR · 2026-09-19 · rodada 41
Estado de governança: V2.3 é CANDIDATA — a oficial VIGENTE hoje é a V2.2 `df7f7cfd…` (aprovada 2026-09-19). Nada circula direto entre IAs: tudo flui pelo operador.

DIGITAIS (conferir com sha256sum):
· oficial vigente  V2.2 `df7f7cfdfc01cf77d658885f30dfefe29dcf380229ea56e6b3af02920df22ae1` (52.181 b · CRLF)
· candidata        V2.3 `498e7df9d8abe8be4f3145bb7a9bd34215bc87a4502148e9d203391c9ce6ef73` (52740 b)
· schema N1 corrente (referência) v1.3 `b06660fd985a8186dbe5ed2878f15d3badd2356e11f4d0c9b71e78d2b2e4e7da`
· schema N2 corrente (vínculo)    v1.4 `d96ad15b620fa373d8d95d44159a9f3db31c04cfed051d85c7ab014cb3c65050`

O QUE MUDA NA V2.3 (diff medido: exatas 4 linhas substituídas, 0 inseridas/removidas; CRLF 1411/1411; 30 seções únicas intactas):
1. cabeçalho: «…PLATAFORMA V2.2    17.09.26» → «…PLATAFORMA V2.3    19.09.26»  (renumeração pedida pelo operador: rastreabilidade da vigente — 'só mudar a data é pouco');
2. linha Rev: passa a «Rev. V2.3 — 2026-09-19» com o histórico INTEIRO da Rev. V2.2 preservado na mesma linha;
3. §5.1: ponteiro `L05/schema_referencia_v1.1.json` → `L05/schema_referencia_v1.3.json`;
4. §5.2: ponteiro `L05/schema_vinculo_v1.1.json`   → `L05/schema_vinculo_v1.4.json`.
Motivo: os ponteiros citavam 'v1.1' — nomes que nunca existiram como arquivos reais (dívida D-V22-SCHEMA-NOMES). 0 conteúdo normativo alterado.

O QUE NÃO MUDA: todo o restante, byte a byte — §2 completo (fluxos segregados até o Motor · origem_conhecimento · prosa prevalece sobre desenhos · Pasta fora do cânone) · §§3–30 · a âncora interna «(Rev. V2.2, 2026-09-17)» do §2 FICA — é proveniência histórica correta (a regra nasceu na V2.2). Citações por seção/feitas na auditoria da rodada 34 não quebram.

REGISTRO CRUZADO: o ponteiro defasado que você reportou em 19/09 é o mesmo que a casa nomeou D-V22-SCHEMA-NOMES na rodada 36 — convergência independente, agora corrigida na V2.3.
PRECISÕES À SUA RÉPLICA (trilha 56 da casa, 26/26 verdes — disponível se quiser):
(a) autoria: o aceite '…base de fechamento do L-05' (r29) é do comentador; a casa subscreveu após réplica integral — sem erro de mérito, só de atribuição;
(b) genealogia (a única afirmação factual que não se sustentou na bancada): `direcao` e `condicao` existem DESDE a v1.1 (o rename para `direcao_suporte` ocorreu na v1.2) — logo a prosa do §5.2 não estava 'três versões à frente': foi escrita em 15/09, contra a própria v1.1. O defeito real era só o NOME do ponteiro — corrigido agora;
(c) o 'parecer de ontem' citando `CLAIM_KIT_CLINICO` para o enum `origem_pipeline` do N1 NÃO chegou à casa (0 ocorrências na base arquivada · 0× na minuta v1.4). Por favor reenvie os bytes verbatim; a proposta fica registrada e subordinada à homologação do fluxo de claims e à cadeia formal de alteração do N1 (regra nova de versionamento — a mesma agora aplicada à arquitetura).
ESTADO DOS SCHEMAS (alinhado à sua própria leitura de 19/09): N1 v1.3 / N2 v1.4 = correntes validados tecnicamente (ciclo r29; 52/52 + 26/26); selo formal do operador com sha/data ainda pendente — os nomes internos de arquivo e o rótulo 'PROPOSTA — não normativo' nas descriptions permanecem como dívida editorial (D-L05-NOME-X-ID).
