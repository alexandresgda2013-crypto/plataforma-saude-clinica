#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prepara o lote de auditoria G2->G3:
- planilha CSV (uma linha por vinculo N2) com especie pre-preenchida (MeSH),
  sugestao de G2 (NUNCA marca eligible sozinha) e colunas para o avaliador;
- JSONL com abstract anexado por vinculo para leitura do G3;
- foco de alto-risco separado (evidencia humana/MA/RCT)."""
import json, csv, re
from pathlib import Path
BASE=Path(__file__).resolve().parent
pac=BASE/"ato2_pacote"
abs_=json.loads((BASE/"corpus/abstracts_pubmed.json").read_text(encoding="utf-8"))
refs=json.loads((pac/"Evidencias/Bibliografia/01_pmids.json").read_text(encoding="utf-8"))
meta=json.loads((pac/"Evidencias/Bibliografia/02_meta_analises.json").read_text(encoding="utf-8"))
vinc=json.loads((pac/"Evidencias/Vinculos/vinculos_referencia_afirmacao.json").read_text(encoding="utf-8"))

# indice id_interno -> registro
by_id={}
for r in refs:
    for i in r["ids_referencia_interna"]: by_id[i]=r
for r in meta: by_id[r["id_referencia_interna"]]=r

def reg(v):
    return by_id.get(v["id_referencia_interna"], {})

def especie(v):
    r=reg(v); return r.get("especie_mesh",[])

def is_meta(r):
    return "meta" in str(r.get("desenho_estudo","")).lower() or r.get("forca_evidencia_afirmacao")

def sugestao_g2(v):
    """Sugestao da ferramenta. NUNCA devolve 'eligible' como veredito final:
    devolve sugestao + motivo; o avaliador decide."""
    r=reg(v); sp=especie(v); role=v.get("evid_role",""); uso=v.get("uso","")
    tem_humano="Humans" in sp
    tem_animal=any(x in sp for x in ("Mice","Rats","Animals","Cells, Cultured","Cattle","Dogs","Zebrafish"))
    desenho=str(r.get("desenho_estudo",""))
    # contaminacao: resposta a tratamento como achado principal num bloco de mecanismo
    if "tratamento" in (v.get("achado_central_molecular","")).lower() and v.get("secao_origem","").startswith("BLOCO_03"):
        return "excluido_contaminacao?", "possivel contaminacao por desfecho de tratamento em bloco mecanistico — confirmar"
    # RCT/meta humano: prova ou marcador clinico
    if is_meta(r):
        return "eligible? (avaliar trilha)", "meta-analise humana: suporta subtipo/marcador; ver se e afirmação mecanistica ou so associativa (pode ir a trilha clinica)"
    if "Randomized" in desenho or "RCT" in desenho:
        return "eligible? (prova humana)", "RCT/ensaio humano: evidencia de prova; confirmar desfecho e subgrupo"
    # so animal/celula
    if tem_animal and not tem_humano:
        return "eligible? (mecanistico)", f"evidencia animal/celula ({'/'.join(sp)}); valida para contexto mecanistico; G3 deve marcar preclinico/extrapolado"
    if tem_animal and tem_humano:
        return "eligible? (mecanistico+revisao)", "revisao/estudo humano+animal; verificar se o achado citado e animal ou humano"
    if tem_humano and role in ("human_clinical","human_experimental","post_mortem"):
        return "eligible? (humano)", "evidencia humana (observacional/pos-morte/experimental); verificar se ha confundidor"
    return "nao_avaliado", "revisar manualmente"

# ---------- JSONL com abstract anexado ----------
aud=BASE/"auditoria_G2G3"; aud.mkdir(exist_ok=True)
with open(aud/"pacotes_vinculos_G3.jsonl","w",encoding="utf-8") as f:
    for v in vinc:
        r=reg(v); pmid=v.get("pmid_oficial") or r.get("pmid_oficial")
        ab=abs_.get(pmid,{})
        sg,sm=sugestao_g2(v)
        f.write(json.dumps({
          "id_vinculo":v["id_vinculo"],"claim_id":v["claim_id"],"secao":v["secao_origem"],
          "id_referencia_interna":v["id_referencia_interna"],"pmid":pmid,"doi":r.get("doi",""),
          "titulo":r.get("titulo_artigo",ab.get("titulo","")),
          "revista_ano":r.get("revista_ano", f"{ab.get('revista','')} ({ab.get('ano','')})"),
          "especie_mesh":especie(v),"evid_role":v.get("evid_role",""),"uso":v.get("uso",""),
          "trecho_ancora":v["trecho_ancora"],"achado_central_molecular":v.get("achado_central_molecular",""),
          "natureza_relacao_gerada":v.get("natureza_relacao",""),"grau_maturidade_gerado":v.get("grau_maturidade",""),
          "extrapolacao_gerada":v.get("extrapolacao_por_analogia",""),
          "sugestao_g2_ferramenta":sg,"sugestao_motivo":sm,
          "abstract":ab.get("abstract",""),"tem_abstract":ab.get("tem_abstract",False),
          # campos a preencher pelo avaliador:
          "g2_elegibilidade":"nao_avaliado","g2_motivo":"",
          "g3_status_auditoria":"","g3_forca_causal":"","g3_verification_status":"pendente",
          "g3_verificado_por":"","g3_notas":""
        },ensure_ascii=False)+"\n")

# ---------- CSV planilha ----------
cols=["id_vinculo","claim_id","secao","pmid","id_referencia_interna","especie_mesh","evid_role",
      "sugestao_g2_ferramenta","sugestao_motivo","titulo","tem_abstract",
      "trecho_ancora","g2_elegibilidade","g2_motivo","g3_status_auditoria",
      "g3_forca_causal","g3_verification_status","g3_verificado_por","g3_notas"]
with open(aud/"planilha_G2G3_vinculos.csv","w",newline="",encoding="utf-8-sig") as f:
    w=csv.DictWriter(f,fieldnames=cols); w.writeheader()
    for v in vinc:
        r=reg(v); pmid=v.get("pmid_oficial") or r.get("pmid_oficial"); ab=abs_.get(pmid,{})
        sg,sm=sugestao_g2(v)
        w.writerow({"id_vinculo":v["id_vinculo"],"claim_id":v["claim_id"],"secao":v["secao_origem"],
          "pmid":pmid,"id_referencia_interna":v["id_referencia_interna"],
          "especie_mesh":"/".join(especie(v)),"evid_role":v.get("evid_role",""),
          "sugestao_g2_ferramenta":sg,"sugestao_motivo":sm,
          "titulo":(r.get("titulo_artigo","") or ab.get("titulo",""))[:120],
          "tem_abstract":ab.get("tem_abstract",False),"trecho_ancora":v["trecho_ancora"],
          "g2_elegibilidade":"","g2_motivo":"","g3_status_auditoria":"","g3_forca_causal":"",
          "g3_verification_status":"","g3_verificado_por":"","g3_notas":""})

# ---------- lista de alto-risco (humana/MA/RCT) para auditar primeiro ----------
alto=[]
for v in vinc:
    r=reg(v)
    if is_meta(r) or "Randomized" in str(r.get("desenho_estudo","")) or v.get("evid_role") in ("human_clinical","human_experimental","post_mortem"):
        alto.append(v["id_vinculo"])
print("vinculos totais:",len(vinc))
print("vinculos de alto-risco (evidencia humana/MA/RCT/pos-morte):",len(alto))
print("arquivos em auditoria_G2G3/: planilha CSV, pacotes JSONL")
# distribuicao de sugestao
import collections
c=collections.Counter(sugestao_g2(v)[0] for v in vinc)
for k,n in c.items(): print(f"  {k}: {n}")
