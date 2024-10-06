# <img src="https://cdn-icons-png.flaticon.com/128/1822/1822921.png" alt="Trybe Logo" width="52" height="30" /> 项目 Trybe 不是 Google <img src="https://cdn-icons-png.flaticon.com/128/1822/1822921.png" alt="Trybe Logo" width="52" height="30" />

## 🌐 
[![葡萄牙语](https://img.shields.io/badge/Português-green)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README.md)
[![西班牙语](https://img.shields.io/badge/Español-yellow)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README_es.md)
[![英语](https://img.shields.io/badge/English-blue)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README_en.md)
[![俄语](https://img.shields.io/badge/Русский-lightgrey)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README_ru.md)
[![中文](https://img.shields.io/badge/中文-red)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README_ch.md)
[![阿拉伯语](https://img.shields.io/badge/العربية-orange)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README_ar.md)

<details>
<summary> 
  <h2>
    关于项目
  </h2>
</summary>

该应用程序是一个文件管理和搜索操作系统，允许在文本文件中映射术语的出现。 该项目分为两个主要模块：

1. **文件管理模块**：负责附加和管理系统中的文本文件。
2. **搜索模块**：负责对附加的文件执行搜索操作，查找文档中的特定术语。

该项目**不执行语义分析**或同义词搜索。

</details>

<details>
<summary><h2>开发的技能</h2></summary>

在该项目中，练习了以下技能：

- 操作 **堆栈**；
- 操作 **双端队列**；
- 操作 **节点和链表**；
- 操作 **双向链表**；
- 操作 `.txt` 文件。

</details>

<details>
<summary><h2>项目结构</h2></summary>

该项目的目录和文件结构如下：

```
.
├── dev-requirements.txt           # 开发要求
├── pyproject.toml                 # Python 项目配置
├── README.md                      # 文档文件
├── requirements.txt               # 生产环境要求
├── setup.cfg                      # 其他设置配置
├── setup.py                       # 项目安装脚本
├── statics                        # 包含示例文件的目录
│   ├── arquivo_teste.csv
│   ├── arquivo_teste.txt
│   ├── nome_pedro.txt
│   ├── novo_paradigma_globalizado-min.txt
│   └── novo_paradigma_globalizado.txt
├── tests                          # 测试目录
│   ├── __init__.py
│   ├── test_file_management.py
│   ├── test_file_process.py
│   ├── test_queue.py
│   └── test_word_search.py
├── ting_file_management           # 文件管理模块
│   ├── file_management.py         # 文件管理主代码
│   ├── file_process.py            # 文件处理
│   ├── __init__.py
│   └── queue.py                   # 队列实现 (Queue)
├── ting_word_searches             # 词汇搜索模块
│   ├── __init__.py
│   └── word_search.py             # 搜索术语功能
└── trybe.yml                      # Trybe 项目配置
```

</details>

<details>
<summary><h2>如何运行</h2></summary>

### 先决条件

在开始之前，请确保您的计算机上安装了 Python。 按照以下步骤安装项目依赖项：

1. 克隆存储库：
   ```bash
   git clone git@github.com:SamuelRocha91/trybeIsNotGoogle.git
   ```

2. 进入项目目录：
   ```bash
   cd project-trybe-not-google
   ```

3. 安装依赖项：
   ```bash
   pip install -r requirements.txt
   ```

4. 要运行项目，请使用以下命令：
   ```bash
   python -m ting_file_management.file_management
   ```

</details>

<details>
<summary><h2>测试</h2></summary>

要运行测试，请使用以下命令：

```bash
pytest
```

测试位于 `tests` 目录中，涵盖了文件管理、单词搜索和队列操作的主要功能。

</details>

<details>
<summary><h2>其他项目</h2></summary>

-  [餐厅订单](https://github.com/SamuelRocha91/restaurantOrders/blob/main/README_ch.md)
-  [脚本](https://github.com/SamuelRocha91/scripts/blob/main/README_ch.md)
-  [算法](https://github.com/SamuelRocha91/Algorithms/blob/main/README_ch.md)

</details>
