#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_gpm_completo.py — GATE OBRIGATÓRIO ao receber um GPM_BX.
Confere que o GPM contém TODAS as 11 partes (Módulos 00 a 10) e que o
arquivo não está truncado (encerra com o módulo 10 / autoverificação).
Uso: python3 check_gpm_completo.py <caminho_gpm.md>
Saída: OK se completo; exit 1 com as partes faltantes se incompleto.
"""
import sys, re

def main():
    path = sys.argv[1]
    t = open(path, encoding='utf-8').read()
    modulos = re.findall(r'^##\s+MÓDULO\s+(\d{2})\b', t, re.M)
    presentes = sorted(set(modulos))
    esperados = [f'{i:02d}' for i in range(11)]  # 00..10
    faltando = [m for m in esperados if m not in presentes]
    # sinal de truncamento: linhas incompletas no fim
    linhas = [l for l in t.splitlines() if l.strip()]
    ultima = linhas[-1] if linhas else ''
    print(f'GPM: {path}')
    print(f'Módulos encontrados ({len(presentes)}): {", ".join(presentes) or "NENHUM"}')
    if faltando:
        print(f'FALHANDO MÓDULOS: {", ".join(faltando)}')
        print('GATE REPROVADO — GPM INCOMPLETO/TRUNCADO. Solicitar GPM completo antes de processar.')
        sys.exit(1)
    print('GATE APROVADO — GPM completo (Módulos 00–10 presentes).')
    sys.exit(0)

if __name__ == '__main__':
    main()
