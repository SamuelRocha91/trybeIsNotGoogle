# <img src="https://cdn-icons-png.flaticon.com/128/1822/1822921.png" alt="Trybe Logo" width="52" height="30" /> Проект Trybe не Google <img src="https://cdn-icons-png.flaticon.com/128/1822/1822921.png" alt="Trybe Logo" width="52" height="30" />

## 🌐 
[![Португальский](https://img.shields.io/badge/Português-green)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README.md)
[![Испанский](https://img.shields.io/badge/Español-yellow)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README_es.md)
[![Английский](https://img.shields.io/badge/English-blue)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README_en.md)
[![Русский](https://img.shields.io/badge/Русский-lightgrey)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README_ru.md)
[![Китайский](https://img.shields.io/badge/中文-red)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README_ch.md)
[![Арабский](https://img.shields.io/badge/العربية-orange)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README_ar.md)

<details>
<summary> 
  <h2>
    О Проекте
  </h2>
</summary>

Приложение представляет собой систему управления файлами и поисковыми операциями, которая позволяет отслеживать вхождение терминов в текстовые файлы. Проект разделен на два основных модуля:

1. **Модуль управления файлами**: Отвечает за прикрепление и управление текстовыми файлами в системе.
2. **Модуль поиска**: Отвечает за выполнение поисковых операций по прикрепленным файлам, находя определенные термины в документах.

Этот проект **не выполняет семантический анализ** и поиск синонимов.

</details>

<details>
<summary><h2>Развитые Навыки</h2></summary>

В этом проекте отрабатывались следующие навыки:

- Работа с **Стек**;
- Работа с **Дек**;
- Работа с **Узлы и Связанные Списки**;
- Работа с **Двусвязные Списки**;
- Работа с файлами `.txt`.

</details>

<details>
<summary><h2>Структура Проекта</h2></summary>

Проект имеет следующую структуру каталогов и файлов:

```
.
├── dev-requirements.txt           # Требования для разработки
├── pyproject.toml                 # Настройки проекта Python
├── README.md                      # Документация проекта
├── requirements.txt               # Требования для продакшн
├── setup.cfg                      # Дополнительная конфигурация
├── setup.py                       # Скрипт установки проекта
├── statics                        # Каталог с примерами файлов
│   ├── arquivo_teste.csv
│   ├── arquivo_teste.txt
│   ├── nome_pedro.txt
│   ├── novo_paradigma_globalizado-min.txt
│   └── novo_paradigma_globalizado.txt
├── tests                          # Каталог с тестами
│   ├── __init__.py
│   ├── test_file_management.py
│   ├── test_file_process.py
│   ├── test_queue.py
│   └── test_word_search.py
├── ting_file_management           # Модуль управления файлами
│   ├── file_management.py         # Основной код управления
│   ├── file_process.py            # Обработка файлов
│   ├── __init__.py
│   └── queue.py                   # Реализация очереди (Queue)
├── ting_word_searches             # Модуль поиска слов
│   ├── __init__.py
│   └── word_search.py             # Функции поиска терминов
└── trybe.yml                      # Конфигурация проекта Trybe
```

</details>

<details>
<summary><h2>Как Запустить</h2></summary>

### Предварительные Требования

Перед началом работы убедитесь, что у вас установлен Python. Для установки зависимостей проекта выполните следующие шаги:

1. Клонируйте репозиторий:
   ```bash
   git clone git@github.com:SamuelRocha91/trybeIsNotGoogle.git
   ```

2. Перейдите в каталог проекта:
   ```bash
   cd проект-trybe-не-google
   ```

3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

4. Для запуска проекта используйте команду:
   ```bash
   python -m ting_file_management.file_management
   ```

</details>

<details>
<summary><h2>Тесты</h2></summary>

Для запуска тестов используйте следующую команду:

```bash
pytest
```

Тесты находятся в каталоге `tests` и охватывают основные функции управления файлами, поиска слов и работы с очередями (queue).

</details>

<details>
<summary><h2>Другие Проекты</h2></summary>

-  [Заказы Ресторана](https://github.com/SamuelRocha91/restaurantOrders/blob/main/README_ru.md)
-  [Скрипты](https://github.com/SamuelRocha91/scripts/blob/main/README_ru.md)
-  [Алгоритмы](https://github.com/SamuelRocha91/Algorithms/blob/main/README_ru.md)

</details>
