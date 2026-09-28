SEGUNDA RODADA — AUDITORIA DE CLASSIFICAÇÃO

Escopo: exclusivamente Filosofia do Projeto, Arquitetura Consolidada V2.2 e Roteiro de Trabalho.
Limite assumido: quando um conteúdo existe no projeto mas não nestes três documentos (ex.: schema_vinculo_v1.1.json, arquivos de anamnese), a classificação é "não determinável nesta base documental" — não é afirmação de inexistência.

PARTE A — REVISÃO DOS [E]
#	Afirmação da 1ª rodada	Base textual	Veredito
E1	Motor respeita a cadeia Biblioteca→NT→Ontologia→JSONs→Motor e não trata a Biblioteca como camada final de consumo	§28 (literal)	Confirmado como texto, mas o próprio documento o contradiz em §19 → ver C-2
E2	Cinco operações do Motor: seleção, filtragem, combinação, contextualização, rastreabilidade	§17, diagrama	Confirmado com ressalva — aparece sob "Conceitualmente"; nada indica que a lista seja exaustiva ou normativa
E3	Entradas do Motor: IDs, contexto, relações, condições, evidências, metadados, JSONs	§17, diagrama	Confirmado. Correção: omiti "contexto" na 1ª rodada
E4	Saídas: interpretação contextualizada → três sugestões → explicação narrativa → laudo	§2, §21, §23	Confirmado
E5	Anamnese como entrada; casos simulados admitidos e sem finalidade de eficácia	§2 (bloco DEFINIÇÃO); Roteiro §9	Confirmado
E6	Consulta ativa ao canônico e, quando pertinente, à Pasta de Atualização	§2, bloco DEFINIÇÃO	Confirmado e reforçado — o mesmo trecho estabelece literalmente "preservando a origem de cada informação"
E7	Informação da Pasta nunca equivale ao canônico	§19 (literal)	Confirmado
E8	Conexão não é indicação, eficácia, causalidade, tratamento nem recomendação	§11 (literal, referindo-se a "o sistema")	Confirmado — vincula o Motor explicitamente
E9	Cenário contextualiza; não causa nem indica	§12 (literal)	Confirmado
E10	Proibições de invenção e de elevação de certeza para "nenhuma camada posterior"	§22	Confirmado
E11	"Relação mecanística não vira eficácia clínica" como regra do Motor	§7	Reclassificado. §7 é norma da NT. Para o Motor a regra é derivada de §22 + §25 + Roteiro §10.9
E12	Qualidade narrativa não aumenta certeza	§13; generalizado em §25	Confirmado
E13	Aprofundamento pertence à Biblioteca do objeto científico	§5.5 (literal)	Confirmado como regra de arquitetura. A consequência que enunciei para o runtime do Motor é [P]
E14	Motor não gera explicação científica do zero	§14 ("poderá", "o objetivo é evitar"); §28 ("em vez de depender"); Filosofia ("respostas improvisadas", "conteúdo especulativo")	Reclassificado parcialmente. Estabelecido: proibição de depender de geração espontânea e de improvisar. Não estabelecido: proibição total de composição textual generativa → G10
E15	Motor lê do Grafo "direção" e faz "travessia multidomínio"	§15	Reclassificado para [P]. §15 apenas diz que a Ontologia formaliza relações. "Travessia" é termo meu; "direção" é campo do vínculo (§5.2) e do modelo de relação (§11), não interface declarada do Grafo
E16	Uma entidade pode gerar múltiplos JSONs	§16	Confirmado
E17	Inventário de campos N1 (§5.1) e N2 (§5.2)	§5.1, §5.2	Confirmado quanto ao inventário. "O Motor lê N1/N2 diretamente" é [?] (G1). "O Motor não altera" é derivado de §22
E18	Motor lê da Biblioteca "identificador para fechamento da trilha"	—	Reclassificado para [?]. Não há base textual. Erro da 1ª rodada
E19	Relevância relativa, descarte e explicitação de mecanismos improváveis	Filosofia (literal)	Confirmado como exigência da plataforma
E20	Três trilhas de sugestão	§2, §21	Confirmado

Correção estrutural importante: afirmei que a arquitetura de módulos "não cria funções novas, apenas decompõe as cinco do §17". A afirmação é imprecisa. A decomposição em M1–M9 e T1–T3, os nomes, as fronteiras e a ordem dos módulos são integralmente [P]. Nenhum documento define módulos internos do Motor.

PARTE B — REVISÃO DOS [P]
#	Proposta	Situação após reexame
P1	Módulos M1–M9 / T1–T3	Permanece [P] integralmente
P2	Delimitação das três trilhas de sugestão	Permanece [P] — e colide com a taxonomia de duas trilhas do §5.2 → C-6
P3	Registro de trilha de decisão	Parcialmente normatizado. A Filosofia exige no relatório "as razões que sustentam cada hipótese" e "a fundamentação das sugestões"; §23 exige "explicações científicas". O requisito de saída é [E]; o log interno auditável permanece [P]
P4	Calibração verbal por nível de evidência	Permanece [P], com piso estabelecido: Filosofia ("considerando níveis de evidência, qualidade metodológica…") + §22 + §25
P5	Separação de uso entre trilha clínica e mecanística	Permanece [P]. O campo existe (§5.2); a regra de uso pelo Motor, não
P6	Reprodutibilidade e selo de versão	Permanece [P], com base mais fraca do que declarei. Roteiro §12 ("possibilidade de reprodução do processo") trata de replicação para outros IDs, não de determinismo do laudo
P7	Buscar a NT do objeto ao explicá-lo	Permanece [P], com sustentação forte (§5.5 + §8 + §10)
P8	Ordem de fechamento das lacunas	Permanece [P] metodológica, não normativa

Nenhum [P] foi promovido integralmente a [E]. Um (P3) teve sua metade de saída reconhecida como estabelecida.

PARTE C — [?] RESOLVIDOS OU REDUZIDOS PELOS DOCUMENTOS
Antes	Depois	Base
G3 — ancoragem aos IDs	Reduzido. A função de integrar informações clínicas, sintomas, exames e escalas aos 146 IDs é [E] (Filosofia). Permanece pendente: quais classes de ID recebem sintomas e escalas	Filosofia; Arq §1, §3
G6 — estrutura do laudo	Substancialmente reduzido. O conteúdo obrigatório é [E], pela união de §23 (achados, mecanismos possíveis, relações relevantes, evidências, explicações científicas, sugestões auxiliares) e Filosofia (mecanismos improváveis, razões de cada hipótese, fundamentação das sugestões, rastreabilidade de toda afirmação, linguagem clara e didática). Pendente apenas: formato/schema	§23; Filosofia
G10 — papel do LLM	Reduzido. Piso estabelecido: proibidas respostas improvisadas e conteúdo especulativo; proibida dependência de geração espontânea. Pendente: a fronteira exata	Filosofia; §14, §28
G15 — critérios de aceitação	Reduzido. O conjunto de critérios já existe: Roteiro §10 (15 verificações) e §12 (9 critérios de replicação). Pendente: operacionalização executável	Roteiro §10, §12
Preservação de procedência	Resolvido → [E]. "preservando a origem de cada informação"	§2, bloco DEFINIÇÃO
Titularidade do Contrato do Motor	Resolvido → [E]. Pertence ao Grupo 1, que tem entre suas funções "contrato do Motor"	Roteiro §2
Finalidade dos casos simulados	Resolvido → [E]. Testam comportamento do sistema, não eficácia clínica	Roteiro §9
G9 — modalidade da Pasta de Atualização	Confirmado como pendência declarada pelo próprio documento, não como lacuna inferida por mim	§19 (literal)

Não resolvido, e agravado: G1. Os documentos não apenas omitem a superfície de consulta em runtime — eles se contradizem sobre ela (C-2).

PARTE D — MATRIZ DE DECISÕES PENDENTES DO MOTOR
ID	Decisão necessária	Motivo	Documentos afetados	Módulo afetado	Consequência de não decidir	Bloqueante
G1	Quais camadas o Motor lê em runtime (só JSONs, ou JSONs + Grafo + N1/N2 + NT)	§2/§21/§30 mostram só JSONs→Motor; §14 mostra NTs→Motor; §19 mostra Biblioteca/NT/JSONs→Motor; §17 lista evidências e JSONs como entradas distintas	Arq §2, §14, §17, §19, §21, §28, §30	Todos	Impossível definir interfaces, forma dos JSONs e custo da rastreabilidade; retrabalho total	Sim — raiz
G2	Contrato de entrada da anamnese	Não determinável nesta base; Roteiro §9 apenas informa que os arquivos existem	Roteiro §9, item 23	M1, M2	Motor não especificável na borda de entrada	Sim
G3	Classes de ID que recebem sintomas, achados e escalas	§1 e §3 não listam esses domínios; a Filosofia exige a ancoragem	Filosofia; Arq §1, §3	M2	Ancoragem indefinida; o Motor não sabe a que o caso se liga	Sim
G4	Forma avaliável por máquina do campo "condição"	O campo existe em §5.2, §11 e §13, mas sem linguagem formal	Arq §5.2, §11, §13	M4, M5	Condições viram texto livre; filtragem não auditável	Sim
G5	Domínios de valor de escopo, direção, natureza, força, maturidade, trilha, nível de evidência	Os nomes dos campos são [E]; os valores estão nos schemas L-05, fora desta base	Arq §5.1, §5.2	M4, regra de calibração	Qualificadores não interpretáveis; risco de elevação epistemológica silenciosa	Sim
G6	Formato/schema do Laudo (conteúdo já é [E])	§23 e Filosofia definem o conteúdo, não a estrutura, nem a marcação de nível de evidência por afirmação	Arq §23; Filosofia	M9	Saída não comparável entre execuções; auditoria do Marco 6 inviável	Sim, para Marco 5
G7	Definição operacional das trilhas mecanística, clínica e terapêutica	Os três nomes são [E]; o conteúdo de cada um, não	Arq §2, §21; Filosofia	M7	Sugestões migram de trilha sem critério; risco direto sobre §11	Sim
G8	Regra de relevância relativa e critério de descarte	Filosofia exige estimar relevância e descartar mecanismos pouco compatíveis; nenhum documento define como	Filosofia	M6	Função obrigatória sem especificação; maior lacuna substantiva	Sim
G9	Modalidade de uso da Pasta de Atualização (alerta, atualização, comparação, enriquecimento ou outra modalidade)	Pendência declarada pelo próprio §19	Arq §18, §19, §20	T3	Canal de atualização inutilizável ou usado sem regra	Sim, para T3
G10	Fronteira exata do componente generativo dentro do Motor	Piso estabelecido; limite exato ausente	Filosofia; Arq §14, §28	M8	Risco de o laudo conter texto não rastreável	Sim
G11	Existência de tipos de relação para sinergia, interação e contraindicação na Ontologia	Exigidos pela Filosofia; sem contrapartida na Arquitetura	Filosofia; Arq §15	M7	Requisito da Filosofia sem suporte ontológico	Sim, para Marco 3
G12	Precedência em conflito entre vínculos de direções opostas	Nenhum documento trata conflito	Arq §5.2, §11	M4	Comportamento indeterminado; laudo não reprodutível	Condicional (Marco 6)
G13	Versionamento do conhecimento e determinismo do laudo	Checklist 30 prevê reexecução após correções	Roteiro §12, item 30	T1	Impossível distinguir correção de variação	Condicional (Marco 6)
G14	Onde termina a trilha de rastreabilidade de um claim clínico	§22 coloca a Biblioteca na cadeia; Roteiro §7 desvia dela → C-4	Arq §22; Roteiro §7; Filosofia	T1, M9	Trilha quebrada para toda a classe de claims clínicos	Sim
G15	Operacionalização executável dos 15 critérios do Roteiro §10	Critérios existem em prosa	Roteiro §10, §12	Todos	Teste ponta a ponta sem critério de aprovação	Sim, para Marcos 5 e 6
G16	Fronteira entre Anamnese e Motor: onde ocorre a ancoragem aos IDs	Filosofia atribui a integração à "anamnese estruturada e inteligente"; Arq §2 trata a anamnese como entrada de dados do caso	Filosofia; Arq §2, §21	M1, M2	M2 pode não pertencer ao Motor; escopo do contrato indefinido	Sim
G17	Comportamento diante de caso fora do escopo declarado (ansiedade e depressão)	Escopo só aparece na Filosofia	Filosofia	M2, M9	Saída para caso fora de escopo sem regra	Não, para o piloto
G18	Reconciliação da taxonomia de trilhas: duas no vínculo (§5.2) × três na saída	Mapeamento inexistente	Arq §5.2, §2, §21	M4, M7	Vínculo de trilha clínica sustentando sugestão terapêutica sem regra	Sim
G19	Hierarquia normativa entre Filosofia e Arquitetura V2.2 para o contrato do Motor	Roteiro §16 subordina apenas o Roteiro; a relação Filosofia × Arquitetura não é declarada	Filosofia; Arq; Roteiro §16	Governança	Duas bases normativas divergentes (ver C-1, C-3, C-5)	Sim
G20	Admissibilidade, no laudo, de conteúdo não derivado de uma Biblioteca (Pasta de Atualização; claims clínicos)	Contradiz frontalmente a Filosofia → C-3 e C-4	Filosofia; Arq §19; Roteiro §7	M9, T3	Ou o Motor viola a Filosofia, ou §19 e Roteiro §7 ficam inertes	Sim

Dos 20 itens, G1, G16 e G19 são anteriores aos demais: definem, respectivamente, o que o Motor lê, onde ele começa e qual documento prevalece. As outras dezessete não são estáveis antes desses três.

PARTE E — CONTRADIÇÕES E DIVERGÊNCIAS
ID	Natureza	Descrição	Impacto sobre o Motor
C-1	Filosofia × Arquitetura	A Filosofia define a NT como "representação integrada… responsável por conectar os diferentes domínios científicos". §8 determina que cada NT permanece no seu domínio e que "a integração ocorre por meio das relações"; §9 separa NT e Grafo	Decide se M3 percorre o Grafo ou lê uma NT já integrada. Altera a arquitetura de recuperação
C-2	Interna à Arquitetura	O que o Motor lê: §2/§21/§30 (só JSONs) × §14 (NTs → Motor) × §19 (Biblioteca/NT/JSONs → Motor) × §28 (Biblioteca não é camada de consumo) × §17 (evidências como entrada distinta de JSONs)	É a causa de G1. Sem resolver, nenhuma interface é especificável
C-3	Filosofia × Arquitetura	Filosofia: "Todo conteúdo apresentado ao usuário deve derivar exclusivamente das Bibliotecas de Conhecimento correspondentes". §19 autoriza o Motor a consultar a Pasta de Atualização	Se algo da Pasta aparecer no laudo, a Filosofia é violada; se não puder aparecer, §19 perde função
C-4	Filosofia × Roteiro	Filosofia: "Todo conhecimento científico ingressa obrigatoriamente pela Biblioteca de Conhecimento correspondente". Roteiro §7: claims fechados seguem Evidências → N1 → N2 → NT/Ontologia e "não entram na Biblioteca Canônica de mecanismos"	Quebra a cadeia de autoridade do §22 para uma classe inteira de conteúdo. Origem de G14
C-5	Cobertura	A tríade da Filosofia (Biblioteca → NT → JSON) omite Evidências/Vínculos e Ontologia/Grafo, presentes na V2.2	Dois mapas normativos distintos da mesma cadeia; origem de G19
C-6	Taxonomia	§5.2 qualifica o vínculo como "trilha clínica ou mecanística" (dois valores); a saída tem três trilhas	Sem mapa, uma sugestão terapêutica pode ser sustentada por vínculo de outra trilha. Origem de G18
C-7	Interna à Arquitetura	Sentido da relação Evidência ↔ Biblioteca: §2, §21 e §30 colocam a Biblioteca antes das Evidências; §5.3 e §22 colocam a Evidência antes da Biblioteca	Define onde termina a trilha de rastreabilidade e se pode existir evidência fora de qualquer Biblioteca
C-8	Arquitetura × Roteiro	Status da B1: §26 afirma que ela "já possui sua Biblioteca Canônica e passou pelo processo de auditoria"; checklist item 9 registra "🔄 EM CONSOLIDAÇÃO" e item 8 registra claims "🔄 EM VALIDAÇÃO"; §29 mantém a auditoria científica como função ativa	Afeta a leitura do resultado do piloto: falha do teste pode ser da engenharia ou do conteúdo
C-9	Interna ao Roteiro	§17 lista "separação conceitual entre os dois grupos" como já consolidada; checklist item 2 registra "⬜ PENDENTE DE REGISTRO"	Menor. Afeta apenas o controle de progresso
C-10	Documental	O arquivo se intitula "Arquitetura Consolidada da Plataforma V2"; os diagramas internos e o Roteiro referem "V2.2"	Menor, mas relevante para versionamento normativo (G13, G19)
PARTE F — SÍNTESE
Classe	Conteúdo
ESTABELECIDO	Posição do Motor na cadeia; as cinco operações do §17; o inventário de entradas do §17; a sequência de saídas; a anamnese e os casos simulados como entradas; a consulta ativa com preservação de origem; o conteúdo obrigatório do laudo; a exigência de relevância relativa, descarte e explicitação de mecanismos improváveis; as três trilhas de sugestão; as sete proibições epistemológicas (§11, §12, §19, §22, §25); o inventário de campos N1 e N2; a titularidade do contrato (Grupo 1)
DERIVADO	Toda a modularização M1–M9 / T1–T3; a delimitação das três trilhas; o log interno de decisão; a calibração verbal; a regra de separação de trilhas; o determinismo do laudo; a regra de busca da NT do objeto; a aplicação ao Motor da proibição mecanística→eficácia; a leitura de direção e travessia no Grafo
PENDENTE	G1 a G20 — três deles (G1, G16, G19) precedem os demais; G9 é pendência declarada pelo próprio documento
CONTRADITÓRIO	C-1 a C-8 substantivos, C-9 e C-10 menores. Quatro deles (C-2, C-3, C-4, C-7) impedem a especificação da rastreabilidade e das interfaces, e não podem ser resolvidos dentro do contrato do Motor: exigem decisão nos documentos de origem

Uma observação de método, sem propor conteúdo: C-2, C-3, C-4, C-7 e C-1 não são lacunas do contrato do Motor — são divergências entre documentos normativos superiores. Escrever o contrato antes de resolvê-las faria o contrato arbitrar, por omissão, questões que pertencem à Filosofia e à Arquitetura.
