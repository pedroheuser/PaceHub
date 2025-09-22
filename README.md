# PaceHub

> Um software sob encomenda para organizadores de eventos esportivos e clubes de corrida que precisam de uma plataforma eficiente para gerenciar todas as etapas de uma corrida, desde a divulgação até a publicação dos resultados.

O PaceHub se diferencia por oferecer uma solução unificada e robusta para a gestão integral do evento, em contraste com alternativas que exigem o uso de múltiplas planilhas e plataformas descentralizadas.

## 📋 Tabela de Conteúdos
1. [Visão Geral](#-visão-geral)
2. [Público-Alvo](#-público-alvo)
3. [Funcionalidades Principais](#-funcionalidades-principais)
4. [Regras de Negócio](#-regras-de-negócio)
5. [Arquitetura do Sistema](#-arquitetura-do-sistema)
6. [Tecnologias Utilizadas](#-tecnologias-utilizadas)
7. [Como Executar o Projeto](#-como-executar-o-projeto)

## 🎯 Visão Geral

O projeto ataca o problema da gestão manual de corridas de rua, que resulta na ausência de informações precisas, falta de controle automatizado de inscrições e dificuldade na comunicação com os atletas. A solução automatiza o processo de inscrição, o controle de percursos e a disponibilização de resultados em tempo real.

**Benefícios:**
* Redução do tempo gasto em tarefas administrativas manuais.
* Diminuição de custos operacionais com a automação de processos.
* Melhoria na comunicação e transparência entre organizadores e atletas.
* Fornecimento de dados e análises precisas para apoiar a tomada de decisões.

## 👥 Público-Alvo

O sistema é projetado para dois tipos principais de usuários:

* **Organizadores de Eventos:** Responsáveis por gerenciar o ciclo de vida completo da corrida, desde o planejamento até a análise pós-evento. O conhecimento em informática pode variar de básico a avançado.
* **Atletas:** Usuários com interesse principal no acompanhamento da corrida, inscrição e consulta de resultados. Geralmente possuem conhecimento básico em informática.

## ✨ Funcionalidade Implementada: Criação de Eventos (Organizador)

Este módulo foca na principal funcionalidade do organizador de corridas, permitindo o gerenciamento completo da criação de um novo evento. Os requisitos funcionais implementados incluem:

* **RF03:** Permite ao organizador criar um novo evento de corrida. [cite: 29]
* **RF12:** Permite que o organizador cadastre múltiplos kits de corrida (ex: camiseta, medalha), vinculando-os a um evento específico. 

## 📜 Regras de Negócio

O sistema opera sob um conjunto de regras de domínio específicas para o universo das corridas de rua:

* **RN01:** A inscrição é permitida apenas para atletas que atendam à idade mínima para cada distância (5km: 14 anos, 10km: 16 anos, 21km: 18 anos, 42km: 20 anos).
* **RN04:** A categoria do atleta é definida pela idade que ele terá em 31 de dezembro do ano do evento.
* **RN05:** Para efetivar a inscrição, é obrigatório o preenchimento da ficha médica e o aceite do termo de responsabilidade.
* **RN06:** A "Classificação Geral" é composta pelos 5 primeiros colocados de cada gênero.
* **RN07:** Atletas não classificados no top 5 geral são classificados por faixas etárias: Júnior (até 17 anos), Adulto (18-49 anos) e Master (50+ anos).
* **RN08/RN10:** O cancelamento da inscrição só é permitido até a data limite definida pelo organizador.
* **RN11/RN12:** Não é permitido o cadastro de atletas ou organizadores com CPFs duplicados.
* **RNF05:** Todas as senhas de usuários devem ser armazenadas de forma segura, utilizando um algoritmo de hashing com salt.

## 🏗️ Arquitetura e Estrutura do Projeto

O projeto é estruturado seguindo uma variação do padrão arquitetural **Model-View-Controller (MVC)**, que promove a separação de responsabilidades.

* **Model (Camada de Dados):** Representa a camada de dados e lógica de negócio. É composta por múltiplos arquivos:
    * `evento.py`, `kit_de_corrida.py`, `usuario.py`, `organizador.py`: Contêm as classes de domínio que modelam as entidades do sistema.
    * `database.py`: Gerencia toda a comunicação com o banco de dados SQLite, abstraindo a complexidade das queries SQL.

* **View (Camada de Apresentação):**
    * `visao.py`: Responsável por construir todas as janelas e elementos da interface gráfica utilizando a biblioteca PySimpleGUI.

* **Controller (Camada de Controle):**
    * `main.py`: Atua como o ponto de entrada da aplicação e contém a lógica de controle. Ele gerencia o loop de eventos da interface, recebe as ações do usuário (View), aciona as operações necessárias no Model e atualiza a View com os resultados.

## 💻 Tecnologias Utilizadas

* **Linguagem:** Python
* **Banco de Dados:** SQLite
* **Interface Gráfica:** PySimpleGUI
* **Dependências:** tkcalendar

### Modelo de Domínio
O sistema é modelado através de um conjunto de classes inter-relacionadas:
* **Usuario:** Classe abstrata com os atributos comuns a todos os usuários, como `cpf`, `nome` e `email`.
* **Atleta e Organizador:** Classes que herdam de `Usuario` e representam os papéis específicos no sistema.
* **Evento:** Centraliza todas as informações de uma corrida, como `distancia`, `data` e `tempoCorte`. Um organizador pode gerenciar múltiplos eventos (1:N).
* **Inscricao:** Modela o processo de inscrição, ligando um `Atleta` a um `Evento` e controlando o status da ficha médica e do termo de responsabilidade.



## 🚀 Como Executar o Projeto

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/pedroheuser/PaceHub
    cd <diretorio-do-projeto>
    ```

2.  **Instale as dependências a partir do `requirements.txt`:**
    Crie um arquivo `requirements.txt` na raiz do projeto com o seguinte conteúdo:
    ```
    pysimplegui
    tkcalendar
    ```
    Em seguida, execute o comando:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Execute a aplicação:**
    O ponto de entrada do módulo é o arquivo `main.py`.
    ```bash
    python main.py
    ```



