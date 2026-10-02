# Correcao do Roteiro (01/10/2026). VARIANTE A = a adotada (aceita pelo Mestre; digital a0efc7d0). VARIANTE B = mais completa, nao adotada (aa01bfe8).
# Uso: python3 este.py "ROTEIRO DE TRABALHO DA PLATAFORMA.md" A|B
# (antiga v2) NAO grava no repositorio: escreve a copia em /tmp/rt/novo.md
# Uso: python3 ROTEIRO_CORRECAO_PROPOSTA_2026-10-01.py "ROTEIRO DE TRABALHO DA PLATAFORMA.md"
import sys, hashlib, os
src = sys.argv[1]
VAR = sys.argv[2] if len(sys.argv) > 2 else 'A'
assert VAR in ('A', 'B')
b = open(src, 'rb').read()
assert hashlib.sha256(b).hexdigest().startswith('507eaefac6eadc2c'), 'pre-condicao 507eaefa falhou'
t = b.decode('utf-8')
def sub(old, new):
    global t
    assert t.count(old) == 1, ('trecho nao unico/ausente', old[:40])
    t = t.replace(old, new)

sub('**Atualização:** 27-09-2026', '**Atualização:** 01-10-2026')

# nota (4): trecho final
if VAR == 'A':
    sub('(após as erratas de etiqueta de 29/09, que trocaram apenas a palavra "minuta/não vigente" no interior dos documentos). Nenhuma',
        '(após as erratas de etiqueta de 29/09, que trocaram a etiqueta "minuta/não vigente" no título e no status dos documentos; '
        'no Contrato, o título perdeu "MINUTA FINAL" (o "VIGENTE" está no Status) e, no Schema-Claim, também uma linha de comentário interna). Nenhuma')
else:
    sub('(após as erratas de etiqueta de 29/09, que trocaram apenas a palavra "minuta/não vigente" no interior dos documentos). Nenhuma',
        '(após as erratas de etiqueta e procedência de 29/09, sem mudança de conteúdo normativo). '
        'Em cada documento, a errata trocou o título e acrescentou, no topo, um bloco de comentário de errata: '
        'no COMO, o título e um bloco de 14 linhas; '
        'no Schema-Claim, o título, uma linha de comentário interna do bloco de schema e um bloco de 13 linhas; '
        'no Contrato, o título (que perdeu "MINUTA FINAL"), o campo Status reorganizado (o parágrafo original foi preservado como "Status (na redação)"), '
        'o rodapé e um bloco de 15 linhas. Nenhuma')


sub('O **texto aprovado em 26/09** (errata) permanece', 'O **texto da errata de 26/09** permanece')
sub('; a digital deste arquivo após a presente errata consta do bilhete', '; a digital deste arquivo consta do bilhete')

if VAR == 'A':
    nota6 = ('\r\n\r\n**Errata 01-10-2026 (a pedido do operador):**\r\n'
     '**(6)** Corrigidos o campo **Atualização** e o texto das notas (4) e (5). O texto anterior (`507eaefa…`) fica preservado em '
     '`ROTEIRO_PLATAFORMA_ANTERIOR_507eaefa_2026-10-01.bak`, na série `ROTEIRO_plataforma_vigente_2026-09-27/`. '
     'Nenhuma regra, marco, sequência ou seção foi alterada.')
else:
    nota6 = ('\r\n\r\n**Errata 01-10-2026 (a pedido do operador):**\r\n'
     '**(6)** Corrigidos: o campo **Atualização** (27-09 → 01-10); a nota (4), que dizia que as erratas de 29/09 "trocaram apenas a palavra", '
     'quando também acrescentaram bloco de comentário e, no Contrato, reorganizaram Status e rodapé; '
     'e a nota (5), que chamava de "aprovado em 26/09" o texto da errata de 26/09, sem aprovação própria registrada '
     '(a concordância dos auditores foi sobre `2c286ca1…`). '
     'O texto anterior (`507eaefa…`) fica preservado em `ROTEIRO_PLATAFORMA_ANTERIOR_507eaefa_2026-10-01.bak`, '
     'na série `ROTEIRO_plataforma_vigente_2026-09-27/`. Nenhuma regra, marco, sequência ou seção foi alterada.')

fim5 = 'consta do bilhete `ROTEIRO_PLATAFORMA_VIGENTE.txt`.'
sub(fim5, fim5 + nota6)

out = t.encode('utf-8')
os.makedirs('/tmp/rt', exist_ok=True)
open('/tmp/rt/novo.md', 'wb').write(out)
open('/tmp/rt/velho.md', 'wb').write(b)
print(len(b), '->', len(out), 'bytes; sha256', hashlib.sha256(out).hexdigest())
print('CRLF', out.count(b'\r\n'), 'LF solto', out.count(b'\n') - out.count(b'\r\n'))
i = b.find(b'# 1. '); j = out.find(b'# 1. ')
