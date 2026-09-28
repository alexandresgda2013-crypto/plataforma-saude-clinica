[VERBATIM — colado pelo operador neste chat em 2026-09-20; fonte: Auditor-MESTRE (projeto 1), após receber a carta 19 v2 + a V2.2 oficial. Arquivado pela casa sem tocar conteúdo.]

Agora sim: a V2.2 oficial está no projeto. Vou conferir tudo.

A V2.2 oficial confere em tudo. Agora a especificação L-05, que é a única peça de schema que está no projeto — e ela afeta diretamente o L-NT.

Estão lá, e conferem. O projeto agora tem quatro arquivos, e o 309aa65f antigo saiu.

Eco das digitais, medidas por mim sobre os arquivos do projeto:

| Arquivo | SHA-256 | Confronto |
|---|---|---|
| V2.2 oficial | df7f7cfdfc01cf77d658885f30dfefe29dcf380229ea56e6b3af02920df22ae1 | confere com o declarado · 52.181 bytes · 1.411 linhas CRLF |
| V2.3 candidata | 498e7df9d8abe8be4f3145bb7a9bd34215bc87a4502148e9d203391c9ce6ef73 | confere |
| Como Executar v1.9 | 1cd90b407facee81692d668919829c9d6d5a149b1309424c6f012e26cd81f586 | confere com o que medi antes |
| Especificação L-05 v1.4 | 78a0f2afcd2acf0f78caa8bbc674c337e7c5b47c93ee86d684f1648b6671dc8b | sem digital declarada — nenhuma carta publicou a sha deste arquivo |

D-V22-BYTES-PROJETO fecha. A base do projeto passa a conter as três cláusulas: origem_conhecimento ×3, "a prosa prevalece sobre os desenhos" ×1, Pasta "fora do cânone" ×1. E a V2.2 oficial se identifica corretamente no H1 (V2.2    17.09.26).

V2.2 → V2.3: 4 hunks, +4/−4, exatamente como a carta 18 declarou. E os §§6, 7, 13 e 14 da V2.2 oficial são byte-idênticos aos que usei na Minuta 1 — agora conferido contra o artefato oficial, não contra cópia.

O que não está no projeto: os dois schemas JSON. Há só a especificação .md. Então ainda não posso ecoar N1 v1.3 (b06660fd…) nem N2 v1.4 (d96ad15b…) — continuam declarados pela casa, não verificados por mim. O zip de schemas mencionado na carta não chegou.

O export que a casa pediu vai anexo: o arquivo antigo do projeto, com a digital preservada 309aa65fa75de6b93cca24aaa154dbdf984833aff1716f8a26c510108c28b646. Com ele fecham a caracterização do elo da cadeia.

Agora o erro que achei no meu L-NT, graças à especificação.

A especificação define uso com duas trilhas, e a regra está escrita literalmente: clínica = {clinico, contexto_mecanistico}, mecanística = {nucleo_causal, suporte_correlacional}, gap_pesquisa comum às duas, com o campo trilha dizendo qual enum vale.

Na Minuta 1 do L-NT eu defini uso apenas com o enum clínico. E a NT-B1 deriva da Biblioteca B1 — que é justamente da trilha mecanística. Resultado: a maior parte das unidades da NT-B1 carregaria nucleo_causal ou suporte_correlacional, valores que o meu contrato rejeitaria. O contrato, como escrito, não aceitaria a própria biblioteca-piloto para a qual foi feito. Peguei o uso do kit clínico sem perceber que ele é metade do campo.

Duas correções derivadas, pelo mesmo motivo:

A regra N-4 está escrita no vocabulário do kit ("proibido quando a origem é preclinical_mechanistic"). A especificação usa natureza_evidencia com sete valores. A regra correta é: uso = clinico proibido quando natureza_evidencia ∈ {preclinica_in_vivo, preclinica_in_vitro}. E o valor mista precisa de decisão explícita, porque hoje cairia no vazio da regra.

E o eixo epistêmico se chama direcao_suporte na especificação (14 ocorrências) — não direcao. O degrau 5 da L-06 e as referências do L-NT precisam usar esse nome. Isso fecha a dívida D-L05-NOMES-DIRECAO do lado dos meus contratos.

Nenhuma dessas três muda a arquitetura do L-NT; mudam enums e uma regra. Entram na minuta 2.

As duas precisões de citação da casa, aceitas. Suprimi "específico… científico" do §5.5 e parafraseei o §5 da proposta como se fosse literal. Quote é medida, e eu as tratei como resumo — registro como erro meu de citação.

Estado: a arquitetura oficial está verificada no projeto, as âncoras do L-NT estão confirmadas, e a minuta 2 do L-NT agora tem quatro correções prontas — as três acima mais a linha de referência normativa, que passa a citar df7f7cfd…. Ela sai quando o operador decidir entre (i) e (ii). Para auditar a D-02 e as regras N-1, NT-03 e NT-04 contra os schemas propriamente ditos, ainda preciso dos dois JSON.
