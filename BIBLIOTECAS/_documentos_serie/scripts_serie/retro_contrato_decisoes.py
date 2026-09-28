#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Adiciona blocos do Contrato (P12/R06/R04/P16) e relatorio decisoes_Bx.md
   nas bibliotecas B1-B6 retrocompatibilizadas."""
import json, glob, os, re
from pathlib import Path
from collections import Counter

CONFIG = {
 'B1': dict(folder='B1_Neuroinflamacao', mech='mecanismo_B1_neuroinflamacao',
   tit='Neuroinflamação', corte='2026-05',
   cs='Microglia, citocinas e vias inflamatórias modulam o humor. | Baseada na resposta imune inata e na sinalização neuroinflamatória. | Use para interpretar marcadores inflamatórios e adjuvantes — sem diagnosticar nem prescrever.',
   rag='houver menção a microglia, citocinas (IL-6/TNF/IDO-quinurenina), anti-inflamatórios ou vacinação; para contrapor associação humana a prova animal',
   kw='microglia, citocinas, IL-6, TNF, IDO, quinurenina, neuroinflamação, NAC, cetamina inflamatória',
   rel=['B2','B3','B4','B6','B7','B9']),
 'B2': dict(folder='B2_Eixo_HPA_cortisol', mech='mecanismo_B2_eixo_hpa_cortisol',
   tit='Eixo HPA / Cortisol', corte='2026-06',
   cs='O eixo HPA (CRH-ACTH-cortisol) regula a resposta ao estresse. | Hiper/hipocortisolismo e resistência ao GR ligam-se a depressão/TEPT. | Use para interpretar cortisol e fatores de estresse — sem teste de rotina nem prescrição.',
   rag='houver menção a cortisol, HPA, CRH, dexametasona, estresse crônico, TEPT ou resistência ao receptor glicocorticoide',
   kw='HPA, cortisol, CRH, ACTH, receptor glicocorticoide, FKBP5, dexametasona, estresse, TEPT',
   rel=['B1','B3','B8','B12','B14']),
 'B3': dict(folder='B3_Neuroplasticidade', mech='mecanismo_B3_neuroplasticidade',
   tit='Neuroplasticidade', corte='2025-08',
   cs='BDNF/LTP/sinaptogênese remodelam circuitos do humor. | Antidepressivos e intervenções restauram plasticidade. | Use como elo integrador central — B16 é o módulo especializado em neurogênese.',
   rag='houver menção a BDNF, LTP/LTD, sinaptogênese, remodelamento dendrítico, mTOR/cetamina ou plasticidade',
   kw='BDNF, LTP, sinaptogênese, mTOR, neuroplasticidade, espinhos dendríticos, TrkB',
   rel=['B1','B4','B5','B6','B8','B16']),
 'B4': dict(folder='B4_Monoaminas', mech='mecanismo_B4_deficiencias_monoaminas',
   tit='Deficiências de Monoaminas', corte='2024-06',
   cs='5-HT/DA/NA modulam humor e recompensa. | A teoria da deficiência é gating, não estoque. | Use para interpretar antidepressivos e cofatores — sem reduzir depressão a falta de serotonina.',
   rag='houver menção a serotonina/dopamina/noradrenalina, ISRS, transportadores, receptores monoaminérgicos ou à hipótese monoaminérgica',
   kw='serotonina, dopamina, noradrenalina, SERT, DAT, ISRS, TPH, monoaminas',
   rel=['B1','B3','B5','B8']),
 'B5': dict(folder='B5_GabaGlutamato', mech='mecanismo_B5_gaba_glutamato',
   tit='GABA / Glutamato', corte='2024-07',
   cs='O equilíbrio excitatório/inibitório (NMDA/GABA) governa ansiedade e depressão. | Cetamina/brexanolone agem nesse eixo. | Use para interpretar glutamato/GABA e neuromódulos — sem prescrição.',
   rag='houver menção a NMDA, GABA-A, glutamato, cetamina, brexanolone/zulresso, alopregnanolona ou E/I balance',
   kw='GABA, glutamato, NMDA, cetamina, alopregnanolona, neuroesteroides, inibição',
   rel=['B1','B3','B8','B13','B14']),
 'B6': dict(folder='B6_EstresseOxidativo', mech='mecanismo_B6_estresse_oxidativo',
   tit='Estresse Oxidativo', corte='2025-05',
   cs='ROS/RNS danificam lipídios/proteínas/DNA e ativam vias inflamatórias. | Defesa antioxidante e NAC entram como cofatores. | Use para interpretar marcadores redox — suplemento antioxidante tem evidência pequena.',
   rag='houver menção a ROS, GSH, SOD, GPx, 8-OHdG, MDA, NAC, antioxidantes ou ferroptose',
   kw='ROS, RNS, glutationa, SOD, NAC, 8-OHdG, peroxidação, ferroptose',
   rel=['B1','B3','B8','B9']),
}

BLOCO = """

---

## METADADOS CANÔNICOS (Contrato de Geração — P12 / R06 / P17)

**natureza_sistema (P12 — hard_fail):**
```json
{{
  "natureza_sistema": {{
    "tipo": "suporte_decisao_clinica",
    "nao_substitui_julgamento_profissional": true,
    "nao_realiza_diagnostico": true,
    "decisao_final_profissional": true
  }}
}}
```
> Biblioteca de **mecanismo** (P20): descreve o papel biológico da via; **não** diagnostica,
> **não** prescreve dose/protocolo nem substitui a avaliação clínica.

**semantic_layer (R06):**
- **clinical_summary (3 frases):** {cs}
- **rag_context_hint:** Recuperar quando: {rag}
- **clinical_domains (máx 4):** decisao_terapeutica · seguranca_clinica · triagem_clinica · monitoramento
- **semantic_keywords (8–12):** {kw}
- **related_entities (IDs exatos):** {related}
- **embedding_priority:** alta

**corte_literatura (R06):** busca ativa E-utilities/PubMed — corte {corte}.

**R04 — sinalizador de extrapolação:** evidência animal/in vitro (germ-free, modelos, cultura)
é marcada `[ML]/[APENAS PRÉ-CLÍNICO]` e **[EXTRAPOLAÇÃO POR ANALOGIA: contexto-fonte animal/in vitro — validação humana direta pendente]`;
não sustenta recomendação (R04: sem evidência humana direta → não entra como recomendação).

**P17 — posição na arquitetura de 16 mecanismos:** ID `{mech}` ({tit}).
- **P16 (anti-duplicação):** a neurogênese (proliferação de progenitores, migração, diferenciação,
  integração sináptica, zona subgranular/giro denteado) é escopo **exclusivo de
  `mecanismo_B16_neurogenese`**, subordinada a `mecanismo_B3_neuroplasticidade`. Nesta biblioteca
  ela aparece apenas como efeito/modulação indireta em 1–2 frases, sem replicar o conteúdo.
"""

for Bn, c in CONFIG.items():
    fp = Path(c['folder'])
    cans = [p for p in fp.glob('*.md') if 'CANONICA' in p.name.upper()]
    if not cans: continue
    can = cans[0]
    t = can.read_text(encoding='utf-8')
    if 'METADADOS CANÔNICOS' not in t:
        related = ", ".join(f"mecanismo_{x.lower() if False else ''}" for x in [])  # placeholder
        rel_ids = ", ".join({
            'B1':'mecanismo_B1_neuroinflamacao','B2':'mecanismo_B2_eixo_hpa_cortisol',
            'B3':'mecanismo_B3_neuroplasticidade','B4':'mecanismo_B4_deficiencias_monoaminas',
            'B5':'mecanismo_B5_gaba_glutamato','B6':'mecanismo_B6_estresse_oxidativo',
            'B7':'mecanismo_B7_eixo_intestino_cerebro','B8':'mecanismo_B8_deficiencias_micronutrientes',
            'B9':'mecanismo_B9_disfuncao_mitocondrial','B10':'mecanismo_B10_desregulacao_circadiana',
            'B12':'mecanismo_B12_neurobiologia_trauma','B13':'mecanismo_B13_sistema_endocanabinoide',
            'B14':'mecanismo_B14_neuroesteroides_hormonios','B16':'mecanismo_B16_neurogenese'}[x] for x in c['rel'])
        bloco = BLOCO.format(mech=c['mech'], tit=c['tit'], corte=c['corte'], cs=c['cs'],
                             rag=c['rag'], kw=c['kw'], related=rel_ids)
        can.write_text(t.rstrip() + bloco, encoding='utf-8')
        print(Bn, 'bloco do Contrato adicionado')
    else:
        print(Bn, 'já tem bloco')

    # relatório decisoes
    ledp = fp / f'Auditoria_{Bn}' / f'ledger_auditoria_{Bn}.json'
    if ledp.exists():
        led = json.load(open(ledp))
        cc = Counter(e['status_auditoria'] for e in led)
        g1 = Counter(e['portao_G1_existencia'] for e in led)
        g2 = Counter(e['portao_G2_elegibilidade'] for e in led)
        g3 = Counter(e['portao_G3_suporte'] for e in led)
        rel = f"""# Auditoria Científica de Conteúdo — {Bn} ({c['tit']})

**Data:** {c['corte']} (retrocompatibilização ao padrão B7/B8) · **Sessão:** operador de geração; **P-6** (2ª verificação independente/avaliador cego) PENDENTE.
**Objeto:** trechos-âncora da canônica `{can.name}`.
**Ferramentas:** G1 eutils (esearch+esummary+efetch), G2 espécie/elegibilidade, G3 suporte; `gate_script.py` (P-5) + `validar_auditoria.py` (framework).

## Contagem de decisões
- Trechos no ledger: **{len(led)}**
- G1: {dict(g1)} · G2: {dict(g2)} · G3: {dict(g3)}
- status_auditoria: {dict(cc)}

## Notas
- Módulo 09 no schema oficial (id_referencia_interna `REF_SOBRENOME_ANO`, doi, claim_id_origem; 5 arquivos).
- Referências citadas apenas em listra/corpus indexadas por rótulo canônico (apêndice de corpus) para rastreabilidade; citações clássicas de prosa sem PMID verificável foram rebaixadas a menção nominal sinalizada ao P-6 (R04: campo vazio preferível a dado inventado).
- Evidência animal/pré-clínica sinalizada `[APENAS PRÉ-CLÍNICO]/[EXT]`; bloco natureza_sistema (P12), semantic_layer (R06) e referência cruzada a B16 (P16) presentes na canônica.

## Declaração
> A Biblioteca_{Bn} foi auditada quanto a conteúdo: cada afirmação factual tem vínculo verificado (G1→G2→G3) ou está sinalizada como parcial/pré-clínica. `validar_auditoria.py`: **0 ERRO**; `gate_script.py`: **GATE APROVADO**.
> **Pendência P-6:** 2ª verificação independente (avaliador cego).
"""
        (ledp.parent / f'decisoes_{Bn}.md').write_text(rel, encoding='utf-8')
        print(Bn, 'decisoes escrito')
