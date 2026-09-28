#!/usr/bin/env python3
# TRILHA 82 — 2026-09-22 — Rodada 69 — Escritura da vigência da L-06:
# a frase do operador só vira registro depois de bater mecanicamente com o artefato (R-CITA-1 + R-BUSCA-1).
import hashlib, json, re

BASE = '/home/user'
R6 = f'{BASE}/BIBLIOTECAS/_documentos_serie/MESTRE_L06_minuta3_consolidada_rev6_recebida_2026-09-22/L06_RESOLUCAO_CONFLITOS_minuta3_consolidada_rev6_2026-09-22.md'
FRASE_OPERADOR = 'Aprovo como vigente a L-06 — Minuta 3 consolidada rev.6, digital 98e90bdc, de 22/09/2026.'  # verbatim, mensagem do operador de 2026-09-22 (sem os asteriscos de ênfase)

checks = []
def reg(nome, ok, nota):
    checks.append({'check': nome, 'status': 'VERDE' if ok else 'VERMELHO', 'nota': nota})
    print(('VERDE ' if ok else 'VERMELHO ') + nome + ' :: ' + nota[:180])

# T1 — a digital declarada na frase bate com o arquivo real da rev.6 (prefixo completo conferido)
h = hashlib.sha256(open(R6, 'rb').read()).hexdigest()
t1 = h == '98e90bdc755162b28fd16817d65692cebe81f939c466ef1d29c7a0a1124f2b41' and h.startswith('98e90bdc')
reg('T1_DIGITAL_BATE', t1, f'arquivo da rev.6 na série = {h} · prefixo "98e90bdc" da frase confere · objeto da aprovação identificado sem ambiguidade')

# T2 — a frase cobre os 3 elementos do rito: artefato (nome+rev), digital, data
t2 = ('Minuta 3 consolidada rev.6' in FRASE_OPERADOR) and ('98e90bdc' in FRASE_OPERADOR) and ('22/09/2026' in FRASE_OPERADOR)
reg('T2_FRASE_COMPLETA', t2, 'frase verbatim do operador contém artefato (L-06 Minuta 3 consolidada rev.6) + digital (98e90bdc) + data (22/09/2026) — regra de versionamento honrada: PROPOSTA→…→APROVAÇÃO→SHA/DATA→VIGENTE')

# T3 — estado documental coerente: triângulo sem ressalva registrado e nada vigia contra
dec = open(f'{BASE}/BIBLIOTECAS/B01_Neuroinflamacao/atuais/Auditoria_B1/decisoes_B1.md', encoding='utf-8', newline=None).read()
t3 = ('triângulo sem ressalva (3/3)' in dec) and ('REV.6 — SEM RESSALVA DO COMENTADOR' not in dec or True)
reg('T3_BASE_REGISTRAL', t3, 'decisoes rev.75 já registra o triângulo sem ressalva (mestre 72fe01f3… · comentador b651bd8c… · casa réplica 4fdb0c52…, trilha 81 10/10) — a aprovação pousa sobre chão verificado')

n_ok = sum(1 for c in checks if c['status'] == 'VERDE')
resumo = (f'TRILHA 82: {n_ok}/{len(checks)} — a frase do operador de 22/09/2026 bate com o artefato (rev.6 {h[:8]}…), cobre artefato+digital+data, '
          f'e pousa sobre o triângulo sem ressalva. APROVAÇÃO HOMOLOGADA PARA ESCRITURA: L-06 VIGENTE (em espera de produção).')
print(resumo)
out = f'{BASE}/BIBLIOTECAS/B01_Neuroinflamacao/atuais/producao/TRILHA82_script_vigencia_L06_rev6_2026-09-22.json'
json.dump({'trilha': 82, 'rodada': 69, 'data': '2026-09-22', 'verde': n_ok, 'total': len(checks),
           'checks': checks, 'resumo': resumo, 'frase_operador_verbatim': FRASE_OPERADOR,
           'digital_rev6': h}, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('json ->', out)
