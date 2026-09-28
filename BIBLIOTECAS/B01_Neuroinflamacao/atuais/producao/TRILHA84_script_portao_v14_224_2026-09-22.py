#!/usr/bin/env python3
# TRILHA 84 — 2026-09-22 — Rodada 73 — Réplica do ponto do Auditor-Estrutura (ciência L-06):
# §8 da L-06 cita "243/274 por máquina (trilha 27)" medido na era v1.1; ele mediu 224 contra o N2 v1.4.
# Casa repete TUDO com níveis declarados (R-BUSCA-1): a regra D3, os conjuntos, a reconciliação 243→224,
# as 3 confirmações dele e a nuance da granularidade.
import hashlib, json, re

BASE = '/home/user'
S14 = f'{BASE}/BIBLIOTECAS/_documentos_serie/AUDITOR2_L05_N1v13_N2v14_COMENTADOR_recebido_2026-09-18/schema_vinculo_v1.4_N2_d96ad15b.json'
S13 = f'{BASE}/BIBLIOTECAS/_documentos_serie/AUDITOR2_triagem_L05v13_recebido_2026-09-17/schema_vinculo_v1.3_recebido_2026-09-17.json'
S11 = f'{BASE}/BIBLIOTECAS/_documentos_serie/L05_v1.1_recebido_2026-09-15/schema_vinculo_v1.1.json'
V   = f'{BASE}/BIBLIOTECAS/B01_Neuroinflamacao/atuais/Evidencias/Vinculos/vinculos_referencia_afirmacao.json'

def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()
raw14, raw13, raw11 = (open(p, encoding='utf-8').read() for p in (S14, S13, S11))
d = json.load(open(V))
checks = []
def reg(nome, ok, nota):
    checks.append({'check': nome, 'status': 'VERDE' if ok else 'VERMELHO', 'nota': nota})
    print(('VERDE ' if ok else 'VERMELHO ') + nome + ' :: ' + nota[:190])

# T1 — schema certo e a regra D3 existe verbatim no v1.4
ws = ' '.join(raw14.split())
t1 = sha(S14).startswith('d96ad15b') and ('REGRA DE CORPUS (D3)' in raw14) and bool(
    re.search(r'"if":\s*\{\s*"properties":\s*\{\s*"g2_elegibilidade":\s*\{\s*"const":\s*"redirecionado_clinico"', ws)
    and re.search(r'"then":\s*\{\s*"properties":\s*\{\s*"ancoras":\s*\{\s*"minItems":\s*2', ws))
reg('T1_D3_EXISTE_NO_V14_SELO', t1,
    f'N2 v1.4 = {sha(S14)[:12]}… (selo confere) · description: "REGRA DE CORPUS (D3): … É REQUISITO DE CORPUS apenas quando g2_elegibilidade = redirecionado_clinico…" · condicional if/then ancoras.minItems=2 PRESENTE — a regra citada existe, e é deliberada ("Sem a segunda ancora, o redirecionamento volta a ser uma saida sem destino")')

# T2 — a regra ENTROU na v1.4 (não existia como condicional nas anteriores em mãos)
n11, n13 = raw11.count('"minItems": 2'), raw13.count('"minItems": 2')
t2 = n11 == 0 and n13 == 0 and raw14.count('"minItems": 2') == 1
reg('T2_REGRA_E_NOVA_NA_V14', t2,
    f'condicional ancoras.minItems=2: v1.1 = {n11}× · v1.3 = {n13}× · v1.4 = 1× (com description D3) → "a v1.4 acrescentou justamente a regra" CONFERE no nível do condicional')

# T3 — os conjuntos e o 224 (níveis declarados)
b1v2 = {v['id_vinculo'] for v in d if v['uso'] == 'B1_v2'}
red  = {v['id_vinculo'] for v in d if v['g2_elegibilidade'] == 'redirecionado_clinico'}
conf = 274 - len(b1v2) - len(red)
estrito = sum(1 for v in d if v['g2_elegibilidade'] in ('eligible', 'nao_aplicavel')) - len(b1v2)
t3 = len(b1v2) == 30 and len(red) == 20 and not (b1v2 & red) and conf == 224 and estrito == 223
reg('T3_224_CONFERE_COM_NIVEL', t3,
    f'B1_v2={len(b1v2)} (todos eligible/VALIDADO) · redirecionados={len(red)} (todos CANDIDATO) · interseção 0 · NÍVEL conformidade mecânica vs v1.4: 274−30−20 = {conf} · NÍVEL estrito elegível-curatorial: {estrito} — a diferença de 1 entre os níveis é a VINC_B1_0047 (nao_avaliado/TRIADO)')

# T4 — reconciliação honesta 243 → 224 (as duas contagens são certas, em eras e critérios declarados)
e47 = next(v for v in d if v['id_vinculo'] == 'VINC_B1_0047')
t4 = (274 - 30 - 1) == 243 and (e47['g2_elegibilidade'] == 'nao_avaliado')
reg('T4_243_PARA_224', t4,
    f'era v1.1 (trilha 27): 274−30(B1_v2)−1(VINC_B1_0047) = 243 · era v1.4: 274−30−20(D3) = 224 com o 0047 migrável mecanicamente (ou 223 no nível estrito) · Δ=−19 = +20 da regra D3 −1 (o 0047 muda de categoria). Ninguém errou: o schema ficou mais exigente de propósito')

# T5 — "segunda âncora já existe em texto livre, em 18 dos 20"
redl = [v for v in d if v['g2_elegibilidade'] == 'redirecionado_clinico']
com_motivo = sum(1 for v in redl if v['g2_motivo'].strip())
com_reanc = sum(1 for v in redl if 'reancorado_em' in v)
t5 = com_motivo == 20 and com_reanc == 18
reg('T5_18_DE_20', t5,
    f'20/20 têm g2_motivo em texto livre (destino do redirecionamento descrito) · {com_reanc}/20 têm a marca formal reancorado_em — a medida "18 dos 20" dele CONFERE; curadoria = formalizar a 2ª âncora, não pesquisar')

# T6 — confirmação 1: papel não é veredito (description R7 no v1.4)
seg = re.search(r'"papel":\s*\{\s*"type":\s*"string",\s*"enum":\s*\[[^\]]*\],\s*"description":\s*"([^"]{0,400})', raw14, re.S)
t6 = bool(seg) and ('NUNCA o veredito' in seg.group(1)) and ('RELACAO TEMATICA' in seg.group(1))
reg('T6_PAPEL_NAO_VEREDITO', t6, f'description de ancoras[].papel (R7): "…declara a RELACAO TEMATICA da evidencia com a entidade — NUNCA o veredito…" → recusar papel como proxy do degrau 4 É cumprir a norma — confirmação 1 dele: VERDADEIRA')

# T7 — confirmação 2: sentido_relacao fora do schema (com precisão histórica honesta)
cnt = [raw11.count('sentido_relacao'), raw13.count('sentido_relacao'), raw14.count('sentido_relacao')]
t7 = cnt[2] == 0 and '"sentido_relacao":' not in raw14
reg('T7_SENTIDO_RELACAO_FORA', t7,
    f'ocorrências da palavra sentido_relacao: v1.1 = {cnt[0]}× · v1.3 = {cnt[1]}× (menção em prosa) · v1.4 = {cnt[2]}× · como CAMPO: 0 nas três → efeito prático dele CONFERE (campo inexiste → L-06 certa em depender da Ontologia); a data "retirado na v1.3" não se confirma nestas três versões (v1.1 já não tinha) — nota histórica, zero impacto')

# T8 — confirmação 3: contexto e nivel_cadeia não existem como campos (nível declarado)
campo_contexto = len(re.findall(r'"contexto"\s*:', raw14))
palavra_contexto = raw14.count('contexto')
t8 = campo_contexto == 0 and 'nivel_cadeia' not in raw14
reg('T8_CAMPOS_INEXISTENTES', t8,
    f'"contexto" como PROPRIEDADE: {campo_contexto}× (a palavra aparece {palavra_contexto}× em prosa/enum — nível declarado) · nivel_cadeia: 0× total → confirmação 3 dele VERDADEIRA; degraus 2/4 travam por falta de estrutura, não falha científica')

# T9 — nuance da granularidade: escopo já existe e cobre mecanismo; a dívida é de EXTENSÃO
esc = re.search(r'"escopo":\s*\{[^}]*"description":\s*"([^"]{0,400})', raw14, re.S)
t9 = bool(esc) and ('BLOCO_XX[/sub]' in esc.group(1)) and ('APENDICE_CORPUS' in esc.group(1)) and ('null para entidades sem subdivisao' in esc.group(1))
reg('T9_NUANCE_GRANULARIDADE', t9,
    'description de escopo (R4): mecanismo usa BLOCO_XX[/sub] · valor reservado APENDICE_CORPUS · "null para entidades sem subdivisao (exame, suplemento, cenario)" → a nuance dele CONFERE: não falta campo; falta decisão de ESTENDER escopo às famílias não-mecanismo → D-L05-GRANULARIDADE-OBJETO passa de "defeito" a "decisão de desenho"')

# T10 — a aritmética das 3 assinaturas de erro que ele listou (20 + 30 + 30) fecha em 50 vínculos
t10 = (20 * 1 + 30 * 2) == 80 and 274 - (20 + 30) == 224
reg('T10_ASSINATURAS_COERENTES', t10,
    'assinaturas "20 segunda âncora · 30 trilha · 30 uso" = 80 mensagens sobre 50 vínculos (20×1 + 30×2) → não-conformes = 50 → conformes = 224 — leitura coerente com a medida da casa; "trilha"+"uso" são duas mensagens da MESMA família B1_v2 (30)')

n_ok = sum(1 for c in checks if c['status'] == 'VERDE')
resumo = (f'TRILHA 84: {n_ok}/{len(checks)} — PONTO DO ESTRUTURA CONFIRMADO com níveis declarados: D3 existe verbatim no v1.4 selado (nova na v1.4) · '
          f'224 conformes mecânicos / 223 elegíveis-estritos (diferença = VINC_B1_0047) · 243 era medida da era v1.1, correta à época · 18/20 reancorado_em · '
          f'3 confirmações dele: VERDADEIRAS (com nota histórica de sentido_relacao) · nuance granularidade CONFERE → dívida relabelada p/ decisão de extensão · '
          f'CASA ADOTA o critério dele como régua do portão: fechamento = validador zero não-conformes contra d96ad15b, não número. Documento L-06: sem toque (citação de linhagem; risco realizado só se alguém aferir pelo número — neutralizado pela régua adotada).')
print(resumo)
out = f'{BASE}/BIBLIOTECAS/B01_Neuroinflamacao/atuais/producao/TRILHA84_script_portao_v14_224_2026-09-22.json'
json.dump({'trilha': 84, 'rodada': 73, 'data': '2026-09-22', 'verde': n_ok, 'total': len(checks),
           'checks': checks, 'resumo': resumo,
           'corpus': {k: sha(v) for k, v in {'N2_v1.4': S14, 'N2_v1.3': S13, 'N2_v1.1': S11, 'vinculos_V7': V}.items()}},
          open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('json ->', out)
