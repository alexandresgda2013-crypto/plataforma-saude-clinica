# PUBLICACAO DO ROTEIRO - ERRATA DE 01/10/2026 (programa unico, ASCII puro, tudo embutido).
# Uso, na raiz do repositorio (main atualizado):  python3 PUBLICAR_ROTEIRO_01-10-2026.py
# Tudo e conferido ANTES de gravar qualquer arquivo. Qualquer falha = PARA, sem gravar nada.
import hashlib, os, sys
RAIZ = os.getcwd()
ROT = os.path.join(RAIZ, 'ROTEIRO DE TRABALHO DA PLATAFORMA.md')
SERIE = os.path.join(RAIZ, 'BIBLIOTECAS', '_documentos_serie', 'ROTEIRO_plataforma_vigente_2026-09-27')
BAK = os.path.join(SERIE, 'ROTEIRO_PLATAFORMA_ANTERIOR_507eaefa_2026-10-01.bak')
PASTA = os.path.join(RAIZ, 'ENTREGAS', '2026-10-01_ROTEIRO_E_ATO')
BIL_PASTA = os.path.join(PASTA, 'ROTEIRO_PLATAFORMA_VIGENTE.txt')
ATO_PASTA = os.path.join(PASTA, 'ATO_OPERADOR_2026-10-01.md')
DIG_PASTA = os.path.join(PASTA, 'DIGITAIS.txt')
BIL_DEST = os.path.join(RAIZ, 'BIBLIOTECAS', '_documentos_serie', 'ROTEIRO_PLATAFORMA_VIGENTE.txt')
ANTES = '507eaefac6eadc2ccf9fac506b9ad80ace34296b33ef21c822dfffeb033cbe8e'
DEPOIS = 'aa01bfe87044f4724e6c4928c6d073e0eb24003090ce69099fd363bba40c5579'
BILHETE = 'cadfef35971316b5525421bea397133d22740b3fecc85bf411cb41b21c90f76b'
ATO = '16700dc0c0d792d8ce9863edfe069f24bac88ef7c6f143311a7c0eb58180b76e'
def sha(b): return hashlib.sha256(b).hexdigest()
def parar(msg): print('PARAR:', msg); sys.exit(1)

BIL_LINHAS = [
    "ROTEIRO DE TRABALHO DA PLATAFORMA \u2014 VIGENTE",
    "============================================",
    "Documento de trabalho (n\u00e3o substitui contratos \u2014 \u00a718 do pr\u00f3prio).",
    "Bilhete atualizado em 01/10/2026 (substitui o bilhete de 29/09, digital 0d3e5ab1\u2026).",
    "",
    "Arquivo vigente (principal \u2014 raiz do projeto):",
    "  ROTEIRO DE TRABALHO DA PLATAFORMA.md",
    "  sha256 aa01bfe87044f4724e6c4928c6d073e0eb24003090ce69099fd363bba40c5579",
    "  38.971 bytes \u00b7 1.174 linhas \u00b7 CRLF \u00b7 errata 01-10-2026",
    "",
    "Tr\u00eas datas, tr\u00eas pap\u00e9is:",
    "  T\u00edtulo interno \"- 27.09.2026\": nomeia a edi\u00e7\u00e3o (a s\u00e9rie e os registros a citam).",
    "  Campo Atualiza\u00e7\u00e3o, 01-10-2026: data da \u00faltima errata.",
    "  Nome do arquivo no pacote de 29/09 (..._2026-09-29): data do pacote em que a errata de 29/09 foi entregue.",
    "",
    "Cadeia de vers\u00f5es (digital \u00b7 tamanho \u00b7 papel):",
    "  2c286ca17b582a5fcad425d55b6a8f4ca7fd77cb1e95e23f6280fd58aa8357ce \u00b7 35.438 B",
    "    Vers\u00e3o 27.09. Concordada pelos dois auditores em 26/09, sobre esta digital.",
    "    S\u00e9rie: BIBLIOTECAS/_documentos_serie/ROTEIRO_plataforma_vigente_2026-09-27/ROTEIRO DE TRABALHO DA PLATAFORMA - 27.09.2026.md",
    "  5f8b89dc524adecb3a4046740ff469970996827aae8861e3fdbbdd14d717435d \u00b7 36.237 B \u00b7 CRLF",
    "    Errata de 26/09 (pedido do operador). Sem concord\u00e2ncia pr\u00f3pria registrada.",
    "    S\u00e9rie: ROTEIRO DE TRABALHO DA PLATAFORMA (errata 26-09).md",
    "  507eaefac6eadc2ccf9fac506b9ad80ace34296b33ef21c822dfffeb033cbe8e \u00b7 37.919 B \u00b7 CRLF",
    "    Errata de 29/09 (pedido do operador). Sem concord\u00e2ncia pr\u00f3pria registrada.",
    "    Preservada byte a byte em: ROTEIRO_PLATAFORMA_ANTERIOR_507eaefa_2026-10-01.bak (na mesma s\u00e9rie).",
    "  aa01bfe87044f4724e6c4928c6d073e0eb24003090ce69099fd363bba40c5579 \u00b7 38.971 B \u00b7 CRLF",
    "    Errata de 01/10 (pedido do operador). Este \u00e9 o arquivo vigente.",
    "",
    "Concord\u00e2ncias (2\u00d7 sem ressalva, 26/09, ambas sobre 2c286ca1\u2026):",
    "  Auditor-Estrutura: CONCORDA (digitais \u00b7 ensaio\u00d7piloto \u00b7 \u00a76.1)",
    "  Auditor-Mestre: SIM, CONCORDO (S-1/S-2/S-3/\u00a718 lidos no arquivo; nota:",
    "    \u00a76.1 \u00e9 prospectivo, n\u00e3o reabre bases j\u00e1 fechadas por rito)",
    "  Auditor-Mestre, 01/10/2026: classificou a errata de 01/10 como N\u00c3O SUBSTANTIVA, com medi\u00e7\u00e3o",
    "    independente, sobre a reda\u00e7\u00e3o de digital a0efc7d01765bd24361cbe0d931d92d5442253c3e3e415f9c65d577db777f93c.",
    "    A reda\u00e7\u00e3o final (aa01bfe8\u2026) difere dessa s\u00f3 no detalhamento das notas (4) e (6) e AINDA N\u00c3O foi",
    "    medida por ele nesta data.",
    "",
    "Errata 29-09-2026, descri\u00e7\u00e3o medida em 01/10 (substitui a frase \"trocaram apenas a palavra\"):",
    "  O \u00a718 registra, para cada uma das tr\u00eas bases, as duas digitais: a do texto assinado (preservado",
    "  byte a byte em .bak) e a do arquivo vigente. As erratas de etiqueta e proced\u00eancia de 29/09 mudaram,",
    "  em cada base, s\u00f3 as linhas abaixo; nenhuma regra, marco, sequ\u00eancia ou se\u00e7\u00e3o foi alterada.",
    "    COMO v1.11 rev.2 (2efc0edd\u2026 \u2192 1ea6d354\u2026): o t\u00edtulo e um bloco de coment\u00e1rio de errata de 14 linhas.",
    "    Schema-Claim v1.3 rev.3 (28cbc9c7\u2026 \u2192 e9f9e5d8\u2026): o t\u00edtulo, 1 linha de coment\u00e1rio dentro do bloco",
    "      de schema e um bloco de 13 linhas.",
    "    Contrato de Sa\u00edda rev.2 (841532da\u2026 \u2192 03cdd19a\u2026): o t\u00edtulo (perdeu \"MINUTA FINAL\"), o campo Status",
    "      reorganizado (o par\u00e1grafo original ficou como \"Status (na reda\u00e7\u00e3o)\"), o rodap\u00e9 e um bloco de 15 linhas.",
    "  O texto \"apenas errata de etiqueta\" do corpo do \u00a718 permanece: os documentos se descrevem como",
    "  \"errata de etiqueta e proced\u00eancia, 0 mudan\u00e7a de conte\u00fado\".",
    "",
    "Errata 01-10-2026 (a pedido do operador): corrigidos o campo Atualiza\u00e7\u00e3o (27-09 \u2192 01-10); a nota (4)",
    "(que dizia \"apenas a palavra\"; agora descreve o que mudou em cada base); a nota (5) (que chamava de",
    "\"aprovado em 26/09\" o texto da errata de 26/09, sem aprova\u00e7\u00e3o pr\u00f3pria registrada); e acrescentada a",
    "nota (6). Esta errata n\u00e3o altera o corpo do documento a partir de \"Objetivo:\" (id\u00eantico ao anterior).",
    "",
    "Vig\u00eancia: o Roteiro circula como vigente desde 26/09, ap\u00f3s as duas concord\u00e2ncias sobre 2c286ca1\u2026.",
    "Aprova\u00e7\u00e3o do operador (verbatim): AINDA N\u00c3O REGISTRADA. A frase, citando a digital completa de",
    "aa01bfe8\u2026, ser\u00e1 registrada aqui depois de emitida. O Auditor-Mestre registrou a falta como AUD-007.",
    "",
    "An\u00e1lise da casa: TRILHA110 18/18.",
    "",
    "Substitui: roteiros antigos (em uploads/Antigos/Documentos e s\u00e9rie r34).",
    "Bases normativas do processo (n\u00e3o substitu\u00eddas \u2014 ver \u00a718 do Roteiro):",
    "  Contrato de Sa\u00edda rev.2 \u2014 vigente 03cdd19a\u2026 (texto aprovado 841532da\u2026)",
    "  Schema-Claim v1.3 rev.3 \u2014 vigente e9f9e5d8\u2026 (texto aprovado 28cbc9c7\u2026)",
    "  COMO EXECUTAR v1.11 rev.2 \u2014 vigente 1ea6d354\u2026 (texto aprovado 2efc0edd\u2026)"
]

ATO_LINHAS = [
    "# ATO DO OPERADOR \u2014 01/10/2026",
    "",
    "**Data:** 01/10/2026 \u00b7 registro da Arena-Casa",
    "",
    "O operador colou no chat, em 01/10/2026, as cinco frases abaixo, letra a letra.",
    "",
    "## 1. Ratifica\u00e7\u00e3o das erratas de etiqueta de 29/09 (arquivo vigente atual)",
    "",
    "> Aprovo como vigente o COMO EXECUTAR \u2014 v1.11 rev.2, digital 1ea6d354, de 01/10/2026 (errata de etiqueta de 29/09/2026; texto aprovado em 25/09/2026, digital 2efc0edd).",
    ">",
    "> Aprovo como vigente o Schema-Claim v1.3 \u2014 rev.3, digital e9f9e5d8, de 01/10/2026 (errata de etiqueta de 29/09/2026; texto aprovado em 25/09/2026, digital 28cbc9c7).",
    ">",
    "> Aprovo como vigente o Contrato de Sa\u00edda do Claim Kit \u2014 rev.2, digital 03cdd19a, de 01/10/2026 (errata de etiqueta de 29/09/2026; texto aprovado em 24/09/2026, digital 841532da).",
    ">",
    "> Aprovo como vigente a L-06 \u2014 Minuta 3 consolidada rev.6, digital acd76b24, de 01/10/2026 (errata de etiqueta de 29/09/2026; texto aprovado em 22/09/2026, digital 98e90bdc).",
    "",
    "| Documento | Arquivo vigente (sha256) | Texto aprovado (sha256) |",
    "|---|---|---|",
    "| COMO EXECUTAR v1.11 rev.2 | `1ea6d3547ff5acbc5160c0a5ff4e2fd704611846482caeeaaecdccc6ec7a7033` | `2efc0edd9ba8fdf312cae23aceafc840b9ec3f8a2bc5e9ed147fe2f5bb2f9a2c` |",
    "| Schema-Claim v1.3 rev.3 | `e9f9e5d8d8949b3e38cf2d187520d7611d4665d7750579351e43774a5c70229e` | `28cbc9c76006f485f340da124aa1795833afa56d38e6572a9279d94a88f6b94c` |",
    "| Contrato de Sa\u00edda rev.2 | `03cdd19af99801f34858427f1cc42de85189b29f6e9561fad5872173233e2d27` | `841532dad13cd3fea1356c9e23e37067e78876685db52d3c1f2cd8b2a96e535c` |",
    "| L-06 Minuta 3 rev.6 | `acd76b244b430027506a17f18c4ec4b2196359719f2c09d06749d6682f094740` | `98e90bdc755162b28fd16817d65692cebe81f939c466ef1d29c7a0a1124f2b41` |",
    "",
    "Os Atos de 22 a 25/09 valem para o **texto assinado** (digital antiga). A frase de 01/10 vale para o **arquivo vigente atual** (digital nova). A classifica\u00e7\u00e3o das quatro erratas como **n\u00e3o substantivas** \u00e9 do Auditor-Mestre, com medi\u00e7\u00e3o independente do Auditor-Estrutura e da Casa.",
    "",
    "## 2. Decis\u00e3o do L-NT (op\u00e7\u00e3o i)",
    "",
    "> Decido a op\u00e7\u00e3o (i) do fluxo de claims, com a bifurca\u00e7\u00e3o desenhada: o claim cl\u00ednico \u00e9 insumo de evid\u00eancia, n\u00e3o de conhecimento; a afirma\u00e7\u00e3o vai \u00e0 Biblioteca da entidade pelo rito normal (\u00a75.5 da Arquitetura V2.3, digital 498e7df9), e a evid\u00eancia segue N1 \u2192 N2 \u2192 NT. A op\u00e7\u00e3o (ii) fica descartada. Decis\u00e3o de 01/10/2026.",
    "",
    "Alcance: libera a reda\u00e7\u00e3o da minuta 2 do L-NT. N\u00e3o declara vigente nenhum documento (a minuta 2 ainda n\u00e3o existe).",
    "",
    "## Fora deste Ato",
    "",
    "O **Roteiro de Trabalho da Plataforma** n\u00e3o est\u00e1 nesta ratifica\u00e7\u00e3o. Sua frase ser\u00e1 registrada em ato pr\u00f3prio, com a digital completa do arquivo final."
]

bil = ('\n'.join(BIL_LINHAS) + '\n').encode('utf-8')
ato = ('\n'.join(ATO_LINHAS) + '\n').encode('utf-8')
if sha(bil) != BILHETE: parar('bilhete embutido nao confere (digital %s). Nada foi gravado.' % sha(bil))
if sha(ato) != ATO: parar('Ato embutido nao confere (digital %s). Nada foi gravado.' % sha(ato))
if not os.path.isfile(ROT): parar('Roteiro da raiz nao encontrado. Rode na raiz do repositorio.')
b = open(ROT, 'rb').read()
if sha(b) != ANTES: parar('Roteiro da raiz nao e o 507eaefa (digital %s). Nada foi gravado.' % sha(b))
if not os.path.isdir(SERIE): parar('pasta da serie nao existe: ' + SERIE)
if os.path.exists(BAK): parar('o .bak ja existe; nao sobrescrevo.')
if os.path.exists(PASTA): parar('a pasta do dia ja existe; nao sobrescrevo.')
t = b.decode('utf-8')
def sub(old, new):
    global t
    if t.count(old) != 1: parar('trecho nao unico/ausente: ' + old[:50])
    t = t.replace(old, new)

sub('**Atualiza\u00e7\u00e3o:** 27-09-2026', '**Atualiza\u00e7\u00e3o:** 01-10-2026')
sub('(ap\u00f3s as erratas de etiqueta de 29/09, que trocaram apenas a palavra "minuta/n\u00e3o vigente" no interior dos documentos). Nenhuma',
    '(ap\u00f3s as erratas de etiqueta e proced\u00eancia de 29/09, sem mudan\u00e7a de conte\u00fado normativo). '
    'Em cada documento, a errata trocou o t\u00edtulo e acrescentou, no topo, um bloco de coment\u00e1rio de errata: '
    'no COMO, o t\u00edtulo e um bloco de 14 linhas; '
    'no Schema-Claim, o t\u00edtulo, uma linha de coment\u00e1rio interna do bloco de schema e um bloco de 13 linhas; '
    'no Contrato, o t\u00edtulo (que perdeu "MINUTA FINAL"), o campo Status reorganizado (o par\u00e1grafo original foi preservado como "Status (na reda\u00e7\u00e3o)"), '
    'o rodap\u00e9 e um bloco de 15 linhas. Nenhuma')
sub('O **texto aprovado em 26/09** (errata) permanece', 'O **texto da errata de 26/09** permanece')
sub('; a digital deste arquivo ap\u00f3s a presente errata consta do bilhete', '; a digital deste arquivo consta do bilhete')
nota6 = ('\r\n\r\n**Errata 01-10-2026 (a pedido do operador):**\r\n'
 '**(6)** Corrigidos: o campo **Atualiza\u00e7\u00e3o** (27-09 \u2192 01-10); a nota (4), que dizia que as erratas de 29/09 "trocaram apenas a palavra", '
 'quando tamb\u00e9m acrescentaram bloco de coment\u00e1rio e, no Contrato, reorganizaram Status e rodap\u00e9; '
 'e a nota (5), que chamava de "aprovado em 26/09" o texto da errata de 26/09, sem aprova\u00e7\u00e3o pr\u00f3pria registrada '
 '(a concord\u00e2ncia dos auditores foi sobre `2c286ca1\u2026`). '
 'O texto anterior (`507eaefa\u2026`) fica preservado em `ROTEIRO_PLATAFORMA_ANTERIOR_507eaefa_2026-10-01.bak`, '
 'na s\u00e9rie `ROTEIRO_plataforma_vigente_2026-09-27/`. Nenhuma regra, marco, sequ\u00eancia ou se\u00e7\u00e3o foi alterada.')
fim5 = 'consta do bilhete `ROTEIRO_PLATAFORMA_VIGENTE.txt`.'
sub(fim5, fim5 + nota6)

out = t.encode('utf-8')
if sha(out) != DEPOIS: parar('digital final %s != %s. Nada foi gravado.' % (sha(out), DEPOIS))
if len(out) != 38971 or out.count(b'\r\n') != 1174 or out.count(b'\n') != 1174: parar('tamanho/CRLF fora do esperado.')
k = b'**Objetivo:**'
if out[out.find(k):] != b[b.find(k):]: parar('corpo a partir de Objetivo mudou.')

os.makedirs(PASTA)
open(BAK, 'wb').write(b)
open(ROT, 'wb').write(out)
open(BIL_DEST, 'wb').write(bil)
open(BIL_PASTA, 'wb').write(bil)
open(ATO_PASTA, 'wb').write(ato)
alvos = (('.bak do Roteiro anterior', BAK, ANTES, 37919),
         ('ROTEIRO DE TRABALHO DA PLATAFORMA.md (final)', ROT, DEPOIS, 38971),
         ('bilhete em BIBLIOTECAS/_documentos_serie', BIL_DEST, BILHETE, len(bil)),
         ('bilhete na pasta do dia', BIL_PASTA, BILHETE, len(bil)),
         ('ATO_OPERADOR_2026-10-01.md', ATO_PASTA, ATO, len(ato)))
linhas = ['DIGITAIS - pasta ENTREGAS/2026-10-01_ROTEIRO_E_ATO (medidas apos gravar; sha256 completo)', '']
for nome, p, esp, tam in alvos:
    d = open(p, 'rb').read()
    ok = sha(d) == esp and len(d) == tam
    print(nome, len(d), 'bytes', sha(d), 'OK' if ok else 'DIVERGE')
    if not ok: parar(nome + ' diverge apos gravar.')
    linhas.append('%s  %s (%d bytes)' % (sha(d), nome, len(d)))
open(DIG_PASTA, 'wb').write(('\n'.join(linhas) + '\n').encode('utf-8'))
print('Concluido.')
