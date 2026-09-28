#!/usr/bin/env python3
# B7 — motivos por família para os 131 BAIXO + matriz final
import json, re
BASE='/home/user/BIBLIOTECAS/B07_EixoIntestinoCerebro'
d=json.load(open(f'{BASE}/producao/insumos/matriz_b7_decisao_draft.json'))
itens=d['itens']

def familia(x):
    t=x['titulo'].lower(); pt='|'.join(x['pubtype']).lower(); fo=x['fonte'].lower()
    # manuais específicos
    man={
     '25078296':"BAIXO — revisão 5-HT/Trp no eixo; serotonina entérica já ancorada por Yano 2015 (vigente) e masters Agus/Bosi; sem seta causal nova",
     '24756641':"BAIXO — revisão 'stressed bugs, stressed brain' (2014); programação HPA/IBS já coberta por Sudo (vigente) e Bonaz (vigente)",
     '33093662':"BAIXO — revisão Nat Rev Microbiol (Morais 2021) comportamento/doenças; arquitetura já coberta por Cryan 2019 (vigente)",
     '30292888':"BAIXO — revisão clínica geral do eixo (Osadchiy 2019); mesma arquitetura das vigentes",
     '30823925':"BAIXO — revisão microbiota→SNC (Ma 2019); genérica, mira doenças neurológicas; coberta",
     '34599147':"BAIXO — humano em transtorno por uso de álcool (KYN/inflamação); tangencial ao miolo ansiedade/depressão; V1 já marca alcoolismo como fronteira ilustrativa (12.x)",
     '36758839':"BAIXO — mesmo grupo/pergunta da master Zhao 2022 (36776388: DSS→KYN soro+cérebro via microbiota); redundância de desenho",
     '33893636':"EXC tratado acima",
     '40662222':"BAIXO — revisão sistemática de microglia no eixo; coberta pelas masters primárias Erny/Spichak/Caetano-Silva e revisão Cheng",
     '39408347':"BAIXO — revisão cienciométrica de desordens do Trp; sem conteúdo mecanístico primário; briefing já a listava como não citada",
     '38102897':"BAIXO — ensaio conceitual IDO/quinurenina 'reflexo' neuroimune (Stone); sem foco em microbiota→cérebro",
     '36172468':"BAIXO — revisão Trp×depressão×microbiota (Lukić 2022); coberta pelas masters Chen 2021/Cheng 2024/Zhou 2023/Lin 2023",
     '39875781':"BAIXO — revisão probióticos×depressão (Tiwari 2025); bloco de intervenção da V1 já ancorado em metas vigentes (Moshfeghinia/Cohen Kadosh) — P20",
     '40054458':"BAIXO — revisão terapêutica eixo imune-cérebro (O'Riordan 2025); genérica; arquitetura imune coberta",
     '35066114':"BAIXO — revisão sinalização AGCC no eixo (O'Riordan 2022); redundante com Silva 2020 e masters de AGCC",
     '36014776':"BAIXO — produtos naturais×depressão via eixo (Liaqat 2022); fronteira P20 (fitoterápicos), sem primário de mecanismo",
     '34335190':"BAIXO — revisão translacional genérica (Schächtle 2021); arquitetura coberta",
     '34149693':"BAIXO — revisão Trp hospedeiro/comensal (Grifka-Walk 2021); redundante com master Agus 2018",
     '34473368':"BAIXO — balanço 5-HT↔KYN na imunidade intestinal (Haq 2021); partição Trp já coberta por masters Agus/Bosi e V1 2.5/2.7",
     '31258331':"BAIXO — revisão loop microrganismos-Trp-KYN saúde (Dehhaghi 2019); genérica, coberta",
     '31610413':"BAIXO — revisão Curr Opin Pharmacol 'essentials' Trp-microbiome-gut-brain (Gheorghe 2019); redundante com masters",
     '31825083':"BAIXO — revisão Adv Nutr Trp ligando microbiota-cérebro (Gao K 2020); redundante com masters",
     '33804088':"BAIXO — revisão Trp e homeostase gut-brain (Roth 2021); redundante",
     '35883554':"BAIXO — revisão Trp/QUIN em depressão E neurodegeneração (Hestad 2022); mira mista, foco B4/B1+neurodegenerativo",
     '35819092':"BAIXO — primário Roseburia→AGCC→HDAC×neuroinflamação (Song 2022); mesma seta das masters Erny/Caetano-Silva; sem ponte comportamental",
     '36232464':"BAIXO — Caco-2 LPS + L. rhamnosus (Zheng J 2022); família in vitro barreira",
     '30518529':"(entra)",
     '33403482':"BAIXO — editorial (Akiba 2021) sem abstract no PubMed; pergunta 'galinha-ovo' permeabilidade×inflamação já registrada na V1",
    }
    if x['pmid'] in man: return man[x['pmid']]
    if 'caco-2' in t or 'ipec' in t or ('in vitro' in t and 'barrier' in t):
        return "BAIXO — barreira intestinal in vitro com intervenção única; mecanismo LPS→TJ já coberto pelas masters Guo 2013/2015 + Nighot 2017/2019; sem ponte ao SNC (B7-CAUSAL-01)"
    if any(w in t for w in ('sepsis','septic')):
        return "BAIXO — modelo de sepse; barreira/translocação já coberta (masters + Tulkens humano); fora do miolo psiquiátrico"
    if any(w in t for w in ('cirrhosis','kidney','renal','heart failure','endothelial','endotoxemia and disease')):
        return "BAIXO — doença-órgão não psiquiátrica (fígado/rim/coração/vaso); translocação intestinal coberta; tangencial ao miolo"
    if 'chlorpyrifos' in t or 'vitamin a' in t or 'acrolein' in t or 'syndecan' in t or 'pathogen' in t or 'antibiotics induced' in t or 'zinc gluconate' in t or 'catalpol' in t or 'orexin' in t or 'daidzein' in t or 'l-tryptophan alleviated' in t or 'nec' in t or 'bifidobacterium on intestinal' in t:
        return "BAIXO — barreira intestinal com agente/intervenção isolada; seta LPS→TJ coberta pelas masters; sem ponte causal ao SNC"
    if 'tight junction' in t or 'intestinal barrier' in t or 'intestinal permeability' in t or 'paracellular' in t or 'gut-vascular' in t or 'blood-brain and gut' in t or 'barrier function' in t:
        return "BAIXO — revisão/primário de biologia de tight junctions; arquitetura de barreiras coberta pelas masters (Guo×2/Nighot×2/Kurita/Aburto) + Kuo/Barki novas"
    if 'tryptophan' in t or 'kynurenine' in t or 'quinolinic' in t or 'anthranilic' in t or 'indoleamine' in t or 'serotonin' in t:
        if 'review' in pt or 'systematic' in pt:
            return "BAIXO — revisão geral triptofano/quinurenina; arquitetura coberta pelas masters Agus 2018/Bosi 2020/Schwarcz 2024/Sathyasaikumar 2024 e seção 2.5 da V1"
        return "BAIXO — primário Trp/KYN sem ponte microbiota→SNC fechada (B7-CAUSAL-01/02)"
    if any(w in t for w in ('short-chain fatty acid','short chain fatty acid','scfa','butyrate','propionate','acetate')) :
        if 'review' in pt:
            return "BAIXO — revisão geral AGCC (imunidade/metabolismo/doenças); núcleo AGCC→cérebro coberto por masters Erny 2021/Spichak 2021/Caetano-Silva 2023/Barki 2022/Cheng 2024"
        return "BAIXO — primário AGCC periférico/imune/metabólico; sem ponte ao SNC além das masters"
    if 'microglia' in t:
        return "BAIXO — revisão microglia no eixo; coberta pelas masters primárias de microglia/astrócito"
    if 'immune' in t or 'inflammation' in t or 'immunity' in t or 'inflammatory' in t:
        return "BAIXO — imunologia geral do eixo/metabólitos; núcleo coberto por masters de via imune (B7-CAUSAL-01)"
    if 'gut-brain' in t or 'gut microbiota-brain' in t or 'microbiota-gut-brain' in t or 'brain-gut' in t or 'gut–brain' in t or 'microbiome axis' in t:
        return "BAIXO — revisão narrativa genérica do eixo intestino-cérebro; arquitetura coberta por V1 vigente (Cryan 2019/Bonaz 2018/Margolis 2021) e masters 2024–2025; sem seta causal nova"
    if 'neurological' in t or 'neurodegenerative' in t or 'cns diseases' in t or 'brain disorders' in t:
        return "BAIXO — revisão mira doenças neurológicas/neurodegenerativas em geral; fora do miolo (malha: neurodegeneração não é escopo B7)"
    if 'energy' in t or 'obesity' in t or 'metabolic' in t or 'glucose' in t:
        return "BAIXO — eixo metabólico/obesidade; confundidor registrado na V1 (12.x); sem ponte psiquiátrica"
    if 'gaba' in t or 'glutamat' in t:
        return "BAIXO — neurotransmissor microbiano periférico; coberto (Baj 2019 entra como âncora glutamatérgica; GABA microbiano já na V1)"
    if 'probiotic' in t or 'prebiotic' in t:
        return "BAIXO — intervenção probiótica; bloco de intervenção da V1 já ancorado em metas vigentes — P20 (sem extrapolação)"
    return "BAIXO — redundante/tangencial ao núcleo mecanístico da rodada (ver relatório por família)"

nao_class=[]
for x in itens:
    if x['decisao']=='BAIXO' and not x['motivo']:
        x['motivo']=familia(x)
        if x['motivo'].startswith('BAIXO — redundante/tangencial'): nao_class.append(x['pmid'])
tot={'ENTRA':0,'EXC':0,'BAIXO':0}
for x in itens: tot[x['decisao']]+=1
assert tot=={'ENTRA':31,'EXC':26,'BAIXO':131}, tot
json.dump({'meta':{'total_fila':188,'entra':31,'exc':26,'baixo':131,'gerado':'2026-09-09','criterio':'regras de ouro GPM B7 (B7-CAUSAL-01/02/03) + malha de escopo da série'},'itens':itens}, open(f'{BASE}/producao/insumos/matriz_b7_decisao.json','w'), ensure_ascii=False, indent=1)
print('OK matriz final gravada. fallback genérico:',len(nao_class))
for pm in nao_class:
    x=[i for i in itens if i['pmid']==pm][0]
    print(' -',pm,x['autor'],x['ano'],'|',x['titulo'][:80],'|',x['pubtype'])
