import json

R = json.load(open('/home/user/BIBLIOTECAS/B06_EstresseOxidativo/producao/insumos/matriz_b6_g1.json'))
inv = {i['pmid']: i for i in R['inventario']}
inv['14975445'] = {'pmid': '14975445', 'label': 'Kannan & Jain 2004', 'real_a1': 'Kannan K', 'real_ano': '2004',
                   'titulo': 'Effect of vitamin B6 on oxygen radicals, mitochondrial membrane potential, and lipid peroxidation in H2O2-treated U937 monocytes.',
                   'fonte': 'Free Radic Biol Med', 'pubtype': ['Journal Article'], 'doi': ''}

# decisão ref a ref (auditoria do assistente): ENTRA/BAIXO/EXC — grupo, tag, nota curta baseada no abstract lido
D = {
 # ENZ — enzimologia/estrutura/regulação CBS-CGL-H2S
 '21435402':('ENTRA','ENZ','OB','Aitken 2011 — rev. sítio ativo das enzimas da transulfuração'),
 '7929220':('ENTRA','ENZ','OB','Kéry & Kraus 1994 — CBS é hemoproteína: PLP+heme (RESGATE da auditoria; briefing não achou)'),
 '10531322':('ENTRA','ENZ','OB','Kabil 1999 — domínio regulador CBS; defeito de mutante catalítico'),
 '10052944':('ENTRA','ENZ','OB','Taoka 1999a — cofatores heme/PLP, sítios não-equivalentes'),
 '10529187':('ENTRA','ENZ','OB','Taoka 1999b — mapeamento funções→regiões da CBS (2º registro; GPM citou só o 1º; complementar)'),
 '11483494':('ENTRA','ENZ','OB','Meier 2001 — estrutura cristalina CBS humana (EMBO J)'),
 '15581573':('ENTRA','ENZ','OB','Banerjee 2004 — regulação redox e mecanismo da CBS (rev.)'),
 '16614071':('ENTRA','ENZ','OB','Prudova 2006 — AdoMet estabiliza CBS e modula capacidade redox (PNAS)'),
 '17534535':('ENTRA','ENZ','OB','Singh 2007 — cofator heme incomum da CBS (SEM ABSTRACT no PubMed; G3 por título/periódico/autor)'),
 '18476726':('ENTRA','ENZ','OB','Zhu 2008 — variantes polimórficas/mutantes patogênicas da CGL humana'),
 '21315854':('ENTRA','ENZ','OB','Singh & Banerjee 2011 — biogênese de H2S PLP-dependente'),
 '22738154':('ENTRA','ENZ','OB','Smith 2012 — mutação R266K: ambiente heme/PLP da CBS'),
 '22977242':('ENTRA','ENZ','OB','Yadav 2012 — comunicação alostérica PLP–heme (CBS)'),
 '23981774':('ENTRA','ENZ','OB','Casique 2013 — duas mutações patogênicas CBS, localização intracelular'),
 '24043838':('ENTRA','ENZ','OB','Ereño-Orbea 2013 — base estrutural da regulação/oligomerização da CBS humana (PNAS; briefing não localizou — auditoria confirmou)'),
 '38563463':('ENTRA','ENZ','OB','Al-Sadeq 2024 — duas novas mutações missense CBS (homocistinúria)'),
 '38832404':('ENTRA','ENZ','OB','McFarlane 2024 — inibição gasosa da CBS (NO/CO; fisiologia do heme)'),
 '40327797':('ENTRA','ENZ','OB','Conter 2025 — R336C rompe comunicação com PLP (FEBS J)'),
 '35864237':('ENTRA','ENZ','OB','Petrosino 2022 — biogênese H2S pela CBS; inibição por AOAA; serina'),
 '15189131':('ENTRA','ENZ','OB','Stipanuk 2004 — metabolismo de AA sulfurados (rev. Annu Rev Nutr)'),
 '33000151':('ENTRA','ENZ','OB','Stipanuk 2020 — como o corpo lida com excesso de Met/Cys/sulfeto (rev.)'),
 '30007014':('ENTRA','ENZ','OB','Sbodio 2018 — reguladores da transulfuração (rev.)'),
 '40141131':('ENTRA','ENZ','OB','Pajares 2025 — regulação pós-traducional do metabolismo de enxofre (rev.)'),
 '11001866':('ENTRA','ENZ','OB','Mosharov 2000 — relação quantitativa Hcy↔síntese de GSH; regulação redox'),
 '11001866':None, '11041866':('ENTRA','ENZ','OB','Mosharov 2000 — relação quantitativa Hcy↔síntese de GSH; regulação redox'),
 '26765812':('ENTRA','ENZ','OB','Gregory 2016 — estado de B6/disponibilidade celular de PLP governam transulfuração + H2S'),
 '28245568':('ENTRA','ENZ','OB','Dalto & Matte 2017 — piridoxina↔sistema GPx: elo 1-carbono↔antioxidação (rev.)'),
 '31083508':('ENTRA','ENZ','OB','Gould & Pazdro 2019 — aminoácidos/micronutrientes/dieta → homeostase de GSH (rev.)'),
 '20566639':('ENTRA','ENZ','ML','Ishii 2010 — Cth-KO: camundongo sem CGL precisa de cisteína dietética (prova causal mamífera)'),
 '30671974':('ENTRA','ENZ','OB','Wilson 2019 — distúrbios do metabolismo de B6 (rev. JIMD)'),
 '37451483':('ENTRA','ENZ','OB','Ciapaite 2023 — PLPBP/homeostase de PLP mantém B6 celular e função oxidativa mitocondrial'),
 '38542149':('ENTRA','ENZ','OB','Rivero 2024 — biossíntese de PLP pela PNPO: particularidades por espécie (rev.)'),
 '22116705':('ENTRA','ANTIOX','OB','Wondrak & Jacobson 2012 — B6 além da coenzima: RCS/metais/fotossensíveis (rev. mecanística)'),
 '31480509':('ENTRA','ANTIOX','OB','Ramis 2019 — piridoxamina inibe AGEs via atividade antioxidante primária'),
 # B6DEF — estado/deficiência de B6 → redox (modelos animais)
 '9844729':('ENTRA','B6DEF','ML','Cabrini 1998 — deficiência de B6: TBARS↑, GSH/GSSG↓, GPx/GR↑ compensatórias, GSH total sem Δ (ÂNCORA HETEROGENEIDADE)'),
 '15203107':('ENTRA','B6DEF','ML','Mahfouz 2004 — vit C ou B6 previnem EO e queda de prostaciclina em ratos homocisteinêmicos'),
 '16857832':('ENTRA','B6DEF','ML','Lima 2006 — deficiência de B6 suprime TS hepática MAS aumenta GSH (PARADOXO; ÂNCORA)'),
 '20090886':('ENTRA','B6DEF','ML','Choi 2009 — deficiência de B6 × exercício oxidativo em ratos'),
 '25933612':('ENTRA','B6DEF','ML','Hsu 2015 — status de B6 × defesas/glutationa em camundongos com EO induzido por Hcy'),
 '28024289':('ENTRA','B6DEF','ML','Danielyan 2017 — piridoxina protetora in vivo/in vitro; inibição de xantina oxidase'),
 '40991665':('ENTRA','B6DEF','ML','Todorović 2025 — B6 em ratos hiperhomocisteinêmicos: EO cardíaco, enzimas'),
 '42351801':('ENTRA','B6DEF','ML','Todorović 2026 — B6+folato: biomarcadores cardiometabólicos e EO cardíaco em ratos'),
 '2711414':('ENTRA','B6DEF','ML','McGowan 1989 — status de B6 × intoxicação por Pb: GSH hepático, GR (fatorial 2×2)'),
 # ANTIOX — ação antioxidante direta (química/celular; [APENAS PRÉ-CLÍNICO])
 '7767942':('ENTRA','ANTIOX','ML','Hu 1995 — vitaminas B: atividade antioxidante E pró-oxidante (microsomas; honestidade de polaridade)'),
 '1653565':('ENTRA','ANTIOX','ML','Zhou 1991 — piridoxina como scavenger de ânion superóxido (comparativo)'),
 '11165869':('ENTRA','ANTIOX','ML','Jain & Lim 2001 — piridoxina/piridoxamina inibem superóxido e peroxidação em eritrócitos humanos in vitro'),
 '14975445':('ENTRA','ANTIOX','ML','Kannan & Jain 2004 — B6 reduz radical/ΔΨm/peroxidação em monócitos U937-H2O2 (SEM ABSTRACT no PubMed; G3 título/periódico)'),
 '20209473':('ENTRA','ANTIOX','ML','Mahfouz 2009 — vitâmeros B6 reduzem superóxido/peróxido em endotélio H2O2 (NOX)'),
 '17134167':('ENTRA','ANTIOX','ML','Matxain 2006 — DFT: reatividade da piridoxina com ·OH/·OOH/·O2−'),
 '19558175':('ENTRA','ANTIOX','ML','Matxain 2009 — alta eficiência de captura de ·OH pela B6 (química)'),
 '22231514':('ENTRA','ANTIOX','ML','Natera 2012 — cinética de B6 como antioxidante frente a ROS fotogeradas por B2'),
 '35390394':('ENTRA','ANTIOX','ML','Ngo 2022 — DFT piridoxal: scavenger + risco pró-oxidante (polaridade dupla)'),
 # HUM — humano: estado de B6/dieta → fluxo TS/GSH/marcadores
 '16424114':('ENTRA','HUM','EC','Davis 2006 — restrição dietética de B6 em humanos: GSH e cistationina plasmáticas ↑, fluxo de cisteína sem Δ (ÂNCORA PARADOXO)'),
 '19515736':('ENTRA','HUM','EC','Lamers 2009 — restrição de B6: tendência ↓taxa de síntese eritrocitária de GSH sem Δconcentração (ÂNCORA HETEROGENEIDADE)'),
 '19955400':('ENTRA','HUM','OB','Shen 2010 — PLP ↔ inflamação/EO/8-OHdG/CRP (Boston Puerto Rican; ASSOCIATIVO, transversal)'),
 '31129702':('ENTRA','HUM','OB','Pusceddu 2019 — inflamação subclínica, telômeros, Hcy, B6 e mortalidade (LURIC; ASSOCIATIVO)'),
 '30513795':('ENTRA','HUM','EC','Ford 2018 — RCT complexo B alta dose: metabolismo cerebral (¹H-MRS) × biomarcadores de EO'),
 '32635181':('ENTRA','HUM','EC','Lai 2020 — RCT cirrose: GSH+B6 e capacidade antioxidante (sinal-intervenção; P20)'),
 '27051670':('ENTRA','HUM','EC','Cheng 2016 — RCT HCC pós-ressecção: B6 → ↓Hcy, capacidade antioxidante (sinal-intervenção; P20)'),
 '34229268':('ENTRA','HUM','EC','Van Den Eynde 2021 — quantificação de vitâmeros B6 em plasma/urina (suporte à regra não-intercambiabilidade)'),
 # GSH-CONTEXT — biologia/metodologia da glutationa (não geram claim de B6; regra 6)
 '36707132':('ENTRA','GSH','OB','Averill-Bates 2023 — a glutationa antioxidante (rev.; CONTEXT)'),
 '37237960':('ENTRA','GSH','OB','Giustarini 2023 — como aumentar GSH celular (rev.; CONTEXT)'),
 '36386929':('ENTRA','GSH','OB','Labarrere & Kassab 2022 — GSH: molécula protetora contra EO/envelhecimento/inflamação (rev.)'),
 '37683986':('ENTRA','GSH','OB','Lapenna 2023 — GSH e enzimas GSH-dependentes: bioquímica→gerontologia (rev.)'),
 '32933160':('ENTRA','GSH','OB','Nuhu 2020 — medida de GSH/GSSG por HPLC (método)'),
 '37759691':('ENTRA','GSH','OB','Valgimigli 2023 — peroxidação lipídica e proteção antioxidante (rev.; elo ferroptose B6-V1)'),
 '28807817':('ENTRA','GSH','OB','Giustarini 2017 — razão GSH/GSSG e proteínas S-glutationiladas em sangue/tecidos (método)'),
 '26262996':('ENTRA','GSH','EC','Schmitt 2015 — NAC vs GSH oral vs GSH sublingual: bioavaliação e marcadores (comparativo; P20)'),
 # HIP — hipótese emergente
 '42196957':('ENTRA','HIP','OB','Kato 2026 — hipótese B6→PLP-metabolismo→Nrf2 (rev. hipótese; NÃO-CONSOLIDADO; [G1] explícito)'),
 # NEG-METO — lição anti-extrapolação (âncoras da REGRA B6-STRESS-OXIDATIVO-01)
 '16531614':('ENTRA','NEG','MA','Bønaa 2006 NORVIT — reduzir Hcy com vitaminas B NÃO reduziu eventos pós-IM (RCT 3749; LIÇÃO: biomarcador↓ ≠ desfecho; âncora NEG. Desfecho CV, uso metodológico)'),
 '29776960':('ENTRA','NEG','EC','Christen 2018 WAFACS — folato+B6+B12 não alteraram biomarcadores de inflamação/endotélio (substudy RCT; âncora NEG associação↔causa)'),
 # BAIXO — tangenciais (registrados; adiáveis)
 '14642387':('BAIXO','ANTIOX','ML','Chen 2003 — base de Schiff piridoxal-aminoguanidina (derivado sintético; tangencial)'),
 '31915511':('BAIXO','HUM','EC','Lindschinger 2019 — piloto n=30 natural vs sintético (biodisponibilidade)'),
 '19491213':('BAIXO','NEG','EC','Song 2009 WAFACS-DM2 — Hcy-lowering não reduziu DM2 (lição coberta por Bønaa/Christen)'),
 '35821844':('BAIXO','GSH','EC','Lizzo 2022 — GlyNAC em idosos (GSH sem B6)'),
 '38279310':('BAIXO','GSH','OB','Chen 2024 — GSH mitocondrial (fronteira B9; CONTEXT redundante)'),
 '36717385':('BAIXO','HUM','EC','Lu 2023 — RCT preliminar low-dose B+betaína → Hcy (desfecho intermediário)'),
 '39960689':('BAIXO','HUM','MA','Liu 2025 — network meta suplementos→Hcy em saudáveis'),
 '35454125':('BAIXO','HUM','OB','Bajic 2022 — Hcy/B6/folato em modelos de IM/ICC (rev.)'),
 '34573083':('BAIXO','ANTIOX','ML','Balakina 2021 — novo derivado B6NO (síntese/NO)'),
 '41149254':('BAIXO','HUM','OB','D’Elia 2025 — narrativa Hcy cardiovascular'),
 # EXC — fora de escopo permanente (expostos)
 '33414386':('EXC','','MA','Chen 2021 — meta marcadores EO em AUTISMO (fora de escopo permanente)'),
 '37409540':('EXC','','OB','Corona-Trejo 2023 — transulfuração no PARKINSON (fora de escopo permanente; conteúdo neural relevante mas âncora-alvo excluída)'),
 '31601260':('EXC','','OB','An 2019 — B-vitaminas/metilação em comprometimento cognitivo/MeSH Alzheimer (fora de escopo permanente)'),
 '34058062':('EXC','','MA','Olaso-González 2021 — suplementação B×Hcy em MCI (espectro Alzheimer; fora de escopo)'),
 '40218880':('EXC','','MA','Li 2025 — revisão RCTs B-vitaminas→Hcy→trombose (desfecho cardiovascular; sem lição mecanística nova)'),
 '41393929':('EXC','','MA','Yin 2025 — meta folato+B12/B6 em DM2 (desfecho metabólico)'),
 '38830901':('EXC','','ML','Pilesi 2024 — deficiência de B6 + Ras oncogênico em DROSOPHILA (não-mamífero; tumor)'),
 '19903353':('EXC','','ML','Havaux 2009 — plantas deficientes de B6 × fotoestresse (não-mamífero)'),
 '31961357':('EXC','','ML','Neugart 2020 — Arabidopsis pdx1.3 UV-B (não-mamífero)'),
 '39441545':('EXC','','ML','Hacham 2024 — metabolismo de enxofre vegetal (não-mamífero)'),
 '26823273':('EXC','','ML','Ankisettypalli 2016 — PdxH de micobactérias (não-mamífero)'),
 '31132312':('EXC','','ML','Devi 2019 — CBS de H. pylori (não-mamífero)'),
 '40044138':('EXC','','ML','Lee 2025 — MccB de S. aureus (não-mamífero)'),
 '32913258':('EXC','','ML','Matoba 2020 — CGL de Lactobacillus (não-mamífero)'),
 '32887901':('EXC','','ML','Conter 2020 — CBS de Toxoplasma gondii (não-mamífero; GPM a citou como NON-CANONICAL — série formaliza como EXC-registrada)'),
 '29630349':('EXC','','ML','Tu 2018 — cristal de CBS de levedura (não-mamífero)'),
}
D = {k: v for k, v in D.items() if v}
todas = set(inv.keys())
faltam = todas - set(D.keys())
extra = set(D.keys()) - todas
print('no inventario:', len(todas), '| decididas:', len(D))
print('FALTAM decidir:', [(p, inv[p]['label']) for p in faltam])
print('EXTRA:', extra)
n_e = sum(1 for v in D.values() if v[0]=='ENTRA'); n_b = sum(1 for v in D.values() if v[0]=='BAIXO'); n_x = sum(1 for v in D.values() if v[0]=='EXC')
print(f'ENTRA={n_e} BAIXO={n_b} EXC={n_x} SOMA={n_e+n_b+n_x}')
naoidx = [
 ('Dawood 2024','10.32947/ajps.v24i1.1030','RCT piloto B6 em DM2 — periódico não indexado'),
 ('González-Recio 2020','10.1002/9780470015902.a0028966','eLS (enciclopédia; não indexado)'),
 ('İnceören 2023','10.1556/066.2022.00138','Silybum+derivados B6 × dano DNA (não indexado)'),
 ('Itoh 2024','10.1016/j.nutos.2024.03.011','PLP baixo → ↓GSH/neurotransmissor, ↑suscetibilidade H2O2 em SH-SY5Y — periódico não indexado → [G1]'),
 ('Lee 2019','10.3390/cryst9120656','cristal CGL bacteriana (não indexado; seria EXC-não-mamífero)'),
 ('Li 2026','10.1002/imm3.70032','piridoxal→estresse oxidativo letal em câncer ovariano (não indexado; seria EXC-onco)'),
 ('Mendes 2017','10.4322/2357-9730.70767','B6 isolado × EO/coração em hiperhomocisteinemia (não indexado)'),
 ('Serhiyenko 2025','10.22141/2224-0721.21.1.2025.1493','B6-CV-DM narrativa (não indexado)'),
 ('Shrayner 2025','10.29296/25877305-2025-10-03','regulação de GSH por vitaminas (não indexado; russo)'),
 ('Velásquez 2019','10.2174/1874091x01913010037','piridoxina ↓EO em membrana eritrocitária in vitro (não indexado)'),
]
resgate = [('Kéry & Kraus 1994','7929220','resolvida por busca dirigida da auditoria (DOI CrossRef não registrado no PubMed)')]
matriz = {'decisao': D, 'naoidx': naoidx, 'resgate': resgate,
          'conferencias': {'gpm_tabela_45': '45/45 confirmadas por autor+ano+PMID (Kannan & Jain 2004=14975445 verificado por esummary direto)',
                           'overlap_vigente': '0 — as 36 vigentes (O&NS geral) não colidem com as 98 novas (eixo B6-vitamin→TS→GSH)',
                           'fp': 0, 'divergencias_autor_ano': 0,
                           'contagem_anexo': 'anexo real tem 106 DOIs (briefing/GPM alegavam 93 — incongruência interna exposta)'}}
json.dump(matriz, open('/home/user/BIBLIOTECAS/B06_EstresseOxidativo/producao/insumos/matriz_b6_decisao.json','w'), ensure_ascii=False, indent=1)
print('matriz salva')
