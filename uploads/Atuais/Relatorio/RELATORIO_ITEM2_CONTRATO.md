# ITEM 2 CONCLUÍDO — `ferramentas/contrato.py` v1.0.0
10/09/2026

---

# 1. O que é

Módulo único que os escritores importam. Quatro funções, ~200 linhas de lógica:

```python
from contrato import Contrato, abortar_se

c = Contrato(artefato="vinculo", corpo_canonico=texto)
problemas = c.validar(registros)
abortar_se(problemas, "add_vinculos_b1", c.examinados)   # exit 1 se bloqueante
c.gravar(caminho, registros)                             # backup + atômico
```

**Nada nele é invenção minha.** Cada enum tem fonte: `MAPEAR_VOCABULARIO.md`, `validar_auditoria.py`, Prompt v4.2 (linhas 1256, 1427–1450), Processo v2.1 (P-5). Está citado no cabeçalho do arquivo.

---

# 2. O que ele impede — e o autoteste que prova

O módulo se autotesta reproduzindo **defeitos reais do acervo**:

```
✅ registro correto passa
✅ D1 natureza_relacao com tier_* (bug da V(), 30 vínculos B1)
✅ F2 vocabulário de ledger em vínculo (regressão B14)
✅ D2 trecho fabricado por fallback probe+'.'
✅ G1 assinando G3 (eutils como verificador)
✅ decisão sem registro de quem verificou
✅ cabeçalho markdown como âncora (VINC_B1_0019 real)
✅ 'APROVADO' no LEDGER é correto (não é erro)
8/8 casos corretos
```

O último caso é o mais importante: **o mesmo valor, no artefato certo, passa.** É a fronteira F2 funcionando nos dois sentidos — bloqueia o erro sem criminalizar o uso legítimo.

## Quatro decisões de desenho

**(a) Enum por artefato.** O construtor exige `artefato=` e recusa qualquer outro valor. Não há default — é impossível validar sem declarar qual vocabulário se aplica. Era o buraco da B14.

**(b) Detecta valor do enum de outro *campo*.** O bug da `V()` gravou `tier_*` em `natureza_relacao`. Cada valor era válido *em algum enum*, então "está preenchido?" passava. Agora o erro diz qual campo o valor pertence.

**(c) `verificar_literal()` nunca devolve booleano.** Devolve `{status, casados, total, divergencia}` com 6 status. Um booleano não diria a causa — e cada causa tem reparo diferente.

**(d) G1 não pode assinar G3.** Se `g3_verificado_por` casa `eutils|script|automatico`, é bloqueante. Implementa *"a ferramenta sozinha nunca marca eligible"* e *"o LLM não tem permissão de escrever os campos de verificação"*.

---

# 3. Resultado contra os dados reais

## Ledger B1 — limpo

```
LEDGER B1: examinados 237 | BLOQUEANTES 0 | avisos 0
```

**Confirma a retratação e o adendo A2.1 do outro agente.** O ledger está correto: enum próprio respeitado, 237/237 âncoras literais, verificação registrada em todos. Um artefato sem uma única ressalva.

## Vínculos B1 — 33 bloqueantes

```
VÍNCULOS B1: examinados 257 | BLOQUEANTES 33 | avisos 391

  17  natureza_relacao = 'tier_3_correlacional_mecanistico'  (enum de forca_causal)
  10  natureza_relacao = 'tier_4_descritivo_estrutural'      (enum de forca_causal)
   3  natureza_relacao = 'tier_2_intervencao'                (fora de qualquer enum)
   3  forca_causal     = 'tier_2_intervencao'                (fora de qualquer enum)
```

Os 30 conhecidos aparecem decompostos: 27 são troca de campo, **3 são valor inexistente**.

## 🔴 Achado novo: `tier_2_intervencao` não existe

Está em `VINC_B1V2_0205`, `0207`, `0208` — nos **dois** campos. Não pertence a nenhum enum do projeto. Os tiers oficiais são `tier_1_necessidade_e_suficiencia`, `tier_2_necessidade_ou_suficiencia`, `tier_3_correlacional_mecanistico`, `tier_4_descritivo_estrutural`.

**Isto conecta com o furo G2 do `gate_script.py`**, que filtra alto risco por `forca_causal == "tier_1_intervencao"` — também inexistente. Há uma **família `*_intervencao` fantasma** circulando: um autor escreveu por analogia com `tier_2_necessidade_ou_suficiencia`, e como nada validava enum, o valor entrou nos dados *e* no filtro do gate. O gate procura um valor que nunca existiu; os dados contêm um valor que nunca foi definido.

**Ação:** decidir se `*_intervencao` deve virar tier oficial (é evidência de intervenção — conceito legítimo) ou se os 3 registros devem ser remapeados. É decisão de conteúdo, não minha. Anoto como **AT-11**.

## Avisos: os 391

- **237 legado** (`VALIDADO_G3_IA`, `PENDENTE_FULLTEXT`) — já declarados como ressalva no P-4. Tratei como categoria nomeada: reportados com a tradução equivalente, **nunca silenciados**, nunca confundidos com defeito novo.
- **154 literalidade** (77 ROTULO + 55 PROSA + 22 SELO) — é o AT-02, já mapeado.

---

# 4. Por que 30 avisos e não 30 bloqueios na literalidade

`SELO`, `ROTULO` e `PROSA` são **aviso**; `AUSENTE` e `VAZIO` são **bloqueante**.

O critério: se o prefixo longo casa, a frase existe na Canônica e o vínculo aponta para conteúdo real — é dessincronização, reparável. Se não casa nada, o trecho pode nunca ter existido — é candidato a fabricação, e isso não pode passar.

Bloquear os 154 hoje travaria toda a B1 sem que nenhum dado esteja errado. Bloquear os `AUSENTE` impede que um `probe + "."` novo entre.

---

# 5. Arquivos

```
ferramentas/contrato.py     v1.0.0 · autoteste embutido (python3 contrato.py)
canonico/literalidade_b1.json   fila do AT-02 (do item 1)
validar_roundtrip.py.bak        backup pré-correção
```

---

# 6. Próximo — item 3

Blindar os escritores ativos, um por vez, medindo antes e depois:

1. `aplica_vereditos.py` — escreve `status_auditoria` em vínculos (onde a B14 quebrou)
2. `add_vinculos_b1v2.py` — origem dos 30; corrigir a `V()` de um parâmetro para dois
3. Propagador de selos — idempotência (`.match()` sobre espaço) + **selar antes de extrair**

Em cada um, a mudança é a mesma: importar, validar, `abortar_se`, gravar pelo contrato.

**Pendente de decisão sua:** o AT-11 (`tier_2_intervencao`). Enquanto não decidir, os 3 registros ficam bloqueados — corretamente, porque ninguém sabe o que aquele valor significa.
