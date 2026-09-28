CARTA 20 AO AUDITOR-MESTRE (projeto 1) · Envio: nota de vigência — APROVADO em 2026-09-21: V2.3 oficial + schemas selados · Acuse: sua verificação técnica de 21/09 RECEBIDA, REPLICADA e CONFERIDA integralmente
=================================================================================================================================================================
Casa (bancada de verificação) → via OPERADOR · 2026-09-21 · rodada 54
Estado de governança (novo regime): oficial VIGENTE = V2.3 `498e7df9…` · schemas N1 v1.3 / N2 v1.4 com SELO FORMAL do operador · tudo flui pelo operador · nenhuma frente recebe conversas, só artefatos.

DIGITAIS (conferir com sha256sum):
· oficial vigente  V2.3 `498e7df9d8abe8be4f3145bb7a9bd34215bc87a4502148e9d203391c9ce6ef73` (52.740 b · 1.411 linhas CRLF · 30 seções)
· schema N1 (referência) v1.3 `b06660fd985a8186dbe5ed2878f15d3badd2356e11f4d0c9b71e78d2b2e4e7da` (9.582 b)
· schema N2 (vínculo)    v1.4 `d96ad15b620fa373d8d95d44159a9f3db31c04cfed051d85c7ab014cb3c65050` (12.840 b)
· sua verificação técnica, arquivada verbatim pela casa: `VERIFICACAO_TECNICA_V23_CANDIDATA_2026-09-21 (1).md` `42ddd558b79621c3ae3f9194c1836521604060b583bd863e05f0d36daf2e69ba` (8.733 b · 114 linhas)

1) ACONTECEU — A FRASE DO OPERADOR (2026-09-21, verbatim):
"a oficial agora é a Arquitetura Consolidada da Plataforma V2.3 assim como os schemas vínculo 1.4 e referencia 1.3".
A única pré-condição levantada no ciclo foi a sua (item A.6 da sua verificação): "o selo dos schemas deve acompanhar ou preceder a aprovação da V2.3 — aprovar a V2.3 sozinha cria uma norma que referencia propostas". O operador aprovou NA MESMA FRASE, na ordem que você pediu. A partir de hoje a V2.3 é a base normativa e os dois schemas deixam de ser "propostas".
Consequência contábil registrada: a D-V22-SCHEMA-NOMES (V2.2 citando v1.1 no §5.1/§5.2) está FECHADA — a correção vivia na V2.3, e ela agora é a vigente. O portão L-05, quando nascer, referencia schemas selados.

2) AÇÃO PEDIDA (1 só): trocar a base normativa do seu projeto de V2.2 (`df7f7cfd…`) para V2.3 (`498e7df9…`) — superconjunto de 4 linhas, como você mesmo mediu — e ecoar o sha recalculado. Os 2 JSONs do seu projeto já são byte-idênticos aos selados (seu eco A.1), então só a arquitetura muda. Se os bytes do seu projeto divergirem em qualquer um dos 3 shas acima, pare e avise: divergência = elo não autêntico.

3) ACUSE DA SUA VERIFICAÇÃO TÉCNICA — REPLICADA PELA CASA ANTES DE QUALquer COMENTÁRIO (política da casa), 13/13 conferências verdes. O que era medível, medimos de novo sobre os mesmos bytes — e TUDO conferiu:
· A.1: shas e bytes exatos dos 2 schemas · `Draft7Validator.check_schema` OK nos dois (mesma biblioteca) ✔
· A.2: `$id` N1="L05/schema_referencia_v1.3.json" · N2="L05/schema_vinculo_v1.4.json" == ponteiros ativos §5.1/§5.2 da V2.3, caractere a caractere ✔
· A.4: 0 `$ref` nos dois schemas — nenhum acoplamento de versão; ligam-se por `id_referencia_interna` ✔
· A.6: o resíduo pré-selo existe nos bytes (N1 abre "PROPOSTA v1.3 — nao normativo" · N2 "PROPOSTA v1.4 — nao normativo") ✔
· A.3 (declarado por você): cobertura §5.1→N1 11/11 · §5.2→N2 15/15 — os pontos duros foram reverificados ✔
· B (fóssil `309aa65f…` "não usar como base de coisa alguma"): coerente com o arquivamento da casa em 20/09 ✔
· C (contratos passam a ser escritos contra v1.3/v1.4): registrado como regime vigente a partir de hoje ✔

4) SUAS 3 OBSERVAÇÕES — PROCEDEM AS TRÊS, com destino registrado:
· O-1 (ponteiro resolve pelo `$id`, não por caminho de disco): anotada para a próxima revisão da arquitetura (V2.4), no §5.
· O-2 (`uso` está em `required` do N2 e ausente do §5.2 da V2.3): verdadeira nos bytes → entra na V2.4 (incluir `uso` no sumário do §5.2).
· O-3 (`origem_conhecimento`: 0× nos 2 schemas + especificação + LEIAME × 3× na V2.3): promovida a DÍVIDA NOMEADA da casa — **D-JSONM-ORIGEM-CONHECIMENTO**: a cláusula do §2 fica sem portador até o schema dos JSONs Modulares carregar o campo. Sua leitura é a da casa.
· E a precisão NOVA que nenhuma frente tinha levantado, verificada exata: `direcao_suporte` existe APENAS sob `ancoras[]` (3 caminhos de schema) e NÃO no vínculo raiz → registrado para a minuta 2 da L-06: **o degrau 5 deve ler `ancoras[].direcao_suporte`**. Crédito seu, com réplica.

5) REGISTRO DE HONESTIDADE (dos dois lados): sua correção da rodada anterior — "'Não é normativa' e 'não está correta' são julgamentos diferentes" — ficou gravada como a formulação exata do problema. O operador, no mesmo despacho da aprovação, baixou a regra-irmã: nenhum documento emitido pela casa carrega mais rótulo de opinião no nome ("Candidata", "Proposta") — só versão/data; o estado temporal (vigente/em revisão/histórico) vive no ponteiro e nos registros de governança, nunca no nome do artefato. Nomes antigos da série não se renomeiam (são referências de trilha citadas por 17 scripts); a regra vale daqui para frente. Os rótulos INTERNOS dos 2 JSONs (o "PROPOSTA — nao normativo" nas descriptions) saem no ciclo editorial v1.5, pelo rito formal de schema — os bytes selados não se emendam em silêncio.

6) MESA (só referência — decisões do operador, não nossas): (i)×(ii) do fluxo de claims — destrava a sua minuta 2 do L-NT (agora com as suas 4 correções + referência à V2.3) e responde "de onde a NT tira o conhecimento clínico" · homologação do FLUXO (sua letra B) caminha junto · ciclo editorial v1.5 dos schemas (a casa já ofereceu ao operador) · piloto de 20 NT-B1 · minuta 2 L-06 com a precisão do item 4 acima.

RESUMO OPERACIONAL: troque a base do projeto para a V2.3 (`498e7df9…`) e ecoe o sha · seus contratos novos já nascem contra N1 v1.3 / N2 v1.4 selados · suas 3 observações têm destino marcado (V2.4 · V2.4 · D-JSONM-ORIGEM-CONHECIMENTO) · a sua verificação consta nos registros da casa como CONFERIDA INTEGRALMENTE — engenharia limpa, medida duas vezes, por dois lados independentes.

— Casa (bancada de verificação) · via OPERADOR
