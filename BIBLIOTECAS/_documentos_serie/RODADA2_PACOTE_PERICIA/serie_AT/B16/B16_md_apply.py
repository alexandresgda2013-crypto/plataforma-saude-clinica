#!/usr/bin/env python3
# B16 — rodada [AT 2026-09-09]: V1 -> V2 (ENTRA 2: Doludda 2026, Zhou 2025) + registro de auditoria
import re, shutil, os, datetime

BASE = "/home/user/BIBLIOTECAS/B16_Neurogenese"
V1 = os.path.join(BASE, "B16 NEUROGENESE V1 CANONICA.md")
V2 = os.path.join(BASE, "B16 NEUROGENESE V2 CANONICA.md")
HIST = os.path.join(BASE, "producao", "historico")
os.makedirs(HIST, exist_ok=True)

md = open(V1, encoding="utf-8").read()

def rep(old, new, n=1):
    global md
    c = md.count(old)
    assert c == n, f"âncora não única ({c}): {old[:70]!r}"
    md = md.replace(old, new)

# --- 1. título + cabeçalho V2
rep("HIPOCAMPAL ADULTA V1 CANÔNICA", "HIPOCAMPAL ADULTA V2 CANÔNICA")
rep("ADULTA V2 CANÔNICA\n## Biblioteca",
    "ADULTA V2 CANÔNICA\n*(v2 — rodada de auditoria [AT 2026-09-09]: reconferência ref a ref de todos os insumos; +2 âncoras fundidas — consenso Doludda 2026 e resiliência pós-parto Zhou 2025; 4 identificadores falsos expostos; 1 off-scope oficial ratificado; 290 âncoras G1 eutils)*\n## Biblioteca")

# --- 2. §1.2: consenso Doludda 2026 (prosa + listra)
rep("âncoras humanas de 2025–2026 vêm atualizar sem abolir a cautela.",
    "âncoras humanas de 2025–2026 vêm atualizar sem abolir a cautela. Em 2026, o **consenso dos\n"
    "líderes do campo** (Doludda 2026)[OB] — desdobramento direto do consenso de Kempermann (2018),\n"
    "com Frisén, Gage, Jessberger, Lucassen, Salta, Song, Thuret, Toda e Kempermann entre os\n"
    "signatários — enquadra a neurogênese adulta como processo **estabelecido** na função\n"
    "hipocampal em saúde e doença, declara explicitamente abertas as perguntas de fronteira\n"
    "(identidade das células-tronco e seus aferentes, natureza do nicho, neurogênese sem atividade\n"
    "de célula-tronco, função além do hipocampo, teoria evolutiva e computacional) e registra\n"
    "dezenas de ensaios clínicos rotulados com a palavra-chave \"neurogênese adulta\" — lidos aqui\n"
    "como **sinal de interesse translacional, não validação de alvo**.")
rep("| SCHOENFELD_2015[OB]*", "| SCHOENFELD_2015[OB] | DOLUDDA_2026[OB]*")

# --- 3. §11.2: Zhou 2025 pós-parto (prosa + listra)
rep("(Xie 2025)[ML] [APENAS PRÉ-CLÍNICO].",
    "(Xie 2025)[ML] [APENAS PRÉ-CLÍNICO]. Na **mãe lactante**, a separação breve dos filhotes\n"
    "funciona como fator de **resiliência** ao estresse crônico por contenção — menor\n"
    "ansiedade/depressão-símile, cognição preservada, neurogênese aumentada e menor ativação\n"
    "microglial do eixo NLRP3–IL-1β/IL-18 — e a modulação viral da linhagem mostra que o\n"
    "**comportamento cognitivo mediado pelos neurônios novos participa** dessa resiliência\n"
    "pós-parto, reforçada ainda pela inibição hipocampal de NLRP3 (Zhou 2025)[ML] [APENAS\n"
    "PRÉ-CLÍNICO].")
rep("| BORSINI_2023[OB] | JIN_2016[ML]*", "| BORSINI_2023[OB] | JIN_2016[ML] | ZHOU_2025[ML]*")

# --- 4. CONTROVÉRSIAS (1) e (8) + contagens
rep('comentário "controvérsia consertada" (Lima 2019) lido com ceticismo).',
    'comentário "controvérsia consertada" (Lima 2019) lido com ceticismo; o consenso dos líderes do\n'
    "campo (Doludda 2026) enquadra a neurogênese adulta como processo funcional estabelecido, com as\n"
    "perguntas de fronteira declaradamente abertas).")
rep("(Sah 2012; Xie 2025).", "(Sah 2012; Xie 2025; Zhou 2025 — lacuna de pós-parto parcialmente\n"
    "ancorada na rodada [AT 2026-09-09], evidência ainda exclusivamente pré-clínica).")
rep("288 PMIDs das tabelas do Briefing validados no PubMed; 2",
    "290 PMIDs validados no PubMed (288 das tabelas do\nBriefing + 2 fundidos na rodada de auditoria [AT 2026-09-09]: Doludda 2026 e Zhou 2025); 2")
rep("6 itens não-fundidos (anais/congresso/off-scope)\nregistrados; zero PMID no texto.",
    "6 itens não-fundidos (anais/congresso/off-scope)\nregistrados; 4 identificadores falsos expostos e não fundidos (registro de auditoria abaixo);\nzero PMID no texto.")

# --- 5. REGISTRO DE AUDITORIA [AT] antes de ELEMENTOS MOLECULARES
REG = """## REGISTRO DE AUDITORIA [AT 2026-09-09] — RECONFERÊNCIA REF A REF DOS INSUMOS (ENTRA 2)

**Escopo da rodada.** Reconferência ref a ref de todos os insumos externos contra a canônica
vigente: GPM (298 âncoras validadas, 289 citadas nos blocos A–N), briefing RODADA0 (283
identificadores), briefing consolidado (14 confirmados), matriz de triagem externa em 17 seções,
anexo bibliográfico por DOI e sínteses cruzadas. Regra permanente: auditar antes de fundir;
nenhum identificador entra sem G1 (eutils) + leitura integral de abstract.

**ENTRA 2 — a auditoria detectou falha silenciosa da fusão da rodada 0:** duas obras reais,
demandadas tanto pelo anexo bibliográfico quanto pela matriz externa (Tier 1 e Tier 2), não haviam
sido carregadas e resolveram normalmente no PubMed por DOI — fundidas após G1 + abstract lido: o
**consenso de 2026 dos líderes do campo** (Doludda 2026, *Cell Stem Cell*) e a **resiliência
pós-parto mediada por neurogênese** (Zhou 2025, *Molecular Psychiatry*), esta ancorando a lacuna
declarada de pós-parto/sexo (evidência ainda pré-clínica).

**Expostos e NÃO fundidos — 4 identificadores falsos:** (i) dois fragmentos de DOI lidos por
extração numérica como se fossem PMID — pertencem a Palmer (2000; nicho vascular; obra real mantida
como contexto fora da canônica) e a Fares (2018; revisão com cobertura equivalente, excluída com
razão registrada na rodada 0); (ii) dois identificadores da matriz externa (atribuídos a \"Allen
2025\" e a \"Zhou 2024\") que **não resolvem** no PubMed — exposição registrada, sem fundição e sem
[G1] elegível.

**Ratificações:** Siopi 2016 (*J Neurosci*; bulbo olfatório/ZSV) mantido fora por **decisão
explícita do próprio insumo** (escopo ZSG/giro denteado) e registrado no manifesto; duplicata
consecutiva do anexo (Jones–Zhou–Jhaveri 2022) colapsada na ocorrência única já vigente;
divergências de ano online×impresso resolvidas por DOI — mesma obra vigente, sem nova inserção
(Gage \"2024\" = Gage 2025; Zhang IL-4 \"2020\" = Zhang 2021 em *Science Advances*; Elliott \"2024\" =
Elliott 2025; Simard \"2023\" = pré-print bioRxiv do artigo de 2024). **Exclusões da matriz externa
ratificadas:** Zhang 2017 (modelo APP/PS1 — malha de exclusão/Alzheimer, contexto apenas), Nejad
2024 (morfina — fora do arco ansiedade/depressão), Li 2024 (plasticidade geral — domínio B3), \"W.
2025\" (revisão em periódico de baixa relevância, duplicidade conceitual com B15/B16), Yang 2025 e
Wang 2025 (anais não indexados — permanecem como nota, sem citação formal).

**P-6:** a 2ª verificação cega (Via 2) permanece PENDENTE para o fecho 16/16 da série e abrangerá
também as duas âncoras fundidas nesta rodada. Placar da canônica: 288 → **290 âncoras**.

"""
rep("## ELEMENTOS MOLECULARES CRÍTICOS (UniProt/HGNC)", REG + "## ELEMENTOS MOLECULARES CRÍTICOS (UniProt/HGNC)")

# --- 6. metadados: rag hint, corte, fecho
rep("/Spalding/Dumitru/Peng,", "/Spalding/Dumitru/Peng/Zhou/Doludda,")
rep("curva em U de plasticidade, ou volume hipocampal", "curva em U de plasticidade, resiliência pós-parto mediada por\n  neurogênese, consenso de 2026 da neurogênese adulta, ou volume hipocampal")
rep("— corte\n2026-09-07; 288/288 PMIDs das tabelas resolvem no PubMed.",
    "— corte\n2026-09-07; **rodada de auditoria [AT 2026-09-09]**: reconferência ref a ref de todos os\ninsumos (matriz externa, anexo por DOI, briefings consolidados) — **+2 âncoras fundidas**\n(Doludda 2026; Zhou 2025), 4 identificadores falsos expostos, 1 off-scope oficial ratificado,\nduplicata do anexo colapsada; **290/290 PMIDs resolvem no PubMed**.")
rep("*Fim da B16 CANÔNICA v1 — Neurogênese hipocampal adulta",
    "*Fim da B16 CANÔNICA v2 — Neurogênese hipocampal adulta")
rep("Referências: 288 âncoras (G1 eutils 288/288; ver Módulo 09).",
    "Referências: 290 âncoras (G1 eutils 290/290; ver Módulo 09 e Registro de Auditoria [AT 2026-09-09]).")

# --- asserts finais
assert not re.search(r"(?<!rs)\b\d{7,9}\b", md), "dígito longo na prosa!"
assert md.count("DOLUDDA_2026[OB]") == 1 and md.count("ZHOU_2025[ML]") == 1
assert "REGISTRO DE AUDITORIA [AT 2026-09-09]" in md

open(V2, "w", encoding="utf-8").write(md)
shutil.move(V1, os.path.join(HIST, "v1_canonica_2026-09-09.md"))
wc = len(md.split())
print("V2 gravada:", V2)
print("palavras:", wc, "| linhas:", md.count(chr(10))+1)
print("V1 arquivada em producao/historico/")
print("raiz .md restantes:", [f for f in os.listdir(BASE) if f.endswith('.md')])
