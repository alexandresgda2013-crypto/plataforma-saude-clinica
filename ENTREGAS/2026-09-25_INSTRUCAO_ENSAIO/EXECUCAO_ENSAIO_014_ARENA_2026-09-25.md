# EXECUÇÃO DO ENSAIO — B1.SM02.014 · janela da ARENA (IA 2)
## G1 / G2 / G3 executados — sem copiar os outros (leitura própria)

**Arena Casa · 2026-09-25**  
**Natureza:** registro de teste (ensaio). **Não muda** o status do `.014` (segue `aprovado_com_ressalva`).  
**Cego:** esta é a minha leitura isolada, feita **antes** de cruzar com Mestre/IA1 — comparar vem depois.  
**Busca ao vivo:** feita nesta sessão (data 2026-09-25).

---

## G1 — existe? (executado ao vivo nas âncoras)

Contra a internet/PubMed, artigo por artigo nas âncoras de MDD:

| Artigo | Resultado |
|---|---|
| Setiawan 2015 (JAMA Psychiatry) | **existe — PMID 25629589** ⚠️ (ver achado G1-a) |
| Setiawan 2018 (Lancet Psychiatry) | existe — PMID **29496589** ✓ |
| Hannestad 2013 (Brain Behav Immun) | existe — DOI 10.1016/j.bbi.2013.06.010 ✓ |
| Eggerstorfer 2022 (Front Mol Neurosci) | existe — DOI 10.3389/fnmol.2022.981442 ✓ |
| Schubert 2021 (Biol Psychiatry CN) | existe — PMID **33515765** ✓ |
| Richards 2018 (EJNMMI Res) | existe — “increased in unmedicated depressed” ✓ |

**Honesto:** G1 completo (=107 resolvidos) **não** foi feito nesta rodada — resolvi as âncoras que sustentam o claim (as que a materialização usa). Os demais ~90 são fundo/filtro pelo G2; se algum deles for para o lote final, **o G1 dele se resolve na hora**. Anotar data = 2026-09-25.

**Achado G1-a (divergência factual, vai para a fonte):**  
Na execução do Mestre, o Setiawan 2015 aparece com **PMID 25671328**. Ao vivo, o certo é **25629589** — e é esse que está no Bloco. Quem errou? A execução, não o Bloco. Pela regra: divergência factual → confere no artigo → **25629589**.

---

## G2 — serve ao tema? (meu filtro, sobre as 107)

Minha classificação lendo título a título (antes de ver o do Mestre):

| Classe | Minha contagem | Materializa o claim? |
|---|---|---|
| MDD × TSPO-PET humano (grupo) | **~14** (Setiawan 15/18, Holmes, Richards, Schubert, Hannestad, Yrondi, Su, Herzog, Joo, Attwells, Li-TCC, +Cakmak) | **Sim** |
| MDD — abstracts de congresso (27, 28, 65) | 3 | Só com cautela (abstract) |
| MDD — síntese (meta/revisão) | 2–3 (Eggerstorfer, Enache, Gritti) | Como síntese |
| MDD — fora de PET (animal 18/46 · single-cell 73 · esteroidogênese 72 · marcadores 86) | 5 | **Não** (ou contra, no caso 73) |
| Não é TSPO (94 — HDAC6) | 1 | **Não** |
| Outras doenças (AD, PD, EPI, EM, fibromialgia…) | **~60** | Não |
| Método/radioligante/fundo | **~25** | Não |

**Meu veredito do filtro:** a lista é **~80% fundo**; o que materializa é **~14–17**. Parece muito com o que a intuição dizia: a busca é ampla, o G2 é que aperta.

**Peguei sozinho (mesmos três tipos de erro da lista):**
1. **94 (HDAC6)** — nem é TSPO (outro alvo)
2. **`Li 2018` são 2 artigos** (TCC × marcadores) — separar, não apagar
3. Autor corrompido (`De Picker, *.` etc.) — consertar antes de congelar

---

## G3 — sustenta? (meu veredito, com texto na mesa)

Verifiquei ao vivo as âncoras centrais:

| Fonte | Minha direção (`sentido_do_achado`) | Base (ao vivo) |
|---|---|---|
| Setiawan 2015 | `suporta_relacao` | VT elevado em PFC/ACC/ínsula no MDE (objetivo do JAMA confirmado) |
| Hannestad 2013 | **`refuta_relacao`** | “**not elevated**” em depressão leve-moderada (na verdade, menor que controles) |
| Schubert 2021 | `suporta_relacao` (modesto) | “**modest increase**… depressed vs control, p=.01”; sem relação com PCR/IMC |
| Richards 2018 | `suporta_relacao` | “**increased in unmedicated depressed subjects**” |
| Eggerstorfer 2022 | `suporta_relacao` | meta de 8 estudos — existe e confere |
| Holmes / Setiawan 18 / Herzog / Yrondi / Su / Joo / Attwells / Li | **ainda não reli o texto nesta rodada** | entram no fechamento só com texto — senão é “não verificado” |

**Divergência real:** um artigo apoia, outro nega. Isso é **dado** (X-1), não erro — e é para isso que existe `ressalva[tipo=heterogeneidade]`.

---

## As 4 decisões (minha proposta de ensaio — sujeita ao cruzamento)

1. **Estado:** `aprovado_com_ressalva` — **mantido** (ensaio não regrava)
2. **Direção por fonte:** conforme a tabela acima (o que verifiquei ao vivo; o resto, “não verificado até aqui”)
3. **Tipo de ressalva:** `heterogeneidade` (grau: positivos em MDE mais grave; negativo em leve) — **não** condição, **não** maturidade
4. **Moderadores:** gravidade (`atenua` em leve) — fica no claim, não vira condição

---

## Registro operacional (formato S-4)

**Funcionou:** G1 ao vivo, G2 por leitura própria e G3 com texto são executáveis; o Schema 1.3 comportou o caso (direção por fonte + heterogeneidade) sem forçar nada.

**Dificuldades:**
- Lista chega **sem PMID** (G1 resolve em escala, mas custa)
- **~80% fundo** — cruzar 3 filtros sobre 107 é pesado (mesma nota do Mestre)
- Mesmos defeitos de lista: intruso HDAC6 · Li duplicado · nomes corrompidos
- **G1-a:** PMID errado na execução do Mestre (25671328 → certo **25629589**)

**Normativo?** Nada. As 3 bases aguentaram.

**Condições para congelar:** lista saneada (Li separado, HDAC6 fora do lote TSPO, nomes ok) · data de busca anotada · âncoras com G1 resolvido · fundo marcado (não apagado).

---

## Fronteira

Ensaio, não piloto; S-5 (conheço o histórico); ao fim volto à bancada; `.014` **não muda de status**.  
Comparação com as outras IAs: só depois de entregue este registro.

*Digital: sha publicado no pacote. Busca ao vivo 2026-09-25.*
