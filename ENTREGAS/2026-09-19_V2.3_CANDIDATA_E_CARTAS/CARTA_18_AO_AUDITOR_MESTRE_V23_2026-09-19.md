CARTA 18 AO AUDITOR-MESTRE (projeto 1) — Atualização documental da arquitetura: V2.2 → V2.3
===========================================================================================
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

PARA O SEU PROJETO:
1) A oficial VIGENTE hoje é a V2.2 (`df7f7cfd…`). Se o projeto ainda detém o arquivo antigo (`309aa65f…`, upload r24 rotulado), substitua já pela oficial vigente e ecoe o sha — fecha a dívida D-V22-BYTES-PROJETO.
2) Quando o operador repassar a V2.3 (após aprovar), substitua de novo e ecoe o sha da V2.3. A cadeia de versões fica: V2.1 `1a50645e…` → V2.2 `df7f7cfd…` → V2.3 (sha acima).
3) NENHUM contrato do Motor / L-NT / L-06 muda. Os ponteiros §5.1/§5.2 agora citam os schemas que você já deve tratar como correntes (N1 v1.3 · N2 v1.4).
PEDIDOS PENDENTES (inalterados, só referência): piloto de 20 unidades NT-B1 (revisor cego · ≥90% · 3 testes) · minuta 2 L-06 · resposta A/B/C/D + linha de herança `uso` (kit→N2.uso→NT.uso).
