# SUBSCRIÇÃO DO AUDITOR-MESTRE — CONTRATO DE SAÍDA DO CLAIM KIT (D1+R-1+R-2)

**Auditor-Mestre · 2026-09-24**
**Objeto:** `MINUTA_CONTRATO_SAIDA_CLAIMKIT_2026-09-24.md` (Rota A)
**Base verificada:** N2 v1.4 `d96ad15b…` · Schema-Claim v1.2 `56dc0e94…` · Bloco v1.6 `0a630dba…` · vínculos B1 V7 `490675e6…` · L-06 rev.6 vigente

---

## RESPOSTA: **SUBSCREVO SEM RESSALVA**

A minuta integra D1, R-1 e R-2 exatamente como o meu parecer da Rodada 4 pediu, e verifiquei as três peças que sustentam a minha subscrição contra os artefatos reais, não contra a descrição.

### O que confirmei por medição

**R-1 está resolvida no ponto que eu levantei.** Minha ressalva era: a solução impedia fabricar condição mas permitia fabricar direção. A minuta fecha isso em três camadas — direção é decisão científica do fechamento (§3.1), proibição explícita de default (§3.3: não inferir de status, fonte principal, achado ou prosa), e **falha dura** quando a direção não vem decidida (§3.4). É o mesmo rigor que D1 aplicou à condição, agora aplicado à direção. O mapeamento `suporta_relacao→sustenta / refuta_relacao→refuta / inconclusivo→inconclusivo` cai em valores que **existem** no enum selado do N2 — conferido.

**R-2 está resolvida, e o caso do `.001b` está tratado corretamente.** Minha ressalva era a inversão de efeito que um único N2 condicional perde. A minuta materializa `inverte` como **dois N2 complementares** (§4.3), com o `.001b` nomeado como exemplo canônico, e reconhece que a L-06 resolve o par por disjunção de condição. Confirmei que isso é estruturalmente possível e **já praticado**: 30 referências do acervo têm mais de um vínculo hoje (`REF_SWANSON_2019` tem 3). Não é capacidade nova; é o padrão vigente. E a fonte única de `condicao` (§4.1) fecha o risco que apontei de o kit ganhar duas origens concorrentes de condição.

**A minha nota não bloqueante virou destino explícito.** A maturidade agora vai para `grau_maturidade` (§4.4), não para `condicional` — o campo que eu apontei estar em 274/274 no acervo.

### O que registro como correto na condução, não como ressalva

O Comentador escolheu a Rota A — integrar R-1 e R-2 **antes** de fechar D1, em vez de empurrá-las para outro ciclo — e concordo com a razão dele: R-1 e R-2 são o mesmo princípio de D1 nos outros eixos, e materializar sem elas seria deixar o materializador interpretar ciência. É a leitura certa.

A **trava do §7** é o ponto que me faz subscrever com tranquilidade: a primeira materialização não começa enquanto P-K1 (direção por fonte) e P-K2 (`ressalvas[]` com tipo) não existirem no contrato do kit. Isso responde exatamente ao alerta que dei na rodada passada — que o `.001b` cai nas duas ressalvas e não pode ser materializado antes delas fecharem. A trava está escrita; o risco está contido.

### Os quatro pontos do meu território, respondidos

1. **Suficiência epistemológica** — suficiente: os quatro eixos de decisão (estado, direção, tipo de ressalva, modificação) cobrem os casos que medi no kit.
2. **Preservação do significado** — preservada: nenhuma ressalva vira condição por derivação; a inversão não perde metade; a magnitude não vira direção.
3. **Caso não coberto** — o que eu havia achado (inversão de efeito) está agora coberto pelo §4.3. Não encontrei outro nesta medição.
4. **Fabricação** — impedida nos dois eixos: condição (D1) e direção (R-1, §3.3/§3.4).

### Uma observação que NÃO é ressalva, para o ciclo do kit

A minuta cita o vocabulário `sentido_do_achado` do **Schema-Claim v3.1** (§3.1, P-K1). Eu tenho apenas a v1.2, onde esse campo não existe (0 ocorrências). Não é ressalva porque a própria minuta trata isso como **pendência do ciclo do kit** (P-K1) sob trava — não pressupõe a v3.1 como vigente. Registro só para que a subscrição fique honesta: **subscrevo a regra de materialização; não verifiquei a v3.1, que não recebi.** Quando o contrato do kit fechar P-K1, o vocabulário efetivo precisa ser conferido contra o que a materialização espera — e isso é território de quem fecha o kit, com auditoria de fidelidade depois.

### Fronteiras

Não opino sobre a compatibilidade estrutural fina do N2 (cardinalidade de dois vínculos sobre a mesma âncora, if/then de schema) — território do Auditor-Estrutura. Confirmei apenas que **nada no N2 v1.4 impede** o padrão, e que o acervo já o pratica; a validação de schema é dele.

---

## Subscrição formal

> **Subscrevo, sem ressalva, a minuta do contrato de saída do Claim Kit que integra D1 + R-1 + R-2 conforme a Rota A, com as pendências P-K1..P-K5 travando a primeira materialização até o ciclo do kit as fechar.**

Pelo rito do operador, D1 encerra quando o Auditor-Estrutura também subscrever sem ressalva e a casa verificar mecanicamente a correspondência minuta↔pareceres. Minha parte está dada.

---

*Verificações: enum `direcao_suporte` do N2 v1.4 (sustenta/refuta/inconclusivo/condicional presentes); `id_vinculo` e `id_referencia_interna` como required (múltiplos vínculos por referência permitidos); 30 referências com >1 vínculo no acervo B1 V7; ausência de `sentido_do_achado` na Schema-Claim v1.2 que tenho; efeitos de moderador no Bloco (inverte no .001b). A Schema-Claim v3.1 não me foi entregue — a subscrição cobre a regra de materialização, não o vocabulário do kit.*
