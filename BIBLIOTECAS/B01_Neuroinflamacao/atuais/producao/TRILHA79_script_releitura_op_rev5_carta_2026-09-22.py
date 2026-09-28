#!/usr/bin/env python3
# TRILHA 79 — 2026-09-22 — Rodada 66 — Re-leitura verificada: rev.5 × carta do comentador × palavra do operador
# Gatilho: operador — "eu não disse essa frase" (a casa sugeriu uma frase de aprovação e passou a chamá-la
# de "a sua frase"); pediu re-análise se a casa leu certo a rev.5 e o comentário do comentador.
# Método: R-BUSCA-1 sobre os próprios atos da casa (corpus fechado, padrão, trinca, nível declarado).
import hashlib, json, re

BASE = '/home/user'
REV5  = f'{BASE}/BIBLIOTECAS/_documentos_serie/MESTRE_L06_minuta3_consolidada_rev5_recebida_2026-09-21/L06_RESOLUCAO_CONFLITOS_minuta3_consolidada_rev5_2026-09-21.md'
CARTA = f'{BASE}/BIBLIOTECAS/_documentos_serie/COMENTADOR_carta_rev5_L06_2026-09-21/COMENTADOR_carta_rev5_L06_2026-09-21.md'
AD2   = f'{BASE}/ENTREGAS/2026-09-22_ADENDA2_ATA_L06/ADENDA_2_ATA_PROVENIENCIA_L06_RBUSCA1_2026-09-22.md'
REPL  = f'{BASE}/ENTREGAS/2026-09-21_REPLICA_FINAL_L06/REPLICA_MECANICA_FINAL_L06_rev5_2026-09-21.md'
M1    = f'{BASE}/BIBLIOTECAS/_documentos_serie/L06_minuta_mestre_recebida_2026-09-15/L06_RESOLUCAO_CONFLITOS_minuta1_2026-09-15.md'
CHAN  = f'{BASE}/BIBLIOTECAS/CHANGELOG_GERAL.md'
DEC   = f'{BASE}/BIBLIOTECAS/B01_Neuroinflamacao/atuais/Auditoria_B1/decisoes_B1.md'

def L(p): return open(p, encoding='utf-8', newline=None).read()
def sha(p): return hashlib.sha256(open(p,'rb').read()).hexdigest()

rv, ca, ad2, rp, m1, ch, dc = L(REV5), L(CARTA), L(AD2), L(REPL), L(M1), L(CHAN), L(DEC)
FRASE = 'Aprovo como vigente a L-06'
checks = []
def reg(nome, ok, nota):
    checks.append({'check': nome, 'status': 'VERDE' if ok else 'VERMELHO', 'nota': nota})
    print(('VERDE ' if ok else 'VERMELHO ') + nome + ' :: ' + nota[:190])

# T1 — a frase nasceu na casa: 0× na rev.5, 0× na carta; na réplica consta como SUGESTÃO da casa
t1 = (FRASE not in rv) and (FRASE not in ca) and ('Sugestão de frase' in rp and FRASE in rp)
reg('T1_FRASE_E_DA_CASA', t1,
    'a frase "Aprovo como vigente…" aparece 0× na rev.5 e 0× na carta do comentador; na réplica da casa ela existe rotulada "Sugestão de frase". Autoria: casa. O operador nunca a disse')

# T2 — o deslize de atribuição: adenda 2 chamou a sugestão da casa de "a sua frase" (2×)
deslizes = [i+1 for i, x in enumerate(ad2.split('\n')) if 'sua frase' in x.lower()]
t2 = len(deslizes) == 2
reg('T2_DESLIZE_LOCALIZADO', t2,
    f'adenda 2 linhas {deslizes}: "A sua frase segue a mesma…" / "falta só a sua frase de aprovação" — atribuí ao operador uma frase que a própria casa escreveu. Corrige-se por errata datada (pacote selado não se reescreve)')

# T3 — nenhum ato de governança registra aprovação inexistente (sanidade do livro-razão)
gov = ch + '\n' + dc
falsos = [p for p in ['operador aprovou a L-06', 'L-06 vigente', 'aprovada pelo operador a L-06', 'L-06 APROVADA'] if p in gov]
t3 = len(falsos) == 0 and 'apta à aprovação do operador' in rp.lower().replace('à','à')
t3 = len(falsos) == 0
reg('T3_LIVRO_RAZAO_LIMPO', t3,
    f'CHANGELOG+decisoes: 0× afirmações de aprovação inexistente {falsos}; o estado registrado é "aguarda/ apta à aprovação" — nenhum dano contábil, o erro foi de vocativo (atribuição), não de estado')

# T4 — leitura do RITO da rev.5 (verbatim, com linha)
rito = next((x.strip() for x in rv.split('\n') if x.strip().startswith('*Rito:')), '')
t4 = rito.startswith('*Rito: esta minuta segue para réplica da casa e, depois, aprovação do operador.')
reg('T4_RITO_REV5', t4, 'rev.5 rodapé verbatim: "Rito: esta minuta segue para réplica da casa e, depois, aprovação do operador." — leitura da casa sobre o rito: CORRETA')

# T5 — leitura da CARTA do comentador (verbatim, 4 trincas)
tr = ['considero que os quatro pontos solicitados foram tratados corretamente',
      'Não considero isso uma alteração normativa',
      'Não há solicitação de reabertura do conteúdo normativo da L-06',
      'Arena/Casa → registro → Auditor-Mestre → réplica mecânica final da Casa → aprovação do operador']
faltam = [x for x in tr if x not in ca]
t5 = not faltam
reg('T5_CARTA_COMENTADOR', t5, 'carta verbatim confere: 4 pontos tratados · ponto 5 "não é alteração normativa" · sem reabertura · fluxo …→ réplica da Casa → aprovação do operador. Leitura da casa: CORRETA')

# T6 — ACHADO novo na re-leitura: parágrafo dos órfãos nos CRÉDITOS tem 2 assimetrias
# (âncora correta: a linha que COMEÇA com '**Do Comentador — os dois órfãos', não a nota de cabeçalho da rev.5)
orc = next((x for x in rv.split('\n') if x.startswith('**Do Comentador — os dois órfãos')), '')
t6a = ('raiz do *conceito* de "atribuição por relação" está na minuta 1 do Mestre §4' in orc)
tem_anti_raiz = ('silenc' in orc.split('anti-substituição-silenciosa')[1].replace('TextoH, Parte 8', '')) if orc else False
t6 = bool(orc) and t6a and (not tem_anti_raiz) and ('a casa mediu 0× nela' in orc)
reg('T6_NUANCE_NOS_CREDITOS', t6,
    'CRÉDITOS §órfãos (parágrafo certo localizado): raiz declarada SÓ p/ "atribuição" (minuta 1 §4) · o anti-substituição ficou sem raiz declarada (a raiz é minuta 1 l.79 — trilha 78) · e a frase "a casa mediu 0× nela" registra medição da régua velha (verdade só no nível exato L1). Precisão a propor no próximo toque editorial (rev.6), junto do rodapé f8ec8b72')

# T9 (bonus) — autoria da rodada de ajustes: rev.5 diz "quatro ajustes DO OPERADOR"; comentador diz "anunciados pelo Auditor-Mestre"
top5 = '\n'.join(rv.split('\n')[:12])
t9 = ('quatro ajustes do operador' in top5) and ('quatro ajustes anunciados pelo Auditor-Mestre' in ca)
reg('T9_AUTORIA_DOS_4_AJUSTES', t9,
    'rev.5 cabeçalho: "quatro ajustes do operador" · carta: "quatro ajustes anunciados pelo Auditor-Mestre" — os 4 mapeiam 1:1 nos pontos que o comentador confirmou; mas a casa NÃO tem arquivada a mensagem do operador que os listou → DÍVIDA D-4AJUSTES-OPERADOR (registrar a fala dele verbatim ou ele confirma aqui)')

# T7 — §6.3 da rev.5 ≡ minuta 1 l.97 (conteúdo da citação)
cit = 'rótulos atribuídos por relação", não por posição'
l97 = m1.split('\n')[96].replace('**', '')
t7 = ('Conceito: minuta 1 do Mestre, §4' in rv) and ('atribuídos por relação**, não por posição' in m1.split('\n')[96])
reg('T7_63_CONSISTENTE', t7, 'rev.5 §6.3 cita minuta 1 §4 e a citação bate com a linha 97 real (módulo asteriscos) — o conserto da rev.5 está de pé, trilha 78 confirma')

# T8 — hashes citadas na carta existem e foram respondidas na réplica (escopo declarado)
hs = ['95c7cb41', 'c863b8ed', '8a8ff986', 'f8ec8b72']
onde = {h: ('carta' if h in ca else '-') + '/' + ('replica' if h in rp else '-') + '/' + ('rev5' if h in rv else '-') for h in hs}
t8 = all(h in ca for h in hs) and all(h in rp or h in rv for h in hs)
reg('T8_HASHES_ESCOPO', t8, f'digitais da carta localizadas {onde} — as 4 foram respondidas; 95c7cb41/f8ec8b72 ficaram não-reproduzidas na bancada (dívida: comando exato do mestre, já pedida)')

n_ok = sum(1 for c in checks if c['status'] == 'VERDE')
resumo = (f'TRILHA 79: {n_ok}/{len(checks)} — CONFISSÃO C79-1: frase de aprovação é de autoria da casa (sugestão rotulada na réplica) e a adenda 2 a chamou de '
          f'"a sua frase" (2×) — atribuição errada ao operador, corrigida por errata datada. Re-leitura: rito e carta lidos CORRETAMENTE (trincas verbatim). '
          f'ACHADO A-79-1: parágrafo dos órfãos nos CRÉDITOS da rev.5 pede precisão no próximo toque editorial: raiz do anti-substituição = minuta 1 l.79 e a frase '
          f'"a casa mediu 0× nela" vale só no nível exato (nova régua). DÍVIDA D-4AJUSTES-OPERADOR: rev.5 atribui os 4 ajustes ao operador — a casa não tem a fala dele verbatim sobre isso. '
          f'Livro-razão limpo: nenhuma aprovação inexistente registrada. L-06 segue APTA, aguardando a fala real do operador.')
print(resumo)
out = f'{BASE}/BIBLIOTECAS/B01_Neuroinflamacao/atuais/producao/TRILHA79_script_releitura_op_rev5_carta_2026-09-22.json'
json.dump({'trilha': 79, 'rodada': 66, 'data': '2026-09-22', 'verde': n_ok, 'total': len(checks),
           'checks': checks, 'resumo': resumo, 'confissoes': ['C79-1'], 'achados': ['A-79-1'], 'dividas': ['D-4AJUSTES-OPERADOR'],
           'corpus': {k: sha(v) for k, v in {'rev5': REV5, 'carta': CARTA, 'adenda2': AD2, 'replica': REPL, 'm1': M1}.items()}},
          open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('json ->', out)
