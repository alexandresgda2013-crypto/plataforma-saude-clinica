# SUBSCRIÇÃO TERRITORIAL — SCHEMA-CLAIM v1.3 (ciclo do kit)

**Auditor-Mestre · 2026-09-25**
**Objeto:** minuta `SCHEMA-CLAIM v1.3 rev.2` (P-K1/P-K2/P-K3/P-K5, com ajuste V-K3)
**Verificado contra:** Schema-Claim-Mecanismo v3.1 (recebido) · N2 v1.4 `d96ad15b…` (projeto) · Schema-Claim v1.2 (baseline) · contrato de saída rev.2 (vigente) · L-06 rev.6

---

## RESPOSTA: **SUBSCREVO SEM RESSALVA**

A v1.3 implementa no schema o que o contrato rev.2 já determinou, com mínima alteração e sem importar nada além do necessário. Verifiquei os enums importados byte a byte, porque um vocabulário "importado literalmente" que divirja numa letra quebra a materialização — e eles batem.

## Os cinco pontos do meu território

**1. Suficiência científica das classificações.** Suficiente. Os três tipos de ressalva (condição, heterogeneidade, maturidade) cobrem os casos que medi no kit, e a v1.3 os torna estruturados em vez de texto livre — o que era a lacuna real que o Comentador identificou na rodada da interface.

**2. P-K1 impede fabricação de direção?** Sim, e confirmei o vocabulário. `sentido_do_achado` na v1.3 é `{suporta_relacao, refuta_relacao, inconclusivo}` — **idêntico byte a byte** ao v3.1. As quatro proibições de default estão escritas (não inferir de status, nível, achado ou prosa), e a **falha dura** está declarada: ausência do campo em claim materializável = claim não fechado. É o mesmo rigor de R-1, agora no schema. O materializador copia `suporta_relacao→sustenta` etc.; não decide. **Impede a fabricação.**

Registro o que verifiquei além do pedido: **`sentido_do_achado` é por fonte, dentro de `fontes[]`**, não no nível do claim. Isso importa e está certo — permite representar o caso que mais me preocupava, duas fontes do mesmo claim com direções opostas (uma sustenta, outra refuta). Sob a v1.3 isso vira dois sentidos por fonte mais uma `ressalva[tipo=heterogeneidade]`. A heterogeneidade real fica representável em vez de achatada numa direção única — que era exatamente o risco epistemológico do eixo de direção.

**3. P-K2 preserva o significado das ressalvas?** Sim. A classificação é decisão do fechamento científico, nunca inferência do materializador; `nota_ressalva` permanece como sumário legível mas deixa de ser fonte estrutural de `condicao`. E a fonte única de condição (P-K3) fecha a porta que eu tinha apontado: `condicao` só nasce de `ressalvas[tipo=condicao_aplicacao]`, e `nota_ressalva`, `moderadores` e `sentido_do_achado` estão explicitamente proibidos de gerá-la. Isso impede que D1 reabra em outro campo.

**4. P-K5 transforma maturidade em força ou condição?** Não. Confirmei os cinco valores: `grau_maturidade_cientifica` na v1.3 é idêntico ao v3.1 e ao enum do N2 v1.4 (que aceita os mesmos cinco mais `null`). A regra é `maturidade_evidencia → grau_maturidade`, **nunca → condicional**, e o V-K4 amarra a bi-implicação (campo preenchido ⟺ existe ressalva de maturidade). Maturidade e condição ficam em eixos separados, como devem. Não vira força: `forca_causal` e `forca_biologica_conexao` do v3.1 **não** foram importados — e é correto não importar, são semântica mecanística.

**5. A saída ao materializador é suficiente para preservar o significado?** Sim, com uma consciência clara do que fica de fora e por quê. A v1.3 entrega ao materializador: estado, direção por fonte, tipo de ressalva, condição (quando houver), maturidade. O único caso que **não** é materializável — `inverte` — está corretamente barrado por P-K6, com a informação preservada no claim até o N2 v1.5 saber representá-la. Isso não é perda de significado; é recusa honesta de comprimir significado num molde que o schema atual não comporta. É a mesma disciplina da escada degradada da L-06.

## O ajuste V-K3 — correto

A precisão do Comentador está certa: exigir `sentido_do_achado` de fonte **exploratória que não materializa** seria transformar um requisito de qualidade do kit em pré-requisito de N1/N2. A opção preferida — direção obrigatória só para fontes que participam da materialização — mantém a exigência onde ela tem consequência estrutural e a declara como regra de kit onde é só qualidade. Correto, e evita que a validação futura leia ausência em exploratória como erro de materialização.

## Migração — correta

Não reescrever o corpus v1.2 retroativamente é a decisão certa, pela mesma razão que sustentei nas rodadas do kit: preencher P-K1/P-K2 num claim antigo seria **falsificar retroativamente uma decisão científica que não foi tomada no fechamento original**. A falha dura no momento da materialização (não antes) é a barreira no lugar certo — o claim só precisa estar completo quando tenta virar N1/N2.

## O que confirmo não ter sido importado indevidamente

Verifiquei que a v1.3 importou **apenas** `sentido_do_achado` e `grau_maturidade_cientifica` do v3.1, e **não** `relacoes_causais_declaradas`, `forca_causal`, `classificador_tipo_fonte`, `forca_biologica_conexao`, `dominios_grade_observados`, `origem_da_evidencia` nem `teste_conexao_fenotipo`. A regra do Comentador — "reutilizar vocabulário quando o conceito é comum; não importar estrutura só porque existe em outra trilha" — foi seguida. Importar esses eixos contaminaria o namespace clínico com semântica mecanística, e não foi feito.

---

## Subscrição formal

> **Subscrevo, sem ressalva, a minuta Schema-Claim v1.3 rev.2 (P-K1, P-K2, P-K3, P-K5, com o ajuste V-K3), como implementação no schema do que o contrato de saída rev.2 determina.**

Não reabri D1, não alterei N1/N2, não importei eixos mecanísticos — as três fronteiras que o encaminhamento marcou. A v1.3 é implementação, não norma nova; a vigência depende da dupla subscrição sem ressalva e do rito do operador.

---

*Verificações: enum de `sentido_do_achado` idêntico entre v1.3 e v3.1; cinco valores de `grau_maturidade_cientifica` idênticos entre v1.3, v3.1 e o enum do N2 v1.4 (+null no N2); `sentido_do_achado` posicionado dentro de `fontes[]` (por fonte); ausência dos sete eixos mecanísticos não importados; V-K3, V-K4, P-K6 lidos na minuta. N2 lido no projeto; demais artefatos recebidos no pacote, digitais declaradas nas trilhas 97/98.*
