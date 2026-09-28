# ADENDO 2 à RESPOSTA 5 — resposta do comentador PÓS-JSON (N1/N2): convergência quase total; 2 pontos novos confirmados com prova; 1 tensão interna nomeada

**Data:** 2026-09-16 · **Ref.:** `RESPOSTA_COMENTADOR_POS_JSON_N1N2_2026-09-16.md` sha `d4ad1545de7fc7d1311571b84a1245806893fe5380af1e58730b6a15528b6f57` (verbatim na pasta `L05_v1.2_schemas_recebidos_2026-09-16/`) · **Trilha:** 39 · **Ciência tocada:** 0

---

## 0. Cronologia corrigida (esclarecimento do operador)

O parecer §1–§24 (nosso ADENDO 1) foi escrito **sem os JSONs**; a análise de 3 pontos (nossa RESPOSTA 5) foi intermediária; **esta resposta é a posição pós-JSONs**. Isso explica a premissa envelhecida do §12 medida na trilha 38 — e é coerente que aqui, no §2.6, ele acerte o mesmo ponto sozinho. Registrado sem custo: a trilha 38 mediu o dado, não a intenção.

## 1. Veredito geral dele: fechamento, não reestruturação — a casa **confirma**

Nada na bancada mediu incompatibilidade estrutural N1×N2 (trilhas 37–39: incorporação 9/9, validações sintéticas, superfície em massa). As 8 separações que ele declara consolidadas (§7) são exatamente as que a v1.2 implementa e a bancada verificou campo a campo.

## 2. Pontos NOVOS confirmados — com prova e proposta

**§2.3/D2 — `pmid_oficial` vazio: CONFIRMADO com prova executável.** O pattern `^[0-9]{0,8}$` admite vazio **sempre**; nenhum `allOf` toca pmid. Ficha `humana_observacional` com pmid vazio **passa hoje** no validador. E draft-07 **expressa** — a casa oferece o bloco, medido em 6 casos:

```json
{ "if":   { "properties": { "natureza_evidencia": { "not": { "const": "nao_aplicavel" } } },
            "required": ["natureza_evidencia"] },
  "then": { "properties": { "pmid_oficial": { "pattern": "^[0-9]{1,8}$" } } } }
```

Medição: molde íntegro ok ✔ · furo fecha ✔ · `nao_aplicavel` sem pmid segue válido ✔ · letras reprovam (pattern já certo nisso) ✔. Dado hoje: 0/237 vazio e natureza 0/237 — a regra só trabalha **pós-migração**. Recomendação da casa: fica no **schema** (mesmo princípio do `condicao`, carta 5 §2); a inversa (`nao_aplicavel` exigir vazio) deixamos como decisão de design sua.

**§3.4/D5-fino — description de `uso` imprecisa: CONFIRMADO.** A união tem **5 valores**: 2 exclusivos da clínica + 2 exclusivos da mecanística + `gap_pesquisa` comum. "3 primeiros + 3 últimos" lê-se como 3+3. Texto oferecido: *"clinica: {clinico, contexto_mecanistico} · mecanistica: {nucleo_causal, suporte_correlacional} · gap_pesquisa: comum às duas (interseção). A trilha do vínculo seleciona o sub-conjunto permitido."*

**§2.4/D3 — medições dentro de descriptions: ADOTADO, com eco da nossa própria norma.** Localizamos **2 instâncias**: *"Medido hoje: 0/66 mordem…"* (`natureza_evidencia`) e *"…até os 20 vinculos…"* (`g2_elegibilidade`). A norma da casa é "medida sem comando gravado não vale" — em texto normativo o comando se perde. **Regra permanece na description; a medição vai ao relatório/gate de migração, com data e trilha** (as nossas trilhas 35/37 regeneram os dois números a qualquer tempo).

## 3. Convergências (registro — são pontos da carta 5/adições da casa)

**D1 ≡ Adição A** (paradoxo do alias): a versão dele é estrutural; a nossa chega com o dado — **162/237 compostos** passando no alias sem enum + fix de 2 linhas + aposentadoria por "100% idênticos" (que o §2.2 dele agora também pede). **D6/§3.5 ≡ fino 2** (`forca_biologica` ao **portão** — recomendação idêntica; 24 medidos na zona). **D5 ≡ §5 da carta 5** (Decisão 1: implementada no schema, falta **registro** — ele diz o mesmo). **§3.1** (V-17 com os 3 testes no portão) ≡ oferta da casa já embarcada. **§6** (ciclo Schema→Derivador→Acervo→Gate→Medição→Correções→Reexecução→Convergência) ≡ o método bilateral da casa (P-8, cartas 10–12). §2.1, §2.5, §3.2: aprovados e já verificados pela bancada.

## 4. Tensão interna nomeada (obrigação da bancada)

§3.3 daqui (*"A implementação está correta… a solução atual é suficiente"*) **colide com o ponto 1 da análise anterior dele** (*"Peço que seja fechado no schema/gate para evitar estado semanticamente inválido"* — a exclusividade do `condicao`). Ambos verbatim arquivados com sha. A casa **não escolhe o que ele quis dizer**: pede-se confirmação explícita — retirado ou mantido? Importante: nossa proposta (carta 5 §2, bloco medido em 5 casos) **não depende da resposta** — o furo está provado executável independentemente de quem o apontou.

## 5. Tabuleiro atualizado para a 1.2-normativa (dono a dono)

- **Auditor-2:** minuta 1.2 (prosa §3 R1+R7 · §4B rodapé · linha (ii) triagem `direcao`) · fechos: `condicao` (§2 carta 5) · alias N1 (§6 carta 5) · `cross-over` (fino 1) · texto de `uso` (§2 acima) · escolha pmid (§2 acima) · ponteiro `forca_biologica`→portão · medições→relatório de migração (§2 acima) · **relatório de execução 172/102 — pedido reiterado** (ADENDO 1 §1).
- **Operador:** D1–D5 do parecer (trilha/uso · 30 review · retroancoragem B1 · destino citacao_confirmada · catálogo) + confirmação da tensão do §4 com o comentador.
- **Casa:** derivador estrutural do catálogo (D-L05-IDS-JSON — 146 confirmados estruturalmente, 48+71+16+11); réplica da minuta 1.2 e da execução final; assinatura se tudo verde.

## 6. Crédito e registro

Resposta pós-JSON: **comentador externo**. Blocos e provas: **bancada**. Trilha **39** · decisoes **rev.27** · **0 ciência** (V7/manifesto íntegros; nada escrito no acervo).

— a casa
