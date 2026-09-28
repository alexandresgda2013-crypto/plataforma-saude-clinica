# Auditoria Científica de Conteúdo — B2 (Eixo HPA / Cortisol)

**Data:** 2026-06 (retrocompatibilização ao padrão B7/B8) · **Sessão:** operador de geração; **P-6** (2ª verificação independente/avaliador cego) PENDENTE.
**Objeto:** trechos-âncora da canônica `B2 EIXO HPA CORTISOL V1 CANONICA.md`.
**Ferramentas:** G1 eutils (esearch+esummary+efetch), G2 espécie/elegibilidade, G3 suporte; `gate_script.py` (P-5) + `validar_auditoria.py` (framework).

## Contagem de decisões
- Trechos no ledger: **185**
- G1: {'VERIFIED_REFERENCE': 185} · G2: {'ELIGIBLE_SOURCE': 178, 'NAO_APLICAVEL': 7} · G3: {'APROVADO': 184, 'APROVADO_COM_RESSALVA': 1}
- status_auditoria: {'APROVADO': 184, 'APROVADO_COM_RESSALVA': 1}

## Notas
- Módulo 09 no schema oficial (id_referencia_interna `REF_SOBRENOME_ANO`, doi, claim_id_origem; 5 arquivos).
- Referências citadas apenas em listra/corpus indexadas por rótulo canônico (apêndice de corpus) para rastreabilidade; citações clássicas de prosa sem PMID verificável foram rebaixadas a menção nominal sinalizada ao P-6 (R04: campo vazio preferível a dado inventado).
- Evidência animal/pré-clínica sinalizada `[APENAS PRÉ-CLÍNICO]/[EXT]`; bloco natureza_sistema (P12), semantic_layer (R06) e referência cruzada a B16 (P16) presentes na canônica.

## Declaração
> A Biblioteca_B2 foi auditada quanto a conteúdo: cada afirmação factual tem vínculo verificado (G1→G2→G3) ou está sinalizada como parcial/pré-clínica. `validar_auditoria.py`: **0 ERRO**; `gate_script.py`: **GATE APROVADO**.
> **Pendência P-6:** 2ª verificação independente (avaliador cego).

---

## Rodada [AT] 2026-09-08 — reconciliação de insumo externo (P-7) → V2

**Objeto:** insumo externo "matriz canônica B2" oferecido pelo usuário para revisão cruzada da B2 (V1 → **V2**).
**Fluxo:** P-7 (mini-ciclo Pré→G1→G2→G3→nova versão). V1 **não** editada in place — arquivada em `producao/historico/v1_canonica_2026-09-08.md`.

### Entrada do insumo
- 34 PMIDs + 1 DOI (duplicata Müller/Ller) + 21 itens só (Autor, Ano).
- G1 eutils: **35/35 resolvidos**. **Zero falsos positivos** — qualidade do insumo alta.
- Correção de registro: meta HPA-treatments (34566653) veio sem autor → **Ding Y 2021**.
- Duplicata Müller/Ller 2000 (mesmo DOI) → **1 entrada** (PMID 11089561).

### Decisões de conteúdo — ENTRARAM 28 refs verificadas (185 → 213)
- **Metrologia (3):** Stalder 2016 (CAR consenso), Wesarg-Menzel 2024 [MA; NEG — diurno≠reatividade], Sugaya 2020 (cabelo=janela integrada).
- **Síntese HPA/TDM — novo 6.17 (7):** Swaab 2005, Von Werne Baes 2012, Ceruso 2020, Sahu 2022, Machahary 2025, Jarcho 2013, Zajkowska 2022.
- **FKBP5 G×E — 4.3/4.4 (8):** Zobel 2010, Xie 2010, Zimmermann 2011, Wang 2018 [MA], Tozzi 2018, Kaul 2026 [fronteira], Zhang S 2025 [ML], Balfour 2026 [MA; downgrade].
- **CRH/PVN circuito — novo 2.12 (3):** Stanton 2023, Zheng 2026, Sukhareva 2021.
- **Farmacologia sonda (4):** Spiga 2009 [ML], Sun 2023 [ML], Ding 2021 [MA], Lombardo 2019 [MA].
- **Mecânica GR (1):** Tatro 2009 [ML; FKBP51/52 translocação].
- **B2↔B1 (1):** Van Den Noortgate 2025 [OB; crosstalk bidirecional].
- **Foldossomo/dup:** Müller 2000 [ML] (registro-índice da duplicata mesclada).
- Regra estrutural adotada como governança textual: modelo simples "TDM→cortisol alto" **rejeitado**;
  "diurno ≠ resposta aguda" e "metilação ≠ biomarcador clínico" viraram regras explícitas [AT].

### NÃO ENTRARAM
- 21 itens só (Autor, Ano): `[G1: a cravar]` — sem identificador verificável (incl. Peng 2018 incompleto; Klinger-König 2019, Ising 2008, Khoury 2019, Klengel 2013 já tinham equivalente na B2).
- Regras B2.R01–R20 e arquitetura 52 submódulos do insumo: não são fontes; convergem ~90% com a B2 vigente.

### Portões pós-fusão (V2)
- gate P-5: **APROVADO** (refs 213 | vínculos 89).
- framework: **0 ERRO** (213 avisos não-bloqueantes citacao_literal — padrão da série).
- checklist entrega: **41/41** (após correção de 10 vínculos com âncora ≤20 chars → ampliadas).
- Incidente registrado: edições em lote paralelas ao .md causaram perda transitória de 1 parágrafo (CAR) — detectado e reaplicado; varredura final confirma 27/27 menções de prosa únicas.

**P-6:** continua PENDENTE — leva [AT] integra o pacote cego de alto risco.
