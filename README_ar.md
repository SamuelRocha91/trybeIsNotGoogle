# <img src="https://cdn-icons-png.flaticon.com/128/1822/1822921.png" alt="شعار Trybe" width="52" height="30" /> مشروع Trybe ليس Google <img src="https://cdn-icons-png.flaticon.com/128/1822/1822921.png" alt="شعار Trybe" width="52" height="30" />

## 🌐 
[![البرتغالية](https://img.shields.io/badge/Português-green)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README.md)
[![الإسبانية](https://img.shields.io/badge/Español-yellow)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README_es.md)
[![الإنجليزية](https://img.shields.io/badge/English-blue)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README_en.md)
[![الروسية](https://img.shields.io/badge/Русский-lightgrey)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README_ru.md)
[![الصينية](https://img.shields.io/badge/中文-red)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README_ch.md)
[![العربية](https://img.shields.io/badge/العربية-orange)](https://github.com/SamuelRocha91/trybeIsNotGoogle/blob/main/README_ar.md)

<details>
<summary> 
  <h2>
    حول المشروع
  </h2>
</summary>

يتكون التطبيق من نظام لإدارة الملفات وعمليات البحث التي تتيح تعيين حدوث المصطلحات في ملفات النصوص. ينقسم المشروع إلى وحدتين رئيسيتين:

1. **وحدة إدارة الملفات**: مسؤولة عن إرفاق الملفات النصية وإدارتها في النظام.
2. **وحدة البحث**: مسؤولة عن إجراء عمليات البحث في الملفات المرفقة، والعثور على مصطلحات محددة داخل المستندات.

هذا المشروع **لا يقوم بالتحليل الدلالي** أو البحث عن المرادفات.

</details>

<details>
<summary><h2>المهارات المطورة</h2></summary>

في هذا المشروع، تم تطوير المهارات التالية:

- التعامل مع **المكدسات**؛
- التعامل مع **قوائم الانتظار المزدوجة**؛
- التعامل مع **العقد والقوائم المرتبطة**؛
- التعامل مع **القوائم المزدوجة المرتبطة**؛
- التعامل مع ملفات `.txt`.

</details>

<details>
<summary><h2>هيكل المشروع</h2></summary>

يتبع المشروع الهيكل التالي للدلائل والملفات:

```
.
├── dev-requirements.txt           # متطلبات التطوير
├── pyproject.toml                 # إعداد مشروع Python
├── README.md                      # ملف التوثيق
├── requirements.txt               # متطلبات الإنتاج
├── setup.cfg                      # إعدادات إضافية
├── setup.py                       # نص التثبيت للمشروع
├── statics                        # دليل يحتوي على ملفات أمثلة
│   ├── arquivo_teste.csv
│   ├── arquivo_teste.txt
│   ├── nome_pedro.txt
│   ├── novo_paradigma_globalizado-min.txt
│   └── novo_paradigma_globalizado.txt
├── tests                          # دليل يحتوي على الاختبارات
│   ├── __init__.py
│   ├── test_file_management.py
│   ├── test_file_process.py
│   ├── test_queue.py
│   └── test_word_search.py
├── ting_file_management           # وحدة إدارة الملفات
│   ├── file_management.py         # الكود الرئيسي للإدارة
│   ├── file_process.py            # معالجة الملفات
│   ├── __init__.py
│   └── queue.py                   # تنفيذ قائمة الانتظار (Queue)
├── ting_word_searches             # وحدة البحث عن الكلمات
│   ├── __init__.py
│   └── word_search.py             # وظائف البحث عن المصطلحات
└── trybe.yml                      # إعدادات مشروع Trybe
```

</details>

<details>
<summary><h2>كيفية التشغيل</h2></summary>

### المتطلبات المسبقة

قبل البدء، تأكد من تثبيت Python على جهازك. لتثبيت التبعيات الخاصة بالمشروع، اتبع الخطوات التالية:

1. استنساخ المستودع:
   ```bash
   git clone https://github.com/your-user/project-trybe-not-google.git
   ```

2. الوصول إلى دليل المشروع:
   ```bash
   cd project-trybe-not-google
   ```

3. تثبيت التبعيات:
   ```bash
   pip install -r requirements.txt
   ```

4. لتشغيل المشروع، استخدم الأمر:
   ```bash
   python -m ting_file_management.file_management
   ```

</details>

<details>
<summary><h2>الاختبارات</h2></summary>

لتشغيل الاختبارات، قم بتنفيذ الأمر التالي:

```bash
pytest
```

تقع الاختبارات في دليل `tests` وتشمل الوظائف الرئيسية لإدارة الملفات، البحث عن الكلمات، والتعامل مع قوائم الانتظار (queue).

</details>

<details>
<summary><h2>مشاريع أخرى</h2></summary>

-  [طلبات المطعم](https://github.com/SamuelRocha91/restaurantOrders/blob/main/README_ar.md)
-  [البرامج النصية](https://github.com/SamuelRocha91/scripts/blob/main/README_ar.md)
-  [الخوارزميات](https://github.com/SamuelRocha91/Algorithms/blob/main/README_ar.md)

</details>
