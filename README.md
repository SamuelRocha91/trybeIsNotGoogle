# <img src="https://cdn-icons-png.flaticon.com/128/1822/1822921.png" alt="Trybe Logo" width="52" height="30" />  Projeto Trybe is not Google <img src="https://cdn-icons-png.flaticon.com/128/1822/1822921.png" alt="Trybe Logo" width="52" height="30" />

## 🌐 
[![Português](https://img.shields.io/badge/Português-green)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README.md)
[![Español](https://img.shields.io/badge/Español-yellow)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README_es.md)
[![English](https://img.shields.io/badge/English-blue)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README_en.md)
[![Русский](https://img.shields.io/badge/Русский-lightgrey)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README_ru.md)
[![中文](https://img.shields.io/badge/中文-red)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README_ch.md)
[![العربية](https://img.shields.io/badge/العربية-orange)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README_ar.md)


<details>
<summary> 
  <h2>
    Sobre o Projeto
  </h2>
</summary>

A aplicação consiste em um sistema gerenciador de arquivos e operações de busca que permitem o mapeamento da ocorrência de termos em arquivos de texto. O projeto está dividido em dois módulos principais:

1. **Módulo de Gerenciamento de Arquivos**: Responsável por anexar e gerenciar arquivos de texto no sistema.
2. **Módulo de Buscas**: Responsável por realizar operações de busca nos arquivos anexados, encontrando termos específicos dentro dos documentos.

Este projeto **não realiza análise semântica** ou busca por sinônimos.

</details>

<details>
<summary><h2>Habilidades Desenvolvidas</h2></summary>

Neste projeto, foram exercitadas as seguintes habilidades:

- Manipulação de **Pilhas**;
- Manipulação de **Deque**;
- Manipulação de **Nó & Listas Ligadas**;
- Manipulação de **Listas Duplamente Ligadas**;
- Manipulação de arquivos `.txt`.

</details>

<details>
<summary><h2>Estrutura do Projeto</h2></summary>

O projeto segue a seguinte estrutura de diretórios e arquivos:

```
.
├── dev-requirements.txt           # Requisitos de desenvolvimento
├── pyproject.toml                 # Configuração do projeto Python
├── README.md                      # Arquivo de documentação
├── requirements.txt               # Requisitos de produção
├── setup.cfg                      # Configuração adicional de setup
├── setup.py                       # Script de instalação do projeto
├── statics                        # Diretório contendo arquivos de exemplo
│   ├── arquivo_teste.csv
│   ├── arquivo_teste.txt
│   ├── nome_pedro.txt
│   ├── novo_paradigma_globalizado-min.txt
│   └── novo_paradigma_globalizado.txt
├── tests                          # Diretório contendo os testes
│   ├── __init__.py
│   ├── test_file_management.py
│   ├── test_file_process.py
│   ├── test_queue.py
│   └── test_word_search.py
├── ting_file_management           # Módulo de gerenciamento de arquivos
│   ├── file_management.py         # Código principal de gerenciamento
│   ├── file_process.py            # Processamento de arquivos
│   ├── __init__.py
│   └── queue.py                   # Implementação da fila (Queue)
├── ting_word_searches             # Módulo de busca de palavras
│   ├── __init__.py
│   └── word_search.py             # Funções de busca de termos
└── trybe.yml                      # Configurações do projeto Trybe
```

</details>

<details>
<summary><h2>Como Executar</h2></summary>

### Pré-requisitos

Antes de começar, certifique-se de ter o Python instalado em sua máquina. Para instalar as dependências do projeto, siga os passos abaixo:

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/projeto-trybe-is-not-google.git
   ```

2. Acesse o diretório do projeto:
   ```bash
   cd projeto-trybe-is-not-google
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Para executar o projeto, utilize o comando:
   ```bash
   python -m ting_file_management.file_management
   ```

</details>

<details>
<summary><h2>Testes</h2></summary>

Para rodar os testes, execute o seguinte comando:

```bash
pytest
```

Os testes estão localizados no diretório `tests` e cobrem as funcionalidades principais de gerenciamento de arquivos, busca de palavras e manipulação de filas (queue).

</details>

<details>
<summary><h2>Outros projetos</h2></summary>

-  [Restaurant Orders](https://github.com/SamuelRocha91/restaurantOrders)
-  [Scripts](https://github.com/SamuelRocha91/scripts)
-  [Algorithms](https://github.com/SamuelRocha91/Algorithms)

</details>
