# <img src="https://cdn-icons-png.flaticon.com/128/1822/1822921.png" alt="Trybe Logo" width="52" height="30" /> Proyecto Trybe no es Google <img src="https://cdn-icons-png.flaticon.com/128/1822/1822921.png" alt="Trybe Logo" width="52" height="30" />

## 🌐 
[![Portugués](https://img.shields.io/badge/Português-green)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README.md)
[![Español](https://img.shields.io/badge/Español-yellow)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README_es.md)
[![Inglés](https://img.shields.io/badge/English-blue)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README_en.md)
[![Ruso](https://img.shields.io/badge/Russian-lightgrey)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README_ru.md)
[![Chino](https://img.shields.io/badge/Chinese-red)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README_ch.md)
[![Árabe](https://img.shields.io/badge/Arabic-orange)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README_ar.md)

<details>
<summary> 
  <h2>
    Sobre el Proyecto
  </h2>
</summary>

La aplicación consiste en un sistema de gestión de archivos y operaciones de búsqueda que permite mapear la ocurrencia de términos en archivos de texto. El proyecto está dividido en dos módulos principales:

1. **Módulo de Gestión de Archivos**: Responsable de adjuntar y gestionar archivos de texto en el sistema.
2. **Módulo de Búsquedas**: Responsable de realizar operaciones de búsqueda en los archivos adjuntos, encontrando términos específicos dentro de los documentos.

Este proyecto **no realiza análisis semántico** ni búsqueda de sinónimos.

</details>

<details>
<summary><h2>Habilidades Desarrolladas</h2></summary>

En este proyecto, se practicaron las siguientes habilidades:

- Manipulación de **Pilas**;
- Manipulación de **Deque**;
- Manipulación de **Nodos y Listas Enlazadas**;
- Manipulación de **Listas Doblemente Enlazadas**;
- Manipulación de archivos `.txt`.

</details>

<details>
<summary><h2>Estructura del Proyecto</h2></summary>

El proyecto sigue esta estructura de directorios y archivos:

```
.
├── dev-requirements.txt           # Requisitos de desarrollo
├── pyproject.toml                 # Configuración del proyecto Python
├── README.md                      # Archivo de documentación
├── requirements.txt               # Requisitos de producción
├── setup.cfg                      # Configuración adicional de setup
├── setup.py                       # Script de instalación del proyecto
├── statics                        # Directorio que contiene archivos de ejemplo
│   ├── archivo_teste.csv
│   ├── archivo_teste.txt
│   ├── nome_pedro.txt
│   ├── novo_paradigma_globalizado-min.txt
│   └── novo_paradigma_globalizado.txt
├── tests                          # Directorio que contiene las pruebas
│   ├── __init__.py
│   ├── test_file_management.py
│   ├── test_file_process.py
│   ├── test_queue.py
│   └── test_word_search.py
├── ting_file_management           # Módulo de gestión de archivos
│   ├── file_management.py         # Código principal de gestión de archivos
│   ├── file_process.py            # Procesamiento de archivos
│   ├── __init__.py
│   └── queue.py                   # Implementación de la cola (Queue)
├── ting_word_searches             # Módulo de búsqueda de palabras
│   ├── __init__.py
│   └── word_search.py             # Funciones de búsqueda de términos
└── trybe.yml                      # Configuración del proyecto Trybe
```

</details>

<details>
<summary><h2>Cómo Ejecutar</h2></summary>

### Prerrequisitos

Antes de comenzar, asegúrese de tener Python instalado en su máquina. Para instalar las dependencias del proyecto, siga los siguientes pasos:

1. Clone el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/proyecto-trybe-no-es-google.git
   ```

2. Acceda al directorio del proyecto:
   ```bash
   cd proyecto-trybe-no-es-google
   ```

3. Instale las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Para ejecutar el proyecto, utilice el siguiente comando:
   ```bash
   python -m ting_file_management.file_management
   ```

</details>

<details>
<summary><h2>Pruebas</h2></summary>

Para ejecutar las pruebas, use el siguiente comando:

```bash
pytest
```

Las pruebas se encuentran en el directorio `tests` y cubren las principales funcionalidades de gestión de archivos, búsqueda de palabras y manipulación de colas (queue).

</details>

<details>
<summary><h2>Otros Proyectos</h2></summary>

-  [Pedidos de Restaurante](https://github.com/SamuelRocha91/restaurantOrders/blob/main/README_es.md)
-  [Scripts](https://github.com/SamuelRocha91/scripts/blob/main/README_es.md)
-  [Algoritmos](https://github.com/SamuelRocha91/Algorithms/blob/main/README_es.md)

</details>
