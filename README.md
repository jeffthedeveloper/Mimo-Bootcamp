# 🐍 MIMO Bootcamp — Python em Ação

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Projetos](https://img.shields.io/badge/Projetos-11%20Scripts-2EA44F?style=for-the-badge)
![Metodologia](https://img.shields.io/badge/Metodologia-Gamifica%C3%A7%C3%A3o-FF6F00?style=for-the-badge)
![Instituição](https://img.shields.io/badge/Educa%C3%A7%C3%A3o-CIEPE-6A1B9A?style=for-the-badge)

> **Laboratório de código, pesquisa didática e gamificação aplicada ao ensino de programação em Python.**

---

## 📖 Visão Geral

Este repositório reúne **11 projetos práticos** desenvolvidos originalmente durante a formação **Python em Ação** do *Bootcamp MIMO* e posteriormente consolidados para fins de pesquisa e aprimoramento didático.

O propósito central deste acervo é servir como **base metodológica para as aulas ministradas aos alunos da CIEPE**, transformando conceitos fundamentais da ciência da computação em desafios interativos, contextualizados e gamificados. Ao conectar lógica de programação com jogos, finanças, automação e cultura pop, os scripts reduzem a barreira de entrada para iniciantes e estimulam o protagonismo estudantil.

---

## 🎯 Pilares da Metodologia Didática

A organização deste repositório reflete uma abordagem ativa de ensino baseada em três eixos:

1. **🎮 Gamificação e Feedback Imediato:** Desafios inspirados em mecânicas de RPG e jogos clássicos (*Damage Calculator*, *Rock Paper Scissors*) mantêm o engajamento alto e tornam o teste de hipóteses divertido.
2. **🌍 Problemas do Mundo Real:** Simulações de carteiras digitais, análise de extratos financeiros, delivery e bibliotecas (*Crypto Wallet*, *Transactions Analyzer*, *Food Delivery*, *Library*) mostram como o Python resolve problemas reais do mercado.
3. **📈 Progressão Gradual de Complexidade:** Os scripts evoluem desde entradas e saídas simples no terminal (~375 bytes) até manipulação estruturada de coleções, validação de dados e consumo de APIs externas (>2 KB de lógica).

---

## 🗺️ Trilha de Aprendizagem Progressiva

Para facilitar a aplicação em sala de aula na **CIEPE**, os 11 scripts estão organizados em **4 níveis de maturidade técnica**:

```text
Nível 1: Fundamentos & Lógica Inicial
 ├── Projeto_Bot.py          (Interação e fluxo básico)
 ├── Damage_Calculator.py    (Operadores e fórmulas de RPG)
 └── Crypto_Wallet.py        (Variáveis, dicionários e saldos)

Nível 2: Controle de Fluxo, Validação & Matrizes
 ├── Task_List.py            (Listas e operações CRUD em memória)
 ├── Sensor_Validator.py     (Condicionais compulsórias e faixas de segurança)
 └── Draw_Letter.py          (Laços aninhados e manipulação visual de strings)

Nível 3: Sistemas Interativos & Regras de Negócio
 ├── Rock_Paper_Scissors.py  (Aleatoriedade, placar e validação de jogadas)
 ├── Food_Delivery.py        (Catálogo, carrinho e fechamento de pedidos)
 └── Library.py              (Gestão de acervo, empréstimos e estado)

Nível 4: Integração Web & Análise de Dados
 ├── StarWars_Api.py         (Requisições HTTP, API REST e parsing JSON)
 └── Transactions_Analyzer.py(Processamento de lotes, métricas e relatórios)
```

---

## 📂 Catálogo Detalhado e Guia de Sala de Aula

Abaixo está o mapeamento técnico de cada arquivo, acompanhado de **missões gamificadas** que podem ser propostas aos estudantes como extensão de aula:

### 🟢 Nível 1 — Fundamentos e Lógica Inicial

#### 1. [`Projeto_Bot.py`](./Projeto_Bot.py) — Assistente Interativo de Terminal
* **Escopo Técnico:** Introdução à comunicação homem-máquina via console (`input` e `print`), tratamento básico de strings e respostas condicionadas.
* **Foco Didático:** Quebrar o gelo na primeira aula prática, mostrando como um programa recebe dados, processa decisões e responde ao usuário.
* **🏆 Missão Extra (Desafio XP):** Adicionar um menu de comandos (`ajuda`, `hora`, `curiosidade`, `sair`) mantendo o bot ativo em loop `while`.

#### 2. [`Damage_Calculator.py`](./Damage_Calculator.py) — Calculadora de Dano (RPG)
* **Escopo Técnico:** Expressões aritméticas, precedência de operadores, variáveis numéricas e regras de multiplicação de dano.
* **Foco Didático:** Ensinar matemática computacional e lógica condicional usando o universo de jogos eletrônicos.
* **🏆 Missão Extra (Desafio XP):** Implementar chance de *Acerto Crítico* (dano $\times 2$) e cálculo de redução por armadura do oponente.

#### 3. [`Crypto_Wallet.py`](./Crypto_Wallet.py) — Simulador de Carteira Cripto
* **Escopo Técnico:** Armazenamento de ativos, conversão de valores, atualização de saldo e formatação numérica.
* **Foco Didático:** Introduzir o conceito de estado de aplicação e estruturação de dados chave-valor (`dict`).
* **🏆 Missão Extra (Desafio XP):** Criar uma função de compra/venda entre duas moedas (ex.: BRL $\rightarrow$ BTC) validando se há saldo suficiente.

---

### 🟡 Nível 2 — Controle de Fluxo, Validação e Padrões

#### 4. [`Task_List.py`](./Task_List.py) — Gerenciador de Tarefas (CLI)
* **Escopo Técnico:** Manipulação dinâmica de listas (`.append()`, `.remove()`, indexação), iteração com `enumerate()` e controle de menu.
* **Foco Didático:** Consolidar as quatro operações fundamentais de dados (**CRUD**: Criar, Ler, Atualizar e Remover).
* **🏆 Missão Extra (Desafio XP):** Permitir marcar tarefas como `[CONCLUÍDA]` sem apagá-las da lista e exibir a porcentagem de progresso.

#### 5. [`Sensor_Validator.py`](./Sensor_Validator.py) — Validador de Leituras de Sensores
* **Escopo Técnico:** Operadores relacionais e lógicos (`and`, `or`, `not`), filtragem de anomalias e emissão de alertas técnicos.
* **Foco Didático:** Simular cenários de IoT e automação industrial, destacando a importância de validar entradas antes de processá-las.
* **🏆 Missão Extra (Desafio XP):** Classificar as leituras em três faixas (`NORMAL`, `ATENÇÃO` e `CRÍTICO`) e contabilizar a taxa de falhas do lote.

#### 6. [`Draw_Letter.py`](./Draw_Letter.py) — Gerador de Arte ASCII no Terminal
* **Escopo Técnico:** Laços de repetição aninhados (`for`), controle de coordenadas linha/coluna e construção visual de caracteres.
* **Foco Didático:** Desenvolver o raciocínio espacial e a visualização concreta de como matrizes e loops bidimensionais operam.
* **🏆 Missão Extra (Desafio XP):** Permitir que o aluno escolha o símbolo de preenchimento (`#`, `*`, `@`) e adicione novas letras ao alfabeto do script.

---

### 🟠 Nível 3 — Sistemas Interativos e Regras de Negócio

#### 7. [`Rock_Paper_Scissors.py`](./Rock_Paper_Scissors.py) — Pedra, Papel e Tesoura
* **Escopo Técnico:** Uso do módulo nativo `random`, normalização de entradas do usuário, tabela de regras de vitória/empate e controle de placar.
* **Foco Didático:** Trabalhar lógica booleana composta e resiliência contra entradas inválidas digitadas pelo usuário.
* **🏆 Missão Extra (Desafio XP):** Transformar a partida em uma disputa "Melhor de 5" e adicionar as jogadas *Lagarto* e *Spock*.

#### 8. [`Food_Delivery.py`](./Food_Delivery.py) — Sistema de Pedidos e Delivery
* **Escopo Técnico:** Estruturação de cardápio com preços, seleção múltipla de itens, cálculo de subtotal, taxas e resumo final do pedido.
* **Foco Didático:** Integrar listas, dicionários e funções em um fluxo comercial completo de ponta a ponta.
* **🏆 Missão Extra (Desafio XP):** Adicionar cupons de desconto promocionais e cálculo de frete grátis acima de um valor mínimo.

#### 9. [`Library.py`](./Library.py) — Sistema de Gestão de Biblioteca
* **Escopo Técnico:** Modelagem de acervo, controle de disponibilidade (disponível/emprestado), busca por título/autor e modularização em funções.
* **Foco Didático:** Preparar os alunos para a transição da programação procedural para a Programação Orientada a Objetos (POO).
* **🏆 Missão Extra (Desafio XP):** Registrar o nome do aluno que pegou o livro emprestado e gerar um relatório de obras atualmente fora do acervo.

---

### 🔴 Nível 4 — Integração Externa e Análise de Dados

#### 10. [`StarWars_Api.py`](./StarWars_Api.py) — Explorador do Universo Star Wars (SWAPI)
* **Escopo Técnico:** Consumo de API REST pública via protocolo HTTP (`requests`), interpretação de respostas em formato `JSON` e tratamento de status codes.
* **Foco Didático:** Conectar o código local à internet real, desmistificando como aplicativos modernos trocam dados com servidores.
* **🏆 Missão Extra (Desafio XP):** Exibir a lista de filmes em que o personagem consultado aparece e tratar erros de conexão com `try/except`.

#### 11. [`Transactions_Analyzer.py`](./Transactions_Analyzer.py) — Analisador de Transações Financeiras
* **Escopo Técnico:** Script mais robusto do repositório; realiza varredura de registros financeiros, agregação de entradas/saídas, filtragem e geração de resumo analítico.
* **Foco Didático:** Introduzir pensamento analítico e fundamentos de Ciência de Dados usando apenas Python puro.
* **🏆 Missão Extra (Desafio XP):** Identificar automaticamente a maior despesa, a média de gastos e exportar o resumo final para um arquivo `.txt`.

---

## 🏅 Sistema de Gamificação Sugerido (CIEPE)

Para aplicar este repositório em formato de trilha gamificada em sala de aula, recomenda-se a seguinte tabela de progressão:

| Patente | Critério de Conquista | Projetos Associados |
| :--- | :--- | :--- |
| 🥉 **Aprendiz de Sintaxe** | Executar e explicar os 3 scripts iniciais sem erros de sintaxe. | `Projeto_Bot`, `Damage_Calculator`, `Crypto_Wallet` |
| 🥈 **Construtor de Lógica** | Implementar estruturas de repetição e validação de dados. | `Task_List`, `Sensor_Validator`, `Draw_Letter` |
| 🥇 **Desenvolvedor de Sistemas** | Construir fluxos completos com regras de negócio e estado. | `Rock_Paper_Scissors`, `Food_Delivery`, `Library` |
| 💎 **Arquiteto Python** | Integrar APIs externas, analisar conjuntos de dados e concluir ao menos 3 Missões Extras. | `StarWars_Api`, `Transactions_Analyzer` |

---

## 🚀 Como Configurar e Executar

### 1. Pré-requisitos
* **Python 3.10** ou superior instalado no ambiente de laboratório ou máquina pessoal.

### 2. Clonar o Repositório
```bash
git clone https://github.com/jeffthedeveloper/Mimo-Bootcamp.git
cd Mimo-Bootcamp
```

### 3. Instalar Dependências Externas
Dez dos onze projetos utilizam exclusivamente a **Biblioteca Padrão do Python**. Apenas o script `StarWars_Api.py` requer a biblioteca `requests`:
```bash
pip install requests
```

### 4. Executar os Projetos
No terminal, execute o script desejado:
```bash
python Transactions_Analyzer.py
```

---

## 🛠️ Roadmap de Evolução Didática

* [ ] Adicionar comentários guiados (`# DESAFIO DO ALUNO:`) em versões de exercício para sala de aula.
* [ ] Incluir docstrings padronizadas em todas as funções dos 11 scripts.
* [ ] Criar uma pasta `/desafios_resolvidos` com implementações das Missões Extras.
* [ ] Adicionar testes automatizados simples com `assert` para ensinar validação de código aos estudantes.

---

## 👨‍💻 Autor

**Jefferson Firmino Mendes** ([@jeffthedeveloper](https://github.com/jeffthedeveloper))  
*Educador e Desenvolvedor — Projeto aplicado aos estudos de didática e gamificação na **CIEPE**.*
