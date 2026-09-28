#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera 01_pmids.json da B9 a partir das âncoras G1 verificadas (esummary+GPM)."""
import json, re, unicodedata

META = json.load(open('/home/user/BIBLIOTECAS/B09_DisfuncaoMitocondrial/producao/g1_resolvidos.json'))
def sem(s): return ''.join(c for c in unicodedata.normalize('NFKD',str(s)) if not unicodedata.combining(c))

# role/selo por âncora (conforme GPM)
CUR = {
 'Konradi_2004':('human_clinical','post_mortem bipolar; supressão OXPHOS hipocampo; associativo'),
 'Ben-Shachar_2008':('human_clinical','pós-morte; padrão do complexo I varia por doença/região'),
 'Andreazza_2010':('human_clinical','pós-morte; dano ETC/oxidativo bipolar (CPrF)'),
 'Holper_2019':('human_clinical','meta 125 artigos/5 doenças; complexo I sinal mais consistente'),
 'Karabatsiakis_2014':('human_clinical','PBMC; respiração basal/reserva/turnover ATP reduzidos na TDM'),
 'Hroudova_2013':('human_clinical','plaquetas; respiração/capacidade máximas reduzidas (até remissão parcial)'),
 'Fernstrom_2021':('human_clinical','sangue; função da cadeia respiratória reduzida na TDM'),
 'Khan_2023':('review','revisão "Connecting Dots" disfunção mitocondrial × depressão'),
 'Scaini_2021':('human_clinical','dinâmica/mitofagia periférica (Mfn2/Fis1/PINK1/parkin) na TDM; CRP'),
 'Gebara_2020':('preclinical_mechanistic','animal; MFN2 no NAc reverte ansiedade/depressão; causal'),
 'Papageorgiou_2024':('review','revisão dinâmica mitocondrial (OPA1 hub) em transtornos psiquiátricos'),
 'Fanibunda_2019':('preclinical_mechanistic','célula/animal; 5-HT→5-HT2A→SIRT1-PGC1α biogênese'),
 'Deng_2024':('preclinical_mechanistic','animal; PGC-1α hipocampal/giro denteado media depressão/estresse'),
 'Ryan_2019':('human_clinical','PGC-1α sanguíneo associado a sintomas/resposta à ECT'),
 'Madrigal_2001':('preclinical_mechanistic','animal clássico; estresse crônico depleta GSH/peroxida/mitocôndria'),
 'Casaril_2021':('review','revisão disfunção mitocondrial neuronal/bioenergética na depressão inflamatória'),
 'Picard_McEwen_2018':('review','revisão sistemática (23 estudos) estresse psicológico × mitocôndria; COX'),
 'Alcocer-Gomez_2014':('human_clinical','NLRP3 ativo em mononucleares de sangue de TDM'),
 'Ciubuc-Batcu_2024':('review','"nexus mitocondrial" psicoimunoendócrino na TDM'),
 'Calarco_2024':('human_clinical','mtDNA copy number sangue total em populações clínicas (direção mista)'),
 'Trumpff_2021':('human_clinical','cf-mtDNA/ccf-mtDNA de estado; estresse e variação minuto-a-minuto'),
 'Bansal_2016':('review','revisão disfunção mitocondrial na depressão (neurobioenergética)'),
 'Filiou_2019':('review','revisão ansiedade × mitocôndrias cerebrais (crosstalk bidirecional)'),
 'Ceylan_2024':('review','mitoepigenética em transtornos de humor'),
 'Verbal_2026':('review','framework "Mito-Mood"/mitohormese; ritmo × mitocôndria (conceitual)'),
 'Torrell_2013':('human_clinical','mtDNA em amostras cerebrais (pós-morte) de deprimidos'),
 'Picard_2021':('review','natureza social das mitocôndrias (comportamento/saúde)'),
 'Turck_2025':('preclinical_mechanistic','proteômica hipocampal sináptica/não-sináptica (Filipović & Turck)'),
}
PAPEL = {
 'Konradi_2004':'[EC] pós-morte bipolar (Konradi 2004)',
 'Ben-Shachar_2008':'[EC] pós-morte complexo I (Ben-Shachar 2008)',
 'Andreazza_2010':'[EC] pós-morte ETC (Andreazza 2010)',
 'Holper_2019':'[MA] meta complexos I/IV (Holper 2019)',
 'Karabatsiakis_2014':'[EC] respirometria PBMC (Karabatsiakis 2014)',
 'Hroudova_2013':'[EC] respirometria plaqueta (Hroudová 2013)',
 'Fernstrom_2021':'[EC] cadeia respiratória sangue (Fernström 2021)',
 'Khan_2023':'[OB] revisão mitocôndria-depressão (Khan 2023)',
 'Scaini_2021':'[EC] dinâmica/mitofagia sangue (Scaini 2021)',
 'Gebara_2020':'[ML] MFN2 NAc ansiedade (Gebara 2020)',
 'Papageorgiou_2024':'[OB] dinâmica mitocondrial (Papageorgiou 2024)',
 'Fanibunda_2019':'[ML] 5-HT/biogênese (Fanibunda 2019)',
 'Deng_2024':'[ML] PGC-1α hipocampo (Deng 2024)',
 'Ryan_2019':'[EC] PGC-1α/ECT (Ryan 2019)',
 'Madrigal_2001':'[ML] GSH/estresse crônico (Madrigal 2001)',
 'Casaril_2021':'[OB] bioenergética/inflamação (Casaril 2021)',
 'Picard_McEwen_2018':'[OB] SR estresse-mitocôndria (Picard & McEwen 2018)',
 'Alcocer-Gomez_2014':'[EC] NLRP3 sangue TDM (Alcocer-Gómez 2014)',
 'Ciubuc-Batcu_2024':'[OB] nexus mitocondrial (Ciubuc-Batcu 2024)',
 'Calarco_2024':'[EC] mtDNAcn sangue (Calarco 2024)',
 'Trumpff_2021':'[EC] cf-mtDNA/estresse (Trumpff 2021)',
 'Bansal_2016':'[OB] disfunção mitocondrial TDM (Bansal 2016)',
 'Filiou_2019':'[OB] ansiedade-mitocôndria (Filiou 2019)',
 'Ceylan_2024':'[OB] mitoepigenética (Ceylan 2024)',
 'Verbal_2026':'[OB] Mito-Mood/ritmo (Verbal 2026)',
 'Torrell_2013':'[EC] mtDNA cérebro pós-morte (Torrell 2013)',
 'Picard_2021':'[OB] mitocôndria social (Picard 2021)',
 'Turck_2025':'[ML] proteômica hipocampal (Filipović & Turck 2025)',
}

refs=[]
seen={}
for pmid,m in sorted(META.items(), key=lambda x:int(x[0])):
    anchor=m['anchor']; role,motivo=CUR.get(anchor,('human_clinical',''))
    label=anchor.split('_')[0]
    sob=re.sub(r'[^A-Za-z]','',sem(label)).upper(); ano=anchor[-4:]
    base=f'REF_{sob}_{ano}'
    if base in seen:
        seen[base]+=1; oid=f'{base}{chr(ord("a")+seen[base]-1)}'
    else:
        seen[base]=1; oid=base
    refs.append({
      'pmid_oficial':pmid,'titulo_artigo':m['title'],
      'autores':m['authors'],'revista_ano':f"{m['journal']} ({m['pubdate'][:4]})",
      'desenho_estudo':PAPEL.get(anchor,'[OB] fundo mitocondrial'),
      'secao_origem':'mecanismo_B9_disfuncao_mitocondrial',
      'achado_central_molecular':motivo or m['title'],
      'extrapolacao_por_analogia':('SIM — evidência em roedor/célula; tradução humana por analogia [EXT]' if role=='preclinical_mechanistic' else 'não'),
      'ids_referencia_interna':[f'REF_{anchor}'],
      'id_referencia_interna':oid,'doi':'','claim_id_origem':'',
      'evid_role':role,'especie_mesh':(['Animals'] if role=='preclinical_mechanistic' else ['Humans']),
      'verification_status':('preclinico' if role=='preclinical_mechanistic' else 'verificado'),
      'citacao_confirmada':True,'g1_metodo':'eutils_automatico (esearch+esummary; tema validado contra o GPM)',
      'g2_elegibilidade':('redirecionado_mecanistico' if role=='preclinical_mechanistic' else 'eligible'),
      'g2_motivo':('animal/célula — causalidade forte pré-clínica; humana associativa' if role=='preclinical_mechanistic' else 'humano (pós-morte/funcional/revisão); transversal/associativo quando marcador'),
      'g3_verificado_por':'IA G3 Rodada 2: esummary confere autor+ano+tema do GPM; abstracts de alto risco lidos; P-6 pendente',
      'status_auditoria':'CONFIRMADO','origem_pipeline':'BUSCA_FERRAMENTA',
      '_aliases':list({sob,sob.title(),label}),
    })
json.dump(refs, open('/home/user/BIBLIOTECAS/B09_DisfuncaoMitocondrial/Evidencias/Bibliografia/01_pmids.json','w'), ensure_ascii=False, indent=1)
for f in ['02_meta_analises','03_ensaios_clinicos','04_atualizacoes_literatura','05_manuais_e_livros']:
    json.dump([], open(f'/home/user/BIBLIOTECAS/B09_DisfuncaoMitocondrial/Evidencias/Bibliografia/{f}.json','w'))
from collections import Counter
print('refs B9:',len(refs), Counter(r['evid_role'] for r in refs))
