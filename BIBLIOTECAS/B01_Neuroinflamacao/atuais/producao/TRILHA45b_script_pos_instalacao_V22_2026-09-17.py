#!/usr/bin/env python3
# TRILHA 45b — PÓS-INSTALAÇÃO da V2.2 vigente (rodada 26 · 2026-09-17).
# Confirma: digitais, escopo cirúrgico vs SUPERSEDED, contagens-chave e 0 ciência.
import hashlib, json, re, unicodedata, pathlib

ROOT  = pathlib.Path('/home/user')
SERIE = ROOT/'BIBLIOTECAS/_documentos_serie'
NOVA  = SERIE/'ARQUITETURA CONSOLIDADA DA PLATAFORMA V2.2  -  17.09.26.md'
SUP   = SERIE/'SUPERSEDED_ARQUITETURA CONSOLIDADA DA PLATAFORMA V2.1  -  17.09.26.md'
PONT  = SERIE/'ARQUITETURA_VIGENTE.txt'
V7    = ROOT/'BIBLIOTECAS/B01_Neuroinflamacao/atuais/B1 NEUROINFLAMAÇÃO V7 CANONICA.md'
MAN   = ROOT/'BIBLIOTECAS/B01_Neuroinflamacao/atuais/Evidencias/Bibliografia/_manifesto_biblioteca.json'
P8    = ROOT/'Ferramentas de geração e auditoria/06_portao_P8_coerencia/scripts/validar_coerencia_camadas.py'
VINC  = ROOT/'BIBLIOTECAS/B01_Neuroinflamacao/atuais/Evidencias/Vinculos/vinculos_referencia_afirmacao.json'
OUT   = ROOT/'BIBLIOTECAS/B01_Neuroinflamacao/atuais/producao/TRILHA45b_pos_instalacao_V22_2026-09-17.json'

sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
R = {'trilha': '45b', 'data': '2026-09-17', 'objeto': 'pós-instalação V2.2 vigente', 'checks': []}
def check(nome, ok, det=''):
    R['checks'].append({'check': nome, 'ok': bool(ok), 'detalhe': det})

s_nova, s_sup = sha(NOVA), sha(SUP)
check('vigente = sha da candidata aprovada (df7f7cfd…)', s_nova == 'df7f7cfdfc01cf77d658885f30dfefe29dcf380229ea56e6b3af02920df22ae1', s_nova[:16])
check('SUPERSEDED V2.1 intacta (1a50645e…)', s_sup == '1a50645e260984ab7b78b95abc177bdb171203f55f22990c195e5cefa0a94b60', s_sup[:16])
pont = PONT.read_bytes().decode('utf-8')
check('ponteiro aponta p/ V2.2 com sha e cadeia V1→V2→V2.1→V2.2',
      'df7f7cfdfc01cf77d658885f30dfefe29dcf380229ea56e6b3af02920df22ae1' in pont and 'V2.2' in pont
      and pont.count('SUPERSEDED:') == 3 and '1a50645e' in pont and '09692e18' in pont and '8f050469' in pont)

def linhas(p):
    return p.read_bytes().decode('utf-8').split('\r\n')
Ln, Ls = linhas(NOVA), linhas(SUP)
Tn = unicodedata.normalize('NFC', '\n'.join(Ln))
i0 = next(i for i, l in enumerate(Ln) if l == '```text'); i1 = next(i for i, l in enumerate(Ln) if i > i0 and l == '```')
des = unicodedata.normalize('NFC', '\n'.join(Ln[i0:i1]))
check('desenho §2: 0 unificad · 1 PASTA DE ATUALIZAÇÃO própria',
      des.casefold().count('unificad') == 0 and des.count('PASTA DE ATUALIZAÇÃO') == 1)
check('unificad total na vigente = 1 (citação histórica na linha Rev)', Tn.casefold().count('unificad') == 1, str(Tn.casefold().count('unificad')))
hc = [l for l in Ln if re.match(r'^# ', l)]; hn = [int(m.group(1)) for l in Ln if (m := re.match(r'^# (\d+)\.', l))]
check('31 cabeçalhos "# " · 30 seções numeradas únicas 1..30', len(hc) == 31 and len(hn) == 30 and sorted(hn) == list(range(1,31)), f'{len(hc)}/{len(hn)}')
check('origem_conhecimento ×3 (Rev · desenho · prosa)', Tn.casefold().count('origem_conhecimento') == 3)
R['confissao_2'] = ('1ª régua deste check esperava 2 (desenho+prosa); a linha Rev também carrega o par — real medido = 3. '
                    'Régua corrigida para ==3 com camada declarada (Rev · desenho · prosa). Confissão datada 2026-09-17.')
check('canonico | atualizacao presente (Rev + desenho + prosa)', Tn.count('canonico | atualizacao') == 3)
check('tríade + explicação + anamnese + busca ativa + conexão preservadas',
      all(x in Tn for x in ('MECANÍSTICA','TERAPÊUTICA','EXPLICAÇÃO NARRATIVA','ANAMNESE','O Motor busca ativamente','[ CONEXÃO / CONSULTA ]')))
icn = next(i for i, l in enumerate(Ln) if l.startswith('# 3. CATÁLOGO'))
ics = next(i for i, l in enumerate(Ls) if l.startswith('# 3. CATÁLOGO'))
check('ESCOPO CIRÚRGICO: sufixo §3→fim BYTE-IDÊNTICO vs V2.1 (catálogo 146 · §§5-30 · §18/§19/§20)',
      '\r\n'.join(Ln[icn:]) == '\r\n'.join(Ls[ics:]))
R['selos'] = {'V7': sha(V7), 'manifesto': sha(MAN), 'P8': sha(P8), 'vinculos': sha(VINC)}
check('0 ciência: V7 6e2c2979… · manifesto 79d1309a… · P-8 84fa918d… · vínculos 490675e6…',
      R['selos']['V7'].startswith('6e2c2979') and R['selos']['manifesto'].startswith('79d1309a')
      and R['selos']['P8'].startswith('84fa918d') and R['selos']['vinculos'].startswith('490675e6'))
R['resultado_ok'] = all(c['ok'] for c in R['checks'])
OUT.write_text(json.dumps(R, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps({'checks': f"{sum(1 for c in R['checks'] if c['ok'])}/{len(R['checks'])}",
                  'falhas': [c['check'] for c in R['checks'] if not c['ok']]}, ensure_ascii=False))
