#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
from pathlib import Path
out = Path(__file__).resolve().parent / "ato2_pacote"
corpo = (out / "CHECKPOINT_02_BLOCO02_corpo.md").read_text(encoding="utf-8") if (out/"CHECKPOINT_02_BLOCO02_corpo.md").exists() else None
n1 = json.loads((out/"mod9_BLOCO02_N1_01_pmids.json").read_text(encoding="utf-8"))
n2 = json.loads((out/"mod9_BLOCO02_N2_vinculos.json").read_text(encoding="utf-8"))

# corpo embutido: se o arquivo _corpo foi removido, reconstruir do checkpoint atual
if corpo is None:
    atual = (out/"CHECKPOINT_02_BLOCO02.md").read_text(encoding="utf-8")
    corte = atual.find("# MÓDULO 9")
    corpo = atual[:corte].split("---",1)[0] if corte>0 else atual
    # remove cabecalho inicial do checkpoint (ate o primeiro '## BLOCO_02')
    i = corpo.find("## BLOCO_02")
    corpo = corpo[i:] if i>=0 else corpo

cab = ("# CHECKPOINT 2 — BLOCO_02 VIAS MOLECULARES (B1, Rodada 2)\n\n"
       "> 24 claims (BLOCO02.001-024) · GPM v3 Mod. 01-02 · corpus com abstracts reais.\n"
       "> Modulo 9 nativo (Prompt 4.2 atualizado): N1 = 01_pmids (schema 09.1), N2 = vinculos por frase (E3).\n"
       "> g1_metodo=eutils_automatico; g3_verificado_por vazio; g2=nao_avaliado; verification_status=pendente.\n"
       "> Nenhum PMID de memoria; todos do corpus/ancoras (busca por ferramenta).\n\n")

fim = f"""

---

# MODULO 9 (NATIVO) — BLOCO_02

## Nivel 1 — /Evidencias/Bibliografia/01_pmids.json ({len(n1)} referencias; schema 09.1 oficial)

Arquivo: `mod9_BLOCO02_N1_01_pmids.json`

```json
{json.dumps(n1, ensure_ascii=False, indent=1)}
```

## Nivel 2 — /Evidencias/Vinculos/vinculos_referencia_afirmacao.json ({len(n2)} vinculos; um por frase-ancora)

Arquivo: `mod9_BLOCO02_N2_vinculos.json`

```json
{json.dumps(n2, ensure_ascii=False, indent=1)}
```

## Inventario negativo / honestidade do lote
- **BLOCO02.006 (RLRs RIG-I/MDA5):** busca por ferramenta nao retornou literatura direta SNC/comportamental. Registrado `nao_estabelecido`/N-A parcial; so evidencia periferica (TBK1 humano, PMID 34363755). Nao forçado.
- **BLOCO02.012 (polimorfismos):** apenas IL-6/5-HTTLPR x IFN-alfa (Bull 2009, PMID 18458677) tem vinculo humano forte neste lote. IL1B, TNF -308, TLR4, NLRP3, CRP: heranca do GPM, sem PMID dedicado no top-10 — lote de genetica humana, nao inventado.
- **BLOCO02.022 (miR-155):** miR-146a (freio) tem artigo SNC forte (PMID 40349816); miR-155 (SOCS1) nao retornou artigo SNC-comportamental — `nao_estabelecido` no SNC comportamental.
- **BLOCO02.017 (PGE2/EP/CRH):** febre/COX-2 ancoradas; estimulo especifico de CRH hipotalamico por PGE2 fica como mecanismo de revisao de febre, sem vinculo de manipulacao dedicado.
- Meta-analises humanas de marcadores (Dowlati/Haapakoski/Osimo) e o RCT do infliximabe (Raison 2013) pertencem ao BLOCO05 em **02_meta_analises** (schema 09.2) e **03_ensaios_clinicos** (09.3), nao ao 01_pmids de vias.
"""

(out/"CHECKPOINT_02_BLOCO02.md").write_text(cab + corpo.strip() + fim, encoding="utf-8")
print("montado:", (out/"CHECKPOINT_02_BLOCO02.md").stat().st_size, "bytes | N1", len(n1), "| N2", len(n2))
