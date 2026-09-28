# -*- coding: utf-8 -*-
"""B10 rodada [AT] 2026-09-09 — fusão GPM externo auditado (P-7) na canônica V1 -> V2."""
import re, json, sys, shutil

P = "/home/user/BIBLIOTECAS/B10_DesregulacaoCircadiana/B10 DESREGULACAO CIRCADIANA V1 CANONICA.md"
doc = open(P, encoding='utf-8').read()
orig_len = len(doc)

def sub(anc, new, count=1):
    global doc
    assert doc.count(anc) == 1, f"âncora não-única ({doc.count(anc)}×): {anc[:70]!r}"
    doc = doc.replace(anc, new)

# ---------- 1) cabeçalho ----------
sub("# B10 DESREGULAÇÃO CIRCADIANA V1 CANÔNICA",
    "# B10 DESREGULAÇÃO CIRCADIANA V2 CANÔNICA")
sub("**artefato_rotulo:** CANÔNICA v1 · G1 (39 PMIDs eutils, autor+ano+tema validado) + G2 + G3.",
    "**artefato_rotulo:** CANÔNICA v2 · G1 (137 PMIDs eutils, autor+ano+tema validado) + G2 + G3 · fusão [AT] GPM rodada externa 2026-09-09 (+98 refs auditadas ref a ref, P-7).")
sub("**ID canônico:** mecanismo_B10_desregulacao_circadiana · **Prompt v4.2** · Corte: 2026-09-06.",
    "**ID canônico:** mecanismo_B10_desregulacao_circadiana · **Prompt v4.2** · Corte: 2026-09-06.\n**Fusão [AT] 2026-09-09:** GPM molde v2.0 (M00–M10) + dossiê RODADA0 + matriz RC.SM02.001–058, reconciliados ref a ref (P-7).")

# ---------- 2) BLOCO_01 — TTFL em detalhe ----------
anc1 = "O transplante de SCN determina o período (Ralph 1990)[ML]."
b1 = anc1 + "\n\n### 1.1a [[AT 2026-09-09]] TTFL — a arquitetura molecular em detalhe (camada 1)\nA química do laço é causal e está entre as melhores documentadas da neurociência: a repressão por\nretroalimentação é obrigatória para a função do relógio (Sato 2006)[ML]; CRY1/CRY2 são componentes\nessenciais do braço negativo (Kume 1999)[ML]; o modelo bioquímico canônico foi reconstituído in\nvitro (Ye 2011)[ML], com CRY e PER inibindo CLOCK:BMAL1 por dois modos (Ye 2014)[ML] e feedback\nnegativo via complexos repressivos macromoleculares (Duong 2011)[ML]; (Aryal 2017)[OB]. A montagem\ndo complexo PER–CRY é etapa estrutural própria (Nangle 2014)[ML], mediada pelo bolso secundário de\nCRY1 (Michael 2017)[ML] e por interações dinâmicas com o C-terminal de BMAL1 (Xu 2015)[ML]. No\nbraço ativador, CLOCK–BMAL1 realimenta o maquinário basal de transcrição (Lande-Diner 2013)[ML] e\na transcrição rítmica do próprio Bmal1 estabiliza o sistema (Abe 2022)[ML]; o relógio incorpora\nainda o componente de núcleo CHRONO (Goriki 2014)[ML]. Pós-tradução: a fosforilação de CLOCK/BMAL1\né mecanismo regulador chave (Otobe 2026)[OB] e CK1δ nuclear é determinante crítico da dinâmica do\ncomplexo PER:CRY e do período (Serrano 2026)[ML]. Do núcleo saem os genes de saída tecido-\nespecíficos — o mapa original de saída CLOCK-dependente no fígado (Oishi 2003)[ML] — com revisões\nconsolidando a arquitetura (Takahashi 2015)[OB]."
sub(anc1, b1)

# ---------- 3) BLOCO_01 — SCN rede + fótica ----------
b2 = b1 + "\n\n### 1.1b [[AT 2026-09-09]] SCN como rede — acoplamento, entrada fótica e variabilidade (camada 2)\nO SCN é um conjunto de osciladores com autonomia celular **e** propriedades de rede (Mohawk\n2011)[OB]; (Welsh 2010)[OB]: a imagem dual em célula única revela papel circadiano na sincronia da\nrede (Shan 2020)[ML], consolidado na retrospectiva de 50 anos do núcleo (Ono 2024)[OB]. A entrada\nfótica usa projeções retinianas mapeadas até o marcapasso (Fernandez 2016)[ML] e fisiologia de\nentrançamento de referência (Golombek 2010)[OB]; neurônios VIP são essenciais ao reajuste luminoso\n(Jones 2018)[ML] e sinalizam via ERK1/2–DUSP4 (Hamnett 2019)[ML], enquanto NPAS4 estrutura a\nresposta transcricional do SCN à luz (Xu 2021)[ML] e CREB é interface molecular dos estímulos de\nfase (Von Gall 1998)[ML]. A resposta da área supraquiasmática humana à luz varia entre indivíduos\ne é mapeável por fMRI (McGlashan 2018)[EC]. Fora do núcleo, osciladores centrais e periféricos\nconversam (Schibler 2015)[OB], com retroalimentação periférica promovendo sincronia e saúde\n(Ramkisoensing 2015)[OB] e laços coexistentes gerando ritmos tecido-específicos (Pett 2018)[ML]. A\nluz também fala com o HPA por atalho: em roedor, estimula a adrenal por via retino-hipotalâmica\nindependente do relógio do SCN (Kiessling 2014)[ML]; em humano, o comprimento de onda influencia os\nritmos do eixo (Robertson-Dixon 2023)[OB], com corroboração pré-clínica em meta-análise\n(Robertson-Dixon 2026)[OB]."
sub(b1, b2)

# ---------- 4) BLOCO_02 — HPA circadiano ----------
anc4 = "base para o risco de\nturno/*jet lag*."
b3 = anc4 + "\n\n### 2.4 [[AT 2026-09-09]] O eixo HPA como saída rítmica nuclear (camada 3)\nA integração relógio↔HPA é bidirecional: o HPA tem ritmicidade circadiana própria acoplada ao\nrelógio (Nicolaides 2014)[OB]; (Nader 2010)[OB]; (Kalsbeek 2012)[OB]; (Spiga 2014)[OB], com\nosciladores biológicos coordenando estresse e adaptação neurocomportamental (Russell 2015)[OB] —\nfeedback glicocorticoide e pulsatilidade são escopo B2. Modelos de sistemas endossam o significado\nfisiológico da dinâmica circadiana do HPA e suas trocas alostáticas (Rao & Androulakis 2019a)[OB];\n(Rao & Androulakis 2019b)[OB], inclusive sob restrição crônica de sono (Rao 2021)[OB]. Em humano:\no horário do estressor modifica a resposta aguda do eixo (Yamanaka 2019)[EC]; o sono influencia a\nreatividade do HPA em revisão sistemática (van Dalfsen & Markus 2018)[OB]; parâmetros diurnos de\ncortisol se associam a reatividade/recuperação em meta-análise (Wesarg-Menzel 2024)[OB]; a relação\nsono–HPA é clássica (Buckley 2005)[OB]; e a dinâmica pulsátil de ACTH/cortisol é referência\nfisiológica com implicações para doença (Lightman 2020)[OB]. Em modelo: padrões circadiano/\nultradiano do HPA em roedor orientam a leitura funcional (den Boon & Sarabdjitsingh 2017)[OB]; o\ndesalinhamento experimental (turno simulado) aumenta a vulnerabilidade de humor em humano\n(Chellappa 2020)[EC]; e, no estresse leve crônico, a atividade circadiana do HPA é diferencialmente\nafetada nos animais que desenvolvem fenótipo depressivo (Christiansen 2012)[ML]. O relógio↔HPA é\nsubstrato de resiliência (Kinlein & Karatsoreos 2020)[OB]."
sub(anc4, b3)

# ---------- 5) BLOCO_02 — evidência clínica ----------
b4 = b3 + "\n\n### 2.5 [[AT 2026-09-09]] Fase, cronotipo e a evidência clínica humana (camada 4)\nEm jovens com depressão unipolar, marcadores circadianos definem **subgrupos fisiopatológicos** com\nperfis psiquiátricos distintos (Robillard 2018)[EC]; a cronotipagem molecular in vivo mostra altas\ntaxas de depressão quando fase endógena e ambiente não concordam (Nguyen 2019)[EC]; e a ritmicidade\ndos sintomas de humor já aparece em indivíduos de risco (Pilz 2018)[EC]. O afeto tem ritmo próprio\n— pico noturno de afeto negativo coincidente ao vale do afeto positivo (Emens 2020)[EC]. No\ntranstorno de fase atrasada do sono (DSPD), o subtipo **circadiano** (DLMO desalinhado) carrega\nmais sintomas depressivos que o não-circadiano — e quase metade dos casos clínicos não mostra\ndesalinhamento: distúrbio de estado ≠ distúrbio de *timing* (Murray 2017)[EC]. Em escala\npopulacional, ritmicidade disruptiva se associa a transtornos de humor, bem-estar e cognição (Lyall\n2018)[EC]; dados longitudinais de wearables permitem modelar a dinâmica causal diária sono–fase–\nhumor (Song 2024)[EC]. Ansiedade tem lastro próprio: a relação cronotipo–ansiedade persiste\ncontrolando distúrbio de sono e afeto negativo (Cox & Olatunji 2019)[EC]. E em jovens com\ntranstornos de humor emergentes há **desalinhamento interno** entre marcadores de fase — DLMO vs\npico de cortisol (Carpenter 2025)[EC]."
sub(b3, b4)

# ---------- 6) BLOCO_03 — genética ----------
anc6 = "BDNF/CREB/GSK3β rítmicos (B3)."
b5 = anc6 + "\n\n### [[AT 2026-09-09]] Genética humana dos genes-relógio — associação, não causação\nA varredura de genes circadianos em transtornos do humor achou sinais diferenciais — CRY1 e NPAS2\ncom depressão unipolar, CLOCK e VIP com bipolar (Soria 2010)[EC] —, mas o panorama genômico é de\ninconsistência entre estudos, sem gene-relógio replicado como determinante (von Schantz 2021)[OB].\nModelagens sugerem como polimorfismos de relógio poderiam se conectar a humor (Liberman 2018)[OB]\ne variação funcional na via REV-ERBα se associa à resposta ao lítio no bipolar (McCarthy 2011)[EC].\nLeitura disciplinar: associação genética sinaliza **vulnerabilidade circadiana**; não demonstra que\na alteração rítmica cause o transtorno — vale a assimetria com a causalidade animal."
sub(anc6, b5)

# ---------- 7) BLOCO_05 — exposição luminosa objetiva ----------
anc7 = "Cortes e horários de luz/melatonina ficam no módulo operacional, não aqui."
b6 = anc7 + "\n\n### 5.y [[AT 2026-09-09]] Exposição luminosa objetiva (contexto ambiental, não marcador de fase)\nA luz à noite como exposição ambiental mensurável se associa a indicadores de saúde mental em\nrevisão sistemática/meta-análise, com métodos de avaliação de exposição ainda em evolução (Deprato\n2025)[OB] — é contexto ambiental mensurável, **não** marcador de fase e não teste diagnóstico."
sub(anc7, b6)

# ---------- 8) BLOCO_06 — cronoterapia sinal ----------
anc8 = "Qualquer intervenção rítmica é sinal de direção, não conduta."
b7 = anc8 + "\n\n**[[AT 2026-09-09]] Realinhamento circadiano — o que a revisão sistemática endossa:** intervenções\ncronoterapêuticas podem melhorar a depressão, sobretudo com atraso circadiano basal e depressão\nelevada; mas poucos estudos mediram a fase fisiológica, de modo que **não está demonstrado** que a\nmudança de fase seja o mediador necessário do efeito antidepressivo (Wescott 2025)[OB]. Fototerapia\ntem alcance além do sazonal em revisão clássica (Campbell 2017)[OB] — sempre como sinal de direção;\nprotocolos pertencem ao módulo terapêutico (P20)."
sub(anc8, b7)

# ---------- 9) BLOCO_07 — cadeias causais novas ----------
anc9 = "6. **Regra anti-prescrição:** mecanismo rítmico robusto ≠ terapia com dose/horário prescritos."
b8 = anc9 + "\n7. **[[AT 2026-09-09]] Cadeias causais experimentais incorporadas nesta rodada [ML]:**\n   - o knockout de *Per2* desorganiza a corticosterona e produz comportamento tipo-depressivo com\n     déficit de startle (Russell 2021)[ML];\n   - o desalinhamento crônico (fotoperíodo variável) eleva Bmal1 oligodendroglial, inibe AKT/mTOR e\n     reduz a mielinização em PFC/hipocampo, gerando fenótipo tipo ansiedade/depressão (Zuo\n     2024)[ML];\n   - a microbiota intestinal regula a responsividade ao estresse através do sistema circadiano\n     (ritmicidade do HPA) (Tofani 2025)[ML] — ponte B7;\n   - a regulação de humor/ansiedade pelo relógio é **tipo-celular específica** (Francis 2023)[ML];\n   - a melatonina reajusta o relógio do SCN ao entardecer via transcrição E-box de Per1/Per2\n     (Kandalepas 2016)[ML]."
sub(anc9, b8)

# ---------- 10) BLOCO_08 — pontes ----------
anc10 = "sinalizado como bipolar, nunca fundido à TDM."
b9 = anc10 + "\n\n### [[AT 2026-09-09]] Pontes reforçadas nesta rodada\n- **B10↔B2 sobe ao nível mais denso da biblioteca:** o HPA como saída rítmica (bloco 2.4) consolida\n  Nicolaides/Nader/Kalsbeek/Spiga/Russell/Rao & Androulakis/Lightman (todas [OB]).\n- **B10↔B7 (microbiota) — HIGH-emergente e mecanística em modelo:** o registro experimental de\n  Tofani acima e a revisão crítica do eixo intestino–cérebro–circadiano em ansiedade/depressão\n  (Bautista 2025)[OB] — com a barreira honesta: disbiose→depressão humana via relógio **não\n  demonstrada**.\n- **B10↔B3/B15 (plasticidade/mTOR):** o eixo Bmal1→AKT/mTOR→mielina de Zuo (bloco 07).\n- **B10↔B12:** quebra de ritmo/turno como fator de contexto (bloco 2.4, trabalho por turnos\n  simulado)."
sub(anc10, b9)

# ---------- 11) BLOCO_11 — bipolar corpus ----------
anc11 = "5. **Ansiedade com lastro próprio:** NAc Per/Npas2 (animal); insônia como fator bidirecional\n   (Riemann 2019)[OB]."
b10 = anc11 + "\n6. **[[AT 2026-09-09]] Bipolar — o corpus clínico mais denso do mecanismo:** cronotipo/ritmo em\n   revisão sistemática (Melo 2017)[OB]; curso clínico do ritmo (Takaesu 2018)[OB]; desregulação no\n   espectro (Alloy 2017)[OB]; fase **avançada** na mania e **atrasada** na depressão bipolar/mista\n   com normalização pós-tratamento (Moon 2016)[EC]; cronotipo tardio prediz mais sintomas\n   depressivos em seguimento de cinco anos (Vidafar 2021)[EC]; ritmos de atividade associados a\n   recaída em coorte prospectiva (Esaki 2021)[EC]; cortisol diurno desregulado com elevação noturna\n   (Mukherjee 2022)[EC]; disfunção rítmica e psicopatologia em descendentes de pais bipolares (Lei\n   2024)[EC]; meta-análise em alto risco/início precoce (Scott 2022)[OB]; alterações rítmicas\n   ligadas a resiliência e desregulação emocional em episódio depressivo (Palagini 2022)[EC];\n   consenso multidisciplinar da task force ISBD (McCarthy 2022)[OB]; cronobiologia dos transtornos\n   do humor em revista de referência (Geoffroy & Maruani 2025)[OB]; revisão contemporânea de genes-\n   relógio e tratamento cronobiológico (Chakraborty 2026)[OB]; e da psicopatologia à fenotipagem\n   digital (Tonon 2024)[OB]. Sempre sinalizado como bipolar, nunca fundido à TDM."
sub(anc11, b10)

# ---------- 12) BLOCO_12 — sínteses da rodada ----------
anc12 = "- Outras condições (esquizofrenia, turno/obesidade, Alzheimer, TDAH) entram só como\n  estudo-ponte `[EXTRAPOLADO]`."
b11 = anc12 + "\n\n### [[AT 2026-09-09]] Sínteses que enquadram a rodada\nA interface sono–circadiano como janela para os transtornos mentais (Meyer 2024)[OB]; o sono como\ncontribuinte ativo — não mero sintoma — do curso psiquiátrico (Hyndych 2025)[OB]; cronotipo e ritmo\nnos transtornos psiquiátricos, evidências e mecanismos (Zou 2022)[OB]; a disrupção circadiana e a\nsaúde mental como campo (Walker 2020)[OB]; e o convite programático do campo (Dollish 2024)[OB];\n(McClung 2007)[OB]; (McClung 2013)[OB]; (Lamont 2007)[OB]; (Kırıloğlu 2020)[OB]; (Smith 2024)[OB];\n(Pandi-Perumal 2022)[OB]; com relógios centrais e periféricos relacionados ao humor (Ketchesin\n2020)[OB]."
sub(anc12, b11)

# ---------- 13) CONTROVÉRSIAS ----------
anc13 = "e ficou como revisão coberta\n  por Mohawk 2012."
b12 = anc13 + "\n\n### [[AT 2026-09-09]] — regras fundadoras e inventário negativo fixados nesta rodada\n1. ***timing* ≠ *estado*:** o sono é *output* da rede temporal (fase/amplitude/período/estabilidade/\n   sincronização); insônia é distúrbio de **estado**, não sinônimo — o subtipo DSPD circadiano vs\n   não-circadiano do bloco 2.5 é a demonstração clínica.\n2. **Não há biomarcador circadiano único validado para diagnóstico** (endossado pela revisão de\n   referência de Geoffroy & Maruani): DLMO, actigrafia e genes-clock periféricos seguem de pesquisa.\n3. **Causalidade assimétrica:** animal causal (ClockΔ19, Bmal1-SCN, Per2-KO, Npas2, relógio-mPFC) vs\n   humana majoritariamente associativa/preditiva; genética humana de genes-relógio inconsistente e\n   sem determinante replicado (bloco BLOCO_03-AT).\n4. **Intervenção ≠ mediador demonstrado:** o realinhamento melhora a depressão em subgrupos, mas a\n   mediação pela fase fisiológica não está provada (bloco BLOCO_06-AT) — cronoterapia segue sinal.\n5. **Melatonina ≠ antidepressivo:** marcador de fase/saída; agomelatina é fármaco (módulo próprio).\n6. **[ML] é roedor/modelo:** oligodendrócito-Bmal1, microbiota-HPA, Per2-KO e tipo-celular são\n   extrapolação por analogia com tradução humana pendente — nunca recomendação.\n7. **Descartes desta rodada (expostos):** Burns 2024 é registro medRxiv (preprint indexado no\n   PubMed — não entra como evidência canônica); Burns 2022/2023 e Mendoza 2024 (Nature Mental\n   Health) NAO-IDX → [G1]; Sandate 2020 (cristalografia) e Palagini 2023 (resumo de congresso)\n   NAO-IDX; fontes predatórias/não indexadas (Cao 2025; Gosztyła 2026; Noweta 2026; You 2024; Feng\n   2025; Rumanova 2020; Albrecht 2012) EXC; Serrano-Serrano 2021 (amostra com transtorno por uso de\n   substância) e Boiko 2022 (pós-COVID) BAIXO por malha de escopo; Sassone-Corsi 2016 (capítulo de\n   manual) BAIXO — arquitetura já coberta por artigos de revista.\n8. **Correções do insumo externo (P-7), revalidadas aqui:** Palagini 2022 real resgatado (o dossiê\n   o confundira com Pandi-Perumal); Rao 2021 recebeu o PMID do Robertson-Dixon 2023 no dossiê\n   (resolvido); Spiga 2014 **é** indexada (o dossiê dizia NAO-IDX); anos canônicos pelo print\n   (McCarthy 2022; Dollish 2024; Ketchesin 2020; Kinlein & Karatsoreos 2020; van Dalfsen & Markus\n   2018; Kırlıoğlu 2020).\n9. **Pendências honestas:** Satyanarayanan 2020 (agomelatina) segue sem resolução [G1]; Mendoza\n   2024 [G1]; DLMO/fase fisiológica como desfecho em ensaios; GRADE formal. P-6 (2ª verificação\n   cega, avaliador externo) pendente — sem autocertificação."
sub(anc13, b12)

# ---------- 14) TABELA ----------
anc14 = "| Intervenção rítmica | Luz/wake/IPSRT (sinal, não conduta nesta biblioteca) | emergente/médio |"
b13 = anc14 + "\n| [[AT]] Genética-clock humana | Sinais diferenciais (CRY1/NPAS2 vs CLOCK/VIP); inconsistência; REV-ERBα×lítio | baixo-médio [EC]/[OB] |\n| [[AT]] Cronoterapia (revisão sistemática) | Realinhamento melhora depressão em subgrupos; mediador de fase não demonstrado | médio [OB] |\n| [[AT]] Dinâmica temporal (wearables) | Modelagem diária sono–fase–humor em pacientes | emergente [EC] |\n| [[AT]] Luz×HPA | Comprimento de onda influencia ritmos do HPA (humano RS; animal meta) | médio [OB] |\n| [[AT]] Microbiota→relógio→HPA | Ritmicidade do HPA e responsividade ao estresse reguladas pela microbiota | alto em modelo [ML] |\n| [[AT]] Relógio→oligodendrócito/mielina | Bmal1↑→AKT/mTOR↓→mielinização↓→fenótipo afetivo | alto em modelo [ML] |\n| [[AT]] DSPD circadiano vs não-circadiano | Subtipo circadiano carrega mais depressão; quase metade sem desalinhamento | médio [EC] |"
sub(anc14, b13)

# ---------- 15) APÊNDICE ----------
anc15 = "*OZBURN_2017[ML] | VADNIE_2017[OB] | SCHUCH_2018[MA] | HASTINGS_2018[OB] | FERNANDEZ_2018[MA] | LOGAN_2019[OB] | FONKEN_2019[OB] | CARMASSI_2019[OB] | RIEMANN_2019[OB] | COLEMAN_2019[MA] | CROUSE_2021[OB] | LIANG_2025[ML] | GEOFFROY_2025[OB] | GARDNER_2026[ML]*"
refs_data = json.load(open('/home/user/BIBLIOTECAS/B10_DesregulacaoCircadiana/producao/insumos/b10_refs_data.json'))
listra = " | ".join(f"{r['id_referencia_interna'][4:]}[{r['_tag']}]" for r in refs_data)
b14 = anc15 + "\n*[[AT 2026-09-09]] " + listra + "*"
sub(anc15, b14)

# ---------- 16) fecho ----------
anc16 = "externo."
b16 = anc16 + "\n\n> **Canônica v2 (Rodada [AT] 2026-09-09 — insumo externo auditado, P-7).** 98 referências novas\n> reconciliadas ref a ref (esearch DOI[aid]/PMID + esummary + efetch; abstracts lidos nos claims\n> direcionais): TTFL/SCN/luz (camadas 1–2), HPA circadiano (camada 3), clínica humana (camada 4),\n> genética, bipolar, causal experimental e sínteses. Falso-positivo exposto: Burns 2024 é preprint\n> medRxiv (não entra). Correções do dossiê externo aplicadas e registradas (Palagini 2022; Rao 2021;\n> Spiga 2014; anos de print). NAO-IDX declarados. P-6 segue pendência honesta do avaliador externo."
sub(anc16, b16)

# ---------- VARREDURAS ----------
import re as _re
# 1) une citações quebradas por quebra de linha (V1 legada + blocos novos): "(Autor\nano)[TAG]" -> "(Autor ano)[TAG]"
doc, n1 = _re.subn(r'\(\s*([A-ZÀ-Þ][^\(\)\n]{0,60}?)\s*\n\s*(\d{4}[ab]?)\s*\)\[', lambda m: f'({m.group(1).strip()} {m.group(2)})[', doc)
doc, n2 = _re.subn(r'\(\s*([A-ZÀ-Þ][^\(\)\n]{0,60}?-)\s*\n\s*([A-Za-zÀ-ÿ]+)\s+(\d{4}[ab]?)\s*\)\[', lambda m: f'({m.group(1)}{m.group(2)} {m.group(3)})[', doc)
print('citações reundidas:', n1+n2)
digs = _re.findall(r'\d{7,9}', doc)
assert not digs, f"PMID/dígitos longos na prosa: {digs[:5]}"
# citações sem quebra de linha
quebras = _re.findall(r'\([A-ZÀ-Þ][^\)\n]{0,60}\n[^\)]{0,20}\)\[(?:ML|EC|OB|MA)\]', doc)
assert not quebras, f"citação quebrada: {quebras[:5]}"
open(P, 'w', encoding='utf-8').write(doc)
print("OK md aplicado. delta bytes:", len(doc)-orig_len)
# contagens por bloco
for marcador in ["[[AT 2026-09-09]]"]:
    print("inserções AT:", doc.count(marcador))
cits = _re.findall(r'\([A-ZÀ-Þ][^\)]{1,60}\)\[(?:ML|EC|OB)\]', doc)
print("citações prosa total:", len(cits))
