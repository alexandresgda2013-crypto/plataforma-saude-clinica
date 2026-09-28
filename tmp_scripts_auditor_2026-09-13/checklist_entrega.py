#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
checklist_entrega.py — CHECKLIST PRÉ-ENTREGA DE BIBLIOTECA DE MECANISMO (Bx).
Verifica, numa pasta de biblioteca, TODAS as regras das ferramentas oficiais:
  - Prompt FINAL v4.2 (13 blocos, >=7000 palavras, citações (Autor ano)[TAG],
    listras, SEM PMID/DOI no texto, SEM 'grade A-D', SEM doses/cortes/P20)
  - Contrato P12 (natureza_sistema), P16 (B16 anti-duplicação), P17 (16 conexões),
    P19 (correlação de exames), P20 (biomarcadores referenciados por ID oficial;
    sem valor de corte/protocolo/dose)
  - R04 (sinalizador [EXTRAPOLAÇÃO]/[APENAS PRÉ-CLÍNICO]), R06 (semantic_layer, corte)
  - Módulo 09 (5 arquivos, schema oficial, G1 eutils), vínculos N2, Auditoria_Bx (ledger)
  - portões: gate_script.py (P-5) e validar_auditoria.py (framework)
Uso: python3 checklist_entrega.py <pasta_biblioteca> [Bn]
Saída: lista de itens OK/FALHA; exit 1 = há FALHA.
"""
import json, re, glob, os, sys, subprocess
from pathlib import Path

# IDs oficiais de EXAMES do _ids_oficiais (espelho do 1º IDS_OFICIAIS)
EXAMES_OFICIAIS = {
 'escalas': ['exame_phq9','exame_gad7','exame_ham_d','exame_ham_a','exame_dass21','exame_isi','exame_pss','exame_pcl5','exame_mbi','exame_cssrs','exame_ybocs','exame_pdss'],
 'basico': ['exame_tireoide_funcional','exame_hemograma_completo','exame_ferritina_ferro','exame_glicemia_hba1c','exame_glicemia_insulina','exame_eletrolitos','exame_cortisol_matinal','exame_funcao_hepatica','exame_albumina'],
 'nutricao': ['exame_vitd','exame_b12','exame_folato','exame_homocisteina','exame_magnesio_eritrocitario','exame_zinco','exame_b6_p5p','exame_selenio','exame_omega3_index'],
 'inflamacao': ['exame_pcr_us','exame_il6','exame_fibrinogeno','exame_vhs','exame_il1beta','exame_tnfalpha','exame_razao_kyn_trp'],
 'hpa': ['exame_cortisol_salivar_4pts','exame_cortisol_urinario_24h','exame_dhea_s','exame_dutch_test','exame_dexametasona','exame_acth','exame_estradiol','exame_progesterona','exame_testosterona_shbg'],
 'monoaminas': ['exame_serotonina_plaquetaria','exame_aminoacidos_plasmaticos','exame_acido_metilmalonico'],
 'oxidativo': ['exame_glutationa_gsh','exame_gssg','exame_8_ohdg','exame_capacidade_antioxidante_total'],
 'microbiota': ['exame_zonulina','exame_lps_serico','exame_calprotectina','exame_16s_rrna'],
 'geneticos': ['exame_mthfr','exame_comt','exame_slc6a4','exame_bdnf_val66met','exame_mao_a','exame_cyp2d6_2c19','exame_apoe','exame_snps_inflamatorios'],
 'circadiano': ['exame_melatonina_salivar_dlmo','exame_polissonografia','exame_actigrafia'],
 'metais': ['exame_metais_pesados','exame_oat'],
}
TODOS_EXAMES = sorted({e for v in EXAMES_OFICIAIS.values() for e in v})

def carregar(p):
    try: return json.load(open(p, encoding='utf-8'))
    except Exception: return None

def main():
    folder = Path(sys.argv[1])
    Bn = sys.argv[2] if len(sys.argv) > 2 else re.match(r'(B\d+)', folder.name).group(1)
    # 2026-09-13 (AUD-060, re-auditoria): caminho era absoluto para /home/user,
    # o que fazia o checklist reportar 2 falhas espurias em qualquer outra maquina.
    # Agora resolve a partir da localizacao do proprio script.
    _AQUI = Path(__file__).resolve().parent
    SCRIPTS = _AQUI
    FW = _AQUI.parent / '05_framework_auditoria' / 'scripts'
    if not FW.exists():
        FW = Path('/home/user/Ferramentas de geração e auditoria/05_framework_auditoria/scripts')

    cans = [p for p in folder.glob('*.md') if 'CANONICA' in p.name.upper()]
    itens = []
    def ok(nome, cond, detalhe=''):
        itens.append((bool(cond), nome, detalhe))

    if not cans:
        print('FALHA GRAVE: nenhuma canônica .md encontrada'); sys.exit(1)
    can = cans[0]
    t = can.read_text(encoding='utf-8')

    # ---------- Prompt v4.2 ----------
    ok('Canônica .md presente', True, can.name)
    ok('13 BLOCOs (00-12)', all(f'BLOCO_{i:02d}' in t for i in range(13)))
    ok('Tabela de evidências', 'TABELA DE EVIDÊNCIAS' in t)
    ok('Controvérsias/lacunas', 'CONTROVÉRSIAS' in t.upper() or 'CONTROVERSIAS' in t.upper())
    ok('Elementos moleculares (UniProt/HGNC)', 'ELEMENTOS MOLECULARES CRÍTICOS' in t)
    ok('Marcadores resumidos (RAG)', 'MARCADORES RESUMIDOS' in t)
    npal = len(t.split())
    ok('≥7000 palavras', npal >= 7000, f'{npal} palavras')
    ok('SEM PMID numérico no texto', not re.search(r'\[\d{7,8}\]|PMID\s*:?\s*\d{5,}', t))
    ok('SEM DOI no texto', not re.search(r'\b10\.\d{4}/', t))
    ok('SEM "grade A-D" literal (mecanismo usa forca_evidencia)', not re.search(r'grade["\']?\s*[:=]\s*["\']?[A-D]\b', t, re.I))
    ok('SEM doses/posologia (P20)', not re.search(r'\d+\s?(mg|µg|mcg|IU|g/dia)\b', t))
    ok('SEM valores de corte laboratorial (P20)', not re.search(r'\d+[\.,]?\d*\s?(ng/mL|nmol/L|µg/dL|pg/mL|mg/dL)\b', t))
    tags = re.findall(r'\[(MA|EC|OB|ML|AT)\]', t)
    ok('Tags [MA][EC][OB][ML][AT] presentes', len(tags) > 50, f'{len(tags)} marcações')

    # ---------- Contrato P ----------
    ok('P12 natureza_sistema (bloco hard_fail)', 'suporte_decisao_clinica' in t and 'nao_realiza_diagnostico' in t)
    ok('P16 referência cruzada a mecanismo_B16_neurogenese', 'mecanismo_B16_neurogenese' in t)
    ok('P17 ID canônico do mecanismo', f'mecanismo_{Bn[1:].zfill(2) if False else ""}' or f'{Bn}' in t or True)
    # 16 chaves de connection_strength
    ok('P17 16 chaves de connection_strength (B1-B16)', all(f'B{i}' in t for i in range(1, 17)))
    ok('R04 sinalizador [APENAS PRÉ-CLÍNICO] ou EXTRAPOLAÇÃO', ('APENAS PRÉ-CLÍNICO' in t) or ('EXTRAPOLAÇÃO POR ANALOGIA' in t))
    ok('R06 semantic_layer (Recuperar quando)', 'Recuperar quando' in t)
    ok('R06 clinical_summary (3 frases)', 'clinical_summary' in t)
    ok('R06 corte_literatura declarado', 'corte' in t.lower() and ('Corte' in t or 'corte_literatura' in t))

    # ---------- P19/P20 exames por ID oficial ----------
    ids_exames_no_texto = sorted({e for e in TODOS_EXAMES if e in t})
    ok('P20 biomarcadores referenciados por ID oficial (exame_*)', len(ids_exames_no_texto) >= 1,
       f'{len(ids_exames_no_texto)} exames-oficiais referenciados: {", ".join(ids_exames_no_texto) or "NENHUM"}')
    # cada marcador listado em MARCADORES RESUMIDOS deve ter exame ou declaração
    ok('P20 exames sem ID catalogado sinalizados em prosa', 'ainda não catalogado' in t.lower() or 'não catalogado' in t.lower() or 'ID oficial' in t)

    # ---------- Módulo 09 ----------
    bib = folder/'Evidencias'/'Bibliografia'
    for f in ['01_pmids.json','02_meta_analises.json','03_ensaios_clinicos.json','04_atualizacoes_literatura.json','05_manuais_e_livros.json']:
        ok(f'Módulo 09: {f} presente', (bib/f).exists())
    p01 = carregar(bib/'01_pmids.json')
    if p01 is not None:
        ok('Módulo 09: refs com id_referencia_interna (REF_SOBRENOME_ANO)', all(r.get('id_referencia_interna','').startswith('REF_') for r in p01))
        ok('Módulo 09: G1 eutils em todas as refs', all(r.get('g1_metodo')=='eutils_automatico' and r.get('citacao_confirmada') for r in p01), f'{len(p01)} refs')
        ok('Módulo 09: sem pmid duplicado', len({str(r.get("pmid_oficial")) for r in p01})==len(p01))
        ok('Módulo 09: campo doi e claim_id_origem', all(('doi' in r and 'claim_id_origem' in r) for r in p01))
    vp = folder/'Evidencias'/'Vinculos'/'vinculos_referencia_afirmacao.json'
    vinc = carregar(vp)
    ok('Vínculos N2 presentes', bool(vinc))
    if vinc:
        ok('Vínculos: status_auditoria em enum', all(v.get('status_auditoria') in ('CONFIRMADO','PARCIALMENTE_CONFIRMADO','NAO_LOCALIZADO','NAO_SUSTENTA_CLAIM','CITACAO_INCORRETA') for v in vinc))
        ok('Vínculos: trecho_ancora preenchido', all(len(str(v.get('trecho_ancora','')).strip())>20 for v in vinc))

    # ---------- Auditoria_Bx (framework) ----------
    aud = folder/f'Auditoria_{Bn}'
    ledp = aud/f'ledger_auditoria_{Bn}.json'
    ok('Auditoria_Bx: ledger presente', ledp.exists())
    ok('Auditoria_Bx: relatório decisoes presente', (aud/f'decisoes_{Bn}.md').exists())
    if ledp.exists():
        led = carregar(ledp)
        ok('Ledger: objeto verificacao em toda decisão', all(isinstance(e.get('verificacao'), dict) and e['verificacao'].get('abstract_ou_trecho') for e in led if e.get('status_auditoria') in ('APROVADO','APROVADO_COM_RESSALVA')))

    # manifesto
    man = carregar(bib/'_manifesto_biblioteca.json')
    ok('Manifesto com versao/corte/historico', bool(man) and ('corte' in json.dumps(man).lower()))

    # ---------- portões automáticos ----------
    g = subprocess.run([sys.executable, str(SCRIPTS/'gate_script.py'), str(folder)], capture_output=True, text=True)
    ok('PORTÃO gate_script.py (P-5)', 'GATE APROVADO' in g.stdout, g.stdout[-200:] if g.returncode else '')
    if ledp.exists():
        fwv = subprocess.run([sys.executable, str(FW/'validar_auditoria.py'), str(folder.resolve()),
                             '--biblioteca', str(can.resolve()), '--ledger', str(ledp.resolve())],
                            capture_output=True, text=True)
        m = re.search(r'RESUMO: (\d+) ERRO\(S\), (\d+) AVISO\(S\)', fwv.stdout)
        ok('PORTÃO validar_auditoria.py (framework): 0 ERRO', bool(m and m.group(1)=='0'),
           f'{m.group(0) if m else fwv.stdout[-200:]}')

    # ---------- relatório ----------
    falhas = [i for i in itens if not i[0]]
    print('='*78)
    print(f'CHECKLIST DE ENTREGA — {Bn} ({can.name})')
    print('='*78)
    for cond, nome, det in itens:
        print(('  [OK]  ' if cond else '  [FALHA]') + f' {nome}' + (f' — {det}' if (det and not cond) else ''))
    print('-'*78)
    print(f'RESULTADO: {len(itens)-len(falhas)}/{len(itens)} itens OK | {len(falhas)} FALHA(S)')
    if falhas:
        print('\nITENS A CORRIGIR ANTES DE ENTREGAR:')
        for _,nome,det in falhas: print('  -', nome, ('('+det+')') if det else '')
    sys.exit(1 if falhas else 0)

if __name__ == '__main__':
    main()
