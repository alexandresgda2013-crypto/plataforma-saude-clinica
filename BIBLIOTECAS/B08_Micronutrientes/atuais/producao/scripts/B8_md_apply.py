#!/usr/bin/env python3
# B8 — fusao V1(96) -> V2(145): insere 49 refs [AT 2026-09-09] na canonica.
# Asserts: cada ancora aparece exatamente 1x; varredura de 7-9 digitos = 0.
import json, re, shutil, os

BASE='/home/user/BIBLIOTECAS/B08_Micronutrientes'
V1=f'{BASE}/B8 DEFICIENCIAS DE MICRONUTRIENTES V1 CANONICA.md'
V2=f'{BASE}/B8 DEFICIENCIAS DE MICRONUTRIENTES V2 CANONICA.md'

doc=open(V1, encoding='utf-8').read()
trechos_ancora={}  # rotulo -> trecho literal que fica na canonica (para os Vinculos)

OPS=[]  # (modo, ancora, novo)
def rep(anc,new,key=None):
    OPS.append(('replace',anc,new,key))
def app(anc,ins,key=None):
    OPS.append(('after',anc,ins,key))

# ---------- 1) cabecalho ----------
rep('# B8 DEFICIÊNCIAS DE MICRONUTRIENTES V1 CANÔNICA',
    '# B8 DEFICIÊNCIAS DE MICRONUTRIENTES V2 CANÔNICA','titulo')
rep('**artefato_rotulo:** CANÔNICA v1 · G1 (96/96 PMIDs eutils) + G2 (espécie/desenho/elegibilidade) + G3 (suporte por vínculo; abstracts de alto risco lidos: VITAL-DEP, B12-nulo, selênio, Mg Rajizadeh/Tarleton, MR Carnegie, SMILES, metas de vitamina D).',
    '**artefato_rotulo:** CANÔNICA v2 (rodada [AT] GPM 2026-09-09 — reconciliação de insumo externo, P-7; 96→145 refs: 49 ENTRA — 41 masters GPM + Bourre 2006, Mattei 2019, Moore 2019, Ferriani 2022, Kohl 2025, Islam 2025, Yang 2026 e Horsdal 2025 —; 30 BAIXO; 12 EXC pela malha de escopo; 0 falso positivo; 7 erros do briefing externo revertidos e expostos) · G1 (145/145 PMIDs eutils) + G2 (espécie/desenho/elegibilidade) + G3 (suporte por vínculo; abstracts de alto risco lidos: VITAL-DEP, B12-nulo, selênio, Mg Rajizadeh/Tarleton, MR Carnegie/Hui/Lu, SMILES, metas de vitamina D, Moroianu, Plevin, Horsdal, Ye).','rotulo')

# ---------- 2) §1.1 fundamentacao historica (Bourre) ----------
app('(deficiência confirmada — reposição é medicina).',
    '\n\nFundamentação histórica do escopo: a atualização clássica dos requisitos de micronutrientes para o cérebro (Parte 1 da série) fixou que vitaminas e minerais exercem funções específicas e insubstituíveis na estrutura e no funcionamento do sistema nervoso — o enunciado bioquímico sobre o qual esta biblioteca opera (Bourre 2006)[OB].',
    'REF_BOURRE_2006')

# ---------- 3) §1.2 metilacao ----------
app('B12/folato no idoso (Petridou 2016)[MA].',
    '\n\n[[AT 2026-09-09]] O desdobramento neuropsiquiátrico da deficiência de B12 é revisado em detalhe — os sintomas podem preceder a anemia e incluir depressão, alteração cognitiva e sintomas psicóticos (Sahu 2022)[OB]; (Mathew 2024)[OB]; um relato de caso autobiográfico documenta a possibilidade clínica de transtornos neuropsiquiátricos associados à deficiência, sem valor epidemiológico (Badar 2022)[EC]. Em idosos da coorte TUDA, status bioquímico baixo de vitaminas do complexo B associou-se a maior risco de depressão — associação transversal, não prova de que suplementar previna (Moore 2019)[EC]; no ELSA-Brasil, maior ingestão de antioxidantes e do complexo B associou-se a menor depressão, com a ressalva de que ingestão alimentar não equivale a deficiência bioquímica (Ferriani 2022)[EC]. Mecanismos, níveis de exposição e eficácia das vitaminas B no cérebro foram sistematizados em revisão de referência (Kennedy 2016)[OB].',
    'REF_SAHU_2022')

# ---------- 4) §1.3 energia ----------
app('A maquinaria detalhada de ETC é a B9.',
    '\n\n[[AT 2026-09-09]] Revisões recentes alargaram o catálogo de nutrientes com papel no sistema nervoso central (Nogueira-de-Almeida 2023)[OB] e na saúde mental em geral (Muscaritoli 2021)[OB]; a tese de que nutrientes protegem a função mitocondrial e a sinalização de neurotransmissores foi revista no contexto de depressão e comportamento suicida (Du 2016)[OB] — a mesma revisão abrange TEPT, que permanece fora do escopo nominal desta biblioteca (TEPT ≠ depressão ≠ ansiedade), sendo citada apenas pela mecânica mitocondrial compartilhada com a B9. O papel dos micronutrientes em transtornos neurológicos também foi revisto (Lahoda Brodska 2023)[OB] — fronteira ilustrativa, sem extrapolar mecanismo de doença neurológica para o psiquiátrico.',
    'REF_NOGUEIRA_2023')

# ---------- 5) §1.6 VDR (fundamentos) ----------
app('e **prevenção nula** no VITAL (Okereke 2020)[EC].',
    '\n\n[[AT 2026-09-09]] A neurobiologia da vitamina D no desenvolvimento e no cérebro adulto foi consolidada por Eyles e colaboradores (Eyles 2013)[OB]; a ligação com esquizofrenia — duas décadas de pesquisa — entra como fronteira ilustrativa de método (associação epidemiológica forte, intervenção sem prova), não como escopo causal desta biblioteca (Cui 2021)[OB]. No plano molecular, propõe-se que a deficiência de vitamina D toque a depressão por remodelamento sináptico mediado por complemento e por sinalização VDBP-megalin — hipótese de revisão mecanicista, sem lastro intervencional (Yang 2026)[OB].',
    'REF_EYLES_2013')

# ---------- 6) §2.1 metilacao/BH4 ----------
app('não específica de um nutriente (Bottiglieri 2000)[EC];\n(Almeida 2008)[MA].',
    '\n\n[[AT 2026-09-09]] O status de folato prejudicado em pacientes com transtornos mentais foi confirmado em amostra clínica (Rajen 2025)[EC], e deficiências combinadas de vitamina D, B9 e B12 associaram-se à gravidade clínica em pacientes psiquiátricos (Faugere 2025)[EC]; no Líbano, a deficiência de B12 associou-se transversalmente a sintomas neuropsiquiátricos (Al Jassem 2024)[EC]. As três leituras são associativas: não demonstram que a deficiência precedeu ou causou o quadro (regra B8-CAUSAL-02).',
    'REF_RAJEN_2025')

# ---------- 7) §2.2 VDR via ----------
app('**sem efeito sobre ansiedade** e **nula em prevenção de\nlongo prazo** (Okereke 2020)[EC].',
    '\n\n[[AT 2026-09-09]] Em mulheres brasileiras, deficiência/insuficiência de vitamina D associou-se a transtornos mentais comuns (Kohl 2025)[EC]. O maior caso-coorte de base populacional mediu 25(OH)D e a proteína ligadora (DBP) neonatais em amostra dinamarquesa: encontrou relações inversas significativas com esquizofrenia, TEA e TDAH — **mas não para a TDM** (n≈24 mil casos analisados), apesar do tamanho amostral (Horsdal 2025)[EC]. É a demonstração, em larga escala, de que o status neonatal de vitamina D carrega sinal para transtornos mentais posteriores — com resultado **nulo no desfecho-âncora desta biblioteca**, o que impede transformar associação de outros transtornos em tese D→depressão. Status/suplementação de vitamina D quanto a BDNF e humor-cognição: revisão estruturada mostra quadro inconsistente (Skoczek-Rubińska 2025)[OB]. E a revisão sistemática com meta-análise exploratória de vitamina D e B12 em transtornos psiquiátricos mostrou que os sinais inversos iniciais **colapsam ao nulo após correção de viés de publicação** (trim-and-fill: OR 0,88; IC95% 0,48–1,63 para suplementação de vitamina D), com evidência de suplementação de B12 esparsa e nula — apoiando avaliação direcionada de deficiência, **não** suplementação de rotina (Moroianu 2026)[MA].',
    'REF_KOHL_2025')

# ---------- 8) §2.3 Zn/Mg ----------
app('a tradução suplementar é fraca e dependente de baseline.',
    '\n\n[[AT 2026-09-09]] A modulação de transtornos mentais por oligoelementos essenciais (Zn, Mg, Se, Fe) foi revista (Shayganfard 2022)[OB]; a etiologia multifacetada dos transtornos mentais, com foco em elementos-traço, foi sistematizada (Astorino 2025)[OB]; e perturbações da homeostase do zinco no início de transtornos neuropsiquiátricos foram revistas (Faa 2025)[OB]. O quadro permanece mecanicista: nenhuma das revisões sustenta suplementação em não-deficientes.',
    'REF_SHAYGANFARD_2022')

# ---------- 9) §2.4 ferro ----------
app('pode elevá-la e mascarar ferro\nfuncional baixo.',
    '\n\n[[AT 2026-09-09]] O ferro é o nutriente-modelo para estudar as origens nutricionais das doenças neuropsiquiátricas: a deficiência precoce programa a paisagem epigenômica do hipocampo, com efeitos que persistem apesar da correção posterior (Barks 2019)[OB]; (Barks 2021)[OB]. A janela desenvolvimental é fronteira ilustrativa: revisões de escopo ligam a deficiência de ferro a transtornos do neurodesenvolvimento (McWilliams 2022)[OB]; (Fiani 2023)[OB] — TDAH e TEA não são escopo causal desta biblioteca, e a ligação é citada apenas como evidência de que a janela crítica do ferro existe. O desenvolvimento cerebral dependente de micronutrientes foi revisto por Mattei (Mattei 2019)[OB].',
    'REF_BARKS_2019')

# ---------- 10) BLOCO_05 mensuracao ----------
app('Periférico/sérico ≠ SNC.',
    '\n\n[[AT 2026-09-09]] Adendos de mensuração: correlações hematológicas como preditores de manifestações em transtornos mentais foram avaliadas (Domański 2025)[EC]; e, na coorte ABCD de juventude (com TEA — fronteira ilustrativa, não escopo), a associação encontrada foi entre **ingestão estimada** de nutrientes e problemas psiquiátricos e de sono — reforçando que proxy de ingestão não é biomarcador de deficiência (Radoeva 2025)[EC].',
    'REF_DOMANSKI_2025')

# ---------- 11) §6.3 adjuvantes ----------
app('- **Vitamina D** — benefício concentrado nos deficientes/curto prazo (Ghaemi 2024)[MA], com GRADE\n  muito baixa (Mikola 2023)[MA] e prevenção nula (Okereke 2020)[EC].',
    '\n- **[[AT]] Psicose (fronteira ilustrativa):** deficiências nutricionais são prevalentes no primeiro episódio psicótico e associam-se a piores correlatos clínicos (Firth 2018)[MA]; a suplementação de vitaminas/minerais em esquizofrenia mostra sinais adjuvantes modestos (Firth 2017)[MA] — janela de método (associação forte vs intervenção modesta), não escopo causal da B8.\n- **[[AT]] Suplementação pró-mitocondrial:** revisão sistemática dos desfechos clínicos de nutracêuticos que visam à função mitocondrial em transtornos psiquiátricos — campo heterogêneo, estudos pequenos, coerente com a ponte B8→B9 (Tortajada 2026)[OB].\n- **[[AT]] Ingestão com suplementação:** ingestão dietética combinada à suplementação de vitamina D, B6 e magnésio associou-se a melhor saúde mental em estudo observacional (Rajasekar 2024)[EC].',
    'REF_FIRTH_FEP_2018')

# ---------- 12) §7.5 MR ----------
app('lê-se como "causalidade potencial, não comprovada".',
    '\n\n[[AT 2026-09-09]] Novos estudos de randomização mendeliana reforçam a heterogeneidade: polimorfismos associados a micronutrientes mapeiam padrões distintos por par nutriente×transtorno (Hui 2024)[EC]; os efeitos estimados dos níveis séricos de B12 sobre transtornos psiquiátricos variam por desfecho (Lu 2025)[EC]; e a revisão sistemática com meta-análise da relação causal entre vitaminas B e transtornos neuropsiquiátricos conclui por relações distintas por par vitamina×transtorno — não há um "efeito geral do complexo B" (Ye 2025)[MA]. MR é evidência causal geneticamente instrumentada — **não** demonstra eficácia da suplementação (B8-CAUSAL-03).',
    'REF_HUI_2024')

# ---------- 13) BLOCO_08 pontes ----------
app('12. **B8↔B14–B16:** registros de borda a preencher quando esses módulos forem abertos.',
    '\n13. **[[AT 2026-09-09]] Atualização das pontes:** com a **B7**, a microbiota intestinal também **produz** vitaminas (K e complexo B) — potência subestimada na saúde psiquiátrica (Rudzki 2021)[OB] — e a interação microbioma–micronutriente é bidirecional (Barone 2022)[OB]; com a **B9**, "alimentar a mitocôndria" com componentes nutricionais ganhou revisão dedicada (Wesselink 2019)[OB], ao lado da revisão sistemática de suplementação pró-mitocondrial em psiquiatria (Tortajada 2026)[OB]; com a **B1**, estudo caso-controle registra interações micronutriente-imunes (vitamina C, ferro, zinco, magnésio e índices celulares periféricos) em transtornos de humor e psicóticos (Shahini 2026)[EC], e a revisão de nutrientes funcionais, sinalização de resiliência redox e neuroesteroides conecta a B8 à B6 e à B3 (Scuto 2024)[OB]. Cada ponte é **conexão entre mecanismos**, não duplicação (B8-CAUSAL-10).',
    'REF_RUDZKI_2021')

# ---------- 14) BLOCO_11 populacoes ----------
app('não há\n   preditor validado de "quem responde a suplemento".',
    '\n5. **[[AT 2026-09-09]] Por população:** obesidade — excesso calórico coexistindo com deficiência micronutricional paradoxal (Alexa 2026)[OB]; perinatal — revisão sistemática sobre micronutrientes e depressão no período (Islam 2025)[OB]; infância/adolescência — em 729 internados psiquiátricos jovens, folato insuficiente em 42,9% e B12 em 19,4%, com B12 insuficiente associado a transtornos depressivos (e B12 baixa ao espectro da esquizofrenia, fronteira) (Anmella 2025)[EC]; deficiências e suplementos em escolares e adolescentes revistos (Berger 2024)[OB]; e o papel dos micronutrientes no tratamento das doenças mentais pediátricas consolidado em revisão anual do campo (Rucklidge 2025)[OB].',
    'REF_ANMELLA_2025')

# ---------- 15) BLOCO_12 cenario F ----------
app('bipolar (NAC/CoQ10, atenção à maniabilidade)\n  `[EMERGENTE]`.',
    '\n- **Cenário F — "vitamina C para o humor":** a deficiência de vitamina C associa-se a alterações de humor e cognição, MAS a revisão sistemática não encontrou estudos de desfecho adequados demonstrando o efeito da reposição (Plevin 2020)[OB] — associação sem prova intervencional (B8-CAUSAL-02/04/09).',
    'REF_PLEVIN_2020')

# ---------- 16) CONTROVERSIAS ----------
app('2 PDFs cinzentos não indexados descartados.',
    '\n- **REGRAS CAUSAIS FIXADAS (rodada [AT] 2026-09-09 — insumo externo auditado, P-7):** as dez regras B8-CAUSAL foram incorporadas ao contrato desta biblioteca e protegem as formulações:\n  (01) deficiência não deve ser convertida automaticamente em causa do transtorno;\n  (02) associação entre micronutriente baixo e diagnóstico não demonstra que a deficiência precedeu ou causou o diagnóstico;\n  (03) MR representa evidência causal geneticamente instrumentada, não evidência de eficácia da suplementação;\n  (04) suplementação/reposição é pergunta causal diferente da associação entre status nutricional e doença;\n  (05) ingestão alimentar não equivale a deficiência bioquímica;\n  (06) biomarcador sérico não deve ser tratado automaticamente como deficiência funcional;\n  (07) evidência animal/celular não pode receber linguagem clínica sem ponte humana independente;\n  (08) é proibido o termo genérico "deficiência de micronutrientes" mascarar heterogeneidade — cada micronutriente×desfecho é um par específico;\n  (09) toda afirmação sobre suplementação deve ser sustentada por evidência intervencional específica;\n  (10) a relação B8→B6/B9/B3 (e demais módulos) registra-se como conexão entre mecanismos, não como duplicação.\n- **Vitamina C — lacuna intervencional explícita:** deficiência associada a humor e cognição, sem estudos de desfecho adequados de reposição (Plevin 2020)[OB].\n- **Vitamina D — eficácia antidepressiva não demonstrada:** estimativas agrupadas iniciais não sobrevivem à correção de viés de publicação; avaliação direcionada de status, não suplementação universal (Moroianu 2026)[MA].\n- **Formulações protegidas (P-7):** Badar 2022 é relato de caso — possibilidade clínica, não epidemiologia; Firth 2017/2018 e Cui 2021 tratam de psicose/esquizofrenia — fronteira ilustrativa de método, fora do escopo causal B8; McWilliams 2022 e Fiani 2023 tratam de neurodesenvolvimento (TDAH/TEA) — fronteira ilustrativa, TEA permanece na malha de escopo excluído; Radoeva 2025 usa juventude com TEA da coorte ABCD apenas para ilustrar que ingestão ≠ status; Du 2016 abrange TEPT — citado apenas pela mecânica mitocondrial (TEPT ≠ depressão ≠ ansiedade); Lahoda Brodska 2023 trata de transtornos neurológicos — aproveitamento seletivo da mecânica de micronutrientes, sem extrapolação de mecanismo neurológico; Horsdal 2025 é significativo para esquizofrenia/TEA/TDAH e **nulo para a TDM** — citado exatamente por isso.',
    'REF_CONTROVERSIAS')

# ---------- 17) TABELA ----------
app('| Mendelian randomization | MR tradicional nulo; ferro/cobre/25(OH)D sugestivos na recorrente (Carnegie; Fang) | emergente (MR≠RCT) |',
    '\n| MR de micronutrientes (2024–25) | Padrões distintos por par nutriente×transtorno (Hui; Lu; Ye) — MR mede associação instrumental, não absorção/risco da suplementação | emergente (MR≠RCT) |\n| Status no primeiro episódio psicótico | Deficiências prevalentes no FEP, piores correlatos clínicos (Firth 2018) | alto (associação; fronteira) |\n| Suplementação em esquizofrenia | Vitaminas/minerais adjuvantes — sinais modestos (Firth 2017) | baixo-médio (fronteira) |\n| Vitamina D — eficácia antidepressiva | Sinais iniciais colapsam ao nulo após trim-and-fill; suplementação de B12 esparsa e nula (Moroianu) | baixo-nulo (avaliação dirigida, não universal) |\n| Vitamina D neonatal × risco futuro | Inverso significativo p/ esquizofrenia/TEA/TDAH; **nulo para TDM** (n≈24 mil casos) (Horsdal) | emergente (associação; NEG no desfecho-âncora) |\n| Vitamina C | Deficiência ↔ humor/cognição; sem prova intervencional adequada (Plevin) | lacuna (sem evidência intervencional) |\n| Vitaminas B × neuropsiquiatria (causal) | Relações distintas por par vitamina×transtorno; sem efeito geral do "complexo B" (Ye) | emergente/heterogêneo |',
    'REF_TABELA')

# ---------- 18) MARCADORES ----------
app('vitamina D GRADE muito baixa; selênio).',
    ' Rodada [AT] 2026-09-09: +49 refs (49 ENTRA / 30 BAIXO / 12 EXC); regras B8-CAUSAL-01..10 fixadas (ver CONTROVÉRSIAS); fronteiras ilustrativas sinalizadas (psicose — Firth 2017/2018, Cui 2021; neurodesenvolvimento — Barks 2019/2021, McWilliams 2022, Fiani 2023, Mattei 2019; TEPT — Du 2016; neurológicos — Lahoda Brodska 2023); microbiota produz vitaminas (Rudzki 2021, ponte B7); complemento-sinapse/VDBP-megalin como hipótese D→depressão (Yang 2026); Horsdal 2025 nulo para TDM; vitamina C sem prova intervencional (Plevin 2020); eficácia antidepressiva da vitamina D não demonstrada (Moroianu 2026).',
    'REF_MARCADORES')

# ---------- 19) fecho ----------
old_fecho='''> **Canônica v1 (Consolidação, Rodada 3).** Portões: G1 (eutils, 96/96), G2
> (espécie/desenho/elegibilidade), G3 (suporte por vínculo; abstracts de alto risco lidos:
> VITAL-DEP D3/ômega-3, B12-nulo, selênio, Mg Rajizadeh/Tarleton, MR Carnegie, SMILES, metas de
> vitamina D). Prosa em (Autor, ano)[tag], sem número de PMID no texto. Causalidade animal é
> [ML]/[EXT] (Sartori/Kemp); MR é [EMERGENTE] e não é RCT; suplemento em não-deficiente não tem
> lastro (sem prescrição, P20); o padrão alimentar é a alavanca com melhor evidência. 2ª
> verificação independente (P-6) é pendência do avaliador cego.'''
new_fecho='''> **Canônica v2 (Rodada [AT] 2026-09-09 — reconciliação de insumo externo, P-7).** 96→145
> referências (49 ENTRA — 41 masters GPM + Bourre 2006, Mattei 2019, Moore 2019, Ferriani 2022,
> Kohl 2025, Islam 2025, Yang 2026 e Horsdal 2025 —; 30 BAIXO; 12 EXC pela malha de escopo:
> autismo ×5, neurodegeneração ×2, anorexia, epilepsia, delirium, botânica e demência/AVC). Os 7
> erros factuais do briefing externo foram revertidos e expostos (Mattei ≠ McWilliams; Yoon;
> Dehesh; Cortés-Albornoz; Das; Bourre dado como não indexado — é o artigo-âncora Parte 1; Wang
> 2018 já vigente). Portões: G1 (eutils, 145/145), G2 (espécie/desenho/elegibilidade), G3 (suporte
> por vínculo; abstracts de alto risco lidos, incl. Moroianu, Plevin, Horsdal e os MRs). Prosa em
> (Autor, ano)[tag], sem número de PMID/DOI no texto. Regras B8-CAUSAL-01..10 fixadas em
> CONTROVÉRSIAS e protegem as formulações. Fronteiras ilustrativas citadas sem extrapolação causal
> (psicose: Firth 2017/2018, Cui 2021; neurodesenvolvimento: Barks 2019/2021, McWilliams 2022,
> Fiani 2023, Mattei 2019; TEPT: Du 2016; neurológicos: Lahoda Brodska 2023); TEA/TEPT/anorexia
> seguem fora do escopo. Badar 2022 é relato de caso. MR (Carnegie, Fang, Hui, Lu, Ye) ≠ eficácia
> de suplementação. Vitamina C sem prova intervencional (Plevin 2020); eficácia antidepressiva da
> vitamina D não demonstrada (Moroianu 2026); Horsdal 2025 nulo para TDM. Causalidade animal
> permanece [ML]/[EXT] (Sartori/Kemp). 2ª verificação independente (P-6) permanece pendência do
> avaliador cego.'''
rep(old_fecho,new_fecho,'fecho')

# ---------- 20) listras-resumo ----------
rep('Rai2017_MTHFR_pos[MA] | Papakostas2012_LMethylfol[EC]*',
    'Rai2017_MTHFR_pos[MA] | Papakostas2012_LMethylfol[EC]*','listra00')  # sem ancora extra no BLOCO_00 (placebo replace p/ assert)
rep('*Bottiglieri2000_homocisteina[EC] | Bottiglieri2005_review[OB] | Coppen2005_B12folato[OB] | Almeida2008_homocis_idoso[MA] | Gilbody2007_folato_meta[MA] | Bender2017_folato_meta[MA] | Petridou2016_B12idoso[MA] | Markun2021_B12_nulo[MA] | Tarleton2019_Mg_soro[EC] | Han2025_complexoB[OB] | Gao2025_defic_idoso[OB] | Wang2018_ZnMgSe[OB] | Johnson2013_Se_agua[EC] | Wang2023_antiox_meta[MA] | Carnegie2024_MR_TDM[EC] | Appleton2010_n3_meta[MA] | Su2018_n3_ansiedade[MA] | Liao2019_n3_meta[MA] | Fleig2026_n3_review[OB] | Okereke2021_VITAL_n3[EC] | Kemp2024_Fe_n3_dev[ML] | Kouba2022_D_mecanismo[OB] | Anglin2013_D_meta[MA] | Ghaemi2024_D_dose[MA] | Mikola2023_D_meta[MA] | Srifuengfung2023_D[MA] | Musazadeh2023_D_umbrella[MA] | Wang2025_D_meta[MA] | Okereke2020_VITAL_D3[EC] | Kim2014_ferro[OB] | Sartori2012_Mg_ansiedade[ML] | Wu2022_ingestaoB[EC] | Nguyen2022_B1B3[EC] | Xu2024_tiamina[EC]*',
    '*Bottiglieri2000_homocisteina[EC] | Bottiglieri2005_review[OB] | Coppen2005_B12folato[OB] | Almeida2008_homocis_idoso[MA] | Gilbody2007_folato_meta[MA] | Bender2017_folato_meta[MA] | Petridou2016_B12idoso[MA] | Markun2021_B12_nulo[MA] | Tarleton2019_Mg_soro[EC] | Han2025_complexoB[OB] | Gao2025_defic_idoso[OB] | Wang2018_ZnMgSe[OB] | Johnson2013_Se_agua[EC] | Wang2023_antiox_meta[MA] | Carnegie2024_MR_TDM[EC] | Appleton2010_n3_meta[MA] | Su2018_n3_ansiedade[MA] | Liao2019_n3_meta[MA] | Fleig2026_n3_review[OB] | Okereke2021_VITAL_n3[EC] | Kemp2024_Fe_n3_dev[ML] | Kouba2022_D_mecanismo[OB] | Anglin2013_D_meta[MA] | Ghaemi2024_D_dose[MA] | Mikola2023_D_meta[MA] | Srifuengfung2023_D[MA] | Musazadeh2023_D_umbrella[MA] | Wang2025_D_meta[MA] | Okereke2020_VITAL_D3[EC] | Kim2014_ferro[OB] | Sartori2012_Mg_ansiedade[ML] | Wu2022_ingestaoB[EC] | Nguyen2022_B1B3[EC] | Xu2024_tiamina[EC] | Bourre2006_requisitos_cerebro[OB] | Sahu2022_B12_neuropsiquiatria[OB] | Mathew2024_B12_nervoso[OB] | Badar2022_B12_relato_caso[EC] | Moore2019_TUDA_Bvit_idoso[EC] | Ferriani2022_ELSA_antiox_B[EC] | Kennedy2016_Bvit_cerebro[OB] | Nogueira2023_neuronutrientes_SNC[OB] | Muscaritoli2021_nutrientes_mente[OB] | Du2016_nutrientes_mitocondria[OB] | LahodaBrodska2023_neurologicos_fronteira[OB] | Eyles2013_D_neurodesenv[OB] | Cui2021_D_esquizofrenia_fronteira[OB] | Yang2026_D_complemento_megalin[OB]*',
    'listra01')
rep('*Bottiglieri2000_homocisteina[EC] | Almeida2008_homocis_idoso[MA] | Kouba2022_D_mecanismo[OB] | Anglin2013_D_meta[MA] | Mikola2023_D_meta[MA] | Ghaemi2024_D_dose[MA] | Okereke2020_VITAL_D3[EC] | Swardfager2013_Zn_review[OB] | Li2026_Zn_homeostase[OB] | Sartori2012_Mg_ansiedade[ML] | Varga2025_Mg_review[OB] | Kemp2024_Fe_n3_dev[ML] | Kim2014_ferro[OB]*',
    '*Bottiglieri2000_homocisteina[EC] | Almeida2008_homocis_idoso[MA] | Kouba2022_D_mecanismo[OB] | Anglin2013_D_meta[MA] | Mikola2023_D_meta[MA] | Ghaemi2024_D_dose[MA] | Okereke2020_VITAL_D3[EC] | Swardfager2013_Zn_review[OB] | Li2026_Zn_homeostase[OB] | Sartori2012_Mg_ansiedade[ML] | Varga2025_Mg_review[OB] | Kemp2024_Fe_n3_dev[ML] | Kim2014_ferro[OB] | Rajen2025_folato_status[EC] | Faugere2025_D_B9_B12_gravidade[EC] | AlJassem2024_B12_Libano[EC] | Kohl2025_D_mulheres_CMD[EC] | Horsdal2025_D_neonatal_NuloTDM[EC] | Skoczek2025_D_BDNF_humor[OB] | Moroianu2026_D_B12_meta[MA] | Shayganfard2022_oligoelementos[OB] | Astorino2025_trace_etiologia[OB] | Faa2025_Zn_homeostase[OB] | Barks2019_ferro_modelo[OB] | Barks2021_ferro_epigenoma[OB] | McWilliams2022_neurodesenv_scoping[OB] | Fiani2023_ferro_neurodesenv[OB] | Mattei2019_desenvolvimento[OB]*',
    'listra02')
rep('Lassale2019_dieta_meta[MA] | Jacka2017_SMILES[EC] | Sartori2012_Mg_ansiedade[ML] | Mikola2023_D_meta[MA]*',
    'Lassale2019_dieta_meta[MA] | Jacka2017_SMILES[EC] | Sartori2012_Mg_ansiedade[ML] | Mikola2023_D_meta[MA] | Plevin2020_vitC_SR[OB]*','listra03')
rep('Kouba2022_D_mecanismo[OB]*\n\n---\n\n## BLOCO_05',
    'Kouba2022_D_mecanismo[OB]*\n\n---\n\n## BLOCO_05','listra04')  # placebo: BLOCO_04 sem novos
rep('Wu2022_ingestaoB[EC] | Hajhashemy2025_Mg_ingestao[MA]*',
    'Wu2022_ingestaoB[EC] | Hajhashemy2025_Mg_ingestao[MA] | Domanski2025_hematologico_preditores[EC] | Radoeva2025_ABCD_ingestao[EC]*',
    'listra05')
rep('Hoepner2021_intervencoes[OB] | Sajjadi2022_Se_meta[MA]*',
    'Hoepner2021_intervencoes[OB] | Sajjadi2022_Se_meta[MA] | Firth2018_FEP_status[MA] | Firth2017_supl_esquizofrenia[MA] | Tortajada2026_mito_SR[OB] | Rajasekar2024_D_B6_Mg[EC]*',
    'listra06')
rep('Kemp2024_Fe_n3_dev[ML] | Carnegie2024_MR_TDM[EC] | Fang2025_MR_ansiedade[EC]*',
    'Kemp2024_Fe_n3_dev[ML] | Carnegie2024_MR_TDM[EC] | Fang2025_MR_ansiedade[EC] | Hui2024_SNP_MR[EC] | Lu2025_B12_MR[EC] | Ye2025_Bvit_causal_meta[MA]*',
    'listra07')
rep('Sartori2012_Mg_ansiedade[ML] | Kouba2022_D_mecanismo[OB] | Fleig2026_n3_review[OB]*',
    'Sartori2012_Mg_ansiedade[ML] | Kouba2022_D_mecanismo[OB] | Fleig2026_n3_review[OB] | Rudzki2021_microbiota_vitaminas[OB] | Barone2022_microbioma_micronutriente[OB] | Wesselink2019_mitocondria_nutricao[OB] | Shahini2026_imune_micronutriente[EC] | Scuto2024_redox_neuroesteroides[OB]*',
    'listra08')
rep('Sliwinski2024_Bmetab[EC] | Carnegie2024_MR_TDM[EC] | Fang2025_MR_ansiedade[EC]*',
    'Sliwinski2024_Bmetab[EC] | Carnegie2024_MR_TDM[EC] | Fang2025_MR_ansiedade[EC] | Hui2024_SNP_MR[EC] | Lu2025_B12_MR[EC] | Ye2025_Bvit_causal_meta[MA]*',
    'listra8x')
rep('Almeida2008_homocis_idoso[MA] | Gao2025_defic_idoso[OB]*',
    'Almeida2008_homocis_idoso[MA] | Gao2025_defic_idoso[OB] | Alexa2026_obesidade_paradoxo[OB] | Islam2025_perinatal_SR[OB] | Anmella2025_B12_jovens_internados[EC] | Berger2024_escolares_adolescentes[OB] | Rucklidge2025_pediatria_review[OB]*',
    'listra11')
rep('Johnstone2020_multinutri_meta[MA]*',
    'Johnstone2020_multinutri_meta[MA] | Plevin2020_vitC_SR[OB]*',
    'listra12')

# ---------- aplica ----------
erros=[]
for modo,anc,new,key in OPS:
    c=doc.count(anc)
    if c!=1:
        erros.append((key,anc[:80],c))
if erros:
    for e in erros: print('FALHA ANCORA',e)
    raise SystemExit(2)

for modo,anc,new,key in OPS:
    if modo=='replace':
        doc=doc.replace(anc,new,1)
    else:
        doc=doc.replace(anc,anc+new,1)
    if key:
        trechos_ancora[key]=new if len(new)<1200 else new[:1200]

# varredura: 7-9 digitos (PMID no texto) — permitidos apenas IDs exame_/anos
hits=re.findall(r'(?<![\w.])\d{7,9}(?![\w.])', doc)
hits=[h for h in hits]
assert not hits, ('PMID/DIGITOS NO TEXTO', hits[:10])

# regras B8-CAUSAL presentes 1x bloco
assert doc.count('B8-CAUSAL-02')>=2, doc.count('B8-CAUSAL-02')
assert doc.count('[[AT 2026-09-09]]')==11, doc.count('[[AT 2026-09-09]]')
for n in ['01','02','03','04','05','06','07','08','09','10']:
    assert f'({n}) ' in doc, ('regra ausente', n)

# rotacao V1 -> historico
os.makedirs(f'{BASE}/producao/historico', exist_ok=True)
shutil.copy2(V1, f'{BASE}/producao/historico/v1_canonica_2026-09-09.md')
open(V2,'w',encoding='utf-8').write(doc)
os.remove(V1)

json.dump(trechos_ancora, open(f'{BASE}/producao/insumos/b8_trechos_ancora.json','w'), ensure_ascii=False, indent=1)

print('OK — V2 gravada:', len(doc), 'chars; ~', len(doc.split()), 'palavras')
print('rotulos AT:', doc.count('[[AT 2026-09-09]]'))
print('refs-rotulo listras OK; digitos 7-9:', len(hits))
