# MAPA DE AUTORIDADE E COMUNICAÇÃO — quem faz o quê na plataforma (2026-09-15, rodada 14)

**Pergunta respondida:** schema (auditor de estrutura) e Motor (Auditor-Mestre) são a mesma coisa?
**Não. São contratos de camadas diferentes da mesma cadeia — e já estão encaixados por verificação.**

---

## 1. A cadeia (onde cada um está)

```
Biblioteca Canônica (fonte da ciência)               → autoria: pipeline da casa + rodadas auditadas
  → Evidências/Vínculos (N1 fichas · N2 vínculos)    → contrato de DADOS: auditor de estrutura (L-05 v1.1 → 1.2)
    → NT (unidades narrativas)                       → contrato L-NT: a nascer (dono a definir na V2 §29)
      → Ontologia/Grafo                              → L-06: nasce depois do L-05 1.2
        → JSONs Modulares                            → transporte (derivados dos ítens acima)
          → MOTOR CLÍNICO                            → contrato de EXECUÇÃO: Auditor-Mestre (L-05 1.1, minuta 2 APROVADA)
            → Laudo (lê NT+JSONs; nunca a prosa)     → D-01…D-08 regem; P-8 vigia o estoque
```

- **O schema diz** *em que forma* o conhecimento está guardado (campos, enums, `$id`s).
- **O contrato do Motor diz** *o que pode ser computado e emitido* sobre esse estoque — e o que é
  proibido (nunca preencher lacuna, nunca elevar força, nunca escolher entre relações concorrentes).
- **Encaixe já medido (trilhas 27–30):** o contrato do Motor consome os campos do schema pelos nomes
  reais; o P-8 novo mede o acervo contra os campos do schema (2 ERRO = `natureza_evidencia` e
  `trilha` ainda fora do dado — apagam quando a migração v1.1 entrar).

## 2. Papéis das quatro IAs + humanos

| Quem | Produz | Não faz |
|---|---|---|
| **Auditor-Mestre** (projeto Claude 1) | contratos de execução (L-05 1.1), portões P-8/gate, defaults com método publicado | não toca schema de dados; não altera ciência |
| **Auditor de estrutura** (projeto Claude 2) | schemas de dados L-05 (N1/N2), critérios de aceitação do derivador | não toca o Motor; não altera ciência |
| **Agente Arena (a casa)** | **bancada de verificação**: réplica tudo que chega, de qualquer origem, antes de aceitar · derivadores/medições · portões da casa (checklist, framework, censo) · registro e créditos | não é autoridade de conteúdo: não cria dado científico, não fecha decisão sem trilha |
| **Comentador externo** (ChatGPT) | esclarecimentos e minutas a pedido do operador (ex.: rascunho da Arquitetura Consolidada, adotada após verificação), restrições de desenho (D-01/D-02) | não é autoridade final: suas peças entram pelo mesmo funil de verificação |
| **Claude de narrativas/anamnese** (projeto 3, free; adendo 2026-09-15) | **ferramentas de NT** (narrativas transversais, NT template) + restauração dos documentos de **anamnese** — camada sem dono até aqui | **não faz um segundo Motor**: a fase é de contrato e duas normas concorrentes são vedadas; sua versão free não sustenta a trilha reproduzível que a casa exige. Seu valor comparativo é o previsto na própria D-05: **revisor cego** das 20 unidades NT-B1 (regra do contrato, ≥90% nos 3 testes) |
| **Operador (você)** | decisão final, ponte entre os projetos um a um, dono da V2 | — |
| **Especialistas humanos (P-6)** | revisão cega do fim (fila 108/91 + casos nomeados) | instância do fechamento |

**Proveniência registrada:** a ARQUITETURA CONSOLIDADA V2 foi rascunhada pelo comentador externo a
pedido do operador e **adotada após verificação da casa** (146 IDs exatos, constantes de segurança,
pointer-ômega). Autoria não dispensa medição — e não a dispensou.

## 3. Regra de comunicação (o que manter)

1. **Ninguém fala direto com ninguém fora da ponte.** O operador repassa artefatos formais um a um.
   É o que preserva a auditoria mútua sem contaminação — e foi ela que achou os erros reais desta
   semana (F-1: o mestre não tinha os schemas; errata 446; delimitador 94→91).
2. **A conversa acontece no papel:** cada contrato cita suas dependências do outro lado **pelo nome**
   (V2 §5.1/§5.2 cita os `$id`s do schema; o Contrato do Motor cita os enums do v1.1; o P-8 mede os
   campos dele). Se um documento precisar de algo que o outro não entregou, vira **dívida nomeada**,
   nunca suposição silenciosa.
3. **Tudo que chega é verificado pela casa antes de valer** — inclusive quem concorda com a casa.
   Medida sem comando gravado não vale (norma da casa, rodada 13).
4. **Crédito preservado em cada peça** (quem propôs o quê), para que nenhuma das quatro partes
   herde a autoria da outra por acidente.

## 4. Estado agora e próximos passos

1. **Ao mestre:** falta o operador repassar o **ADENDO 1 + kit v1.1** (3 arquivos da pasta
   `L05_v1.1_recebido_2026-09-15/` + adendo da carta 8) — é a causa-raiz curada do F-1.
2. **Ao estrutura:** pacote pronto → `_documentos_serie/ENVIO_AUDITOR_ESTRUTURA_2026-09-15/`
   (carta 3 com fecho + V2 + trilhas 27/30). Aguardamos 4 respostas de 1 linha.
3. **Quando as 4 linhas chegarem:** a casa verifica e o **L-05 1.2-normativo** pode ser escrito
   (autoridade: auditor de estrutura; verificação: casa) — última peça antes da migração dos dados,
   que apaga os 2 ERRO do P-8 por construção.
4. **Depois:** L-06 (ontologia) e L-NT, na ordem das fases da V2. Piloto B1 vertical; multidomínio só
   com IDs do catálogo (146 válidos).
5. **P-6 (humano)** continua instância do fim — nada neste mapa substitui a revisão cega.
6. **Claude 3 (narrativas/anamnese):** terminar a atualização das ferramentas dele e **colher só os
   artefatos** (NT template, anamnese) — documentos entram pela ponte, conversas não se importam.
   Critério para migrar o trabalho para instância paga no futuro: só se a produção pesada da NT-B1
   travar no free; aí migram os documentos, nunca as conversas.
7. **Kit da trilha clínica (5 documentos: SCHEMA-CLAIM v1.2 · COMO EXECUTAR v1.7 · LISTA CANÔNICA
   B1/SM-02 v1.3 · BLOCO DE ESTADO v1.6 · PROTOCOLO DE ESCOPO B1 v1.3):** dívida do operador
   vencendo agora — causa-raiz do caso `uso` (§9 da v1.1), régua dos anexos do 1.2 e da tipagem de
   risco da D-08. Destino: arquivamento e medição na casa + repasse ao mestre pela ponte.

---

*Documento de governança da casa. Todos os fatos citados têm trilha (25–30) e sha publicados;
qualquer número desta página se reproduz com os comandos gravados nelas.*
