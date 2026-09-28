#!/usr/bin/env python3
# TRILHA 47 — rodada 28 (2026-09-18): reconstrução do P-8 do mestre a partir das 3 regiões
# coladas, contra a base oficial 84fa918d… (658 linhas, LF). Alvo: 665 linhas · sha be48a5ef…
# Critério de troca CORRIGIDO pelo mestre: não é só o comentário F-C2 — é comentário (6) +
# quebra da V-08 (1) [+ variações de bytes que ele entregou exatas: 'G3/revisão humana',
# parênteses do s_man, f-string da mensagem]. Fallback dele: comportamento 2/299 · V-14 verde ·
# F-C2 dispara ⇒ fica a sha viva da casa. Casa mede TUDO antes de trocar.
import hashlib, json, re, subprocess, sys, pathlib, shutil, difflib, os

BASE  = pathlib.Path('/home/user/Ferramentas de geração e auditoria/06_portao_P8_coerencia/scripts/validar_coerencia_camadas.py')
AT    = pathlib.Path('/home/user/BIBLIOTECAS/B01_Neuroinflamacao/atuais')
PROD  = AT/'producao'
STAGE = PROD/'P8_candidato_be48a5ef_staging_2026-09-18.py'
OUT   = PROD/'TRILHA47_reconstrucao_P8_be48a5ef_2026-09-18.json'
ALVO_SHA = 'be48a5efa1d67f9e7b4ae3a38fdcf562b924cc03fc58e91baa2c63a3c6b33e92'
sha = lambda p: hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()

R = {'trilha': 47, 'data': '2026-09-18', 'rodada': 28, 'checks': []}
def check(nome, ok, det=''):
    R['checks'].append({'check': nome, 'ok': bool(ok), 'detalhe': str(det)[:300]})

raw  = BASE.read_text(encoding='utf-8')
L    = raw.split('\n'); assert raw.endswith('\n') and L[-1] == ''
check('B0 base oficial intacta: sha 84fa918d… · 658 linhas · LF', sha(BASE).startswith('84fa918d') and len(L) == 659 and '\r' not in raw)

# --- spans verificados na base (camada: linha exata, 1-based) ---
L20  = '  V-06  DERIVA ficha/vínculo × prosa ancorada (detector heurístico — só AVISO;'
L21o = '        nunca prova de coerência semântica; semântica = G3/humano)'
L21m = '        nunca prova de coerência semântica; semântica = G3/revisão humana)'
BLQ  = ['        rel_txt = do_texto(r"\\*\\*Mecanismos relacionados \\(IDs oficiais\\):\\*\\*\\s*(.+)")',
        '        if rel_txt:',
        '            s_txt = {x.strip() for x in rel_txt.split(",") if x.strip()}']
SM_O = '            s_man = {str(x).strip() for x in (man.get("semantic_layer") or {}).get("related_entities") or []}'
SM_M = '            s_man = {str(x).strip() for x in ((man.get("semantic_layer") or {}).get("related_entities") or [])}'
ERR1 = ['            if s_txt != s_man:', '                rel.erro("V-07", "related_entities",']
MS_O = ['                         f"identidade divergente (fonte única violada) — "']
MS_M = ['                         "identidade divergente (fonte única violada) — "']
ERR2 = ['                         f"só na canônica: {sorted(s_txt - s_man)} · "',
        '                         f"só no manifesto: {sorted(s_man - s_txt)}")']
span_doc = L[19:23]; span_v07 = L[493:502]
check('B1 spans da base batem (docstring 20-23 · V-07 494-502)',
      span_doc[0] == L20 and span_doc[1] == L21o and 'V-08' in span_doc[3]
      and span_v07[:3] == BLQ and span_v07[3] == SM_O and span_v07[4:6] == ERR1 and span_v07[6:9] == MS_O + ERR2,
      json.dumps(span_doc[:2], ensure_ascii=False)[:200])

COMENT = ['        # 2026-09-15 (precisão 3 da casa, F-C2): o teste comparava CARDINALIDADE.',
          '        # Contraexemplo reproduzido nesta bancada: trocar um ID por outro falso,',
          '        # preservando 15 itens, atravessava o portão em silêncio — e isto é classe',
          '        # BLOQUEANTE. Passa a comparar CONJUNTOS, como o ramo irmão clinical_domains',
          '        # (F-C3) já fazia. Relevante sobretudo para a ingestão de B2..B16, quando IDs',
          '        # de mecanismo passam a caminhar.']
V08 = ['  V-08  claim quantitativo sem âncora na MESMA LINHA (alerta de triagem;',
       '        lastro estrutural = V-01/V-04/V-05, não esta regra)']

# --- espaço de variantes: 3 pontos instáveis (V-06 redação · s_man parênteses · f-string) ---
cands = {}
for v06n, v06 in (('mestre', L21m), ('nosso', L21o)):
    for smn, sm in (('mestre', SM_M), ('nosso', SM_O)):
        for msn, ms in (('mestre', MS_M), ('nosso', MS_O)):
            doc  = [L20, v06, '  V-07  sincronia manifesto × canônica (fonte única)'] + V08
            v07  = COMENT + BLQ + [sm] + ERR1 + ms + ERR2
            novas = L[:19] + doc + L[23:493] + v07 + L[502:]
            txt = '\n'.join(novas)
            nome = f'v06={v06n}·sman={smn}·msg={msn}'
            ok_janelas = all(
                (a0 >= 15 and b0 <= 28) or (a0 >= 488)      # hunks só nas 2 zonas
                for tg, a0, b0, c0, d0 in
                (o for o in difflib.SequenceMatcher(None, L, novas, autojunk=False).get_opcodes() if o[0] != 'equal')
            )
            cands[nome] = {'sha': hashlib.sha256(txt.encode('utf-8')).hexdigest(),
                           'linhas': len(novas) - (1 if novas[-1] == '' else 0),
                           'compila': None, 'ok_janelas': ok_janelas, 'txt': txt}
            try: compile(txt, nome, 'exec'); cands[nome]['compila'] = True
            except SyntaxError: cands[nome]['compila'] = False
R['candidatos'] = {k: {kk: vv for kk, vv in v.items() if kk != 'txt'} for k, v in cands.items()}
alvo = [k for k, v in cands.items() if v['sha'] == ALVO_SHA]
check('C1 exatamente UMA candidata com 665 linhas e sha be48a5ef…', len(alvo) == 1
      and all(v['linhas'] == 665 and v['compila'] and v['ok_janelas'] for v in cands.values()),
      'matches: ' + json.dumps(alvo))
R['aritmetica_linhas'] = ('658 + 6 comentário + 1 quebra V-08 = 665 ✔ (confere a correção dele ao critério: '
                          '+17/−7 em diffstat, +7 líquido)')

# --- comportamento da candidata selada ---
def gate(script, pasta):
    r = subprocess.run([sys.executable, str(script), str(pasta)], capture_output=True, text=True)
    e = re.findall(r'(\d+)\s+ERRO', r.stdout); a = re.findall(r'(\d+)\s+AVISO', r.stdout)
    v14 = [l for l in r.stdout.splitlines() if 'V-14' in l and 'ERRO' in l]
    return {'exit': r.returncode, 'erro': int(e[-1]) if e else None, 'aviso': int(a[-1]) if a else None,
            'v14_erro_linhas': v14[:2], 'tail': r.stdout[-400:], 'stdout': r.stdout}
if alvo:
    melhor = cands[alvo[0]]['txt']; R['variante_selada'] = alvo[0]
    STAGE.write_text(melhor, encoding='utf-8', newline='\n')
    g_base = gate(BASE, AT); g_nova = gate(STAGE, AT)
    R['comportamento'] = {'base': {k: v for k, v in g_base.items() if k != 'tail'},
                          'candidata': {k: v for k, v in g_nova.items() if k != 'tail'}}
    check('D1 candidata: 2 ERRO / 299 AVISO / exit 1 — idêntico à base (V-14 sem ERRO)',
          g_nova['exit'] == 1 and g_nova['erro'] == 2 and g_nova['aviso'] == 299 and not g_nova['v14_erro_linhas']
          and (g_base['erro'], g_base['aviso'], g_base['exit']) == (g_nova['erro'], g_nova['aviso'], g_nova['exit']),
      json.dumps(R['comportamento'])[:280])
    # F-C2: contraexemplo — trocar 1 ID do manifesto por falso, preservando contagem
    tmp = pathlib.Path('/tmp/p8_fc2_trilha47')
    if tmp.exists(): shutil.rmtree(tmp)
    shutil.copytree(AT, tmp, symlinks=True)
    man_l = tmp/'Evidencias/Bibliografia/_manifesto_biblioteca.json'
    man = json.loads(pathlib.Path(os.path.realpath(man_l)).read_text(encoding='utf-8'))
    rel = (man.get('semantic_layer') or {}).get('related_entities') or []
    assert len(rel) == 15, f'related_entities={len(rel)}'
    rel[0] = 'mecanismo_B999_inexistente'
    man_l.unlink(); man_l.write_text(json.dumps(man, ensure_ascii=False, indent=2), encoding='utf-8')
    # CONFISSÃO datada (2026-09-18): a 1ª execução procurou 'identidade divergente' só nos 400
    # chars finais (tail); a linha de ERRO vive na seção enumerada por regra, antes do resumo.
    # Comportamento estava certo — o detector estava errado. Procura agora no stdout inteiro.
    g_f  = gate(STAGE, tmp); g_fb = gate(BASE, tmp)
    R['fc2'] = {'related_entities_original': 15, 'candidata': {k: g_f[k] for k in ('exit','erro','aviso')},
                'base_tambem_dispara': 'identidade divergente' in g_fb['stdout'],
                'candidata_dispara': 'identidade divergente' in g_f['stdout'],
                'linha_erro': next((l.strip() for l in g_f['stdout'].splitlines() if 'identidade divergente' in l), '')[:160]}
    check('D2 F-C2 DISPARA na candidata (troca 1 ID falso → ERRO V-07 identidade divergente; exit 1; 3 ERRO = 2 design + 1)',
          R['fc2']['candidata_dispara'] and g_f['exit'] == 1 and g_f['erro'] == 3, json.dumps(R['fc2'], ensure_ascii=False)[:260])
    check('D3 paridade: a base oficial também dispara no mesmo contraexemplo (correção já era funcional desde a rodada 20)',
          R['fc2']['base_tambem_dispara'])
else:
    R['fallback'] = ('nenhuma variante das 3 zonas instáveis reproduziu be48a5ef… — HONRAR O FALLBACK DO MESTRE: '
                     'ficam os bytes 84fa918d… como sha viva única; regiões arquivadas verbatim para rastro futuro.')
    g_base = gate(BASE, AT)
    R['comportamento'] = {'base': {k: v for k, v in g_base.items() if k != 'tail'}}
    check('FALLBACK: base oficial permanece comportamental (2/299/exit 1)',
          g_base['exit'] == 1 and g_base['erro'] == 2 and g_base['aviso'] == 299)

# --- selos ---
V7 = AT/'B1 NEUROINFLAMAÇÃO V7 CANONICA.md'; MAN = AT/'Evidencias/Bibliografia/_manifesto_biblioteca.json'
check('S 0 ciência: V7 6e2c2979… · manifesto 79d1309a… (o contraexemplo rodou em /tmp, nunca no acervo)',
      sha(V7).startswith('6e2c2979') and sha(MAN).startswith('79d1309a'))

R['checks_ok'], R['checks_tot'] = sum(1 for c in R['checks'] if c['ok']), len(R['checks'])
R['falhas'] = [c['check'] for c in R['checks'] if not c['ok']]
OUT.write_text(json.dumps(R, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps({'checks': f"{R['checks_ok']}/{R['checks_tot']}", 'falhas': R['falhas'],
                  'variante_selada': R.get('variante_selada'), 'alvos': alvo}, ensure_ascii=False, indent=2))
