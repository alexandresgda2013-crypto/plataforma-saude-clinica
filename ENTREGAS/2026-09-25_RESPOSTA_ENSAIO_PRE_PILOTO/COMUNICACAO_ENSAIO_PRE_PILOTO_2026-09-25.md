# COMUNICAÇÃO AO ARENA CASA, AUDITOR-MESTRE E AUDITOR-ESTRUTURA

## Assunto: Ensaio operacional pré-piloto do B1.SM02.014 e posterior transferência para a tríade operacional dedicada

Após o fechamento e a entrada em vigência das três bases atuais do processo:

* **Contrato de Saída do Claim Kit rev.2** — `841532da`
* **Schema-Claim v1.3 rev.3** — `28cbc9c7`
* **COMO EXECUTAR v1.10** — `49514344`

decidimos realizar uma etapa intermediária antes da execução do piloto oficial do claim **B1.SM02.014**.

### 1. O que será feito agora

Será realizado um **ensaio operacional pré-piloto** utilizando as IAs que participaram diretamente de toda a construção, discussão, correção e auditoria das versões atualmente vigentes.

A razão é objetiva: essas IAs conhecem o histórico completo do processo.

Elas acompanharam, entre outras etapas:

* a evolução do v1.9 para o v1.10;
* C-1 a C-5;
* a necessidade de independência e cegamento;
* o fechamento conjunto;
* a separação entre parecer e fechamento;
* D1 e sua resolução;
* P-K1, P-K2, P-K3 e P-K5;
* V-K6 e V-K7;
* as travas de materialização;
* as interfaces entre Claim, Schema e N1/N2;
* as rodadas de auditoria e as falhas que foram encontradas e corrigidas durante a construção.

Por conhecerem esse histórico, elas não constituem a população adequada para serem consideradas, desde já, a tríade **cega e independente do piloto oficial**.

Por outro lado, justamente por conhecerem todo o processo, são o grupo mais adequado para realizar primeiro um **ensaio de funcionamento do conjunto de ferramentas, documentos, instruções e interfaces operacionais**.

### 2. O objetivo desse primeiro exercício

O objetivo não é validar novamente as normas.

Também não é reabrir decisões já encerradas.

O objetivo é descobrir eventuais problemas de **execução prática** que não aparecem necessariamente numa auditoria documental.

O ensaio deverá verificar, por exemplo:

* se os pacotes de entrada estão completos e coerentes;
* se os documentos vigentes são corretamente interpretados;
* se a organização dos arquivos funciona na prática;
* se a sequência operacional é clara;
* se o claim e o corpus chegam corretamente a cada ambiente;
* se as etapas G1, G2 e G3 são executáveis sem ambiguidade;
* se as três análises conseguem ser produzidas separadamente;
* se o retorno e a comparação entre análises funcionam conforme o v1.10;
* se o fechamento consegue produzir as decisões exigidas pelo Contrato de Saída;
* se há alguma dificuldade operacional que precise ser corrigida antes de entregar o processo ao grupo dedicado.

Em outras palavras:

> **primeiro testaremos se a máquina funciona; depois colocaremos a máquina em operação com a equipe dedicada.**

### 3. O que esse ensaio não significa

O ensaio não substitui o piloto oficial.

Ele também não autoriza alteração automática de:

* Contrato de Saída rev.2;
* Schema-Claim v1.3 rev.3;
* COMO EXECUTAR v1.10;
* N1;
* N2.

Caso apareça um problema, primeiro será classificado como:

**problema operacional de execução**
ou
**problema real de norma/contrato**.

Somente o segundo tipo poderá justificar uma abertura formal de novo ciclo documental.

Portanto, nenhum ajuste será feito silenciosamente durante o ensaio para “fazer funcionar”.

### 4. Como o ensaio será organizado

A estrutura pretendida é:

```text
B1.SM02.014
      ↓
descoberta bibliográfica
      ↓
consolidação das listas
      ↓
corpus do ensaio
      ↓
execução com as IAs que participaram da construção
      ↓
comparação do comportamento real
      ↓
registro dos problemas operacionais
      ↓
correções de pacote/processo, se necessárias
      ↓
pacote final congelado
      ↓
tríade operacional dedicada
      ↓
PILOTO OFICIAL B1.SM02.014
```

A parte de descoberta bibliográfica poderá utilizar o fluxo que já está sendo estruturado pelo operador, incluindo Consensus, PubMed e ferramentas de recuperação de texto completo.

A lista obtida dessas ferramentas será tratada como **pool de descoberta**.

Depois haverá consolidação e desduplicação.

A partir do momento em que o corpus do piloto for congelado, todas as IAs da execução oficial receberão o mesmo corpus-base.

### 5. Independência continua sendo obrigatória no piloto oficial

O fato de o ensaio preliminar ser realizado pelo grupo que conhece todo o histórico não altera a regra do piloto oficial.

Quando chegar a execução oficial, a tríade dedicada será:

**IA 1 — ChatGPT dedicado**
**IA 2 — Arena dedicado**
**IA 3 — Claude dedicado**

e cada uma deverá receber seu pacote de entrada sem acesso às análises produzidas pelas outras.

A finalidade é preservar o desenho estabelecido no COMO EXECUTAR v1.10:

```text
IA 1 → análise independente
IA 2 → análise independente
IA 3 → análise independente + parecer
        ↓
comparação posterior
        ↓
retorno às IAs 1 e 2
        ↓
fechamento conjunto
        ↓
decisões do Schema/Contrato
```

Portanto, o conhecimento histórico deste primeiro grupo será usado **para testar a operação**, e não para contaminar a independência da futura execução oficial.

### 6. O papel de cada um durante esse ensaio

Durante esta etapa, o Arena Casa, o Auditor-Mestre e o Auditor-Estrutura estarão temporariamente envolvidos no exercício porque são os agentes que conhecem integralmente a construção e conseguem identificar rapidamente inconsistências de operação.

Isso é uma **atribuição transitória para o ensaio**.

Não haverá mudança permanente de território.

Após o encerramento dessa etapa:

* o **Auditor-Estrutura** retorna ao seu território de estrutura, schema e materialização;
* o **Auditor-Mestre** retorna ao seu território de governança, contrato, auditoria e execução do protocolo;
* o **Arena Casa** retorna ao seu papel anterior de bancada/confronto e governança do processo;
* a execução rotineira dos claims passa para o grupo dedicado de **ChatGPT + Arena dedicado + Claude dedicado**.

### 7. O que esperamos obter

Ao final do ensaio, deverá existir um registro objetivo contendo:

**o que funcionou;**
**o que apresentou dificuldade;**
**o que foi apenas problema de pacote ou instrução;**
**o que eventualmente exigiria novo ciclo normativo;**
**e quais condições devem ser congeladas para o piloto oficial.**

O resultado do ensaio não deverá produzir uma nova interpretação científica do `.014` por consenso entre as IAs.

Ele deverá produzir principalmente uma resposta para a pergunta operacional:

> **“Com as ferramentas, documentos e pacotes atuais, conseguimos executar o COMO EXECUTAR v1.10 de ponta a ponta sem introduzir erro de processo?”**

### 8. Encerramento da fase de transição

Depois que essa pergunta estiver respondida, o conhecimento operacional obtido será transformado em **pacotes finais de entrada** para as três IAs dedicadas.

A partir daí, o grupo atual deixa de atuar como executor permanente e retorna integralmente às suas funções anteriores.

O piloto oficial B1.SM02.014 será então executado com o desenho congelado, com separação entre:

**descoberta bibliográfica → corpus congelado → análises cegas independentes → comparação → fechamento → auditoria.**

Essa separação é importante porque permite testar primeiro a ferramenta e, em seguida, testar de fato o método independente que acabou de ser aprovado.

## Decisão operacional

Fica, portanto, aberta a seguinte sequência:

**1. Ensaio operacional pré-piloto com o grupo que participou da construção.**

**2. Registro dos problemas e ajustes exclusivamente operacionais que forem necessários.**

**3. Congelamento dos pacotes das três IAs dedicadas.**

**4. Execução do piloto oficial B1.SM02.014 pela tríade independente.**

**5. Retorno do Arena Casa, Auditor-Mestre e Auditor-Estrutura aos seus territórios originais.**

Nenhuma das três bases normativas vigentes será modificada apenas porque o ensaio foi aberto. Qualquer necessidade de alteração normativa deverá seguir um novo ciclo formal.

O objetivo agora é simples: **testar o sistema em ambiente real antes de colocar a execução definitiva nas mãos da tríade dedicada.**
