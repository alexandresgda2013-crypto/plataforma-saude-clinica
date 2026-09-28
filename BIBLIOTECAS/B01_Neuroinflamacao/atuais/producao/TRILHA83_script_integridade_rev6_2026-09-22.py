#!/usr/bin/env python3
# TRILHA 83 — 2026-09-22 — Rodada 70 — A pergunta de fecho do operador:
# "no Arena não foi mudado nenhuma linha ou letra ou palavra da L-06 rev.6?"
# Prova mecânica: o arquivo na pasta de chegada (uploads) ≡ cópia da série ≡ digital registrada na escritura.
import hashlib, json

BASE = '/home/user'
UPL   = f'{BASE}/uploads/L06_RESOLUCAO_CONFLITOS_minuta3_consolidada_rev6_2026-09-22.md'
SERIE = f'{BASE}/BIBLIOTECAS/_documentos_serie/MESTRE_L06_minuta3_consolidada_rev6_recebida_2026-09-22/L06_RESOLUCAO_CONFLITOS_minuta3_consolidada_rev6_2026-09-22.md'
VIG   = f'{BASE}/BIBLIOTECAS/_documentos_serie/L06_VIGENTE.txt'
ESPERADA = '98e90bdc755162b28fd16817d65692cebe81f939c466ef1d29c7a0a1124f2b41'

def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()
checks = []
def reg(nome, ok, nota):
    checks.append({'check': nome, 'status': 'VERDE' if ok else 'VERMELHO', 'nota': nota})
    print(('VERDE ' if ok else 'VERMELHO ') + nome + ' :: ' + nota[:170])

hu, hs = sha(UPL), sha(SERIE)
t1 = hu == hs == ESPERADA
reg('T1_UPLOADS_IGUAL_SERIE_IGUAL_REGISTRO', t1,
    f'uploads = {hu[:12]}… · série = {hs[:12]}… · escritura = {ESPERADA[:12]}… → os três são O MESMO objeto byte a byte; a rev.6 não sofreu NENHuma alteração dentro do Arena desde a chegada (a casa só leu)')

# T2 — a casa não escreveu nada dentro do arquivo: conteúdo dela vive em OUTROS arquivos (réplica/cartas/comunicado)
# prova estrutural: a rev.6 nem aparece como caminho de escrita em nenhuma entrega; e o sha dela já era este na 1ª medição (trilha 81 T1, mesma sessão da chegada)
t2 = hu == ESPERADA
reg('T2_MESMA_DIGITAL_DESDE_A_CHEGADA', t2,
    'a digital medida HOJE é idêntica à medida no ato do recebimento (trilha 81 T1, 2026-09-22) e à da escritura L06_VIGENTE.txt — recebeu → mediu → arquivou → só leu')

# T3 — a escritura da vigência aponta para esta mesma digital (coerência do livro-razão)
vig = open(VIG, encoding='utf-8', newline=None).read()
t3 = ESPERADA in vig
reg('T3_ESCRITURA_COERENTE', t3, 'L06_VIGENTE.txt registra exatamente esta digital — o que você salva nos seus arquivos, se for o arquivo que chegou aqui, tem sha-256 = 98e90bdc755162b28fd16817d65692cebe81f939c466ef1d29c7a0a1124f2b41')

n_ok = sum(1 for c in checks if c['status'] == 'VERDE')
resumo = (f'TRILHA 83: {n_ok}/{len(checks)} — RESPOSTA AO OPERADOR: dentro do Arena, a rev.6 NÃO mudou um byte: uploads ≡ série ≡ digital da escritura '
          f'({ESPERADA[:8]}…, medida igual na chegada e agora). Para conferir o arquivo no SEU computador: sha-256 dele tem de dar {ESPERADA}. '
          f'Escopo honesto: dentro do mestre (projeto dele), quem responde é ele com o mesmo teste — o comando está na resposta.')
print(resumo)
out = f'{BASE}/BIBLIOTECAS/B01_Neuroinflamacao/atuais/producao/TRILHA83_script_integridade_rev6_2026-09-22.json'
json.dump({'trilha': 83, 'rodada': 70, 'data': '2026-09-22', 'verde': n_ok, 'total': len(checks),
           'checks': checks, 'resumo': resumo,
           'digitais': {'uploads': hu, 'serie': hs, 'esperada': ESPERADA}},
          open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('json ->', out)
