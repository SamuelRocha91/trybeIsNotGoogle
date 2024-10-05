# <img src="https://cdn-icons-png.flaticon.com/128/1822/1822921.png" alt="Trybe Logo" width="52" height="30" />  Trybe is not Google Project <img src="https://cdn-icons-png.flaticon.com/128/1822/1822921.png" alt="Trybe Logo" width="52" height="30" />

## 🌐 
[![Portuguese](https://img.shields.io/badge/Português-green)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README.md)
[![Spanish](https://img.shields.io/badge/Spanish-yellow)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README_es.md)
[![English](https://img.shields.io/badge/English-blue)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README_en.md)
[![Russian](https://img.shields.io/badge/Russian-lightgrey)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README_ru.md)
[![Chinese](https://img.shields.io/badge/Chinese-red)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README_ch.md)
[![Arabic](https://img.shields.io/badge/Arabic-orange)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README_ar.md)


<details>
<summary> 
  <h2>
    About the Project
  </h2>
</summary>

The application is a file management and search system that allows mapping the occurrence of terms in text files. The project is divided into two main modules:

1. **File Management Module**: Responsible for attaching and managing text files in the system.
2. **Search Module**: Responsible for performing search operations in the attached files, finding specific terms within the documents.

This project **does not perform semantic analysis** or search for synonyms.

</details>

<details>
<summary><h2>Skills Developed</h2></summary>

In this project, the following skills were practiced:

- Manipulation of **Stacks**;
- Manipulation of **Deque**;
- Manipulation of **Node & Linked Lists**;
- Manipulation of **Doubly Linked Lists**;
- Manipulation of `.txt` files.

</details>

<details>
<summary><h2>Project Structure</h2></summary>

The project follows this directory and file structure:

```
.
├── dev-requirements.txt           # Development requirements
├── pyproject.toml                 # Python project configuration
├── README.md                      # Documentation file
├── requirements.txt               # Production requirements
├── setup.cfg                      # Additional setup configuration
├── setup.py                       # Project installation script
├── statics                        # Directory containing example files
│   ├── arquivo_teste.csv
│   ├── arquivo_teste.txt
│   ├── nome_pedro.txt
│   ├── novo_paradigma_globalizado-min.txt
│   └── novo_paradigma_globalizado.txt
├── tests                          # Directory containing the tests
│   ├── __init__.py
│   ├── test_file_management.py
│   ├── test_file_process.py
│   ├── test_queue.py
│   └── test_word_search.py
├── ting_file_management           # File management module
│   ├── file_management.py         # Main file management code
│   ├── file_process.py            # File processing
│   ├── __init__.py
│   └── queue.py                   # Queue implementation
├── ting_word_searches             # Word search module
│   ├── __init__.py
│   └── word_search.py             # Term search functions
└── trybe.yml                      # Trybe project configuration
```

</details>

<details>
<summary><h2>How to Run</h2></summary>

### Prerequisites

Before you begin, make sure Python is installed on your machine. To install the project dependencies, follow the steps below:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/trybe-is-not-google-project.git
   ```

2. Navigate to the project directory:
   ```bash
   cd trybe-is-not-google-project
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. To run the project, use the following command:
   ```bash
   python -m ting_file_management.file_management
   ```

</details>

<details>
<summary><h2>Tests</h2></summary>

To run the tests, use the following command:

```bash
pytest
```

The tests are located in the `tests` directory and cover the main features of file management, word search, and queue manipulation.

</details>

<details>
<summary><h2>Other Projects</h2></summary>

-  [Restaurant Orders](https://github.com/SamuelRocha91/restaurantOrders/blob/main/README_en.md)
-  [Scripts](https://github.com/SamuelRocha91/scripts/blob/main/README_en.md)
-  [Algorithms](https://github.com/SamuelRocha91/Algorithms/blob/main/README_en.md)
-  [Trybe is not Google](https://ithub.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README_en.md)

</details>
