lab_number = 1
description = ""
llms = []
frameworks = []
libriries = []
results = ""
conclusion = ""

def generate_report(lab_number: int, description: str, results: str, conclusion: str):

    libriries = []

    with open('source/requirements.txt') as file:
        libriries = file.read().split('\n')

    from llms import llms_list

    with open("README.md", "w", encoding='utf-8') as file:
        file.write(f"""
    # Лабораторная работа №{lab_number}

    ## Описание задания
    {description}

    ## Использованные технологии и модели
    - LLM: {", ".join(llms)}
    - Библиотеки: {", ".join(libriries)}

    ## Результаты работы
    {results}

    ## Выводы
    {conclusion}

    ## Инструкция по запуску
    1. Установить зависимости: `pip install -r source/requirements.txt`
    2. Установить Ollama
    3. Запустить скрипт: `python source/main.py`
        """)