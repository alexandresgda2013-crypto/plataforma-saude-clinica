# RELATÓRIO DE EXECUÇÃO [AT] B6 — 2026-09-08
**V1 → V2 aplicada** (decisão do usuário: aplicar completo, padrão B5 — sem extrapolação, selos honestos)

## Resultado
- **Canônica:** `B6 ESTRESSE OXIDATIVO V2 CANONICA.md` — **10.126 palavras** (V1: 7.571; arquivada em `producao/historico/v1_canonica_2026-09-08.md`).
- **Refs:** 36 → **108** (+72 auditadas ref a ref; 0 falso-positivo; overlap com vigente: 0).
- **Grupos [AT]:** ENZ 33 (enzimologia CBS/CGL/transulfuração/H₂S) · B6DEF 9 (deficiência animal; Cabrini/Lima) · ANTIOX 11 (ação direta, selada [APENAS PRÉ-CLÍNICO]) · GSH 8 (contexto glutationa) · HUM 8 (dieta/observação/sinais) · NEG 2 (NORVIT, WAFACS) · HIP 1 (Kato/Nrf2, [G1]).
- **Regras fixadas:** B6.R01–R09 em CONTROVÉRSIAS (causalidade por seta; "B6 aumenta GSH" proibido; revisão≠ensaio; observacional≠causal; Nrf2=hipótese; CONTEXT≠claim; não-mamífero=EXC; vitâmeros não-intercambiáveis + pró-oxidante honesto; fronteiras B1/B4/B8/B9).
- **Tabela de evidências:** +4 linhas (bioquímica estrutural; animal causal; humano dieta/obs; vitamina B como sonda NEG).
- **Apêndice:** +72 rótulos em 4 listras UPPERCASE (TAOKA_1999b misto, padrão série).

## Arquivos tocados
| Artefato | Estado |
|---|---|
| Canônica V2 | NOVA (10.126 palavras; 6 inserções + regras + nota + tabela + apêndice + cabeçalho/fecho) |
| `Evidencias/Bibliografia/01_pmids.json` | 36→108 (doi em 70/72 novos; Kannan/Wondrak sem DOI capturado) |
| `Evidencias/Vinculos/vinculos_referencia_afirmacao.json` | 36→108; mecanismo_origem bugado dos 36 vigentes corrigido |
| `Auditoria_B6/ledger_auditoria_B6.json` | 36→108 (AUD_B6_0037..0108; abstracts anexados; 2 sem-abstract com G3 por título/periódico) |
| `_manifesto_biblioteca.json` | v2; pmids 108; g1/g2/g3; historico_correcoes+1; atualizacoes_pos_publicacao+1; vinculos_n2 19→108 |
| `04_atualizacoes_literatura.json` | [] (mantido) |
| `producao/04_AT_ciclo_2026-09-08.json` | trilha completa do ciclo (incorporadas, resgates, EXC, BAIXO, NAO-IDX, correções) |
| `Auditoria_B6/decisoes_B6.md` | bloco [AT] completo (pipeline, correções, portões, pendências) |
| `Auditoria_B6/fidelidade_canonica_P4_B6.md` | ADENDO V2 — 15/15 SIM |

## Correções de dado no ciclo
1. Framework pegou 3 citações órfãs → refs renomeadas ao **ano epub oficial** com print documentado: Banerjee 2004 (print 2005), Sbodio 2018 (DEP 20180823, print 2019), Pusceddu 2019 (DEP 20190525, print 2020).
2. Alias 'Bønaa' (ø não decompõe em NFKD; casamento oficial).
3. `mecanismo_origem` bugado da V1 corrigido nos 36 vínculos.
4. Rótulos normalizados: Bonaa_2006, Vandeneynde_2021.

## Portões oficiais
- ✅ `gate_script.py` (P-5): **APROVADO — 108|108** (INFO[6] = ressalva P-6 padrão da série)
- ✅ `validar_auditoria.py` (framework, caminhos relativos de dentro da pasta): **0 ERRO** (avisos não-bloqueantes)
- ✅ `checklist_entrega.py B6`: **41/41**
- ✅ Varredura `\b\d{7,9}\b` na canônica: **0**
- ✅ Tríade ID-cruzada: 108|108|108, trechos-âncora literais

## Pendências declaradas
- **P-6** (2ª verificação cega, Via 2 — inclui a leva [AT] B6): PENDENTE, não autocertificável; registrada em ledger, vínculos, manifesto, decisoes e P-4.
- **[G1]** Itoh 2024 (âncora neuronal SH-SY5Y; periódico não indexado — sem fonte inventada); Nrf2 selado como hipótese (Kato 2026); polimorfismos CBS/CGL↔psiquiatria = zero na coleção [G1].

_Rodada da série: B1 V4 ✅ · B2 V2 ✅ · B3 V2 ✅ · B4 V2 ✅ · B5 V2 ✅ · **B6 V2 ✅** — 6/16._
