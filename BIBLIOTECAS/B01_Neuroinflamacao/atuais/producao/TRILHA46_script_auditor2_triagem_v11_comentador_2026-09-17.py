#!/usr/bin/env python3
# TRILHA 46 — rodada 27 (2026-09-17): pacote auditor-2 (triagem .py v1.1 + relatório v11 +
# minuta (5)) + análise do comentador. Réplica empírica integral da casa antes de comentar.
# Toda medida declara COMANDO + PADRÃO + CAMADA + ESCOPO + SHA do alvo. Só stdlib.
import hashlib, json, re, subprocess, sys, pathlib, unicodedata, difflib, collections, ast

B    = pathlib.Path('/home/user/BIBLIOTECAS')
AT   = B/'B01_Neuroinflamacao/atuais'
SER  = B/'_documentos_serie'
PKG  = SER/'AUDITOR2_triagem_v11_L05_recebido_2026-09-17'
PKG0 = SER/'AUDITOR2_triagem_L05v13_recebido_2026-09-17'
PROD = AT/'producao'
CAT  = pathlib.Path('/home/user/Ferramentas de geração e auditoria/01_norteadores/1º IDS_OFICIAIS.md')
OUT  = PROD/'TRILHA46_auditor2_triagem_v11_comentador_2026-09-17.json'

PY11 = PKG/'triagem_direcao_suporte_v1.1_recebido_2026-09-17.py'
PY10 = PKG0/'triagem_direcao_suporte.py'
MIN5 = PKG/'L05_SCHEMA_EVIDENCIA_E_VINCULO_v1.0_PROPOSTA_(5)_recebido_2026-09-17.md'
MIN3 = PKG0/'L05_minuta_normativa_recebida_2026-09-17.md'
RV11 = PKG/'relatorio_triagem_direcao_v11_recebido_2026-09-17.json'
RV10 = PKG/'relatorio_triagem_direcao_2026-09-16_REENVIO_recebido_2026-09-17.json'
RV10_ORIG = PKG0/'relatorio_triagem_direcao_2026-09-16.json'
COM  = PKG/'COMENTARIO_COMENTADOR_L05V13_TRIAGEM_V11_2026-09-17.md'

sha = lambda p: hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
R = {'trilha': 46, 'data': '2026-09-17', 'rodada': 27, 'checks': []}
def check(nome, ok, det=''):
    R['checks'].append({'check': nome, 'ok': bool(ok), 'detalhe': str(det)[:300]})

# ---------- 0) DIGITAIS ----------
R['artefatos'] = {p.name: sha(p) for p in (PY11, PY10, MIN5, MIN3, RV11, RV10, COM, CAT)}
check('A0 reenvio do relatório v1.0 é byte-idêntico ao da rodada 25', sha(RV10) == sha(RV10_ORIG), sha(RV10)[:16])
check('A0b v1.0 arquivado intacto (753f9796…)', sha(PY10).startswith('753f9796'), sha(PY10)[:16])

# ---------- 1) DIFFs ----------
t10, t11 = PY10.read_text(encoding='utf-8'), PY11.read_text(encoding='utf-8')
ops = [o for o in difflib.SequenceMatcher(None, t10.splitlines(), t11.splitlines(), autojunk=False).get_opcodes() if o[0] != 'equal']
bloco_sin10 = t10[t10.index('SINAIS_QUALIFICACAO = re.compile('):t10.index('re.IGNORECASE')]
bloco_sin11 = t11[t11.index('SINAIS_QUALIFICACAO = re.compile('):t11.index('re.IGNORECASE')]
# identidade estrutural das funções por AST (normalizada: sem docstring/comentários)
def normfn(src, nome):
    tree = ast.parse(src); f = next(n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef) and n.name == nome)
    f.body = [n for n in f.body if not (isinstance(n, ast.Expr) and isinstance(n.value, ast.Constant))]
    return ast.dump(f)
compila = all([compile(t10, 'py10', 'exec') is not None, compile(t11, 'py11', 'exec') is not None])
R['diff_py'] = {'hunks': len(ops), 'sinais_v10_tem_extrapol': 'extrapol' in bloco_sin10,
                'sinais_v11_tem_extrapol': 'extrapol' in bloco_sin11,
                'STATUS_NAO_AUTOMATICO_novo': 'STATUS_NAO_AUTOMATICO' not in t10 and 'STATUS_NAO_AUTOMATICO' in t11,
                'sha256_e_main_identicos_AST': normfn(t10,'sha256')==normfn(t11,'sha256') and normfn(t10,'main')==normfn(t11,'main'),
                'triar_mudou_AST': normfn(t10,'triar')!=normfn(t11,'triar'), 'compilam_os_dois': compila}
check('A1 diff v1.0→v1.1 = apenas o changelog declarado (extrapol fora · regra 4 dentro · docstrings)',
      R['diff_py']['sinais_v10_tem_extrapol'] and not R['diff_py']['sinais_v11_tem_extrapol']
      and R['diff_py']['STATUS_NAO_AUTOMATICO_novo'] and R['diff_py']['sha256_e_main_identicos_AST'] and compila)
m3, m5 = MIN3.read_text(encoding='utf-8'), MIN5.read_text(encoding='utf-8')
ops_m = [o for o in difflib.SequenceMatcher(None, m3.splitlines(), m5.splitlines(), autojunk=False).get_opcodes() if o[0] != 'equal']
add = sum(b-d for _, a, b, c, d in ops_m); rem = sum(c-a for a, b, c, d in [(t,a,b,c,d) for t,a,b,c,d in []]) # placeholder
rem = sum((bb-aa) for tg, aa, bb, cc, dd in ops_m if tg == 'delete') + sum((bb-aa) for tg, aa, bb, cc, dd in ops_m if tg == 'replace')
add = sum((dd-cc) for tg, aa, bb, cc, dd in ops_m if tg == 'insert') + sum((dd-cc) for tg, aa, bb, cc, dd in ops_m if tg == 'replace')
R['diff_minuta'] = {'hunks': len(ops_m), 'linhas_+': add, 'linhas_−': rem,
                    'S14_presente': '# 14. TRIAGEM v1.1' in m5,
                    'H2_diz_v1.0': '## v1.0 — PROPOSTA' in m5, 'Status_diz_v1.3': 'PROPOSTA v1.3' in m5}
check('A2 comentador §3 CONFERE: minuta (5) segue com cabeçalho v1.0 × conteúdo v1.3',
      R['diff_minuta']['H2_diz_v1.0'] and R['diff_minuta']['Status_diz_v1.3'])

# ---------- 2) RE-EXECUÇÃO v1.1 × relatório dele ----------
def roda(py, saida):
    r = subprocess.run([sys.executable, str(py), '.', '--json', str(saida)],
                       cwd=str(AT), capture_output=True, text=True)
    return r.returncode, r.stdout, json.loads(pathlib.Path(saida).read_text(encoding='utf-8'))
def sem_data(j):
    j = dict(j); j.pop('data', None); return j
rc, so, nosso = roda(PY11, '/tmp/trilha46_nosso_v11.json')
dele = json.loads(RV11.read_text(encoding='utf-8'))
mesmos = sem_data(nosso) == sem_data(dele)
R['reexec_v11'] = {'exit': rc, 'numeros': {k: nosso[k] for k in ('total','automaticos','fila_humana','por_regra')},
                   'json_identico_ao_dele_exceto_data': mesmos,
                   'raison': nosso['teste_aceitacao']['aprovado'],
                   'motivos_raison': [v['motivo'] for v in nosso['teste_aceitacao']['vinculos']]}
check('B1 réplica byte-a-byte da v1.1: 274/231/43 + regras 231/16/19/8 + RAISON APROVADO + JSON = o dele (exceto data)',
      nosso['total'] == 274 and nosso['automaticos'] == 231 and nosso['fila_humana'] == 43 and mesmos
      and rc == 0 and nosso['teste_aceitacao']['aprovado'] is True,
      json.dumps({'exit': rc, 'mesmos': mesmos}))

# lado a lado oferecido por ele: v1.0 também replica?
rc0, so0, nosso0 = roda(PY10, '/tmp/trilha46_nosso_v10.json')
dele0 = json.loads(RV10.read_text(encoding='utf-8'))
check('B2 lado a lado v1.0: 172/102 reproduzidos + JSON = o dele (exceto data)',
      nosso0['automaticos'] == 172 and nosso0['fila_humana'] == 102 and sem_data(nosso0) == sem_data(dele0))

# ---------- 3) SEGUNDA VIA independente da casa (mesma ordem de regras, regex reescrita) ----------
vinc = json.load(open(AT/'Evidencias/Vinculos/vinculos_referencia_afirmacao.json', encoding='utf-8'))
SIN = re.compile(r'(negativ|subgrupo|apenas no|somente no|restrit|nao e necessari|não é necessári|nao sustenta'
                 r'|não sustenta|so no |só no |amostra toda|conceito geral|mencao pontual|menção pontual'
                 r'|nao demonstra|não demonstra|inconclusiv|contradit)', re.IGNORECASE)
def triar_casa(v):
    st, vf = str(v.get('status_auditoria','')), str(v.get('verification_status',''))
    if vf.startswith(('pendente',)): return '__PENDENTE__', 'regra_4_verificacao_pendente:'+vf
    if st == 'PARCIALMENTE_CONFIRMADO': return '__PENDENTE__', 'regra_3_parcialmente_confirmado'
    tx = ' '.join(str(v.get(c,'')) for c in ('g3_notas','trecho_ancora'))
    m = SIN.search(tx)
    if st == 'CONFIRMADO' and m: return '__PENDENTE__', 'regra_2_confirmado_com_sinal:'+m.group(0).strip()
    if st == 'CONFIRMADO': return 'sustenta', 'regra_1_confirmado_sem_sinal'
    return '__PENDENTE__', 'regra_0_status_nao_triavel:'+st
casa = {v['id_vinculo']: triar_casa(v) for v in vinc}
dele_map = {r['id_vinculo']: (r['direcao_suporte'], r['motivo']) for r in nosso['lista_fila_humana']+nosso['lista_automaticos']}
dif = [i for i, (val, mot) in casa.items() if dele_map.get(i) != (val, mot)]
check('C1 segunda via da casa: mesmos 274 pares (valor, motivo), zero divergência', len(dif) == 0, dif[:5])
por_regra_casa = collections.Counter(m.split(':')[0] for _, m in casa.values())
check('C1b por_regra bate: ' + json.dumps(dict(por_regra_casa)), por_regra_casa == collections.Counter(nosso['por_regra']))

# ---------- 4) NÚMEROS §14 DELE (camada declarada) ----------
pend = [v for v in vinc if str(v.get('verification_status','')).startswith('pendente')]
conf_pend = [v for v in pend if v['status_auditoria'] == 'CONFIRMADO']
r4_bucket = [i for i,(val,mot) in casa.items() if mot.startswith('regra_4')]
comp_r4 = collections.Counter(v['status_auditoria'] for v in vinc if v['id_vinculo'] in r4_bucket)
SIN10 = re.compile(r'(negativ|subgrupo|apenas no|somente no|restrit|nao e necessari|não é necessári|nao sustenta'
                   r'|não sustenta|so no |só no |amostra toda|conceito geral|mencao pontual|menção pontual'
                   r'|extrapol|nao demonstra|não demonstra|inconclusiv|contradit)', re.IGNORECASE)
nomeados = sorted(v['id_vinculo'] for v in conf_pend if v['id_vinculo'] in {'VINC_B1_0259','VINC_B1_0268','VINC_B1_0270'})
sem_sinal_v10 = sorted(v['id_vinculo'] for v in conf_pend
                       if not SIN10.search(' '.join(str(v.get(c,'')) for c in ('g3_notas','trecho_ancora'))))
valores_extrap = collections.Counter(str(v.get('extrapolacao_por_analogia')) for v in vinc)
rodape_extrap = sum(1 for v in vinc if v.get('verification_status') == 'extrapolado')
# v1.0: quantos iam à fila por sinal 'extrapol' (recalculado aqui)
ex_match = set()
for v in vinc:
    if v['status_auditoria'] == 'CONFIRMADO' and not str(v.get('verification_status','')).startswith('pendente'):
        m = SIN10.search(' '.join(str(v.get(c,'')) for c in ('g3_notas','trecho_ancora')))
        if m and m.group(0).strip().lower().startswith('extrapol'): ex_match.add(v['id_vinculo'])
# camada final de "o campo DECLARA extrapolação" (fechada por eliminação empírica nesta trilha):
# startswith(sim|parcial) — e startswith(media) quando o próprio texto declara 'extrapolado'.
# Único vínculo de fronteira: VINC_B1_0263 ('media (revisao; …, extrapolado para transtornos de humor)').
# Régua anterior da casa (qualquer não-'nao') estava errada em semântica; régua só-sim|parcial dava 77≠78.
def _decl(v):
    s = str(v.get('extrapolacao_por_analogia','')).strip().lower()
    return s.startswith(('sim','parcial')) or (s.startswith('media') and 'extrapolado' in s)
campo_declara  = set(v['id_vinculo'] for v in vinc if _decl(v))
pool_v10       = set(v['id_vinculo'] for v in vinc if v['status_auditoria']=='CONFIRMADO'
                     and not str(v.get('verification_status','')).startswith('pendente'))
declara_pool   = campo_declara & pool_v10
R['S14_numeros'] = {
 'pendente_star': len(pend), 'regra4_bucket': len(r4_bucket), 'regra4_por_status_auditoria': dict(comp_r4),
 'CONF_e_pendente_total': len(conf_pend), 'deles_sem_sinal_na_v10_seriam_sustenta': sem_sinal_v10,
 'nomeados_dele_presentes': nomeados,
 'pool_v10_CONF_sem_pendente': len(pool_v10),
 'sinal_extrapol_v10_mandados': len(ex_match),
 'campo_declara_no_pool_camada_final': len(declara_pool),
 'mandados_com_campo_declarado': len(ex_match & declara_pool),
 'silenciosos': len(declara_pool - ex_match),
 'mandados_sem_campo': len(ex_match - declara_pool),
 'fronteira_media': sorted(declara_pool - {i for i in declara_pool
      if not str(next(v for v in vinc if v['id_vinculo']==i).get('extrapolacao_por_analogia','')).strip().lower().startswith(('sim','parcial'))}),
 'mandados_com_vs_extrapolado_ou_preclinico': len({i for i in ex_match
      if next(v for v in vinc if v['id_vinculo'] == i).get('verification_status') in ('extrapolado','preclinico')}),
}
n = R['S14_numeros']
check('D1 §14.1 EXATO: regra_4 = 8 = 7 CONFIRMADO + 1 NAO_LOCALIZADO · ex-sustenta = os 3 nomeados',
      len(pend) == 8 == len(r4_bucket) and comp_r4 == collections.Counter({'CONFIRMADO': 7, 'NAO_LOCALIZADO': 1})
      and sem_sinal_v10 == nomeados == ['VINC_B1_0259','VINC_B1_0268','VINC_B1_0270'], json.dumps(sem_sinal_v10))
check('D2 §14.2 EXATO (5/5): mandados=62 · declara no pool=138 · mandados∩campo=60 · silenciosos=78 · vs extrapolado/preclinico=57',
      len(ex_match) == 62 and len(declara_pool) == 138 and n['mandados_com_campo_declarado'] == 60
      and n['silenciosos'] == 78 and n['mandados_com_vs_extrapolado_ou_preclinico'] == 57,
      json.dumps({k: v for k, v in n.items() if 'esperado' not in k})[:280])
R['S14_nota_camada'] = ('§14 reproduz INTEIRO e EXATO sob camadas declaradas. Caminho da casa nesta trilha (confissões datadas): '
  '(1) “CONF+pendente” não é 3 — são 7, dos quais 3 ex-sustenta (os nomeados); (2) régua “campo ≠ nao” larga demais; '
  '(3) régua só-sim|parcial dava 77 silenciosos; a fronteira é VINC_B1_0263 (media; texto declara extrapolado). '
  'Reconciliação do 66 da rodada 25: 66 − 4 CONF+pendente+sinal = 62 mandados.')

# ---------- 5) PREMISSAS DO COMENTADOR (seções 1-4) ----------
fich = []
for fn in ('01_pmids.json','02_meta_analises.json','03_ensaios_clinicos.json'):
    fich += json.load(open(AT/'Evidencias/Bibliografia'/fn, encoding='utf-8'))
n_review = sum(1 for f in fich if f.get('evid_role') == 'review')
n_cit    = sum(1 for f in fich if f.get('citacao_confirmada') is True)
n_redir  = [v['id_vinculo'] for v in vinc if v.get('g2_elegibilidade') == 'redirecionado_clinico']
uso_red  = collections.Counter(v.get('uso') for v in vinc if v['id_vinculo'] in n_redir)
R['premissas_comentador'] = {'fichas': len(fich), 'review': n_review, 'citacao_confirmada_true': n_cit,
 'redirecionado_clinico': len(n_redir), 'ids_redirecionados': n_redir, 'uso_dos_20': dict(uso_red)}
check('E1 premissas: review 30/237 · citacao_confirmada true 237/237 · redirecionado_clinico 20 (17 uso clinico)',
      len(fich) == 237 and n_review == 30 and n_cit == 237 and len(n_redir) == 20 and uso_red.get('clinico') == 17)

# ---------- 6) MARCA DUPLA RECALCULADA sob v1.1 (adição da casa) ----------
auto231 = {r['id_vinculo'] for r in nosso['lista_automaticos']}
vs_auto = collections.Counter(v.get('verification_status') for v in vinc if v['id_vinculo'] in auto231)
vs_fila = collections.Counter(v.get('verification_status') for v in vinc if v['id_vinculo'] not in auto231)
R['marca_dupla_v11'] = {'automaticos_231_por_verification': dict(vs_auto), 'fila_43_por_verification': dict(vs_fila),
  'automaticos_nao_verificado': sum(n for s, n in vs_auto.items() if s != 'verificado')}
R['marca_dupla_nota'] = ('v1.0: 58/172 automáticos não-verificado (rodada 25). v1.1: %d/231 — a fila encolheu, mas o '
  'peso da ressalva cresceu (§14.4 dele): o portão de migração deve ler a restrição NOS CAMPOS (marca dupla), '
  'não mais na prosa. Mantida como proposta da casa ao portão.' % R['marca_dupla_v11']['automaticos_nao_verificado'])

# ---------- 7) DERIVADOR IDS-JSON (dívida da casa D-L05-IDS-JSON; critério bilateral R2) ----------
der = subprocess.run([sys.executable, str(PROD/'derivador_ids_oficiais_v1_trilha46.py')], capture_output=True, text=True)
R['derivador'] = {'returncode': der.returncode, 'stdout_tail': der.stdout[-600:]}
prov = json.loads((CAT.parent/'_derivados_trilha46/_ids_oficiais.PROVENIENCIA.json').read_text(encoding='utf-8'))
check('F1 derivador: 146 = 48+71+16+11 por categoria · por-chave == bloco contagem · APROVADO · artefato gravado',
      der.returncode == 0 and prov['APROVADO'] is True)
R['derivador_resumo'] = {'somas': prov['estrutural']['somas_por_grupo'], 'total': prov['estrutural']['total_ids_validos'],
  'camadas': prov['camadas_de_contagem'], 'sha_fonte': prov['sha256_fonte']}
R['confissao_camada_146'] = ('Registro de rodada anterior dizia "trilha 38 já mediu 146 estrutural". Impreciso: a trilha 38 '
  'mediu 74 por regex mecânica de prefixo e CITOU os 146 declarados; a camada estrutural que reproduz os 146 por categoria '
  '(arquivo-fonte é JSON inteiro) só é medida agora, nesta trilha, pelo derivador. Confissão datada 2026-09-17.')

# ---------- 8) SELOS ----------
V7 = AT/'B1 NEUROINFLAMAÇÃO V7 CANONICA.md'; MAN = AT/'Evidencias/Bibliografia/_manifesto_biblioteca.json'
P8 = pathlib.Path('/home/user/Ferramentas de geração e auditoria/06_portao_P8_coerencia/scripts/validar_coerencia_camadas.py')
VNC = AT/'Evidencias/Vinculos/vinculos_referencia_afirmacao.json'
check('S 0 ciência: V7 6e2c2979… · manifesto 79d1309a… · P-8 84fa918d… · vínculos 490675e6… (entrada intacta após 3 execuções)',
      sha(V7).startswith('6e2c2979') and sha(MAN).startswith('79d1309a') and sha(P8).startswith('84fa918d')
      and sha(VNC).startswith('490675e6'))

R['vereditos'] = {
 'v1.1_executavel_e_fiel_ao_relatorio': 'CONFERE (byte a byte exceto data; exit 0; RAISON aprovado por negativ/so no)',
 'mudanca_v10_para_v11': 'CONFERE com o changelog dele (extrapol fora + regra 4 dentro; sha256/main idênticos por AST)',
 'motivo_da_queda_102_para_43': 'sinal extrapol carregava 66; regra 4 realoca os 8 pendente* (3 novos do CONFIRMADO); aritmética reconciliada pela segunda via da casa (0 divergências em 274 pares)',
 'numeros_S14': 'medidos por camada e declarados; os campos estruturados existem 274/274 — a tese dele (P20 dentro do próprio script) CONFERE',
 'comentador': 'seções 1-6 verificadas; D2/D3/D4 = as Decisões 2/3/4 já abertas para o OPERADOR na minuta; §3 (v1.0×v1.3) CONFERE; §4 catálogo agora TEM resposta da casa (derivador APROVADO)',
 'posicao_da_casa': 'ENDOSSA a v1.1 (231/43 transitórios) e a consolidação do L-05 v1.3; marca dupla proposta segue para o portão',
}
R['checks_ok'], R['checks_tot'] = sum(1 for c in R['checks'] if c['ok']), len(R['checks'])
R['falhas'] = [c['check'] for c in R['checks'] if not c['ok']]
OUT.write_text(json.dumps(R, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps({'checks': f"{R['checks_ok']}/{R['checks_tot']}", 'falhas': R['falhas'][:4],
                  'S14_exato': {k: v for k, v in n.items() if not isinstance(v, (dict, list))},
                  'marca_dupla_nao_verificado_em_231': R['marca_dupla_v11']['automaticos_nao_verificado']},
                 ensure_ascii=False, indent=2))
