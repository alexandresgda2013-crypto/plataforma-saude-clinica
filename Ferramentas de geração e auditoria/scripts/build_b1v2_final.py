#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
DST=Path("/home/user/pipeline_auditoria_conteudo/BIBLIOTECAS/B01_Neuroinflamacao/Biblioteca_B1_NEUROINFLAMACAO_CANONICA.md")
t=DST.read_text(encoding="utf-8")

# 1) Cabeçalho: marcar v2
t=t.replace("# B1 — NEUROINFLAMAÇÃO\n## Biblioteca de Conhecimento Canônica — Mecanismo Fisiopatológico",
"# B1 — NEUROINFLAMAÇÃO EM ANSIEDADE E DEPRESSÃO\n## Biblioteca de Conhecimento Canônica v2 — Mecanismo Fisiopatológico",1)
t=t.replace("**artefato_rotulo:** CANÔNICA",
"**artefato_rotulo:** CANÔNICA v2 (ansiedade + depressão; v1 depressão-congelada em /OFICINA_geracao/_historico/versoes)",1)
t=t.replace("**Corte de literatura:** 2026-09-03 · **Rodada de auditoria:** Rodada 3 consolidada + correção pós-auditoria externa e resgate de literatura (2026-09-04):",
"**Corte de literatura:** 2026-09-04 · **Rodada de auditoria:** Rodada 4 — expansão v2 (trilho de ansiedade + imunometabolismo/necroptose/Cx43-AQP4/ansiedade) sobre a Rodada 3 consolidada;",1)

# 2) Cenário 12.4 (ansiedade/TEPT) ANTES da nota de fechamento do BLOCO_12
fecho='> **Nota de fechamento:** estes três cenários são **arquétipos didáticos**'
novo_124='''### 12.4 — TEPT/ansiedade traumática com o subtipo neuroimune suprimido

- **Perfil clínico:** sintomas de TEPT/ansiedade crônica pós-trauma (hipervigilância, evitação, reatividade de sobressalto) que se acompanham de queixas somáticas atenuadas e **falta de elevação** dos marcadores inflamatórios periféricos, ou até tendência ao esgotamento neuroendócrino (conecta com o hipocortisolismo da B2).
- **Substrato mecanístico:** não é "ausência de neuroinflamação", mas um **estado neuroimune distinto** — dado combinado de PET de TSPO e tecido pós-morte aponta supressão neuroimune em subgrupo de TEPT (Bhatt et al., 2020); coexiste reatividade de circuitos de medo/extinção (amígdala, extinção prejudicada; minociclina atenua retenção de medo em humano — Xia 2024).
- **Biomarcadores esperados:** marcadores periféricos podem estar **normais ou baixos** (não esperar PCR/IL-6 elevados); TSPO-PET reduzido quando disponível (atenção ao confundidor genótipo rs6971); possível achatamento da reatividade cortisol/ansiedade.
- **Raciocínio de estratificação:** é um **contra-arquétipo** dos três anteriores — alerta contra tratar "inflamação alta" como universal. No BLOCO_11.4 este perfil tende a **Compatibilidade indeterminada/baixa** pelo Critério A, embora o Critério B/C (hipervigilância, trauma) esteja presente; sinaliza a necessidade de integrar B2 (HPA/TEPT) e B12 (trauma).
- **Nível de evidência do perfil:** PET+pós-morte humano para a supressão neuroimune (força **média**, amostra pequena/heterogênea); ensaio RCT humano para minociclina/memória de medo (força **média**).

---

*PTSD_supressao_2020[EC] | Minociclina_medo_2024[EC] | PTSD_marc_2015[MA] | TSPO_estresse_2022[OB]*

'''
assert fecho in t
t=t.replace(fecho, novo_124+fecho,1)

# 3) Nota de confundidores — inserir logo no fim do BLOCO_05 (antes do BLOCO_06)
conf='''### 5.8 — Controle de confundidores na leitura dos biomarcadores inflamatórios (anti-falso-positivo)

Painel único não decide; variáveis de ruído precisam ser controladas para não rotular como neuroinflamação o que é metabólico, circadiano ou analítico:

| Marcador / exame | Confundidor principal | Cuidado de interpretação |
|---|---|---|
| `exame_pcr_us` | IMC/adiposidade visceral (gordura secreta IL-6/TNF), infecção recente, tabaco, exercício | exigir ajuste por IMC; separar inflamação metabólica da do humor (p. ex. razão sTNFR2/adiponectina) |
| `exame_il6` | pulsatilidade e meia-vida curta; horário da coleta; privação de sono (B10) | padronizar coleta matinal; repetir; afastar privação de sono |
| `exame_tnfalpha` | adiposidade, inflamação metabólica | ajuste por IMC e comorbidades |
| `exame_il1beta` | instabilidade plasmática; difícil detecção em baixo-grau | não usar isolado para excluir mecanismo |
| TSPO-PET (central) | **genótipo rs6971** (baixa afinidade = falso-negativo) | exigir genotipagem antes de interpretar ausência de sinal |
| `exame_razao_kyn_trp` | triptofano dietético recente, insuficiência renal | controle de jejum/função renal |
| `exame_snps_inflamatorios` | marca risco estático, não estado atual | não usar como marcador de estado inflamatório ativo |
| Polifenóis/fitoterápicos como "evidência" | viés de publicação positivo, superdosagem in vitro, biodisponibilidade no SNC incerta | só valorar ensaio humano com desfecho mecanístico robusto (TSPO-PET, KYN/TRP) |

---

*Mediadores_2024[OB]*

'''
ancora6='## BLOCO_06 — TRADUÇÃO CLÍNICA: DO MECANISMO AO SINTOMA'
assert ancora6 in t
t=t.replace(ancora6, conf+'\n'+ancora6,1)

DST.write_text(t,encoding="utf-8")
print("ok. linhas:",t.count(chr(10))+1,"| H3:",t.count("### "))
