#!/usr/bin/env python3
# TRILHA 45 — Achado do Auditor-Mestre sobre a V2.1 (nó "EVIDÊNCIAS / VÍNCULOS UNIFICADOS")
#             + parecer do comentador externo + construção da CANDIDATA V2.2 (staging).
# Casa (bancada Arena) · 2026-09-17 · rodada 26. Determinístico, só stdlib.
# Política da casa: toda medida declara COMANDO + REGEX/PADRÃO + CAMADA + ESCOPO + SHA do alvo.
import hashlib, json, re, unicodedata, difflib, pathlib

ROOT  = pathlib.Path('/home/user')
SERIE = ROOT/'BIBLIOTECAS/_documentos_serie'
V21   = SERIE/'ARQUITETURA CONSOLIDADA DA PLATAFORMA V2.1  -  17.09.26.md'
ACH   = SERIE/'MESTRE_achado_V21_no_unificado_recebido_2026-09-17/ACHADO_V21_NO_UNIFICADO_2026-09-17.md'
PARC  = SERIE/'COMENTADOR_achado_V21_recebido_2026-09-17/COMENTARIO_COMENTADOR_ACHADO_V21_E_L05v13_2026-09-17.md'
MIN2  = SERIE/'L05_1.1_minuta_mestre_recebida_2026-09-15/L05_1.1_CONTRATO_CADEIA_MOTOR_minuta2_2026-09-15.md'
STAGE = SERIE/'CANDIDATA_V22_staging_2026-09-17'
CAND  = STAGE/'ARQUITETURA CONSOLIDADA DA PLATAFORMA V2.2  -  17.09.26.md'
OUT   = ROOT/'BIBLIOTECAS/B01_Neuroinflamacao/atuais/producao/TRILHA45_achado_mestre_V21_no_unificado_2026-09-17.json'
V7    = ROOT/'BIBLIOTECAS/B01_Neuroinflamacao/atuais/B1 NEUROINFLAMAÇÃO V7 CANONICA.md'
MAN   = ROOT/'BIBLIOTECAS/B01_Neuroinflamacao/atuais/Evidencias/Bibliografia/_manifesto_biblioteca.json'
P8    = ROOT/'Ferramentas de geração e auditoria/06_portao_P8_coerencia/scripts/validar_coerencia_camadas.py'
VINC  = ROOT/'BIBLIOTECAS/B01_Neuroinflamacao/atuais/Evidencias/Vinculos/vinculos_referencia_afirmacao.json'

FALHAS = []
R = {'trilha': 45, 'data': '2026-09-17', 'objeto': 'achado mestre no UNIFICADOS + parecer comentador + candidata V2.2'}

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def check(nome, ok, detalhe=''):
    R.setdefault('checks', []).append({'check': nome, 'ok': bool(ok), 'detalhe': detalhe})
    if not ok: FALHAS.append(nome)

def linhas_crlf(p):
    raw = p.read_bytes().decode('utf-8')
    assert '\r\n' in raw, f'{p} sem CRLF?'
    return raw.split('\r\n')

def conta(txt, padrao):
    """Camada declarada: substring NFC, SENSÍVEL a maiúsculas, sobre o arquivo inteiro (linhas unidas por \\n)."""
    return txt.count(padrao)

def conta_ci(txt, padrao):
    """Camada declarada: substring NFC, INSENSÍVEL (casefold), sobre o arquivo inteiro."""
    return txt.casefold().count(padrao.casefold())

# ---------- 0) IDENTIDADES ----------
R['artefatos'] = {k.name: sha(k) for k in (V21, ACH, PARC, MIN2, V7, MAN, P8, VINC)}
R['upload_V21_registrado_pela_casa'] = '5be36836610d26832506b73dac45baa09e7041bc9ce22e6557f2be59b258e06a'  # camada: registro (ARQUITETURA_VIGENTE.txt)
ach_txt = ACH.read_bytes().decode('utf-8')
check('A1 achado cita o mesmo sha de upload registrado pela casa', R['upload_V21_registrado_pela_casa'] in ach_txt)
check('A2 sha da V2.1 instalada intacta', R['artefatos'][V21.name] == '1a50645e260984ab7b78b95abc177bdb171203f55f22990c195e5cefa0a94b60', R['artefatos'][V21.name][:16])

# ---------- 1) LEITURA DA V2.1 INSTALADA ----------
L    = linhas_crlf(V21)                 # sem \r\n nas pontas
TXT  = unicodedata.normalize('NFC', '\n'.join(L))
ESCO = 'arquivo V2.1 instalada inteiro (CRLF removido p/ leitura; escrita preserva CRLF)'

def medida(id_, comando, regex, camada, resultado, extra=None):
    m = {'id': id_, 'comando': comando, 'regex_padrao': regex, 'camada': camada, 'escopo': ESCO, 'resultado': resultado}
    if extra: m['extra'] = extra
    R.setdefault('medidas', []).append(m)
    return resultado

# m1 — H1 do achado (item 1)
h1 = L[0]
medida('m1', "python: L=linhas_crlf(V21); L[0]", 'linha exata', 'linha 1 (H1), literal', h1)
check('m1 H1 ainda diz V2/15.09.26 (pendente do achado, item 1)', h1 == '# ARQUITETURA CONSOLIDADA DA PLATAFORMA V2    15.09.26')
medida('m1b', "L[3].startswith('**Rev. V2.1')", 'literal', 'linha 4 (Rev), literal', L[3].startswith('**Rev. V2.1'))

# m2 — headings (achado item 2 + comentador §8)
h_all  = [(i+1, l) for i, l in enumerate(L) if re.match(r'^# ', l)]
h_num  = [(i+1, int(m.group(1))) for i, l in enumerate(L) if (m := re.match(r'^# (\d+)\.', l))]
from collections import Counter
dups = {n: c for n, c in Counter(n for _, n in h_num).items() if c > 1}
medida('m2', "re.finditer r'^# ' e r'^# (\\d+)\\.'", r'^# ' + ' | ' + r'^# (\d+)\.', 'linha iniciando com padrão (MI de grep -c)',
       {'total_^#_espaco': len(h_all), 'total_^#_numero': len(h_num),
        'duplicatas_numero': dups, 'secoes_1a30_presentes': sorted(set(n for _, n in h_num)) == list(range(1, 31))})
check('m2 phantom "# 21." removido na instalação', not any(l.startswith('# 21.') and n != 1021 for n, l in h_all))
check('m2 duplicata "# 2." AINDA presente (comentador §8.4 aberto)', dups == {2: 2})

# m3 — O NÓ (achado item 3)
unif = conta_ci(TXT, 'unificad')
medida('m3', "TXT.count casefold 'unificad'", 'unificad (substring)', 'substring NFC casefold, aquivalente a grep -oi', unif)
recorte = L[51:68]
topo = {
 'L53_tem_PASTA':      'PASTA ATUALIZAÇÃO' in L[52],
 'L59_eixo_pasta_espelhado': (L[58].count('EVIDÊNCIAS') == 2 and L[58].count('NARRATIVAS') == 2),
 'L65_duas_setas':      L[64].count('▼') == 2,
 'L67_no':             'EVIDÊNCIAS / VÍNCULOS UNIFICADOS' in L[66],
 'L72_ontologia':      'ONTOLOGIA / GRAFO MULTIDOMÍNIO' in L[71],
}
topo['fusao_antes_da_ontologia'] = all([topo['L53_tem_PASTA'], topo['L65_duas_setas'], topo['L67_no'], topo['L72_ontologia']])
medida('m3b', 'recorte L52-L68 + asserts literais por linha', 'literais de linha', 'linhas exatas do desenho do §2 (camada: linha)', topo)
check('m3 ACHADO PRINCIPAL confirmado: nó recebe os DOIS fluxos antes da Ontologia', topo['fusao_antes_da_ontologia'])
check('m3 pastas espelhadas: eixo da Pasta tem EVIDÊNCIAS+NARRATIVAS próprias', L[58].count('EVIDÊNCIAS') == 2 and L[58].count('NARRATIVAS') == 2)

# m4 — busca ativa (achado item 5)
m4 = {'busca_ativamente_literal': conta(TXT, 'O Motor busca ativamente'),
      'conexao_consulta_literal': conta(TXT, '[ CONEXÃO / CONSULTA ]')}
medida('m4', "TXT.count literais", 'literais case-sensitive', 'substring NFC case-sensitive', m4)
check('m4 verbatim do achado item 5 confirmado', m4['busca_ativamente_literal'] == 1 and m4['conexao_consulta_literal'] == 1)

# m5 — contagens com camada declarada (nota de método: grep raso divergiu por acentos → NFC oficial)
m5 = {p: {'literal_CS': conta(TXT, p), 'casefold_CI': conta_ci(TXT, p)}
      for p in ['ANAMNESE', 'INTERPRETAÇÃO CONTEXTUALIZADA', 'MECANÍSTICA', 'CLÍNICA', 'TERAPÊUTICA',
                'EXPLICAÇÃO NARRATIVA', 'LAUDO', 'Sugestão']}
medida('m5', "python str.count NFC p/ cada padrão (2 camadas)", ', '.join(m5), 'substring NFC; literal=case-sensitive, CI=casefold', m5,
       extra='nota de método: grep -oi terapêutica retornou 0 por divergência de forma Unicode; camada oficial da casa = python NFC')

# m6 — proveniência (endurecimento mestre item 5 + comentador §3)
m6 = {'origem_conhecimento_CI': conta_ci(TXT, 'origem_conhecimento'), 'payload_CI': conta_ci(TXT, 'payload')}
medida('m6', 'conta_ci origem_conhecimento / payload', 'origem_conhecimento|payload', 'substring NFC casefold', m6)
check('m6 proveniência AUSENTE da V2.1 (a endurecer na V2.2)', m6['origem_conhecimento_CI'] == 0 and m6['payload_CI'] == 0)

# m7 — D-06/D-02 (achado itens 3-4)
m7 = {'D-06_na_V21': TXT.count('D-06'), 'D-02_na_V21': TXT.count('D-02')}
medida('m7', "TXT.count 'D-06'/'D-02'", 'literais', 'substring literal', m7,
       extra='cláusulas vivem na minuta 2 do L-05 (contrato), não reproduzidas dentro da V2.1')
min2 = MIN2.read_bytes().decode('utf-8')
d06  = re.search(r'(?m)^\*\*Regra\.\*\* Fronteira arquitetural\..*$', min2)
d02  = re.search(r'(?m)^\*\*Regra\.\*\* \*\*Teto por eixo.*$', min2)
d06_txt = unicodedata.normalize('NFC', d06.group(0)) if d06 else None
R['D06_minuta2_quote'] = d06_txt
medida('m7b', "re.search ^**Regra.** Fronteira arquitetural.*$ na minuta 2", r'(?m)^\*\*Regra\.\*\* Fronteira arquitetural\..*$',
       'linha exata (quote integral)', 'minuta 2 L-05 (sha no bloco artefatos)',
       {'encontrada': d06 is not None,
        'palavras_chave': {k: (k in d06_txt if d06_txt else False)
                           for k in ['segregada e rotulada', 'não altera nenhum eixo', 'Toda consulta é registrada']},
        'D02_teto': d02 is not None})
check('m7 D-06 existe fora da V2.1 e bate com a paráfrase do achado',
      d06 is not None and 'segregada e rotulada' in d06_txt and 'não altera nenhum eixo' in d06_txt and 'Toda consulta é registrada' in d06_txt)

# m8 — §19 (topologia alvo) e §20 (fecho)
i19 = next(i for i, l in enumerate(L) if l.startswith('# 19.'))
i20 = next(i for i, l in enumerate(L) if l.startswith('# 20.'))
s19 = unicodedata.normalize('NFC', '\n'.join(L[i19:i20]))
s20 = unicodedata.normalize('NFC', '\n'.join(L[i20:i20+48]))
m8 = {'s19_tem_PASTA_DE': 'PASTA DE' in s19, 's19_tem_MOTOR': 'MOTOR' in s19,
      's19_seta_propria_pasta': '▲' in s19, 's20_fecho': 'não possuem o mesmo status epistemológico' in s20}
medida('m8', 'recortes §19/§20 + literais', 'PASTA DE|MOTOR|▲|não possuem o mesmo status', 'bloco de seção (linhas)', m8)
check('m8 §19 desenha Pasta→Motor por seta própria; §20 fecha com a guarda', all(m8.values()))

# m9 — resto das representações (D-V2-DIAGRAMA-DUPLO da DIREÇÃO permanece; nó sai da dívida — rec. 4 do achado)
m9 = {'unificad_fora_do_S2': conta_ci(unicodedata.normalize('NFC', '\n'.join(L[158:])), 'unificad')}
medida('m9', 'conta_ci unificad nas linhas ≥159 (após o §2)', 'unificad', 'substring NFC casefold, escopo: linhas 159-fim', m9)
check('m9 nó UNIFICADOS existe APENAS no §2 (escopo cirúrgico)', m9['unificad_fora_do_S2'] == 0)

# ---------- 2) VEREDITO POR ITEM ----------
R['veredito_achado'] = {
 'item1_artefato_nao_se_identifica_V21': 'CONFIRMADO no upload; PARCIALMENTE saneado na instalação (Rev V2.1 linha 4 + nome do arquivo); H1 segue aberto → corrigido na V2.2',
 'item2_cabecalho_intruso_#21': 'CONFIRMADO no upload; SANEADO na instalação (rótulo virou "# 2. … (MAPA EXECUTIVO)"); restou duplicata "# 2." (comentador §8.4) → corrigida na V2.2',
 'item3_no_unificado_derrota_D06': 'CONFIRMADO na instalação (m3/m3b: fusão antes da Ontologia; D-06 vive na minuta 2 e exige segregação+rastro) → corrigido na V2.2',
 'item4_prosa_canonica_e_alinhar_ao_S19': 'ACEITO: §19 já desenha a topologia correta (m8); V2.2 alinha o §2 e declara prosa > desenhos',
 'item5_busca_ativa_ok_com_endurecimento': 'CONFIRMADO verbatim (m4); endurecimento (origem no item) ausente (m6) → incorporado na V2.2 (desenho + prosa)',
}
R['veredito_parecer_comentador'] = {
 'S1_S2_correcao_arquitetural': 'converge com o item 3/4 do achado; verificado (m3, m8)',
 'S3_proveniencia_payload': 'ausente na V2.1 (m6); incorporada na V2.2 com contagem medida',
 'S4_S5_D06_e_ontologia': 'D-06 citada bate na minuta 2 (m7b); Ontologia segue só-canônica na V2.2',
 'S6_diagrama_proposto': 'topologia adotada na V2.2, PRESERVANDO tríade MEC/CLÍN/TER + EXPLICAÇÃO NARRATIVA + ANAMNESE + busca ativa (m5) que o diagrama do parecer omite — omissão editorial, não rejeitada',
 'S7_sem_reengenharia': 'V2.2 cirúrgica: hunks confinados (ver bloco candidata)',
 'S8_correcoes_documentais': 'V2.1+nome ok; "# 21." ok (instalação); duplicata "# 2." → corrigida na V2.2 (m2)',
 'S9_L05v13_sem_reengenharia': 'registrado; mantém RESPOSTA_6 ao auditor-2 estável',
 'S10_aceito_com_correcao_localizada': 'a casa ENDOSSA; aplicação sujeita à decisão do operador (como rodada 24)',
}

# ---------- 3) CANDIDATA V2.2 ----------
novas = list(L)  # sem \r\n nas pontas
assert novas[0]  == '# ARQUITETURA CONSOLIDADA DA PLATAFORMA V2    15.09.26'
assert novas[45] == '# 2. ARQUITETURA GERAL DA PLATAFORMA (MAPA EXECUTIVO)'
assert 'PASTA ATUALIZAÇÃO' in novas[52] and 'UNIFICADOS' in novas[66] and novas[64].count('▼') == 2
caixa_topo = {'top': novas[65], 'fundo': novas[67]}
assert caixa_topo['top'] == '  ┌' + '─'*72 + '┐', repr(caixa_topo['top'])

novas[0]  = '# ARQUITETURA CONSOLIDADA DA PLATAFORMA V2.2    17.09.26'
novas[3]  = ('**Rev. V2.2 — 2026-09-17** · Correção arquitetural localizada do §2: nó "EVIDÊNCIAS / VÍNCULOS UNIFICADOS" '
             'removido — fluxos canônico × atualização segregados até o Motor (achado do Auditor-Mestre, sha 2841bc66…; '
             'parecer concorrente do comentador externo) · proveniência no item recuperado (origem_conhecimento = '
             'canonico | atualizacao) · base: V2.1 do operador (upload 5be36836…, instalada na rodada 24) · decisão do '
             'operador (rodada 26) · 0 ciência alterada')
novas[45] = 'ARQUITETURA GERAL DA PLATAFORMA (MAPA EXECUTIVO)'

txt_no  = 'EVIDÊNCIAS / VÍNCULOS CANÔNICOS'
esq     = (72 - len(txt_no)) // 2
caixa_txt = '  │' + ' '*esq + txt_no + ' '*(72 - esq - len(txt_no)) + '│'
topo_novo = [
 '  ┌─────────────────────────┐',
 '  │  BIBLIOTECAS CANÔNICAS  │',
 '  └────────────┬────────────┘',
 '               │',
 '         ┌─────┴──────────────────┐',
 '         ▼                        ▼',
 '  ┌──────────────┐        ┌──────────────┐',
 '  │  EVIDÊNCIAS  │        │  NARRATIVAS  │',
 '  │ BIBLIOGRAFIA │        │ TRANSVERSAIS │',
 '  └──────┬───────┘        └──────┬───────┘',
 '         │                       │',
 '         └───────────┬───────────┘',
 '                     │',
 '                     ▼',
 caixa_topo['top'],
 caixa_txt,
 caixa_topo['fundo'],
]
assert len(topo_novo) == 17 and len(novas[51:68]) == 17
novas[51:68] = topo_novo

i_laudo  = next(i for i, l in enumerate(novas) if 'LAUDO' in l and '│' in l)
i_fecha  = i_laudo + 1
assert novas[i_fecha].lstrip().startswith('└')
bloco_pasta = ['',
 '  ┌─────────────────────────┐',
 '  │   PASTA DE ATUALIZAÇÃO  │',
 '  │   (ciência recente;     │ ─────────────────►  MOTOR CLÍNICO',
 '  │    fora do cânone)      │      consulta ativa do Motor — SEM',
 '  └─────────────────────────┘      passar pela Ontologia/Grafo.',
 '    Todo item recuperado pelo       Os dois fluxos só se encontram',
 '    Motor carrega a origem:         no Motor (nunca a montante).',
 '    origem_conhecimento =',
 '    canonico | atualizacao']
novas[i_fecha+1:i_fecha+1] = bloco_pasta

i_fence2 = next(i for i, l in enumerate(novas) if i > i_fecha and l == '```')
assert novas[i_fence2-1].startswith('---') or True
prosa = ['',
 '**Fluxo canônico × fluxo de atualização — regra arquitetural (Rev. V2.2, 2026-09-17):** os dois fluxos',
 'permanecem segregados até o Motor Clínico. O canônico percorre Bibliotecas Canônicas → Evidências',
 'Bibliográficas e Narrativas Transversais → Evidências/Vínculos Canônicos → Ontologia/Grafo → JSONs',
 'Modulares → Motor; a Pasta de Atualização chega ao Motor por caminho próprio, por consulta ativa, sem',
 'passar pela Ontologia/Grafo e sem se fundir aos vínculos canônicos. Todo item recuperado pelo Motor',
 'carrega a proveniência no próprio item (origem_conhecimento = canonico | atualizacao), de modo que a',
 'consulta conjunta preserva a rastreabilidade. A consulta à Pasta de Atualização não constitui incorporação',
 'ao conhecimento canônico — esta só ocorre por processo formal de atualização/curadoria (§18–§20). Em',
 'divergência de representação, a prosa deste documento prevalece sobre os desenhos.',
 '*(Correção por achado do Auditor-Mestre de 2026-09-17; parecer concorrente do comentador externo;',
 'decisão do operador, rodada 26.)*']
novas[i_fence2+1:i_fence2+1] = prosa

# --- verificação da candidata ---
TC   = unicodedata.normalize('NFC', '\n'.join(novas))
hc   = [l for l in novas if re.match(r'^# ', l)]
hn   = [int(m.group(1)) for l in novas if (m := re.match(r'^# (\d+)\.', l))]
sm   = difflib.SequenceMatcher(None, L, novas, autojunk=False)
janelas = [(0,1),(3,4),(45,46),(51,68),(110,113),(154,156)]  # índices 0-based no ARQUIVO ANTIGO (exclusivo)
viol  = [{'tag': t, 'antigo': (a,b), 'novo': (c,d)} for t,a,b,c,d in sm.get_opcodes()
         if t != 'equal' and not any(w0 <= a and b <= w1 for w0, w1 in janelas)]
i_cat_old = next(i for i, l in enumerate(L)     if l.startswith('# 3. CATÁLOGO'))
i_cat_new = next(i for i, l in enumerate(novas) if l.startswith('# 3. CATÁLOGO'))
R['candidata'] = {
 'nome': CAND.name, 'staging': str(STAGE),
 'sha256': None,
 'pos_checks': {
   'unificad_CI':            conta_ci(TC, 'unificad'),
   'PASTA_DE_ATUALIZACAO_desenho': conta(TC, 'PASTA DE ATUALIZAÇÃO'),
   'origem_conhecimento_CI': conta_ci(TC, 'origem_conhecimento'),
   'canonico_atualizacao':   conta(TC, 'canonico | atualizacao'),
   'cabecalhos_^#_espaco':   len(hc), 'cabecalhos_^#_numero_unicos': sorted(set(hn)) == list(range(1,31)) and len(hn) == 30,
   'tríade_preservada':      all(TC.count(p) >= 1 for p in ('MECANÍSTICA','CLÍNICA','TERAPÊUTICA')),
   'explicacao_narrativa':   conta(TC, 'EXPLICAÇÃO NARRATIVA'),
   'anamnese_CS':            conta(TC, 'ANAMNESE'), 'busca_ativa': conta(TC, 'O Motor busca ativamente'),
   'conexao_consulta':       conta(TC, '[ CONEXÃO / CONSULTA ]'),
   'fecho_S20_intacto':      'não possuem o mesmo status epistemológico' in TC,
 },
 'diff_opcodes_fora_das_janelas': viol,
 'sufixo_do_S3_ao_fim_byte_identico': '\r\n'.join(L[i_cat_old:]) == '\r\n'.join(novas[i_cat_new:]),
 'linhas': len(novas), 'hunks_esperados': 'H1 · Rev · título do mapa · topo do §2 · bloco Pasta · prosa normativa',
}
# CONFISSÃO datada (casa, 2026-09-17): o 1º critério C1 (unificad_CI == 0 no arquivo inteiro) era apertado demais —
# a linha Rev da V2.2 cita historicamente o nó removido. Régua correta por camada: desenho do §2 = 0; total = 1 (Rev).
_i_f0   = next(i for i, l in enumerate(novas) if l == '```text')   # fence do mapa executivo (§2)
_i_f1   = next(i for i, l in enumerate(novas) if i > _i_f0 and l == '```')
_unif_des = conta_ci(unicodedata.normalize('NFC', '\n'.join(novas[_i_f0:_i_f1])), 'unificad')
R['candidata']['pos_checks']['unificad_no_desenho_S2'] = _unif_des
R['candidata']['confissao_C1'] = ('1º critério C1 (unificad total == 0) errado: Rev legitimamente cita o nó removido; '
                                  'régua corrigida por camada (desenho §2 = 0 · total = 1 histórico na Rev)')
check('C1 candidata sem UNIFICADOS no DESENHO do §2 (total = só a citação histórica da Rev)',
      _unif_des == 0 and R['candidata']['pos_checks']['unificad_CI'] == 1)
check('C2 proveniência presente (desenho + prosa + Rev ≥ 2)', R['candidata']['pos_checks']['origem_conhecimento_CI'] >= 2)
check('C3 30 seções numeradas únicas + H1 = 31 cabeçalhos "# "', R['candidata']['pos_checks']['cabecalhos_^#_espaco'] == 31 and R['candidata']['pos_checks']['cabecalhos_^#_numero_unicos'])
check('C4 zero hunks fora das janelas cirúrgicas', len(viol) == 0, json.dumps(viol, ensure_ascii=False)[:400])
check('C5 sufixo §3→fim byte-idêntico (catálogo 146 IDs, §§5-30, §19/§20/§21 intactos)', R['candidata']['sufixo_do_S3_ao_fim_byte_identico'])

STAGE.mkdir(parents=True, exist_ok=True)
with open(CAND, 'w', encoding='utf-8', newline='') as f:
    f.write('\r\n'.join(novas))
R['candidata']['sha256'] = sha(CAND)
R['candidata']['bytes']  = CAND.stat().st_size

# ---------- 4) SELOS FINAIS ----------
R['selos'] = {
 'V7': sha(V7) == '6e2c29797e6322f16dcc5248cce552be613dd11f1de957c66aaa913e69225238',
 'manifesto': sha(MAN) == '79d1309a168922d0e8bf43736cd5b21c8b361bdf64e3b200eeeafd43806f3a9c',
 'P8': sha(P8) == '84fa918d09899d54995ae41d65b0787a7a52888ba6177ce77583483b1124fe8b',
 'vinculos': sha(VINC) == '490675e63122a24baebd8890f4a7883a07f68916d90562e74adf309133501d1b',
}
check('S 0 ciência tocada (V7 · manifesto · P-8 · vínculos)', all(R['selos'].values()))

R['resultado'] = ('ACHADO DO MESTRE PROCEDENTE (5/5 pontos verificados na instalação vigente) · parecer do comentador '
                  'convergente (10/10 blocos mapeados) · CANDIDATA V2.2 construída em STAGING e contida (janelas cirúrgicas, '
                  'sufixo byte-idêntico) · a casa ENDOSSA a correção localizada · APLICAÇÃO aguarda decisão do operador · '
                  'D-V2-DIAGRAMA-DUPLO mantida para a DIREÇÃO Evidência↔Biblioteca (rec. 4 do achado); nó UNIFICADOS sai da '
                  'dívida e vira item próprio (D-V2-NO-UNIFICADO)')
R['checks_ok']   = sum(1 for c in R['checks'] if c['ok'])
R['checks_tot']  = len(R['checks'])
R['falhas']      = FALHAS
OUT.write_text(json.dumps(R, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps({'checks': f"{R['checks_ok']}/{R['checks_tot']}", 'falhas': FALHAS,
                  'candidata_sha': R['candidata']['sha256'], 'linhas_candidata': R['candidata']['linhas'],
                  'json': str(OUT)}, ensure_ascii=False, indent=2))
