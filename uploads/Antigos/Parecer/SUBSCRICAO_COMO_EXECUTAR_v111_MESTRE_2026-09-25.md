# SUBSCRIÇÃO TERRITORIAL — COMO EXECUTAR v1.11 (paradas E-04)

**Auditor-Mestre · 2026-09-25**
**Objeto:** minuta `COMO EXECUTAR v1.11` — sha `ef27f8b3a492cd2f667b8892ec99603e57a5b22f46f5797e52705293d004fc66` (confere com TRILHA105)
**Verificado contra:** v1.10 vigente `49514344…` (subscrito) · meu registro de execução do ensaio de 25/09 (E-04)

---

## RESPOSTA: **SUBSCREVO SEM RESSALVA**

A v1.11 corrige o E-04 — o defeito que eu próprio observei ao executar o ensaio — com a menor alteração possível, e sem tocar em nada que eu já havia subscrito no v1.10.

## 1. As paradas preservam o cegamento e a comparação (C-2/C-3)

Sim, e o mecanismo é o correto. A v1.11 insere `⛔ PÁRA` **entre cada entrega**, de modo que a IA 2 não pode começar antes de a IA 1 ter entregado e parado, a IA 3 não pode começar antes das duas, e a comparação só ocorre `COM COMANDO DO OPERADOR`. Isso **fortalece** o C-2, não o altera: a cegueira do v1.10 dependia de as janelas não se verem; a v1.11 torna isso executável ao impedir que uma janela **corra sozinha até o fim**. O C-3 (confirmo/altero/mantenho, sem apagar as análises originais) permanece no passo 5, agora protegido por uma parada antes e outra depois.

## 2. O comando do operador entre etapas protege o rito — não o enfraquece

Esta é a pergunta que mais me interessava, e a resposta é que **protege**. O risco teórico seria o operador virar um gargalo humano que pudesse influenciar as análises. Não é o caso: o comando entra **entre** entregas já feitas, não durante uma análise. Cada IA decide sozinha e entrega; o operador só autoriza a **transição** para a próxima etapa. O operador comanda a sequência, não o conteúdo — "quem entrega, quem compara, quem abre o fechamento", nunca o que cada uma conclui. É exatamente a função que impede a ancoragem: sem a parada, uma janela lê a anterior e ancora; com a parada, a leitura mútua só acontece depois que as três já se comprometeram por escrito. O comando humano aqui é o **cadeado da cegueira**, não uma decisão científica.

## 3. A nota E-04 é fiel ao que o ensaio observou

Confirmo, porque fui eu quem observou. A nota diz: *"uma janela corre até o fim e faz G1+G2+G3 de uma vez, quebrando o cegamento e a comparação"*. É a descrição exata do que registrei no meu `EXECUCAO_ENSAIO_014` de 25/09 — o rito é executável, mas nada no v1.10 impedia uma IA de emendar as três etapas numa tacada, o que anularia a comparação. A v1.11 nomeia isso como E-04 e o corrige com a parada explícita. A classificação está certa: **é problema operacional** (o rito precisava de um freio de sequência), **não normativo** (G3, portões e as 4 decisões não mudam). A errata do ensaio (§9) exigia exatamente essa classificação, e ela foi respeitada.

## 4. Nenhuma frase nova contradiz o protocolo de 3 IAs do v1.10

Verifiquei os dez elementos que subscrevi no v1.10, um a um, no texto da v1.11: IA 3 emite parecer e não fecha; fechamento conjunto; C-2 (SOZINHA, sem ver); C-3 (confirmo/altero/mantenho); C-4 (fonte primária, nunca votação); C-5 (ressalvas preservadas); X-1 (divergência cega = funcionamento correto); a frase morta do v1.9 ("segunda inspeção sobre a análise da IA 1") **não** voltou; 4 decisões; portões §8. **Os dez presentes, nenhum contradito.** O corpo fora do cabeçalho e da sequência é idêntico ao v1.10 (T6: 27.667 = 27.667 caracteres), então a única mudança é a sequência de paradas — que é aditiva, não substitutiva.

## Sobre o ajuste de T3 do Comentador

O reforço que o Comentador pediu — o T3 verificar a **ordem** ENTREGA→PÁRA→COMANDO, não só a contagem de "PÁRA" — está correto e é do meu tipo de rigor: contar ocorrências prova que a palavra existe, não que ela está no lugar certo da sequência. A TRILHA105 já mede a ordem posicional (`positions == sorted(positions)`), com as cinco marcas em ordem crescente. É a diferença entre "o campo existe" e "o campo faz o que promete" — a mesma distinção que apliquei ao meu próprio V-14. Bem visto, e não é alteração da minuta, é do teste.

---

## Subscrição formal

> **Subscrevo, sem ressalva, a minuta COMO EXECUTAR v1.11 (paradas E-04), como correção operacional do defeito observado no ensaio, com o protocolo de três IAs do v1.10 preservado integralmente.**

Registro que esta é a correção de um achado **meu** do ensaio, o que me deixa numa posição de conferir se a solução corresponde ao problema — e corresponde: o E-04 era "IA avança sozinha e emenda as três etapas", a v1.11 põe uma parada obrigatória entre cada etapa sob comando do operador. Problema e solução batem. A v1.10 permanece vigente até a frase do operador; a v1.11 sobe com a dupla subscrição sem ressalva.

---

*Verificações: sha da v1.11 conferido contra TRILHA105; sequência de paradas lida na íntegra; nota E-04 confrontada com meu registro de execução de 25/09; dez elementos do protocolo v1.10 confirmados presentes na v1.11; frase morta do v1.9 confirmada ausente; T6 (corpo idêntico) aceito da trilha e checado por amostragem dos marcadores C-2..C-5/X-1.*
