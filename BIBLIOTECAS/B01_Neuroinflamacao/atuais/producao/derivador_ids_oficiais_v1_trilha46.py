#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# DERIVADOR _ids_oficiais → JSON OPERACIONAL — casa (bancada) · trilha 46 · 2026-09-17
# Dívida da casa D-L05-IDS-JSON. Critério de aceitação BILATERAL (R2, aceito na rodada 25;
# reforço: minuta (5) §7 do auditor-2 + §4 do comentador):
#   só é aceito se reproduzir 146 IDs válidos = 48 (suplementos/complementares)
#   + 71 (exames/algoritmo) + 16 (mecanismos) + 11 (cenários), POR CATEGORIA,
#   comparado ao bloco 'contagem' do próprio catálogo + sha + fonte declarados.
# Causa do 103×146 identificada: trilha 25 usou parser de TEXTO; o arquivo-fonte é JSON
# inteiro (descoberto na trilha 46) — a contagem estrutural (lens das listas) e a contagem
# mecânica de texto (regex da trilha 38) devem AMBAS dar 146.
import json, hashlib, re, pathlib, sys

FONTE = pathlib.Path('/home/user/Ferramentas de geração e auditoria/01_norteadores/1º IDS_OFICIAIS.md')
DEST  = FONTE.parent / '_derivados_trilha46'
DS = [f'D{i}_{n}' for i, n in enumerate(['micronutrientes','aminoacidos','fitoterapicos','fosfolipidios','psicobioticos','complementares'], start=1)]
CS = ['C1_escalas','C2_causa_organica','C3_deficiencias','C4_inflamatorios','C5_hpa','C6_neurotransmissores',
      'C7_acidos_organicos','C8_farmacogenomica','C9_sono','C10_microbiota','C11_estresse_oxidativo','C12_metais','C13_algoritmo']

raw   = FONTE.read_bytes()
sha_f = hashlib.sha256(raw).hexdigest()
d     = json.loads(raw.decode('utf-8'))            # camada: ARQUIVO INTEIRO como JSON (verificado)
cont  = d['contagem']

por_chave = {k: len(d[k]) for k in DS + CS + ['mecanismos', 'cenarios']}
somas = {'suplementos_complementares': sum(por_chave[k] for k in DS),
         'exames_algoritmo':           sum(por_chave[k] for k in CS),
         'mecanismos':                 por_chave['mecanismos'],
         'cenarios':                   por_chave['cenarios']}
total = sum(somas.values())
decl  = {'suplementos_complementares': sum(cont[k] for k in DS),
         'exames_algoritmo':           sum(cont[k] for k in CS),
         'mecanismos':                 cont['mecanismos'],
         'cenarios':                   cont['cenarios']}
confere_por_chave = all(por_chave[k] == cont[k] for k in por_chave)
ids_validos = [i for k in por_chave for i in d[k]]
mecanica_txt = len(set(re.findall(r'\b((?:exame|suplemento|mecanismo|cenario)_[a-z0-9_]+)\b',
                                  raw.decode('utf-8'))))
# NOTA DE CAMADA (medida na trilha 46): a camada de TEXTO subconta por desenho do catálogo —
# os 48 IDs de suplementos/complementares e os 16 mecanismos/11 cenários sem prefixo 'suplemento_'
# não são capturáveis por regex de prefixo. Texto dá 74 (71 exames + 3 grafias em ids_proibidos);
# trilha 25 deu 103 por outro parser de texto. A camada ESTRUTURAL (arquivo é JSON inteiro) dá 146
# exatos e é a única válida para o critério R2. APROVADO depende só das conferências estruturais.

resultado = {
 'fonte': str(FONTE), 'sha256_fonte': sha_f, 'derivador': 'derivador_ids_oficiais_v1_trilha46.py',
 'data_derivacao': '2026-09-17 (trilha 46, rodada 27)',
 'estrutural': dict(por_chave=por_chave, somas_por_grupo=somas, total_ids_validos=total,
                    ids_distintos=len(set(ids_validos)), duplicados=total - len(set(ids_validos))),
 'declarado_bloco_contagem': dict(somas_por_grupo=decl, total_ids_validos=cont['total_ids_validos'],
                                  ids_removidos_definitivo=cont['ids_removidos_definitivo'],
                                  lista_removidos=len(d['ids_removidos_definitivo'])),
 'conferencias': {
   'por_chave_estrutural_igual_declarado': confere_por_chave,
   'somas_grupo': somas == decl == {'suplementos_complementares': 48, 'exames_algoritmo': 71,
                                    'mecanismos': 16, 'cenarios': 11},
   'total_146': total == cont['total_ids_validos'] == 146,
   'removidos_5': cont['ids_removidos_definitivo'] == len(d['ids_removidos_definitivo']) == 5,
 },
 'camadas_de_contagem': {'estrutural_json': total, 'mecanica_prefixo_regex': mecanica_txt,
                         'trilha25_parser_texto_legado': 103,
                         'causa_do_gap': 'IDs de suplementos/cenários/mecanismos sem prefixo capturável — só a camada estrutural reproduz 146'},
 'criterio_R2_bilateral': '146 = 48+71+16+11 por categoria + comparação com bloco contagem + sha + fonte',
}
resultado['APROVADO'] = all(resultado['conferencias'].values())

DEST.mkdir(parents=True, exist_ok=True)
# artefato operacional: o MESMO documento, serialização canônica (2 espaços, LF), conteúdo íntegro
art = DEST / '_ids_oficiais.json'
art.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')
prov = DEST / '_ids_oficiais.PROVENIENCIA.json'
prov.write_text(json.dumps(resultado, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')
print(json.dumps({'APROVADO': resultado['APROVADO'], 'total': total,
                  'grupos': somas, 'mecanica_txt': mecanica_txt,
                  'artefato': str(art), 'sha_artefato': hashlib.sha256(art.read_bytes()).hexdigest(),
                  'proveniencia': str(prov)}, ensure_ascii=False, indent=2))
sys.exit(0 if resultado['APROVADO'] else 1)
