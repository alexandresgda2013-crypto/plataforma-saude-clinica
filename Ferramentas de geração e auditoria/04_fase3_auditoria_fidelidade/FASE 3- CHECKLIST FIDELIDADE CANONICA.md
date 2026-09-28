# CHECKLIST DE FIDELIDADE CANÔNICA
## Rodada 3 (Consolidação) — portão final antes de uma Biblioteca virar Canônica

Mini-rodada PRÓPRIA e separada (quem gera/auditou não aplica este checklist no
mesmo turno). Reportar item a item: **SIM / NÃO + evidência**. Não corrigir —
reprovar e devolver à reconciliação (Etapa 6.5) ou à Rodada 3.

Documento novo, autônomo. Complementa (não substitui) o Checklist de Auditoria
Estrutural (forma) e o portão científico G1->G2->G3 (suporte).

---

## A. FIDELIDADE AO QUE FOI APROVADO

*Todos os claims passam por G1→G2→G3 e pela re-validação de consolidação. Apenas a revisão cega por um segundo avaliador independente é, nesta fase, restrita aos claims de alto risco (4 critérios), com extensão a todos prevista para a fase com equipe.

- [ ] **A1 — Frase tem lastro.** Toda frase declarativa de achado científico
      na Canônica possui ≥1 claim vinculado com status **aprovado** ou
      **aprovado_com_ressalva** (nada sustentado só por em_busca/rejeitado/aposentado).
      Claim **aposentado** foi válido no passado mas foi substituído por evidência
      melhor: NÃO serve de lastro sozinho. Se a frase ainda for pertinente, deve
      apontar para o claim substituto vigente, não para o aposentado.
      → Se NÃO: listar as frases órfãs (BLOCO + trecho).

- [ ] **A2 — Nada de rejeitado/pendente residual.** Nenhum trecho_ancora de
      claim **rejeitado** ou **pendente_evidencia** permanece no texto final
      sem modificação (foi removido/rebaixado/substituído na 6.5).
      → Se houver: listar os trechos residuais.

- [ ] **A3 — Zero citação nova na Rodada 3.** Nenhuma referência/PMID foi
      introduzida na consolidação que não tenha passado por G1->G2->G3
      (checar `origem_pipeline` e o log de reconciliação).
      → Se houver: citar e devolver (Rodada 3 não faz descoberta).

- [ ] **A4 — Log de reconciliação aplicado integralmente.** Toda ação
      REMOÇÃO/REBAIXAMENTO/SUBSTITUIÇÃO registrada na Etapa 6.5 tem efeito
      verificável no texto final (não ficou só no log).
      → Pendências: listar por claim_id.

## B. MARCAÇÃO DE INCERTEZA (nivelar a força textual)

- [ ] **B1 — Ressalva visível.** Todo claim **aprovado_com_ressalva** no texto
      carrega marcação textual de maturidade explícita (ex.: "evidência
      emergente sugere…", grau de maturidade/selo visível) — nunca apresentado
      com a mesma força de um claim muito estabelecido.

- [ ] **B2 — Selos de verificação por frase.** Toda afirmação factual tem
      `verification_status` propagado: [VERIFICADO] / [PRÉ-CLÍNICO] /
      [EXTRAPOLADO: condição] / [EMERGENTE]. Nenhuma frase humana depende só de
      evidência animal/outra condição sem declarar o limite.

- [ ] **B3 — Pré-clínico/extrapolado não viram afirmação humana.** Frase que
      afirma fato em seres humanos tem lastro humano; o que é animal/in vitro
      ou de outra doença está marcado e não sustenta a afirmação clínica sozinho.

## C. RASTREABILIDADE ESTRUTURAL

- [ ] **C1 — Mão-dupla texto ⇄ Módulo 09.** Toda citação (Autor, Ano)[tipo]
      tem registro (Nível 1) e vínculo (Nível 2); nenhum registro/vínculo ficou
      órfão no corpo (fora adições prospectivas marcadas).

- [ ] **C2 — Vínculos íntegros.** 100% dos vínculos têm trecho_ancora LITERAL
      (não resumo), status_auditoria preenchido e forca_causal preenchido;
      verificação do alto-risco com 2ª avaliação registrada quando aplicável.

- [ ] **C3 — Terminologia GRADE.** Em contexto mecanístico não há "GRADE A/B/C/D"
      como campo (usa forca_evidencia_afirmacao alto|medio|baixo); GRADE fixo do
      R04 aparece só no domínio clínico/intervenção (Zona 1E / recomendação).

- [ ] **C4 — Sem PMID/DOI no texto corrido** (RAG); classificador [tipo]
      consistente e único por tag.

- [ ] **C5 — Escopo preservado:** P20 (sem doses/cortes/protocolos operacionais
      na Biblioteca de Mecanismo; biomarcador por ID); P16 (neurogênese
      aprofundada só em B16); conteúdo terapêutico prescritivo ausente.



## D. SAÍDA / DECISÃO

VEREDITO (um):
- [ ] **APROVADO COMO CANÔNICA** — todos os itens A/B/C/E = SIM.
- [ ] **REQUER NOVA RECONCILIAÇÃO** — falha em A2/A4/B1/B2 (problema de texto):
      voltar à Etapa 6.5.
- [ ] **REQUER NOVA VALIDAÇÃO** — falha em A1/A3/C1/C2 (problema de
      lastro/suporte): voltar ao portão G1->G2->G3.
- [ ] **REQUER NOVA VERIFICAÇÃO (ANTI-AUTOCERTIFICAÇÃO)** — falha em E1/E2/E3:
      um selo de verificação foi promovido por ferramenta (g3_verificado_por
      inválido) ou há trecho truncado com veredito. Não se corrige por
      reconciliação de texto nem por re-leitura pontual: exige varredura
      SISTEMÁTICA de TODOS os vínculos com o mesmo padrão (g3_verificado_por
      vazio/"eutils"/"script", trecho sem fim de frase) em toda a Biblioteca.

Assinatura da rodada:
- aplicado por (sessão/operador): __________
- data: __________
- Biblioteca: B__ ____ (versão / audit_status)
- contagem final: frases verificadas __ / com ressalva __ / pré-clínicas __ /
  extrapoladas __ / removidas na reconciliação __

---

## E. REGRA DE AUTORIDADE DOS CAMPOS DE VERIFICAÇÃO (anti-autocertificação)
- [ ] **E1.** `g1_metodo` é SEMPRE ferramenta (eutils_automatico) — prova EXISTÊNCIA, não suporte.
- [ ] **E2.** `verification_status = "verificado"` só existe com `g3_verificado_por`
      preenchido por AVALIADOR (sessão humana/IA com abstract/full-text lido e registrado).
      Se `g3_verificado_por` contém "eutils"/"script"/"retrofit"/está vazio → NÃO pode
      ser "verificado" (gate reprova). G1 nunca promove a G3.
- [ ] **E3.** Vínculo com `trecho_ancora` truncado (não termina em fim de frase/tag)
      não pode ter status de G3 — reextrair a frase completa antes de julgar.
