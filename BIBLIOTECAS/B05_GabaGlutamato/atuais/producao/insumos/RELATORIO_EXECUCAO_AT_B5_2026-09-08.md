# RELATÓRIO DE EXECUÇÃO [AT] — B5 → V2 (2026-09-08)

**Decisão do usuário:** "colocar na biblioteca o que a ciência diz, sem extrapolar e sem deixar de fora
o que é importante para a análise mecanística de B5" → aplicação **completa** das 116, com selos
honestos (`[ML]`/`[EXT]`/NEG/CONT) — nada extrapolado, nada importante omitido.
**Corpus final: 44 → 160 refs** (10.059 palavras). V1 em `producao/historico/v1_canonica_2026-09-08.md`.

## O que a ciência estabeleceu (e entrou)
- **MRS humano discorda consigo mesmo** e ficou pareado: Godfrey 2018 (GABA↓; glutamato global sem
  diferença — NEG) × Kantrowitz 2021 (Glx↑+GABA↓ vmPFC/ACC — CONT). Steel 2020 × Rideaux 2021/2022
  fixam a trava: **GABA/Glx por MRS ≠ E/I sináptico**.
- **NMDAR não é unidirecional**: Pothula 2021 (potenciação antidepressivo-símile) + Zanos 2023
  (ativação-dependente) contra o antagonismo simplista — e "antagonismo NMDA ≠ mecanismo completo
  da cetamina" (metabólitos, tônico Le 2026a, LTP/scaling Le 2026b, enantiômeros, AMPA-PET Nakajima 2026
  em TRD humano).
- **Circuito > concentração**: Wu 2026 (dmPFC→LHb dual), Ryazantseva 2025 (PV/kainato-GABA-B amígdala),
  Xiao 2021 (BNST→NAc), Fogaça 2021 (mPFC suficiente/necessário), Fee 2021 (SST→α5).
- **Fundamentos como fundamentos** (49 `[ML]` com R04 integral): subunidades NMDA/AMPA, GABA-A
  por subtipo, inibição tônica, PV/SST, ciclo glutamina — SUP mecanístico, nunca evidência clínica.
- **B7 como ponte, não prova** (Zielińska 2026).

## Portões (rodados após aplicação)
- gate_script.py (P-5): **APROVADO (160|160)**.
- validar_auditoria.py: **0 ERRO** (44 avisos não-bloqueantes — padrão listra descritiva da série).
- checklist_entrega.py: **41/41 OK | 0 FALHA**.
- Varredura `\b\d{7,9}\b`: 0.
- decisoes_B5: bloco [AT] · P-4 ADENDO V2: **15/15 SIM** · trilha `producao/04_AT_ciclo_2026-09-08.json`.
- **P-6 PENDENTE** (Via 2 cobrirá a leva [AT] da B5).

## Incidentes corrigidos no caminho (registro honesto)
1. Iterador de grupos omitia AMPA (5 refs) — capturado por assert.
2. `claim_id` formato (`B5.MEC.BLOCOxx.nnn`) — 116 remapeados.
3. Sufixo de colisão de ID — padrão oficial minúsculo (`Zanos_2018b`, `Le_2026b`) alinhado a B3.
4. 2 typos de redação corrigidos; 112/116 DOIs preenchidos (4 antigos sem DOI depositado).
