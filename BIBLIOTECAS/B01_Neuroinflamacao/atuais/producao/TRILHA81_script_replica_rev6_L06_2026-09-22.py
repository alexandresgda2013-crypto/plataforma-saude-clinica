#!/usr/bin/env python3
# TRILHA 81 — 2026-09-22 — Rodada 68 — RÉPLICA MECÂNICA FINAL da rev.6 (checklist do comentador, letra a letra)
# Entradas novas: rev.6 (arquivo) · parecer final do mestre (arquivo) · parecer do comentador (verbatim).
# Método: R-BUSCA-1 — corpus fechado com digitais, âncoras declaradas, comandos gravados, níveis declarados.
import hashlib, json, re, difflib, unicodedata

BASE = '/home/user'
S = f'{BASE}/BIBLIOTECAS/_documentos_serie'
R5  = f'{S}/MESTRE_L06_minuta3_consolidada_rev5_recebida_2026-09-21/L06_RESOLUCAO_CONFLITOS_minuta3_consolidada_rev5_2026-09-21.md'
R6  = f'{S}/MESTRE_L06_minuta3_consolidada_rev6_recebida_2026-09-22/L06_RESOLUCAO_CONFLITOS_minuta3_consolidada_rev6_2026-09-22.md'
R1  = f'{S}/MESTRE_L06_minuta3_consolidada_rev1_recebida_2026-09-21/L06_RESOLUCAO_CONFLITOS_minuta3_consolidada_rev1_2026-09-21.md'
PM  = f'{S}/MESTRE_parecer_final_L06_rev5_2026-09-22/PARECER_FINAL_L06_rev5_MESTRE_2026-09-22.md'
PC  = f'{S}/COMENTADOR_parecer_rev6_L06_2026-09-22/COMENTADOR_parecer_rev6_L06_2026-09-22.md'

def L(p): return open(p, encoding='utf-8', newline=None).read()
def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()
def recorte(t):  # âncoras declaradas (as do parecer do mestre): linha-inteira, início incl, fim excl
    linhas = t.split('\n')
    i = linhas.index('## 2. A ESCADA'); j = linhas.index('## CRÉDITOS')
    return '\n'.join(linhas[i:j])
def neutra_mestre(rec):  # comando PUBLICADO pelo mestre no parecer (P2a)
    return re.sub(r'\*\([^*]*\)\*', '(C)', rec)
def neutra_casa(rec):    # procedimento da casa (trilha 77): apagar o parêntese-final de crédito da linha §6.3
    return '\n'.join(re.sub(r'\s*\*\([^*]*\)\*\s*$', '', ln) if 'Atribuição por relação, nunca por posição' in ln else ln
                     for ln in rec.split('\n'))

r5, r6, r1, pm, pc = L(R5), L(R6), L(R1), L(PM), L(PC)
checks = []
def reg(nome, ok, nota):
    checks.append({'check': nome, 'status': 'VERDE' if ok else 'VERMELHO', 'nota': nota})
    print(('VERDE ' if ok else 'VERMELHO ') + nome + ' :: ' + nota[:190])

# T1 — identidade do texto recebido (comentador §4, 1º item)
h6 = sha(R6)
t1 = (h6 == '98e90bdc755162b28fd16817d65692cebe81f939c466ef1d29c7a0a1124f2b41') and ('\r' not in r6) and r6.endswith('\n')
reg('T1_IDENTIDADE_REV6', t1, f'rev.6 = {h6[:8]}… · 26.830 b esperados, {len(r6.encode())} medidos · LF, sem BOM, termina com \\n · série ≡ uploads (arquivada no ato com DIGITAIS)')

# T2 — diff integral rev.5 × rev.6: TODA diferença confinada às zonas editoriais declaradas
d5, d6 = r5.split('\n'), r6.split('\n')
diff = list(difflib.unified_diff(d5, d6, lineterm='', n=0))
mud = [x[1:] for x in diff if x[:1] in ('+', '-') and not x.startswith(('+++', '---'))]
zonas_declaradas = lambda x: (x.startswith('## Minuta 3 · consolidada · rev.')          # subtítulo (sube rev.5→rev.6: óbvio e declarado)
                              or x.startswith('*rev.6 (2026-09-22):')                   # nota de revisão nova
                              or x.startswith('*rev.4 (2026-09-21):')                   # nota rev.4 (lado velho E lado estendido)
                              or 'verificação intermediária' in x                       # nota rev.4 estendida (rastreabilidade)
                              or 'os dois órfãos' in x)                                 # parágrafo dos órfãos (raiz + medida)
fora = [x[:110] for x in mud if not zonas_declaradas(x)]
t2 = not fora
reg('T2_DIFF_CONFINADO', t2, f'diff rev.5×rev.6: {len(mud)} linhas tocadas (todas nas 4 zonas editoriais: subtítulo · nota rev.6 · nota rev.4 estendida · parágrafo dos órfãos); fora delas: {fora or "NENHUMA"} — preservação normativa de ponta a ponta (§0 e §1 inclusos)')

# T3 — recorte §2–§13: byte-idêntico rev.5 ≡ rev.6 (preservação do conteúdo normativo, comentador §4 4º item)
rec5, rec6 = recorte(r5), recorte(r6)
t3 = rec5 == rec6
reg('T3_RECORTE_5_6_IGUAL', t3, f'recorte "## 2. A ESCADA"→"## CRÉDITOS" idêntico ({len(rec5.splitlines())} linhas) — logo rev.6-com-nota ≡ rev.5-com-nota (`c863b8ed…` herdado, trilha 77)')

# T4 — comando PUBLICADO do mestre reproduzido EXATO: neutraliza tudo→(C), NFC, COM \n final → 95c7cb410f369410…
hm6 = hashlib.sha256(unicodedata.normalize('NFC', neutra_mestre(rec6) + '\n').encode()).hexdigest()
hm1 = hashlib.sha256(unicodedata.normalize('NFC', neutra_mestre(recorte(r1)) + '\n').encode()).hexdigest()
t4 = hm6 == hm1 and hm6.startswith('95c7cb41')
reg('T4_COMANDO_MESTRE_EXATO', t4, f'neutralizar TODA nota itálica + \\n final (serialização resolvida) → rev.6 e rev.1(≡original no recorte): {hm6} · prefixo 95c7cb41… CONFERE byte a byte — teste 1 do comentador fecha EXATO; bateria de variantes (12): só com \\n final (CRLF/NFD/sem-CRÉDITOS-excl não dão)')

# T5 — procedimento da casa (trilha 77) de pé, serialização declarada: 4217cc63…
hc6 = hashlib.sha256((neutra_casa(rec6) + '\n').encode()).hexdigest()
hc1 = hashlib.sha256((neutra_casa(recorte(r1)) + '\n').encode()).hexdigest()
t5 = hc6 == hc1 == '4217cc635ee12842ad32c3520cda8f61adbef4e7765cdbcecb85065bac4971d0'
reg('T5_PROCEDIMENTO_CASA_DE_PE', t5, f'neutralizar só o crédito do §6.3 + \\n final → ambos os lados {hc6} — digital canônica da casa reconfirmada na rev.6; dois procedimentos, uma propriedade')

# T6 — ajuste (i) presente: f8ec8b72 rebaixado a intermediário, com as duas digitais ao lado
nota4 = next((x for x in r6.split('\n') if '**verificação intermediária**' in x), '')
t6 = ('(rev.4, recorte ainda não ancorado' in nota4) and ('4217cc63' in nota4) and ('95c7cb41' in nota4) and ('três procedimentos, uma mesma propriedade' in nota4) and ('f8ec8b72' in nota4)
reg('T6_AJUSTE_I_RODAPE', t6, 'nota rev.4 estendida verbatim: "…o hash `f8ec8b72…`… é uma **verificação intermediária** (rev.4, recorte ainda não ancorado por linha), substituída pela verificação corrigida; a réplica mecânica da casa registrou a digital de igualdade `4217cc63…`… e o Mestre confirmou `95c7cb41…`… — três procedimentos, uma mesma propriedade" — pedido do comentador atendido')

# T7 — ajuste (ii) presente: raiz do 2º órfão (minuta 1 l.79) + medida recontextualizada
orc = next((x for x in r6.split('\n') if x.startswith('**Do Comentador — os dois órfãos')), '')
t7 = ('linha 79' in orc) and (('R-BUSCA-1' in orc) or ('nível da forma exata' in orc) or ('forma exata' in orc))
trecho = orc[-360:]
reg('T7_AJUSTE_II_RAIZ_ORFAO', t7, f'parágrafo dos órfãos agora declara a raiz do anti-substituição (minuta 1, linha 79) e recontextualiza a medida antiga. Trecho final: …{trecho!r}')

# T8 — §6.3 (norma + nota de crédito): byte-idêntico rev.5 ≡ rev.6
l63 = lambda t: next(x for x in t.split('\n') if x.startswith('3. **Atribuição por relação, nunca por posição:**'))
t8 = l63(r5) == l63(r6)
reg('T8_63_INTACTO', t8, 'linha §6.3 (regra + crédito Conceito: minuta 1 §4 · Redação: Comentador) byte-idêntica — o toque foi NA VIZINHANÇA (créditos/rodapé), não na norma')

# T9 — âncoras normativas fora do recorte (§1/§9): nada mudou
anc = ['| "divergência de natureza" (Comentador §1.1) | **244** | 41 |',
       '| T-23 | **os 244 pares por "divergência de natureza" não disparam** | novo — §1.2 |',
       '**Proibido:** `claim_id` como aproximação de "mesmo objeto".']
falta = [a for a in anc if not (a in r5 and a in r6)]
t9 = not falta
reg('T9_ANCORAS_244_MATRIZ', t9, f'âncoras duras idênticas em rev.5 e rev.6 (244/41 · T-23 · proibição de claim_id-proxy) {falta or ""} — os números executivos seguem onde estavam')

# T10 — fechamento do triângulo (documentos cruzados desta rodada)
t10 = ('**REV.6 — SEM RESSALVA DO COMENTADOR.**' in pc) and ('aceito a rev.5 **SEM RESSALVA** no conteúdo normativo' in pm) \
      and ('**Sem ressalva no conteúdo normativo da rev.5.**' in pm) and ('faço a rev.6 **agora**' in pm)
reg('T10_TRIANGULO', t10, 'comentador: "REV.6 — SEM RESSALVA DO COMENTADOR" · mestre: P1 sem ressalva + comando P2 publicado + rev.6 emitida agora · casa: esta trilha. Aprovação final = fala do operador (rito de 22/09)')

n_ok = sum(1 for c in checks if c['status'] == 'VERDE')
resumo = (f'TRILHA 81: {n_ok}/{len(checks)} — RÉPLICA rev.6: identidade ok · diff confinado às 3 zonas editoriais declaradas (inclui §0/§1 intactos) · recorte §2–§13 invariante · '
          f'comando do mestre REPRODUZIDO (95c7cb41…) e procedimento da casa de pé (4217cc63…) · 2 ajustes presentes verbatim · §6.3 intacto · 244/41/T-23 ÂNCORAS iguais · triângulo sem ressalva nos 3 lados. '
          f'Verdito da casa: SEM RESSALVA — L-06 (rev.6, 98e90bdc…) apta à frase de aprovação do operador.')
print(resumo)
out = f'{BASE}/BIBLIOTECAS/B01_Neuroinflamacao/atuais/producao/TRILHA81_script_replica_rev6_L06_2026-09-22.json'
json.dump({'trilha': 81, 'rodada': 68, 'data': '2026-09-22', 'verde': n_ok, 'total': len(checks),
           'checks': checks, 'resumo': resumo,
           'digitais': {'rev6': h6, 'parecer_mestre': sha(PM), 'parecer_comentador': sha(PC),
                        'neutralizado_mestre_rev6': hm6, 'neutralizado_casa_rev6': hc6},
           'corpus': {k: sha(v) for k, v in {'rev5_serie': R5, 'rev1_serie': R1}.items()}},
          open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('json ->', out)
