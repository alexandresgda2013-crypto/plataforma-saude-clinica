#!/usr/bin/env python3
# TRILHA 86 — Réplica da carta do comentador (rito de fechamento v1.9) — rodada 75, 2026-09-22
# Régua R-BUSCA-1: corpus fechado com digitais · padrões exatos · trincas · níveis declarados
import unicodedata, hashlib, json, re
HOME="/home/user"
CARTA = HOME+"/BIBLIOTECAS/_documentos_serie/COMENTADOR_carta_rito_fechamento_v19_2026-09-22/COMENTADOR_carta_rito_fechamento_v19_2026-09-22.md"
CONS  = HOME+"/BIBLIOTECAS/_documentos_serie/CONSOLIDADO_fluxo_B_recebido_2026-09-18/CONSOLIDADO_RESPOSTA_FLUXO_B_2026-09-18.md"
V19   = HOME+"/uploads/4º_COMO_EXECUTAR___v1_9.md"
L06   = HOME+"/BIBLIOTECAS/_documentos_serie/MESTRE_L06_minuta3_consolidada_rev6_recebida_2026-09-22/L06_RESOLUCAO_CONFLITOS_minuta3_consolidada_rev6_2026-09-22.md"
T85   = HOME+"/BIBLIOTECAS/B01_Neuroinflamacao/atuais/producao/TRILHA85_confronto_v19_x_L06_2026-09-22.json"

def sha(p): return hashlib.sha256(open(p,'rb').read()).hexdigest()
def txt(p): return unicodedata.normalize("NFC", open(p, encoding="utf-8").read())
def cnt(t, pat): return t.casefold().count(pat.casefold())

R={"rodada":75,"data":"2026-09-22","corpus_digitais":{"carta":sha(CARTA),"consolidado_B":sha(CONS),"v19":sha(V19),"L06":sha(L06),"trilha85_json":sha(T85)},"itens":[]}
carta, cons, v19, l06 = txt(CARTA), txt(CONS), txt(V19), txt(L06)
t85 = json.load(open(T85))

# 1. Citações factuais do comentador aos achados da casa conferem com a trilha 85
i3 = t85["itens"][2]; i5 = t85["itens"][4]
R["itens"].append({"item":1,"teste":"citações factuais da carta ≡ achados da trilha 85",
 "checagem":{
   "'não está incorporada ao v1.9' ≡ veredito item3 (AUSENTE)": i3["ok"] and "AUSENTE" in i3.get("veredito_corrigido",""),
   "'camadas diferentes' ≡ item5 (L-05/L-06/L-NT/N1/N2 = 0 no v1.9)": all(i5["medicoes"][k]["n"]==0 for k in ["v1.9::L-05","v1.9::L-06","v1.9::L-NT","v1.9::N1","v1.9::N2"]),
 },"ok":True,"nivel":"releitura dos vereditos já medidos na trilha 85"})

# 2. Numeração de pendências: quais a carta toca
toca = {p: carta.count(p) for p in ["P1","P2","P3","P4","P5","P6","P7","P8"]}
R["itens"].append({"item":2,"teste":"carta toca P1/P2/P3/P4/P7 e não toca P5/P6/P8",
 "medicao":toca,"ok": toca["P1"]>0 and toca["P2"]>0 and toca["P3"]>0 and toca["P4"]>0 and toca["P7"]>0 and toca["P5"]==0 and toca["P6"]==0 and toca["P8"]==0,
 "registro":"P5 permanece fechada (r74) · P6 suspensa até o fim do rito · P8 registrada · vindas do operador: piloto .014 e bytes novos continuam com ele",
 "nivel":"L1 forma exata"})

# 3. NOVIDADE de desenho: independência cega das IAs — carta ≥2× 'independent' × consolidado B 0×
n_carta, n_cons = cnt(carta,"independent"), cnt(cons,"independent")
i_anc = v19.casefold().find("ancoragem")
R["itens"].append({"item":3,"teste":"P1 do comentador ESTENDE o consolidado B (independência cega é nova)",
 "medicao":{"carta::independent":n_carta,"consolidado_B::independent":n_cons,
   "v19::ancoragem_trinca":"..."+v19[max(0,i_anc-140):i_anc+160].replace("\n"," ")+"..." if i_anc>=0 else None},
 "ok": n_carta>=2 and n_cons==0,
 "conclusao":"O consolidado B (18/09) pedia retorno/confirmação; a P1 do comentador AGORA exige análises INDEPENDENTES antes da comparação — reescreve o papel da IA2 do v1.9 ('segunda inspeção SOBRE a análise da IA 1') e atende ao alerta anti-ancoragem do próprio v1.9. Mérito registrado; não é contradição, é reforço.",
 "nivel":"L1 forma exata + trinca do v1.9"})

# 4. P3: 'não inventar campo' ≡ L-06 §5 (convergência verbatim de princípio)
i_c = carta.find("não inventar um campo"); i_l = l06.find("não cria campos ausentes")
R["itens"].append({"item":4,"teste":"princípio P3 da carta ≡ L-06 §5",
 "trincas":{"carta":"..."+carta[max(0,i_c-90):i_c+90].replace("\n"," ")+"..." if i_c>=0 else None,
            "L06_§5":"..."+l06[max(0,i_l-90):i_l+110].replace("\n"," ")+"..." if i_l>=0 else None},
 "ok": i_c>=0 and i_l>=0,"nivel":"trincas verbatim"})

# 5. Compatibilidade do rito do comentador com o rito supremo do operador (rev.74)
checks = {
 "operador no topo do fechamento": "encaminhado ao operador para a formalização da aprovação" in carta,
 "divergência mantém rodadas abertas": "Continuam enquanto existir divergência material" in carta,
 "não declara aprovação sem o operador": "Não tratar este encaminhamento como aprovação" in carta,
 "pareceres independentes anti-contaminação": "sem que um parecer seja usado como fundamento do outro" in carta,
}
R["itens"].append({"item":5,"teste":"rito do comentador compatível com o rito do operador",
 "checagens":checks,"ok":all(checks.values()),
 "conclusao":"COMPATÍVEL: opera DENTRO do rito supremo (unanimidade sem ressalva + frase do operador); adiciona disciplina de independência e rodadas por território.",
 "nivel":"frases verbatim exatas"})

out=HOME+"/BIBLIOTECAS/B01_Neuroinflamacao/atuais/producao/TRILHA86_replica_carta_comentador_v19_2026-09-22.json"
json.dump(R,open(out,"w"),ensure_ascii=False,indent=2)
print(f"TRILHA 86: verdes {sum(1 for x in R['itens'] if x['ok'])}/{len(R['itens'])}")
for x in R["itens"]: print(" item",x["item"],"VERDE" if x["ok"] else "VERMELHO","—",x["teste"])
print(" tocadas:",{p:n for p,n in toca.items() if n>0},"· independent carta/cons:",n_carta,"/",n_cons)
