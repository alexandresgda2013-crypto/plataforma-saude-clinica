#!/usr/bin/env python3
# TRILHA 78 — 2026-09-22 — Rodada 65 — Auditoria de método: os 2 "órfãos" da proveniência L-06
# Gatilho: operador encontrou "atribuídos por relação" na minuta 1 (linha 97) onde a casa disse "0×".
# Autópsia: trilha 74 l.40 e trilha 75 l.43 buscaram o padrão de 7 letras "atribui" (i sem acento),
# que NÃO casa com "atribuídos" (í = U+00ED). E usaram radical de 6 letras ("atribu") só na RESPOSTA_10:
# régua assimétrica dentro do mesmo teste. 2º achado: "falta de dado vira afirmação de coexistência"
# é da MINUTA 1 (l.79, mestre), e a ata creditou à RESPOSTA_10 (casa) — fonte trocada.
# Esta trilha refaz as medidas com réguas simétricas e níveis declarados (R-BUSCA-1).
import hashlib, json, unicodedata, re

BASE = '/home/user'
M1  = f'{BASE}/BIBLIOTECAS/_documentos_serie/L06_minuta_mestre_recebida_2026-09-15/L06_RESOLUCAO_CONFLITOS_minuta1_2026-09-15.md'
R10 = f'{BASE}/BIBLIOTECAS/_documentos_serie/RESPOSTA_10_L06_MINUTA1_E_P8_HARMONIZADO_2026-09-15.md'
TH  = f'{BASE}/BIBLIOTECAS/_documentos_serie/COMENTADOR_minuta2_L06_recebida_2026-09-21/COMENTADOR_minuta2_L06_2026-09-21.md'
TM  = f'{BASE}/BIBLIOTECAS/_documentos_serie/COMENTADOR_minuta2_L06_CANONICA_recebida_2026-09-21/COMENTADOR_minuta2_L06_CANONICA_2026-09-21.md'
REV5= f'{BASE}/uploads/L06_RESOLUCAO_CONFLITOS_minuta3_consolidada_rev5_2026-09-21.md'

def L(p): return open(p, encoding='utf-8', newline=None).read()           # régua: texto universal newlines
def sha(p): return hashlib.sha256(open(p,'rb').read()).hexdigest()
def fold(s): return unicodedata.normalize('NFC', s).casefold()            # régua: NFC + casefold

m1, r10, th, tm, rv5 = L(M1), L(R10), L(TH), L(TM), L(REV5)
m1l = m1.split('\n'); thl = th.split('\n'); r5l = rv5.split('\n')

checks = []
def reg(nome, ok, nota):
    checks.append({'check': nome, 'status': 'VERDE' if ok else 'VERMELHO', 'nota': nota})
    print(('VERDE ' if ok else 'VERMELHO ') + nome + ' :: ' + nota[:200])

# T1 — reproduz o erro: padrão antigo de 7 letras na minuta 1
reg('T1_REPRODUCAO_DO_ERRO', ('atribui' not in m1) and ('atribu' in m1),
    'padrão antigo "atribui" (7 letras) = 0× na minuta 1 (cai no í acentuado) · radical "atribu" (6 letras) = 1× — o zero foi artefato do acento; trilha 75 l.43 usou 7 letras em m1 e 6 em r10 (régua assimétrica)')

# T2 — a trinca real: minuta 1 linha 97
lin97 = m1l[96]
t2 = ('atribuídos por relação' in lin97) and ('não por posição' in lin97)
reg('T2_MINUTA1_LINHA97', t2,
    f'minuta 1 (PARTE 4, item 2 — Simetria), linha 97 verbatim: "…rótulos **atribuídos por relação**, não por posição." → CONCEITO está na minuta 1')

# T3 — veredito em níveis (R-BUSCA-1): exata × família × conceito
n_exata = m1.count('atribuição por relação')      # L1 forma exata (substantivo)
n_familia = sum(1 for ln in m1l if 'atribu' in ln) # L2 família/radical
reg('T3_NIVEIS_DECLARADOS', n_exata == 0 and n_familia == 1,
    f'L1 exata "atribuição por relação" = {n_exata}× na minuta 1 · L2 família "atribu*" = {n_familia} linha (l.97) · L3 conceito = PRESENTE via trinca da l.97. O "0×" antigo só era verdade no L1 e foi publicado como se fosse L3')

# T4 — o que é do comentador: a forma-regra autônoma no TextoH (l.229-230)
t4 = 'Atribuição por relação.' in th and 'nunca à posição' in th
reg('T4_REDACAO_COMENTADOR_TEXTOH', t4,
    f'TextoH l.229-230: regra autônoma "3. **Atribuição por relação.** Quando os degraus 5 ou 6 produzirem rótulos, estes serão atribuídos à relação…, nunca à posição…" → a forma-norma encorpada é mesmo da pena do comentador')

# T5 — a rev.5 JÁ carrega a atribuição correta (conceito minuta 1 §4 · redação comentador)
l180 = next((x for x in r5l if 'Atribuição por relação, nunca por posição' in x), '')
t5 = ('Conceito: minuta 1 do Mestre, §4' in l180) and ('Redação desta frase: Comentador' in l180)
reg('T5_REV5_JA_CORRETA', t5,
    'rev.5 §6.3 (l.180): "(Conceito: minuta 1 do Mestre, §4 — \\"rótulos atribuídos por relação, não por posição\\". Redação desta frase: Comentador…)" → o texto NORMATIVO candidato não precisa de emenda; quem erra é o MEU registro histórico')

# T6 — 2º achado: raiz do anti-substituir-silencioso é a MINUTA 1, não a RESPOSTA_10
frase_raiz = 'falta de dado vira afirmação de coexistência'
t6 = (frase_raiz in m1l[78]) and (frase_raiz not in r10)
reg('T6_RAIZ_E_DA_MINUTA1', t6,
    f'minuta 1 l.79 (mestre, 15/09): "…desce silenciosamente a escada… **falta de dado vira afirmação de coexistência**" · RESPOSTA_10 = 0× → a ata creditou a raiz à RESPOSTA_10 (casa): FONTE TROCADA; a raiz é do mestre')

# T7 — o que é do comentador nesse 2º item: a regra-norma do TextoH Parte 8
l278 = 'não autoriza substituição silenciosa por outro campo semanticamente parecido'
t7 = (l278 in th) and (l278 not in m1) and ('substitu' not in m1 and 'silenciosamente' in m1)
reg('T7_NORMA_E_DO_COMENTADOR', t7,
    'TextoH Parte 8 (l.278): "A ausência de uma dependência não autoriza substituição silenciosa por outro campo semanticamente parecido." · minuta 1 tem o diagnóstico (l.79, "silenciosamente") mas 0× "substitu*" → norma-redação = comentador, raiz-conceito = minuta 1 l.79')

# T8 — réguas simétricas desta trilha (meta-checagem da própria trilha)
pats = [('atribu', [m1, r10, th, tm, rv5]), ('silencio', [m1, r10, th, tm, rv5]), ('substitu', [m1, r10, th, tm, rv5])]
res = {p: [fold(t).count(fold(p)) for t in ts] for p, ts in pats}
reg('T8_REGUA_SIMETRICA', True,
    f'mesmos radicais nos 5 corpora (m1, r10, TextoH, TextoM, rev.5), sem vogal acentuável na borda → contagens: {res} — esta é a régua R-BUSCA-1 em exercício')

# T9 — sanidade: rev.5 intacta (digital da rodada 64) e o que não muda
h = sha(REV5)
reg('T9_REV5_INTEGRA', h == '601c1f18d074e6e4488dd8a6ee3364345e51713f7d0277cd1637add838a79608',
    f'rev.5 = {h[:8]}… confere (rodada 64). NOTA: este arquivo vive em uploads/ — série recebe cópia com DIGITAIS nesta rodada (dívida doméstica)')

# T10 — TextoM canônico: a forma-regra "atribuição por relação" não existe lá; cuidado com falso amigo do radical
linha_tm_atribu = next((f'l.{i+1}: {x.strip()[:110]}' for i, x in enumerate(tm.split('\n')) if 'atribu' in x), '—')
t10 = ('atribuição por relação' not in tm) and ('atribuíd' not in tm)
reg('T10_TEXTOM_SEM_A_REGRA', t10,
    f'TextoM (8ad6bc15…): 0× "atribuição por relação" e 0× flexão "atribuíd*" → forma-regra vive só no TextoH. '
    f'FALSO AMIGO DO RADICAL: "atribu" dá 1× no TextoM ({linha_tm_atribu}) — é "atribuir força" (regra de degrau indisponível), outro sentido. '
    f'Lição ao vivo da R-BUSCA-1: radical serve p/ ENCONTRAR candidatos; o veredito exige ler a trinca (sentido), senão o falso amigo vira dado')

n_ok = sum(1 for c in checks if c['status'] == 'VERDE')
resumo = (f'TRILHA 78: {n_ok}/{len(checks)} — MAPA CORRIGIDO: (1) "atribuição por relação": conceito+quase-frase '
          f'= minuta 1 l.97 (PARTE 4, Simetria) · forma-regra = comentador TextoH l.229-230 · rev.5 já correta. '
          f'(2) anti-substituição silenciosa: raiz-conceito = minuta 1 l.79 (mestre) · norma-redação = comentador TextoH Parte 8 l.278. '
          f'CONFISSÕES: C78-1 ("atribui" 7 letras cego ao í de "atribuídos"; régua assimétrica 7l×6l no mesmo teste) · '
          f'C78-2 (raiz creditada à RESPOSTA_10 quando era da minuta 1 — fonte trocada). NADA muda em bytes/digitais/244/matriz/trilha 77.')
print(resumo)
out = f'{BASE}/BIBLIOTECAS/B01_Neuroinflamacao/atuais/producao/TRILHA78_script_r_busca_1_orfaos_L06_2026-09-22.json'
json.dump({'trilha': 78, 'rodada': 65, 'data': '2026-09-22', 'verde': n_ok, 'total': len(checks),
           'checks': checks, 'resumo': resumo,
           'confissoes': ['C78-1', 'C78-2'],
           'corpus': {k: sha(v) for k, v in {'m1': M1, 'r10': R10, 'th': TH, 'tm': TM, 'rev5': REV5}.items()}},
          open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('json ->', out)
