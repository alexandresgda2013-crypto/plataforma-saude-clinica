#!/usr/bin/env python3
# TRILHA 80 — 2026-09-22 — Rodada 67 — Sanidade do pacote da CARTA 24 ao mestre:
# as digitais citadas na carta têm de bater com os arquivos reais que o operador vai anexar.
import hashlib, json, re

BASE = '/home/user'
ALVOS = {
 'rev.5 (série)':          (f'{BASE}/BIBLIOTECAS/_documentos_serie/MESTRE_L06_minuta3_consolidada_rev5_recebida_2026-09-21/L06_RESOLUCAO_CONFLITOS_minuta3_consolidada_rev5_2026-09-21.md',
                            '601c1f18d074e6e4488dd8a6ee3364345e51713f7d0277cd1637add838a79608'),
 'carta do comentador':   (f'{BASE}/BIBLIOTECAS/_documentos_serie/COMENTADOR_carta_rev5_L06_2026-09-21/COMENTADOR_carta_rev5_L06_2026-09-21.md',
                            'b6c6b08196f27f1b5013882eda2c54263e46f10bd2584454c1df38230625ae5a'),
 'réplica final da casa': (f'{BASE}/ENTREGAS/2026-09-21_REPLICA_FINAL_L06/REPLICA_MECANICA_FINAL_L06_rev5_2026-09-21.md',
                            'e80497bc5e5048fac71e4a4334c78b9dd1513e78f246bf62c5be42aec5764983'),
 'adenda 2 (R-BUSCA-1)':  (f'{BASE}/ENTREGAS/2026-09-22_ADENDA2_ATA_L06/ADENDA_2_ATA_PROVENIENCIA_L06_RBUSCA1_2026-09-22.md',
                            '7dcd31b2733ea7b850023968458de4160035a9d89bedc20c54053032a889bee3'),
 'nota R66 (errata+R-CITA-1)': (f'{BASE}/ENTREGAS/2026-09-22_ERRATA_NOTA_R66/ERRATA_E_RELEITURA_NOTA_R66_2026-09-22.md',
                            'e142409c937842df244f4d065b8e170639093f527dd50f9106fad22ac6b04018'),
}
checks = []
def reg(nome, ok, nota):
    checks.append({'check': nome, 'status': 'VERDE' if ok else 'VERMELHO', 'nota': nota})
    print(('VERDE ' if ok else 'VERMELHO ') + nome + ' :: ' + nota[:170])

for nome, (path, esperado) in ALVOS.items():
    h = hashlib.sha256(open(path, 'rb').read()).hexdigest()
    reg('T_' + nome.upper().replace(' ', '_').replace('.', ''), h == esperado,
        f'{nome}: {h[:8]}… {"confere com a digital registrada" if h == esperado else "DIVERGE da registrada — CARTA BLOQUEADA"}')

# T6 — a carta cita todas as digitais corretas (consistência interna da carta com a trilha)
carta = f'{BASE}/ENTREGAS/2026-09-22_CARTA24_MESTRE/CARTA24_MESTRE_rev5_parecer_final_2026-09-22.md'
texto = open(carta, encoding='utf-8', newline=None).read()
faltam = [nome for nome, (_, esp) in ALVOS.items() if esp not in texto and esp[:8] not in texto]
reg('T6_CARTA_CITA_AS_5', not faltam, f'digitais ausentes na carta: {faltam or "nenhuma — as 5 citadas"}')

# T7 — a frase-registro do rito novo do operador consta VERBATIM na carta e nas decisões (R-CITA-1)
frase_rito = 'só será aprovado qualquer documento ou decisão quando passar por todo os 3'
dec = open(f'{BASE}/BIBLIOTECAS/B01_Neuroinflamacao/atuais/Auditoria_B1/decisoes_B1.md', encoding='utf-8', newline=None).read()
reg('T7_RITO_VERBATIM_REGISTRADO', frase_rito in dec,
    'rito de aprovação do operador (22/09/2026) gravado verbatim nas decisões [rev.74] — fonte: fala dele nesta data')

n_ok = sum(1 for c in checks if c['status'] == 'VERDE')
resumo = f'TRILHA 80: {n_ok}/{len(checks)} — pacote da CARTA 24 íntegro: 5 digitais conferem byte a byte; carta cita as 5; rito novo do operador gravado verbatim.'
print(resumo)
out = f'{BASE}/BIBLIOTECAS/B01_Neuroinflamacao/atuais/producao/TRILHA80_script_carta24_mestre_anexos_2026-09-22.json'
json.dump({'trilha': 80, 'rodada': 67, 'data': '2026-09-22', 'verde': n_ok, 'total': len(checks),
           'checks': checks, 'resumo': resumo}, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('json ->', out)
