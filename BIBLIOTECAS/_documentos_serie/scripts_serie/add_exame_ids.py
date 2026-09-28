#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Adiciona referências de exames por ID oficial (P19/P20) ao BLOCO_05 de cada biblioteca."""
import glob, re, os
from pathlib import Path

# exames oficiais pertinentes a cada mecanismo (papel biológico em 1-2 frases, sem cortes/protocolos)
EX = {
 'B1': {
  'marcadores_inflamacao': ['exame_pcr_us','exame_il6','exame_il1beta','exame_tnfalpha','exame_razao_kyn_trp'],
  'marcadores_geral': ['exame_vhs','exame_fibrinogenio','exame_snps_inflamatorios','exame_cortisol_matinal'],
  'nota': 'ID oficial: exame_pcr_us, exame_il6, exame_il1beta, exame_tnfalpha, exame_razao_kyn_trp, exame_vhs, exame_fibrinogenio, exame_snps_inflamatorios. Elementos ainda não catalogados no módulo C-LAB (ex.: marcadores microgliais periféricos) são citados como papel biológico; cortes e protocolos residem no módulo laboratorial, não nesta biblioteca.'
 },
 'B2': {
  'marcadores_hpa': ['exame_cortisol_matinal','exame_cortisol_salivar_4pts','exame_cortisol_urinario_24h','exame_dexametasona','exame_acth','exame_dhea_s','exame_dutch_test'],
  'nota': 'ID oficial: exame_cortisol_matinal, exame_cortisol_salivar_4pts, exame_cortisol_urinario_24h, exame_dexametasona, exame_acth, exame_dhea_s, exame_dutch_test. Valores de corte e protocolos de coleta ficam no módulo C-LAB; a biblioteca descreve apenas o papel no eixo HPA (P20).'
 },
 'B3': {
  'marcadores_plasticidade': ['exame_bdnf_val66met'],
  'nota': 'ID oficial: exame_bdnf_val66met (variante). BDNF sérico e outros marcadores de plasticidade sináptica não têm corte diagnóstico validado; referidos como papel biológico. Elementos não catalogados no C-LAB são citados em prosa sem marcador de evidência (P20).'
 },
 'B4': {
  'marcadores_monoaminas': ['exame_serotonina_plaquetaria','exame_aminoacidos_plasmaticos','exame_slc6a4','exame_comt','exame_mao_a','exame_cyp2d6_2c19'],
  'nota': 'ID oficial: exame_serotonina_plaquetaria, exame_aminoacidos_plasmaticos, exame_slc6a4, exame_comt, exame_mao_a, exame_cyp2d6_2c19. Polimorfismos não são rastreio de rotina; a química sináptica permanece no módulo mecanístico (P20).'
 },
 'B5': {
  'marcadores_gaba_glu': ['exame_aminoacidos_plasmaticos'],
  'nota': 'ID oficial: exame_aminoacidos_plasmaticos (glutamato/GABA). Não há exame sanguíneo de receptor NMDA/GABA-A validado para diagnóstico; quando um biomarcador não tem ID catalogado no C-LAB, informa-se em prosa sem marcador de evidência (P20).'
 },
 'B6': {
  'marcadores_redox': ['exame_glutationa_gsh','exame_gssg','exame_8_ohdg','exame_capacidade_antioxidante_total'],
  'nota': 'ID oficial: exame_glutationa_gsh, exame_gssg, exame_8_ohdg, exame_capacidade_antioxidante_total (categoria C11_estresse_oxidativo, P19). Marcadores são de status clínico/redox geral, não diagnóstico de humor; cortes no C-LAB (P20).'
 },
 'B7': {
  'marcadores_microbiota': ['exame_zonulina','exame_lps_serico','exame_calprotectina','exame_16s_rrna'],
  'nota': 'ID oficial: exame_zonulina, exame_lps_serico, exame_calprotectina, exame_16s_rrna. Não há painel de microbiota validado para diagnóstico psiquiátrico; a biblioteca descreve o papel ecológico. Elementos sem ID catalogado vão em prosa (P20).'
 },
 'B8': {
  'marcadores_nutricao': ['exame_vitd','exame_b12','exame_folato','exame_homocisteina','exame_magnesio_eritrocitario','exame_zinco','exame_b6_p5p','exame_selenio','exame_omega3_index','exame_ferritina_ferro','exame_acido_metilmalonico','exame_mthfr','exame_hemograma_completo','exame_tireoide_funcional'],
  'nota': 'ID oficial: exame_vitd, exame_b12, exame_folato, exame_homocisteina, exame_magnesio_eritrocitario, exame_zinco, exame_b6_p5p, exame_selenio, exame_omega3_index, exame_ferritina_ferro, exame_acido_metilmalonico, exame_mthfr, exame_hemograma_completo, exame_tireoide_funcional. Os exames são de status clínico-nutricional (dosar só por suspeita); não há painel validado para diagnóstico de humor. Corte/faixa e protocolo ficam no C-LAB (P20).'
 },
}

BLOCO_EX = """

### {secao} — Exames referenciados por ID oficial (P19/P20)
{lista}
> {nota}
"""

for Bn in ['B1','B2','B3','B4','B5','B6','B7','B8']:
    folders = glob.glob(f'/home/user/BIBLIOTECAS/{Bn}_*')
    if not folders: continue
    folder = Path(folders[0])
    cans = [p for p in folder.glob('*.md') if 'CANONICA' in p.name.upper()]
    if not cans: continue
    can = cans[0]
    t = can.read_text(encoding='utf-8')
    if 'Exames referenciados por ID oficial' in t:
        print(Bn,'já tem bloco de exames'); continue
    cfg = EX[Bn]
    ids = cfg['marcadores_'+('marcadores_'+list([k for k in cfg if k.startswith('marcadores')])[0].replace('marcadores_','')) if False else list([k for k in cfg if k.startswith('marcadores')])[0]]
    linhas = '\n'.join(f'- **`{e}`**' for e in ids)
    secao = '5.x Biomarcadores (exames oficiais)'
    # insere antes de BLOCO_06 (final do BLOCO_05)
    bloco = BLOCO_EX.format(secao=secao, lista=linhas, nota=cfg['nota'])
    marker = '## BLOCO_06'
    idx = t.find(marker)
    if idx == -1:
        t = t.rstrip() + bloco
    else:
        t = t[:idx] + bloco + '\n' + t[idx:]
    can.write_text(t, encoding='utf-8')
    print(Bn, 'bloco de exames por ID adicionado; ids:', len(ids))
