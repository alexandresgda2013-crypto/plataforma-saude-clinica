#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 22_v7_parecer_rodada3_2026-09-13.py
# Aplica a V7 sobre a V6 final (sha e11dbd95): C4 no algoritmo · AUD-066 · AUD-067 · L717 ·
# apêndice Mehta + duplicata · REGISTRO item 11. Tudo com asserts + contadores impressos.
# Liturgia: backup bit-a-bit ANTES; sha novo DEPOIS registrado no manifesto.
import json, hashlib, shutil

AT = "/home/user/BIBLIOTECAS/B01_Neuroinflamacao/atuais/"
CAN6 = AT + "B1 NEUROINFLAMAÇÃO V6 CANONICA.md"
CAN7 = AT + "B1 NEUROINFLAMAÇÃO V7 CANONICA.md"
log = {"data": "2026-09-13", "trilha": 22, "edicoes": [], "contadores": {}}

def ed(t, a, b, nome, n=1):
    c = t.count(a)
    assert c == n, f"{nome}: esperado {n}, achado {c} :: {a[:90]!r}"
    log["edicoes"].append({"id": nome, "ocorrencias": n})
    return t.replace(a, b)

t = open(CAN6, encoding="utf-8").read()
sha6 = hashlib.sha256(t.encode()).hexdigest()
assert sha6 == "e11dbd959c59d191df18bccb5f73d8e11dbff29322b59172789ebab73ddcba24", sha6
shutil.copy(CAN6, AT + "antigos/historico/v6_canonica_final_sha_e11dbd95_2026-09-13.md")
log["backup_v6"] = "antigos/historico/v6_canonica_final_sha_e11dbd95_2026-09-13.md"

# --- E1 H1
t = ed(t, "# B1 NEUROINFLAMAÇÃO V6 CANÔNICA", "# B1 NEUROINFLAMAÇÃO V7 CANÔNICA", "E1-H1")

# --- E2 rótulo L5: abre camada V7 e fecha-a antes de "(fonte única"
a = "**artefato_rotulo:** CANÔNICA V6 (rev. principal datada 2026-09-13 sobre a V5 — continuidade da re-auditoria do Auditor-Mestre (errata E-01…E-05 + parecer de continuidade):"
b = ("**artefato_rotulo:** CANÔNICA V7 (rev. principal datada 2026-09-13 sobre a V6 final [sha e11dbd95; H1 corrigido no mesmo dia] "
     "— parecer rodada 3 do Auditor-Mestre: **C4 decidida no algoritmo** (Critério C deixa de ser condição de linha e vira "
     "modificador de a priori/especificidade — regra executável anti falso-positivo e falso-negativo demonstrados por ele), "
     "**AUD-066** (condição do PROVISÓRIO amarrada a artefato único: fila operacional 108 vínculos/91 refs, linhagem 59→108→39→~58 "
     "declarada), **AUD-067** (REF_MEHTA_2020b confirmada REVISÃO SISTEMÁTICA por eutils — sem Meta-Analysis; ficha movida 02→01_pmids, "
     "ledger e tokens corrigidos, duplicata de token removida do apêndice), L717-FKBP → (Mehta et al., 2020b) por eliminação de desenho, "
     "**§3-taxonomia replicada** (trilha 21: autodivergentes 7/7 exatas; apêndice×balde 21,5% × 21,3% dele; correção material no pacote "
     "L-05/1.2) · trilhas 21–22 · **linhagem:** V6 (rev. datada 2026-09-13 sobre a V5 — continuidade da re-auditoria do Auditor-Mestre "
     "(errata E-01…E-05 + parecer de continuidade):")
t = ed(t, a, b, "E2-rotulo-abre")
a = "(fonte única do mecanismo B1; o motor/RAG lê somente este arquivo + `/Evidencias/`)."
b = ("· versão imediatamente anterior (V6 final, sha e11dbd95) preservada bit a bit em "
     "`antigos/historico/v6_canonica_final_sha_e11dbd95_2026-09-13.md`) (fonte única do mecanismo B1; o motor/RAG lê somente este arquivo + `/Evidencias/`).")
t = ed(t, a, b, "E2-rotulo-fecha")

# --- E3 cabeçalho AUD-066
a = ("canônica condicionada ao fechamento da revisão cega humana dos 59 vínculos de alto risco declarados pelo pipeline "
     "(declaração obrigatória — R9–R10 da auditoria integral 2026-09-11;")
b = ("canônica condicionada ao fechamento da revisão cega humana da **fila operacional "
     "`FILA_REVISAO_CEGA_ALTO_RISCO_B1_2026-09-12.json` (108 vínculos / 91 referências)** — número único amarrado a artefato desde "
     "2026-09-13 (AUD-066; linhagem declarada: '59' = universo nominal não-preservado da R9–R10/2026-09-11; 39 = subconjunto de claims "
     "de ALTO RISCO sem 2ª verificação contado pelo gate P-5 a cada rodada; '~58' da carta nº 2 = aproximação do 59 nominal) "
     "(declaração original obrigatória — R9–R10 da auditoria integral 2026-09-11;")
t = ed(t, a, b, "E3-cabecalho-59108")

# --- E4a Critério C: título e regra executável
a = "#### Critério C — contexto clínico que eleva a probabilidade do mecanismo\n\nFatores presentes/ausentes, cada um com base mecanística já descrita:"
b = ("#### Critério C — contexto clínico: modificador de a priori e de especificidade (**não** critério de confirmação)\n\n"
     "> **Operacionalização (decisão C4, trilha 22, 2026-09-13, sob delegação científica do operador — a conferir pela equipe humana no P-6):** "
     "os fatores abaixo **não pontuam** para nenhuma classe e **não confirmam** o Critério A. Atuam em dois sentidos, e só neles: "
     "(i) **elevam o a priori de investigação** — justificam coletar o painel do Critério A antes de fechar 'indeterminada'; "
     "(ii) **reduzem a especificidade de A** quando o contexto explica o marcador por si: se o Critério A foi satisfeito **apenas** por "
     "marcadores sistêmicos inespecíficos (`exame_pcr_us`, `exame_il6`, `exame_tnfalpha`/sTNFR2, `exame_il1beta`) **sem nenhum marcador "
     "de via alterado (`exame_razao_kyn_trp`)** e ≥1 fator de C está presente, a classificação 'alta' **rebaixa para 'indeterminada'** — "
     "obesidade, doença autoimune, privação de sono e trauma elevam esses mesmos marcadores fora da depressão. Com KYN/TRP alterado no "
     "painel o modificador **não** rebaixa (a via sugere componente central), mas também **não valida** — as métricas do instrumento "
     "seguem desconhecidas (ressalva do topo).\n\nFatores presentes/ausentes, cada um com base mecanística já descrita:")
t = ed(t, a, b, "E4a-criterioC")

# --- E4b nota de circularidade: acréscimo da correção operacional
a = "\"Compatibilidade alta\" apoiada no Critério C reflete inflamação sistêmica esperável nesses contextos, não evidência de centralidade causal de B1 no quadro individual: **C modula o a priori; a carga classificatória pertence a A (biomarcador) e B (fenótipo).**"
b = a + " **Correção operacional aplicada (V7, trilha 22):** C saiu da condição de linha da tabela e virou modificador — a declaração e o algoritmo agora dizem a mesma coisa (o parecer de rodada 3 demonstrou o falso-positivo — obesidade+apneia — e o falso-negativo — inflamação sem causa sistêmica aparente barrada de 'alta' — produzidos pela versão V5/V6)."
t = ed(t, a, b, "E4b-circularidade")

# --- E4c tabela de classificação
a = ("| Classificação | Critério A (biomarcadores) | Critério B (fenótipo, mínimo) | Critério C (contexto) | Interpretação |\n"
     "|---|---|---|---|---|\n"
     "| **Compatibilidade alta** com mecanismo inflamatório | ≥2 marcadores de A alterados | ≥3 de 6 itens | ≥1 presente | O quadro é **compatível** com leitura mecanística B1 (hipótese não validada — ver ressalva do topo e nota de circularidade do Critério C); integrar aos demais Bx |\n"
     "| **Compatibilidade indeterminada** | 1 marcador alterado **ou** exame indisponível | 2 itens | variável | Dados insuficientes; considerar coleta do painel (C-LAB) antes de fechar |\n"
     "| **Compatibilidade baixa** | nenhum marcador alterado | ≤1 item | ausente | B1 pouco provável como eixo central; ponderar outros mecanismos B2–B16 |")
b = ("| Classificação | Critério A (biomarcadores) | Critério B (fenótipo, mínimo) | Papel do Critério C (**modificador — nunca condição**) | Interpretação |\n"
     "|---|---|---|---|---|\n"
     "| **Compatibilidade alta** com mecanismo inflamatório | ≥2 marcadores de A alterados | ≥3 de 6 itens | **Regra de rebaixamento (V7):** se A foi satisfeito **apenas** por marcadores sistêmicos inespecíficos (PCR-us, IL-6, TNF-α/sTNFR2, IL-1β — **sem** KYN/TRP alterado) **e** ≥1 fator de C está presente → rebaixa para **indeterminada**; C ausente não barra, C presente não eleva | O quadro é **compatível** com a leitura mecanística B1 como **hipótese a confirmar** (instrumento não validado — ver ressalva do topo); integrar aos demais Bx |\n"
     "| **Compatibilidade indeterminada** | 1 marcador alterado **ou** exame indisponível **ou** 'alta' rebaixada pelo modificador C | 2 itens | C atua como **a priori**: justifica coletar o painel (C-LAB) antes de fechar | Dados insuficientes para a leitura B1; investigar antes de descartar |\n"
     "| **Compatibilidade baixa** | nenhum marcador alterado | ≤1 item | C **não eleva** esta classe em nenhuma hipótese | B1 pouco provável como eixo central; ponderar outros mecanismos B2–B16 |")
t = ed(t, a, b, "E4c-tabela")

# --- E5 perfil 12.1
a = "tende a **Compatibilidade alta** no BLOCO_11.4 (Critério A com ≥2 marcadores, Critério B com itens atípicos/fadiga, Critério C com contexto metabólico presente)."
b = ("tende a **Compatibilidade alta** no BLOCO_11.4 (Critério A com ≥2 marcadores **incluindo marcador de via** (KYN/TRP), "
     "Critério B com itens atípicos/fadiga) — **ressalva do modificador C (V7):** se o painel ficar restrito a marcadores sistêmicos "
     "inespecíficos (PCR/IL-6/TNF), o contexto metabólico presente **rebaixa para indeterminada**; é exatamente o confundimento que a regra C4 pune.")
t = ed(t, a, b, "E5-perfil121")

# --- E6 perfil 12.3
a = "**Raciocínio de estratificação:** **Compatibilidade alta** quando o Critério C (histórico de trauma) está presente, mesmo com Critério A parcial — reflete a natureza latente/reativa deste subtipo, distinta dos dois anteriores."
b = ("**Raciocínio de estratificação:** com o esquema V7 (decisão C4), o trauma presente **não eleva** a classe: com Critério A parcial a "
     "leitura fica **Compatibilidade indeterminada** — e é justamente onde o modificador C atua como a priori: a leitura sugere **coletar "
     "o painel completo (C-LAB) antes de fechar**, porque o subtipo é latente/reativo (biomarcadores desproporcionais à gravidade do "
     "estressor atual, não necessariamente basais altos), distinto dos dois anteriores.")
t = ed(t, a, b, "E6-perfil123")

# --- E7 perfil 12.4
a = "No BLOCO_11.4 este perfil tende a **Compatibilidade indeterminada/baixa** pelo Critério A, embora o Critério B/C (hipervigilância, trauma) esteja presente; sinaliza a necessidade de integrar B2 (HPA/TEPT) e B12 (trauma)."
b = ("No BLOCO_11.4 este perfil tende a **Compatibilidade indeterminada/baixa** pelo Critério A — e o contexto C (trauma) presente "
     "**não eleva** a classe por construção (regra C4/V7); sinaliza a necessidade de integrar B2 (HPA/TEPT) e B12 (trauma).")
t = ed(t, a, b, "E7-perfil124")

# --- E8 L717 → 2020b (eliminação de desenho; nota e confissão no REGISTRO item 11)
a = "Biologia de FKBP e sinalização inflamatória é revista (Mehta et al., 2020)[OB; revisão]."
b = "Biologia de FKBP e sinalização inflamatória é revista (Mehta et al., 2020b)[OB; revisão]."
t = ed(t, a, b, "E8-L717")

# --- E9 apêndice linha DONATO: classificadores Mehta contra a própria ficha
a = "WILLIS_2020[ML] | MEHTA_2020[OB] | MEHTA_2020b[MA] | CHUKAEW_2021[MA]"
b = "WILLIS_2020[ML] | MEHTA_2020[EC] | MEHTA_2020b[OB] | CHUKAEW_2021[MA]"
t = ed(t, a, b, "E9-apendice-tokens")

# --- E10 apêndice: remover duplicata do token MEHTA_2020b[MA] que abria linha própria
linhas = t.split("\n")
dup = [i for i, L in enumerate(linhas) if L.startswith("*MEHTA_2020b[MA] | CHENG_2021")]
assert len(dup) == 1, dup
i = dup[0]
linha_antiga = linhas[i]
linha_nova = linha_antiga.replace("*MEHTA_2020b[MA] | CHENG_2021", "*CHENG_2021", 1)
linhas[i] = linha_nova
t = "\n".join(linhas)
log["edicoes"].append({"id": "E10-apendice-duplicata", "ocorrencias": 1})
# fora do REGISTRO (append-only: o item 10 narra o token antigo — histórico não se reescreve)
i_reg = t.find("**REGISTRO DE AUDITORIA")
corpo, reg = (t[:i_reg], t[i_reg:]) if i_reg > 0 else (t, "")
assert corpo.count("MEHTA_2020b[MA]") == 0, "token antigo MEHTA_2020b[MA] fora do REGISTRO"
assert corpo.count("MEHTA_2020b[OB]") == 1 and corpo.count("MEHTA_2020[EC]") == 1
assert corpo.count("MEHTA_2020[OB]") == 0, "token antigo MEHTA_2020[OB] fora do REGISTRO"

# --- E11 REGISTRO item 11 (append ao fim do arquivo, que termina no item 10)
reg11 = """

11. **V7 (2026-09-13, Rodada 7 — parecer rodada 3 do Auditor-Mestre; decisões da casa sob delegação científica do operador; P-6 confere no fim):**
    - **Réplica antes de aceitar (trilha 21):** §3-taxonomia medida dos dois lados — autodivergentes na prosa **7/7 exatas e as mesmas** (Bull 2009, Chen 2024, Huang 2023, Mehta 2020, Yang 2024, Yehuda 2016, Zhang 2025); concordância prosa×balde 39,6% (dele 37,1%); apêndice×balde **21,5% (dele 21,3%)**; refs divergentes prosa×apêndice 84 (dele 71 — mesmo defeito, universos de parser declarados). Achado §3 **confirmado**: três taxonomias de classificador sem autoridade única.
    - **Declaração normativa da casa sobre o [XX]:** a semântica vigente de fato é ambígua (a prosa às vezes registra desenho, às vezes papel da evidência no claim, sem declaração de qual) — confessa. A correção material das demais autodivergentes e das ~84 divergentes NÃO é arbitrada aqui sem fonte primária: entra no **pacote L-05 item 1.2 (taxonomia única de desenho/força)** com o portão **V-15 aceito** (classificador idêntico em prosa, apêndice, ficha e ledger — divergência = ERRO).
    - **C4/AUD-052 decidida NO ALGORITMO:** Critério C sai de condição de linha e vira **modificador de a priori/especificidade** (a alternativa 'b' do parecer, formalizada pela casa: A satisfeito APENAS por marcadores sistêmicos inespecíficos + KYN/TRP não alterado + C presente ⇒ rebaixa alta→indeterminada; C ausente não barra; C presente não eleva). Fundamento: confundidor reduz especificidade, não aumenta sensibilidade — a circularidade declarada na V6 deixa de ser só declaração e passa a ser comportamento. Perfis §12.1/12.3/12.4 harmonizados (o §12.3 dizia 'alta mesmo com A parcial' — corrigido para indeterminada + coleta de painel). Caso-armadilha do Bloco 4 do parecer (obesidade+apneia sem depressão inflamatória) passa a NÃO classificar 'alta'. Instrumento continua NÃO VALIDADO (ressalva do topo intacta).
    - **AUD-066:** condição do PROVISÓRIO amarrada a UM número derivado de artefato: a fila operacional `producao/LOTE_REAUDITORIA_V5_2026-09-12/FILA_REVISAO_CEGA_ALTO_RISCO_B1_2026-09-12.json` (**108 vínculos / 91 refs**); linhagem dos quatro números declarada no cabeçalho.
    - **AUD-067 (Mehta) — inequívoco por eutils, com confissão:** eutils 2026-09-13 (PMID 31951051) pubtype = Journal Article + **Systematic Review, SEM Meta-Analysis** ("A Systematic Review of DNA Methylation and Gene Expression Studies in PTSD, PTG and Resilience", J Trauma Stress 2020 Apr;33(2):171-180, doi 10.1002/jts.22472). A casa propagou [MA] na rodada 2 — confessa e corrige: ficha movida 02_meta_analises→01_pmids; ledger AUD_B1_0151 MA→OB; apêndice MEHTA_2020[OB]→[EC] (a ficha é EC humano fMRI) e MEHTA_2020b[MA]→[OB]; **duplicata de token MEHTA_2020b[MA] removida do apêndice** (âncoras de ledger propagadas). REF_MEHTA_2020b deixa de contar como meta-análise: manifesto 34→33 MAs (refs totais e PMIDs seguem 237).
    - **L717-FKBP decidida por eliminação de desenho:** a prosa pede REVISÃO Mehta 2020 sobre FKBP/biologia inflamatória; das duas fichas Mehta 2020 do acervo, REF_MEHTA_2020 é EC experimental (materialmente impossível) e REF_MEHTA_2020b é a única revisão (escopo HPA/metilação/inflamação — FKBP5 ⊂ HPA). Token corrigido para (Mehta et al., 2020b). **Confissão da margem:** FKBP5 não aparece nominalmente no abstract da RS — a identificação é por desenho↔pedido↔escopo, não por trecho literal; a formalização do vínculo N2 fica para o ciclo P-6 (a casa não fabrica vínculo). Autodivergência Mehta 2020 [EC]/[OB] ZERA com esta correção (fica [EC] único na reward).
    - **Versionamento:** conteúdo científico alterado (algoritmo 11.4) ⇒ **V6 → V7**; V6 final (sha e11dbd95) preservada bit a bit em `antigos/historico/v6_canonica_final_sha_e11dbd95_2026-09-13.md`; portões oficiais re-rodados sobre esta V7.
"""
t = t.rstrip() + reg11

open(CAN6, "w", encoding="utf-8").write(t)
sha7 = hashlib.sha256(t.encode()).hexdigest()
log["sha256_v7"] = sha7

# ---------- PARTE B: JSONs ----------
# B1) mover ficha REF_MEHTA_2020b 02→01
p02 = AT + "Evidencias/Bibliografia/02_meta_analises.json"
p01 = AT + "Evidencias/Bibliografia/01_pmids.json"
M2 = json.load(open(p02, encoding="utf-8"))
M2 = M2 if isinstance(M2, list) else M2.get("referencias", M2)
n0 = len(M2)
ficha = [r for r in M2 if r["id_referencia_interna"] == "REF_MEHTA_2020b"]
assert len(ficha) == 1
ficha = ficha[0]
M2 = [r for r in M2 if r["id_referencia_interna"] != "REF_MEHTA_2020b"]
assert len(M2) == n0 - 1 == 33
ficha["balde_corrigido_em"] = "2026-09-13 (AUD-067/trilha 22): eutils 2026-09-13 pubtype = Journal Article + Systematic Review, SEM Meta-Analysis (abstract colado na trilha); balde 02_meta_analises era resíduo do sinal de título da geração"
ficha["nota_correcao_taxonomia"] = "2026-09-13: classificador de desenho = OB (revisão sistemática); NÃO é MA. Propagado a ledger (AUD_B1_0151) e tokens do apêndice na V7."
M1 = json.load(open(p01, encoding="utf-8"))
M1 = M1 if isinstance(M1, list) else M1.get("referencias", M1)
assert not any(r["id_referencia_interna"] == "REF_MEHTA_2020b" for r in M1)
M1.append(ficha)
json.dump(M2, open(p02, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
json.dump(M1, open(p01, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
log["contadores"]["mover_ficha"] = {"02": [n0, len(M2)], "01": [len(M1) - 1, len(M1)]}

# B2) manifesto
pm = AT + "Evidencias/Bibliografia/_manifesto_biblioteca.json"
m = json.load(open(pm, encoding="utf-8"))
assert m["meta_analises_total"] == 34
m["meta_analises_total"] = 33
m["versao"] = "2.8"
m["sha256_canonica_vigente"] = sha7
m["sha256_registrado_em"] = "2026-09-13"
m.setdefault("historico_sha_v6", []).append({
    "sha256": "e11dbd959c59d191df18bccb5f73d8e11dbff29322b59172789ebab73ddcba24",
    "vigente_ate": "2026-09-13 (mesmo dia — V6 final encerrada pela V7 da rodada 3)",
    "motivo": "parecer rodada 3: C4 no algoritmo + AUD-066 + AUD-067 + §3 replicada (trilhas 21–22); V6 final preservada bit a bit em antigos/historico/",
})
m.setdefault("alteracoes", []).append("2026-09-13 trilha 22 (V7): REF_MEHTA_2020b movida 02→01_pmids (eutils: RS sem MA); meta_analises_total 34→33; C4 algoritmo (C modificador); AUD-066 cabeçalho")
json.dump(m, open(pm, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

# B3) ledger: AUD_B1_0151 + propagação de âncoras das linhas-lote editadas
pl = AT + "Auditoria_B1/ledger_auditoria_B1.json"
L = json.load(open(pl, encoding="utf-8"))
n151 = 0
for e in L:
    if e.get("id_auditoria") == "AUD_B1_0151":
        assert e["tipo_classificador"] == "MA"
        e["tipo_classificador"] = "OB"
        e["arquivo_modulo09"] = "Evidencias/Bibliografia/01_pmids.json"
        e["nota_auditoria"] = e.get("nota_auditoria", "") + " | 2026-09-13 AUD-067/trilha 22: eutils 2026-09-13 confirma REVISÃO SISTEMÁTICA sem meta-análise (doi 10.1002/jts.22472, pubtypes colados na trilha); tipo MA→OB; ficha 02→01_pmids; token apêndice [MA]→[OB]."
        n151 += 1
assert n151 == 1
subs_ancora = [
    (linha_antiga, linha_nova),                     # E10 linha duplicata inteira
    ("MEHTA_2020[OB] | MEHTA_2020b[MA]", "MEHTA_2020[EC] | MEHTA_2020b[OB]"),  # E9 dentro da linha DONATO
    ("Âncora de meta-análise fixada por decisão científica (é a MA de metilação mais diretamente em TEPT)",
     "Âncora de revisão sistemática fixada por decisão científica (é a RS de metilação mais diretamente em TEPT — AUD-067 2026-09-13: NÃO é MA)"),
    ("L717 \\\"(Mehta et al., 2020)\\\" (FKBP) permanece sem ficha inequívoca — fila P-6 humana.",
     "L717 resolvida por eliminação de desenho na V7 (trilha 22): token→(Mehta et al., 2020b); vínculo N2 formal a criar no P-6."),
]
nprop = 0
for e in L:
    ver = e.get("verificacao", {})
    for campo in ("trecho_fonte", "abstract_ou_trecho"):
        if campo in ver and isinstance(ver[campo], str):
            x = ver[campo]
            for a, b in subs_ancora:
                x = x.replace(a, b)
            if x != ver[campo]:
                ver[campo] = x
                nprop += 1
    for campo in ("trecho_ancora", "citacao_literal"):
        if campo in e and isinstance(e[campo], str):
            x = e[campo]
            for a, b in subs_ancora:
                x = x.replace(a, b)
            if x != e[campo]:
                e[campo] = x
                nprop += 1
json.dump(L, open(pl, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
log["contadores"]["ledger_propagados"] = nprop

# B4) vínculos: nota propagada ao 0266 (RS, não MA)
pv = AT + "Evidencias/Vinculos/vinculos_referencia_afirmacao.json"
V = json.load(open(pv, encoding="utf-8"))
nv = 0
for v in V:
    if v["id_vinculo"] == "VINC_B1_0266":
        v["g3_notas"] = v.get("g3_notas", "") + " | 2026-09-13 AUD-067: REF_MEHTA_2020b é REVISÃO SISTEMÁTICA (eutils), não MA; texto da âncora §2.21 permanece literal (já dizia OB/revisão sistemática)."
        nv += 1
    for campo in ("trecho_ancora",):
        if isinstance(v.get(campo), str):
            x = v[campo]
            for a, b in subs_ancora:
                x = x.replace(a, b)
            if x != v[campo]:
                v[campo] = x
                nv += 1
json.dump(V, open(pv, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
log["contadores"]["vinculos_tocados"] = nv

# B5) renomear arquivo para V7
import os
os.rename(CAN6, CAN7)
log["canonica_v7"] = CAN7

json.dump(log, open(AT + "producao/22_v7_parecer_rodada3_2026-09-13.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("V7 gravada:", CAN7)
print("sha V7:", sha7)
print("contadores:", json.dumps(log["contadores"], ensure_ascii=False))
print("edições:", [e["id"] for e in log["edicoes"]])
