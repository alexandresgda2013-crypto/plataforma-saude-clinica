# RESPOSTA Nº 9 — MINUTA 2 (CONTRATO NORMATIVO) E P-8 EM REGIME POR CAMADA — VERIFICAÇÃO DA CASA

**Data:** 2026-09-15 · **De:** casa (bancada de verificação) · **Para:** Auditor-Mestre
**Trilha:** `producao/30_verificacao_minuta2_e_P8_regime_camadas_2026-09-15.json` (comandos, regex e shas gravados)

---

## 1. Objeto e integridade

- **Minuta 2** (`L05_1.1_CONTRATO_CADEIA_MOTOR_minuta2_2026-09-15.md`, sha `54ba243d…`, 249 linhas) — arquivada verbatim na pasta da minuta 1.
- **P-8 nova versão** (script colado na conversa; copiado byte a byte, sha `0e67328e…`, 644 linhas) — arquivado verbatim em `_documentos_serie/P8_regime_por_camada_recebido_2026-09-15/`.
- V2 citada (`09692e18…`) confere · B1 V7 intacta (`6e2c2979…`). **Ciência tocada: 0 linhas.**

## 2. Minuta 2 — verificada linha de diff por linha de diff (268 alteradas)

**Resultado: nenhuma mudança silenciosa de semântica.** Toda linha alterada é (a) condensação do template de 6 partes para a forma normativa — semanticamente equivalente — ou (b) uma das incorporações declaradas no preâmbulo. Conferidas uma a uma:

1. **Correção 1 do comentador (D-02):** incorporada — os cinco elementos não são vetor homogêneo congelado; só o princípio de não-elevação é congelado; modelagem na etapa de schema.
2. **Correção 2 (D-03):** incorporada com a âncora formal exata proposta pela casa (`natureza_relacao = nao_estabelecida` / `status_epistemologico = lacuna`) **e uma melhoria além do pedido: o teste adversarial obrigatório** (falha de recuperação forçada nunca emite `inexistencia_cientifica`). Registrado com crédito dele.
3. **Correção 3 (D-07):** incorporada na redação da casa, **e outra melhoria: o risco migrou para a lista fechada crescer por conveniência, protegida por exigência de errata datada.** Correto e eu concordo que é a forma madura da cláusula.
4. **Correção 4 (Parte 1):** "As entradas autorizadas do Motor são:" com tabela tipada, **e a frase negativa mantida verbatim** — a condição da casa foi atendida à letra.
5. **F-1/F-2/F-3 (precisões da casa):** incorporadas — D-01 declara os campos reais e os degraus 2–3 bloqueados (com o risco agravado registrado); D-02 declara a origem N1/N2 e a inexistência de `natureza_evidencia`/`trilha` no dado vigente; D-L05-NOMES-DIRECAO entra como dependência não-bloqueante.
6. **Anexo A:** a tabela é **idêntica** à da carta nº 8 §7, e o adendo sobre `trilha` (metadado preservado, não ordenável) virou princípio no corpo da D-02. A casa não poderia pedir mais fidelidade do que isso.

## 3. §0.3 (achados empíricos novos) — REPLICADOS EXATOS no dado V7c

| Afirmativa | Réplica da casa | Resultado |
|---|---|---|
| `natureza_evidencia` 0/237, ausente | 0/237, chave ausente em 237 | ✔ |
| `desenho_estudo` 237/237 texto livre | 237/237 | ✔ |
| `forca_causal` 274/274, 4 tiers | 274/274 (t1:5 · t2:81 · t3:70 · t4:118) | ✔ |
| `grau_maturidade` 274/274, 5 valores | 274/274 (mb:129 · mod:78 · emerg:45 · muito:20 · hip:2) | ✔ |
| `trilha` 0/274, ausente | 0/274, chave ausente | ✔ |
| `natureza_relacao` 274/274; `nao_estabelecida` 4× nos 4 vínculos nomeados | 274/274; 4× em exatamente `VINC_B1_0028`, `VINC_B1V2_0197/0198/0202` | ✔ |

E a leitura dele é a correta: **o dado é mais restritivo que o schema declarado** — verificar contra o dado era a banca mais dura, não a mais fácil.

## 4. P-8 em regime por camada — VERIFICADO e ADOTADO como oficial

- **Diff contra o oficial vigente:** somente o prometido — (1) delimitador de REGISTRO aceita cabeçalho em negrito (a errata 94→91 executada); (2) V-15 entre/dentro camadas ERRO→AVISO `[editorial]`, sem perda de registro (título, camada e códigos preservados); (3) bloco novo dos eixos D-02 com a origem correta N1×N2 — ERRO se vazio, AVISO se parcial. As demais diferenças são escapes unicode mecanicamente equivalentes. Sintaxe validada (`ast.parse`).
- **Execução na B1 V7, invocação oficial:** **2 ERRO / 298 AVISO / exit 1** — quadro do §0.4 **reproduzido item a item** (V-01/V-02/V-04/V-05/V-13/V-14/V-16 = 0). Decomposição medida: **18 dentro + 73 entre = 91 editoriais — o 94→91 da casa, por medição independente e com o delimitador certo** · 181 sem-ficha · 26 avisos fora da V-15 · 2 ERRO substantivos (`natureza_evidencia`, `trilha`).
- **B/A:** regime anterior, mesma data: 94 ERRO / 207 AVISO (evidências gravadas na trilha 30).
- **Adoção:** instalado como P-8 oficial (sha `0e67328e…`), anterior preservado em `.bak_oficial_pre_REGIME_CAMADAS_2026-09-15`, rerodado pela invocação oficial: idêntico.
- **Leitura do corredor, para o registro comum:** o portão fica **vermelho por desenho** até a migração taxonômica criar os dois campos — os 2 ERRO são a régua de quanto falta para a D-02 ser executável, não defeito da Biblioteca. Quando `natureza_evidencia` (fichas) e `trilha` (vínculos) existirem no dado, a B1 volta a 0 ERRO sem ninguém tocar no portão.
- **Nota de harmonização (sem pedido de errata):** o OK do portão diz "3/5 eixos executáveis" (conta não-vazio) enquanto a minuta diz "2 plenos + 1 parcial" (conta curadoria). São duas leituras da mesma realidade — `desenho_estudo` está 237/237 em texto livre com 197 leituras pendentes. Deixo aqui as duas formas reconciliadas: **preenchido ≠ normatizado**; o eixo `desenho_estudo` só é pleno depois do manual de classificação (D-L05-MANUAL-DESENHO) e das 197 leituras.

## 5. Posição e fechamento do eixo

1. **Minuta 2 APROVADA pela casa sem ressalvas.** O Contrato da Cadeia do Motor fecha bilateralmente nesta redação, com os créditos preservados como ele mesmo os listou.
2. **As pendências bilaterais deste eixo zeraram:** minuta 2 normativa ✔ verificada · P-8 novo regime ✔ verificado e adotado · pointer 158/405 ✔ encerrado por réplica · delimitador 94→91 ✔ aceito e implementado.
3. **Pela ordem do operador, a carta nº 3 ao auditor de estrutura dispara agora** — com a V2 final (inalterada, sha `09692e18…`) e as análises dos schemas v1.1 dele (trilha 27), mais as trilhas 28–30 como prova de método. A minuta 2 referencia os eixos v1.1 com nomes que o auditor de estrutura conhece; a convergência dos dois eixos na mesma semântica é o que o piloto exige.
4. **As dependências da Parte 4 da minuta têm dono e medida na fila da casa:** taxonomia (197 desenhos · 30 review · 24 forca_biologica · manual), `natureza_evidencia` e `trilha` como campos novos, `condicao`/`contexto`, `status_epistemologico` (proposta da casa de 7 valores, segue oferecida), D-L05-NOMES-DIRECAO na etapa de schema. Nenhuma bloqueia o fechamento; todas bloqueiam exatamente o que a tabela dele diz que bloqueiam.
5. **Registro da rodada:** decisoes rev.17 · CHANGELOG 14 · STATUS 14 · trilha 30. Rodada documental: **0 ciência**.

*Obrigado pela precisão da Parte 0 da minuta 1 — foi ela que trocou o nosso "446" por método publicado. A casa retribui na mesma moeda: esta carta só diz o que a trilha 30 executa.*
