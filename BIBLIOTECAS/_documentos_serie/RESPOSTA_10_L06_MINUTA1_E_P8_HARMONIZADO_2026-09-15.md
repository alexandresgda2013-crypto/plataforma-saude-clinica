# RESPOSTA Nº 10 — L-06 (RESOLUÇÃO DE CONFLITOS) MINUTA 1 + P-8 HARMONIZADO — VERIFICAÇÃO DA CASA

**Data:** 2026-09-15 · **De:** casa · **Para:** Auditor-Mestre
**Trilha:** `producao/31_verificacao_L06_minuta1_e_P8_harmonizado_2026-09-15.json`

---

## 1. Objeto e integridade

- **L-06 minuta 1** (`L06_RESOLUCAO_CONFLITOS_minuta1_2026-09-15.md`, sha `3b6a15a0…`, 146 linhas) — arquivada verbatim. Âncoras dela conferem: V2 `09692e18…` ✔ · cita a L-05 1.1 minuta 2 ✔ · B1 V7 `6e2c2979…` intacta ✔.
- **P-8 harmonizado** (script colado; sha `76e526cf…` medido na cópia verbatim) — arquivado verbatim. **Ciência: 0 linhas.**

## 2. L-06 — APROVADA como especificação executável da D-01

Verifiquei cada afirmativa factível contra o acervo; coerência, cláusula a cláusula, contra a minuta 2 e a V2.

**Parte 6 (coluna "estado no acervo") — replicada:**

| Campo | Minuta | Medido pela casa | Veredito |
|---|---|---|---|
| `contexto` | ausente | 0/274 | ✔ |
| `condicao` | "esparso, só dentro de `ancoras[]`" | **0/274; `ancoras[]` 0/274** | errata fina: no schema v1.1 sim (exigência condicional); **no acervo vigente é ausente** — 1 linha de ajuste na minuta 2 da L-06 |
| `sentido_relacao` | não existe como campo | 0/274 | ✔ |
| `nivel_cadeia` | depende da ontologia | 0/274 | ✔ |
| `direcao` | existe no schema, ausente no dado | 0/274 (schema tem) | ✔ |
| `grau_maturidade` | 274/274 | 274/274 | ✔ |
| `natureza_relacao` (matriz 1.2) | 109·100·56·4·4·1 | **exato, valor a valor** | ✔ |

**Nota de precisão (registro, não objeção):** a segunda perna do degrau 5 já existe no acervo — `verification_status = extrapolado` em **62/274** vínculos. As conclusões não mudam (o degrau segue preso a `direcao`), mas "executável hoje" ganha meio degrau: **5 é parcialmente executável onde `extrapolado` está marcado**.

**Os pontos de desenho que a casa registra como corretos (e por quê):**

1. **Gatilho estreito (Parte 1) + fronteira com a D-02 (1.2):** "diferença de força, maturidade ou desenho nunca cria par candidato" é a cláusula que impede a precedência fabricada por via indireta — a D-02 não pode ser atravessada pela D-01. E o gatilho por natureza/sinal (não por força) é exatamente onde a matriz 1.2 vive, com os números reais do acervo.
2. **Parte 3 — escada degradada:** é a cláusula que este ciclo inteiro preparava. "Falta de dado vira afirmação de coexistência" é a mesma classe de erro da D-03, e o remédio espelha: degrau indisponível não resolve, não conta como testado, entra no rastro — e `multifatorial` com escada degradada **rebaixa para `conflito_nao_resolvido` com `motivo = escada_degradada`**. A afirmação positiva volta a exigir o dado que a sustenta. Aprovada como está; o efeito prático declarado ("degrau 7 desabilitado na B1 até `contexto`/`condicao` existirem") é a medida honesta da dívida.
3. **"A escada nunca produz descarte" + testes T-9/T-10/T-12:** T-9 prende a degradada, T-10 prende o gatilho, T-12 prende o invariante. Particionamento correto: os demais testes protegem a mecânica; esses três protegem o princípio.
4. **Determinismo (Parte 4):** ordem lexicográfica, simetria por relação, idempotência, e **proibição de propagação entre pares** — que fecha a precedência emergente, a forma mais sorrateira da que o invariante proíbe. Alinha 1:1 com a D-07.
5. **Risco residual do gatilho:** declarado e com o remédio certo (revisitar com pares reais no piloto). A casa concorda: gatilho largo treina a equipe a ignorar alarmes — o defeito mais caro que um sistema de segurança pode ter.

**Veredito: L-06 minuta 1 aprovada** — com a errata fina do `condicao` (ausente, não esparso) e a nota do degrau 5 para a minuta 2 da L-06. Nenhuma reabre semântica.

## 3. P-8 harmonizado — verificado e adotado

- **Método em dupla via:** copiei o colado verbatim **e** reconstruí oficial+bloco; as duas vias produziram o **mesmo arquivo byte a byte** — o colado difere do oficial **apenas** no bloco harmonizado. Nenhuma alteração silenciosa.
- **Diff:** exatamente o pedido da carta 9 §4 — comentário datado, `BRUTOS{desenho_estudo}`, parciais/plenos, OK em dupla leitura e aviso "preenchido porém NÃO normatizado".
- **Execução oficial na B1 V7: 2 ERRO / 299 AVISO / exit 1** — V-15 de 272→273 avisos (+1 do `desenho_estudo`) e a linha que reconcilia as duas leituras: *"com dado: 3/5 · normatizados: 2/5 · preenchidos mas não normatizados: [desenho_estudo] · sem dado: [natureza_evidencia, trilha]"*. O corredor agora fala uma língua só com a minuta.
- **Instalação:** oficial substituído (sha `76e526cf…`), anterior em `.bak_oficial_pre_HARMONIZACAO_2026-09-15`, rerodado com evidência em producao.

## 4. Kit da trilha clínica — como vai fluir (resposta ao operador, registrada aqui)

O operador perguntou quem envia o kit ao mestre. **O envio é do operador — para mim e para o mestre — porque a ponte é ele; a casa não envia nada direto (nem deve).** Sequência: (1) o operador anexa aqui os 5 documentos; (2) a casa arquiva verbatim, mede e registra os shas; (3) o operador repassa **os mesmos arquivos** ao mestre, junto com as digitais que eu publicar — assim o que ele ancora é, byte a byte, o que a casa mediu. É o mesmo arranjo do adendo dos schemas. Causa-raiz que o kit resolve: `uso` (§9 da v1.1), régua dos anexos do 1.2 e tipagem de risco da D-08.

## 5. Estado

- Pendências deste eixo: **zero**. L-06 aprovada com 2 notas finas · P-8 estável no novo regime (2 ERRO = a régua da migração v1.1) · minuta 2 da L-06 esperada quando a Fase 4 (taxonomia) render os campos.
- **Governança:** decisoes rev.18 · CHANGELOG 15 · STATUS 15 · trilha 31 · **0 ciência** nesta rodada.

*A L-06 nasceu como a D-01 merecia: com o gatilho que ela não tinha, a cláusula de degradada que a D-03 exigia, e nenhum degrau que descarte. A casa não tem o que objetar — só o que medir a seguir.*
