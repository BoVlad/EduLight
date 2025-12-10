import sqlite3


def db_init_courses():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM lessons")
    conn.commit()
    cursor.execute("""INSERT INTO courses (title, description_short, description, img, modules_quantity) 
                      VALUES (?, ?, ?, ?, ?);
                   """, ("Python для початківців",
                         "Вивчіть Python з нуля до професійного рівня через практичні приклади та проекти.",
                         "Цей курс допоможе вам освоїти мову програмування Python з нуля.\n\n"
                         "Ви пройдете всі ключові теми — від базових типів даних та умовних операторів до роботи з файлами, веб-розробки та створення власних проєктів.\n"
                         "Курс включає практичні завдання та реальні проекти, що дозволить закріпити знання та підготуватися до роботи програмістом.\n"
                         "Після завершення курсу ви зможете створювати власні програми, автоматизувати рутинні завдання та працювати з популярними бібліотеками Python.",
                         "static/images/Python.png",
                         12))
    conn.commit()
    conn.close()

def db_init_modules():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM lessons")
    conn.commit()
    cursor.execute("""INSERT INTO modules (course_id, title, module_number)
                      VALUES (1, 'Вступ до Python: основи та встановлення', 1),
                             (1, 'Типи даних та змінні', 2),
                             (1, 'Умовні оператори та логіка', 3),
                             (1, 'Цикли: for та while', 4),
                             (1, 'Функції та модулі', 5),
                             (1, 'Списки, кортежі та словники', 6),
                             (1, 'Робота з файлами', 7),
                             (1, 'Обробка помилок та виключення', 8),
                             (1, 'Об’єктно-орієнтоване програмування (ООП)', 9),
                             (1, 'Бібліотеки та пакети Python', 10),
                             (1, 'Основи веб-розробки та API', 11),
                             (1, 'Проекти та практичні завдання', 12);
                   """)
    conn.commit()
    conn.close()


def db_init_lessons():
    lessons = [
        (1, 1, "Вступ до Python",
         "Python — це високорівнева інтерпретована мова програмування.\nВона проста для початківців і потужна для професіоналів.\nPython застосовується у веб-розробці, аналізі даних, автоматизації, штучному інтелекті.\nПриклад коду:\nprint('Hello, world!')\nВиведе текст на екран.",
         1),

        (1, 1, "Історія та переваги Python",
         "Python був створений Гвідо ван Россумом у 1991 році.\nОсновні переваги:\n- Простий і читабельний синтаксис\n- Величезна спільнота та бібліотеки\n- Кросплатформеність\nPython підходить як для початківців, так і для професіоналів.",
         1),

        (1, 1, "Встановлення Python",
         "1. Завантажте Python з python.org\n2. Встановіть та оберіть 'Add Python to PATH'\n3. Перевірте:\n$ python --version\nТепер ви готові до програмування.",
         1),

        (1, 1, "Запуск Python: інтерпретатор та скрипти",
         "Інтерактивний режим дозволяє писати код рядок за рядком.\nЗапуск файлу:\n1. Створіть файл hello.py\n2. Напишіть код:\n   print('Привіт, Python!')\n3. Запустіть:\n$ python hello.py",
         1),

        (1, 1, "Коментарі та стилі коду",
         "Коментарі починаються з #:\n# Це коментар\nРекомендації по стилю (PEP8):\n- 4 пробіли для відступу\n- Зрозумілі назви змінних\n- Логічна структура коду",
         1),

        (1, 1, "Типи даних у Python",
         "Основні типи:\n- int — цілі числа\n- float — числа з плаваючою комою\n- str — рядки\n- bool — логічні значення\nПриклад:\nx = 5\ny = 2.5\nname = 'Vlad'\nis_active = True",
         1),

        (1, 1, "Змінні та базові операції",
         "Змінні зберігають дані:\nx = 10\ny = 3\nСкладові операції:\nСума: x + y\nРізниця: x - y\nДобуток: x * y\nДілення: x / y\nЦілочисельне ділення: x // y\nЗалишок від ділення: x % y",
         1),

        (1, 1, "Функція print() та форматування рядків",
         "Функція print() виводить дані на екран.\nprint('Привіт', 'Python')\nФорматування рядків:\nname = 'Vlad'\nage = 20\nprint(f'Мене звати {name} і мені {age} років')",
         1)
    ]


    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM lessons")
    conn.commit()
    cursor.executemany("""
                       INSERT INTO lessons (course_id, module_number, title, content, module_id)
                       VALUES (?, ?, ?, ?, ?)
                       """, lessons)
    conn.commit()
    lessons_module2 = [
        (1, 2, "Огляд типів даних у Python",
         "Python має основні типи даних:\n"
         "- int — цілі числа\n"
         "- float — числа з плаваючою комою\n"
         "- str — рядки\n"
         "- bool — логічні значення\n"
         "- None — пусте значення\n"
         "Приклад:\nx = 10\ny = 3.14\nname = 'Vlad'\nis_active = True\nnothing = None", 2),

        (1, 2, "Числові типи: int та float",
         "Тип int — це цілі числа, наприклад: 5, -10, 0\n"
         "Тип float — числа з плаваючою комою: 3.14, -2.5, 0.0\n"
         "Операції з числами:\n"
         "a = 7\nb = 3\nСума: a + b => 10\nРізниця: a - b => 4\nДобуток: a * b => 21\nДілення: a / b => 2.3333\nЦілочисельне ділення: a // b => 2\nЗалишок від ділення: a % b => 1",
         2),

        (1, 2, "Рядки (str)",
         "Рядки — це текстові дані.\nПриклади:\nname = 'Vlad'\ngreeting = \"Привіт!\"\nКонкатенація:\nfull = name + ' ' + greeting\nПовторення:\n'Hi! ' * 3 => 'Hi! Hi! Hi! '\nДоступ до символів:\nname[0] => 'V'\nСлайси:\nname[0:3] => 'Vla'",
         2),

        (1, 2, "Булеві значення (bool)",
         "Булеві значення можуть бути True або False.\nВони використовуються в умовах та логічних операціях.\nПриклади:\nis_active = True\nis_admin = False\nЛогічні операції:\nnot is_active => False\nis_active and is_admin => False\nis_active or is_admin => True",
         2),

        (1, 2, "None та типи даних",
         "None — це спеціальне значення, що позначає відсутність даних.\nПриклад:\nx = None\nif x is None:\n    print('Змінна порожня')\nФункції можуть повертати None, якщо нічого не повертають явно.",
         2),

        (1, 2, "Змінні: оголошення та присвоєння",
         "Змінні — це іменовані посилання на дані.\nОголошення та присвоєння:\nx = 5\ny = 'Hello'\nis_active = True\nPython динамічно визначає тип змінної.\nПеревірка типу: type(x) => <class 'int'>",
         2),

        (1, 2, "Перетворення типів (Type Casting)",
         "Іноді потрібно змінити тип даних:\nint(x) — перетворення у ціле число\nfloat(x) — у число з плаваючою комою\nstr(x) — у рядок\nbool(x) — у булеве значення\nПриклад:\nx = '10'\ny = int(x) + 5  # результат 15",
         2),

        (1, 2, "Базові операції зі змінними",
         "Математичні операції:\na = 7\nb = 3\nСума: a + b => 10\nРізниця: a - b => 4\nДобуток: a * b => 21\nДілення: a / b => 2.3333\nЦілочисельне ділення: a // b => 2\nЗалишок: a % b => 1\nЛогічні операції:\nx = True\ny = False\nx and y => False\nx or y => True\nnot x => False",
         2)
    ]
    cursor.executemany("""
                       INSERT INTO lessons (course_id, module_number, title, content, module_id)
                       VALUES (?, ?, ?, ?, ?)
                       """, lessons_module2)
    conn.commit()
    lessons_module3 = [
        (1, 3, "Умовні оператори: if, else, elif",
         "Умовні оператори дозволяють виконувати код залежно від умови.\n"
         "Синтаксис:\n"
         "if умова:\n"
         "    блок_коду\n"
         "elif інша_умова:\n"
         "    блок_коду\n"
         "else:\n"
         "    блок_коду\n"
         "Приклад:\nx = 5\nif x > 0:\n    print('x додатнє')\nelif x < 0:\n    print('x від’ємне')\nelse:\n    print('x = 0')",
         3),

        (1, 3, "Логічні оператори: and, or, not",
         "Логічні оператори дозволяють об’єднувати умови.\n"
         "and — обидві умови True\n"
         "or — хоча б одна умова True\n"
         "not — заперечення\n"
         "Приклад:\nx = 5\ny = 10\nif x > 0 and y > 0:\n    print('Обидва додатні')\nif x < 0 or y > 0:\n    print('Хоча б одна умова True')\nif not x == 0:\n    print('x не нуль')",
         3),

        (1, 3, "Вкладені умови",
         "Можна вставляти одну умову в іншу для більш складної логіки.\n"
         "Приклад:\nx = 10\ny = -5\nif x > 0:\n    if y > 0:\n        print('Обидва додатні')\n    else:\n        print('x додатнє, y від’ємне')\nelse:\n    print('x від’ємне або нуль')",
         3),

        (1, 3, "Порівняння чисел",
         "Оператори порівняння:\n"
         "== рівність\n!= нерівність\n> більше\n< менше\n>= більше або рівно\n<= менше або рівно\n"
         "Приклад:\nx = 7\ny = 3\nprint(x == y)  # False\nprint(x != y)  # True\nprint(x > y)   # True", 3),

        (1, 3, "Перевірка значень у списках та рядках",
         "Можна перевіряти, чи належить елемент колекції:\n"
         "fruits = ['apple', 'banana', 'cherry']\nif 'apple' in fruits:\n    print('Яблуко є у списку')\nif 'orange' not in fruits:\n    print('Апельсина немає')",
         3),

        (1, 3, "Умовні вирази (тернарний оператор)",
         "Тернарний оператор дозволяє записати умовне присвоєння в один рядок.\n"
         "Приклад:\nx = 10\ny = 5\nmax_value = x if x > y else y\nprint(max_value)  # 10", 3),

        (1, 3, "Практика: перевірка парності числа",
         "Напишемо програму для перевірки парності числа:\n"
         "num = int(input('Введіть число: '))\nif num % 2 == 0:\n    print('Число парне')\nelse:\n    print('Число непарне')",
         3),

        (1, 3, "Практика: категоризація віку",
         "Напишемо програму для визначення категорії людини за віком:\n"
         "age = int(input('Введіть ваш вік: '))\nif age < 13:\n    print('Дитина')\nelif age < 20:\n    print('Підліток')\nelif age < 65:\n    print('Дорослий')\nelse:\n    print('Пенсіонер')",
         3)
    ]

    cursor.executemany("""
                       INSERT INTO lessons (course_id, module_number, title, content, module_id)
                       VALUES (?, ?, ?, ?, ?)
                       """, lessons_module3)
    conn.commit()
    lessons_module4 = [
        (1, 4, "Вступ до циклів у Python",
         "Цикли дозволяють повторювати блок коду кілька разів.\n"
         "У Python є два основних типи циклів: for та while.\n"
         "Цикли зручні для обробки списків, чисел та інших колекцій.", 4),

        (1, 4, "Цикл for",
         "Цикл for використовується для перебору послідовностей (списків, рядків, діапазонів).\n"
         "Приклад:\nfruits = ['apple', 'banana', 'cherry']\nfor fruit in fruits:\n    print(fruit)\n"
         "Виведе всі елементи списку по черзі.", 4),

        (1, 4, "Функція range() у циклі for",
         "range() дозволяє створювати послідовності чисел.\nПриклад:\nfor i in range(5):\n    print(i)\n# Виведе 0,1,2,3,4\nrange(start, stop, step) — можна вказати початок, кінець та крок.",
         4),

        (1, 4, "Цикл while",
         "Цикл while виконує блок коду поки умова True.\nПриклад:\ni = 0\nwhile i < 5:\n    print(i)\n    i += 1\n# Виведе 0,1,2,3,4",
         4),

        (1, 4, "Команди break та continue",
         "break — припиняє виконання циклу\ncontinue — пропускає поточну ітерацію\nПриклад:\nfor i in range(5):\n    if i == 3:\n        break\n    print(i)\n# Виведе 0,1,2\nfor i in range(5):\n    if i == 2:\n        continue\n    print(i)\n# Виведе 0,1,3,4",
         4),

        (1, 4, "Вкладені цикли",
         "Цикли можна вкладати один в інший для роботи з матрицями або таблицями.\nПриклад:\nfor i in range(3):\n    for j in range(2):\n        print(f'i={i}, j={j}')",
         4),

        (1, 4, "Практика: сума чисел від 1 до 100",
         "Напишемо програму, яка рахує суму чисел від 1 до 100.\n"
         "total = 0\nfor i in range(1, 101):\n    total += i\nprint('Сума:', total)", 4),

        (1, 4, "Практика: вивід парних чисел",
         "Виведемо всі парні числа від 1 до 20.\n"
         "i = 1\nwhile i <= 20:\n    if i % 2 == 0:\n        print(i)\n    i += 1", 4)
    ]

    # Вставка уроків у таблицю
    cursor.executemany("""
                       INSERT INTO lessons (course_id, module_number, title, content, module_id)
                       VALUES (?, ?, ?, ?, ?)
                       """, lessons_module4)

    conn.commit()
    lessons_module5 = [
        (1, 5, "Вступ у функції",
         "Функції дозволяють групувати код для повторного використання.\n"
         "Синтаксис:\ndef назва_функції(аргументи):\n    блок_коду\n"
         "Приклад:\ndef greet(name):\n    print(f'Привіт, {name}!')\ngreet('Vlad')", 5),
        (1, 5, "Параметри та аргументи функцій",
         "Функції можуть приймати аргументи та повертати значення.\n"
         "Приклад:\ndef add(a, b):\n    return a + b\nresult = add(5, 3)\nprint(result)  # 8", 5),
        (1, 5, "Повернення значення return",
         "Ключове слово return дозволяє функції повертати результат.\n"
         "Приклад:\ndef multiply(a, b):\n    return a * b\nprint(multiply(4, 5))  # 20", 5),
        (1, 5, "Локальні та глобальні змінні",
         "Локальні змінні існують лише всередині функції, глобальні — поза функцією.\n"
         "Приклад:\nx = 10\ndef test():\n    y = 5\n    print(y)\n    print(x)\ntest()", 5),
        (1, 5, "Аргументи за замовчуванням",
         "Можна вказувати значення за замовчуванням для параметрів.\n"
         "Приклад:\ndef greet(name='Гість'):\n    print(f'Привіт, {name}!')\ngreet()  # Привіт, Гість!", 5),
        (1, 5, "Модулі та імпорт",
         "Модулі — це файли з кодом Python, які можна підключати.\n"
         "Приклад:\nimport math\nprint(math.sqrt(16))  # 4.0", 5),
        (1, 5, "Практика: функція для обчислення факторіалу",
         "def factorial(n):\n    result = 1\n    for i in range(1, n+1):\n        result *= i\n    return result\nprint(factorial(5))  # 120",
         5),
        (1, 5, "Практика: використання декількох модулів",
         "import math, random\nprint(math.pow(2,3))  # 8.0\nprint(random.randint(1,10))  # випадкове число", 5)
    ]

    # Модуль 6: Списки, кортежі та словники
    lessons_module6 = [
        (1, 6, "Списки (list)",
         "Списки зберігають кілька значень.\nПример:\nfruits = ['apple', 'banana', 'cherry']\nprint(fruits[0])  # apple\nfruits.append('orange')",
         6),
        (1, 6, "Операції зі списками",
         "Додавання елементів: append(), insert()\nВидалення: remove(), pop()\nПерегляд: len(fruits), fruits[1:3]", 6),
        (1, 6, "Кортежі (tuple)",
         "Кортежі — незмінні послідовності.\nПриклад:\ncolors = ('red', 'green', 'blue')\nprint(colors[0])", 6),
        (1, 6, "Операції з кортежами",
         "Доступ до елементів, слайси, перевірка належності:\n'red' in colors => True", 6),
        (1, 6, "Словники (dict)",
         "Словники зберігають пари ключ-значення.\nПриклад:\nperson = {'name':'Vlad','age':20}\nprint(person['name'])  # Vlad",
         6),
        (1, 6, "Методи словників",
         "person.keys(), person.values(), person.items()\nperson.update({'city':'Kyiv'})", 6),
        (1, 6, "Практика: список та словник",
         "fruits = ['apple','banana']\nperson = {'name':'Vlad'}\nfruits.append('orange')\nperson['age']=20\nprint(fruits, person)",
         6),
        (1, 6, "Вкладені структури даних",
         "Словник у словнику, список у словнику:\ndata = {'students':[{'name':'Vlad'},{'name':'Anna'}]}\nprint(data['students'][0]['name'])  # Vlad",
         6)
    ]

    # Модуль 7: Робота з файлами
    lessons_module7 = [
        (1, 7, "Відкриття та закриття файлів",
         "Відкриття: open('file.txt', 'r')\nЗакриття: file.close()\nПриклад:\nfile = open('data.txt','r')\ncontent = file.read()\nfile.close()",
         7),
        (1, 7, "Читання файлів",
         "read() читає весь файл\nreadline() читає рядок\nreadlines() читає всі рядки у список", 7),
        (1, 7, "Запис у файл",
         "w — запис, r — читання, a — додавання\nfile = open('data.txt','w')\nfile.write('Hello World')\nfile.close()",
         7),
        (1, 7, "Менеджер контексту with",
         "Зручний спосіб працювати з файлами:\nwith open('data.txt','r') as file:\n    content = file.read()", 7),
        (1, 7, "Робота з CSV",
         "import csv\nwith open('data.csv', newline='') as csvfile:\n    reader = csv.reader(csvfile)\n    for row in reader:\n        print(row)",
         7),
        (1, 7, "Робота з JSON",
         "import json\nwith open('data.json') as f:\n    data = json.load(f)\nprint(data)", 7),
        (1, 7, "Практика: підрахунок рядків у файлі",
         "with open('data.txt') as f:\n    lines = f.readlines()\nprint(len(lines))", 7),
        (1, 7, "Практика: запис списку у файл",
         "fruits = ['apple','banana']\nwith open('fruits.txt','w') as f:\n    for fruit in fruits:\n        f.write(fruit+'\\n')",
         7)
    ]

    # Модуль 8: Обробка помилок та виключення
    lessons_module8 = [
        (1, 8, "Вступ до обробки помилок",
         "Помилки можуть зупиняти програму. Використовуємо try/except для обробки.", 8),
        (1, 8, "Синтаксис try/except",
         "try:\n    # код\nexcept ExceptionType:\n    # обробка помилки\nПриклад:\ntry:\n    x = int(input())\nexcept ValueError:\n    print('Помилка')",
         8),
        (1, 8, "Блок finally",
         "finally виконується завжди:\ntry:\n    x = 1/0\nexcept ZeroDivisionError:\n    print('Ділення на нуль')\nfinally:\n    print('Завершено')",
         8),
        (1, 8, "Викидання виключень raise",
         "raise Exception('Повідомлення про помилку')\nПриклад:\ndef check_age(age):\n    if age < 0:\n        raise ValueError('Неприпустимий вік')",
         8),
        (1, 8, "Обробка декількох виключень",
         "try:\n    x = int(input())\nexcept (ValueError, TypeError) as e:\n    print('Помилка:', e)", 8),
        (1, 8, "Створення власних виключень",
         "class MyError(Exception):\n    pass\nraise MyError('Моя помилка')", 8),
        (1, 8, "Практика: безпечне ділення",
         "try:\n    a = int(input())\n    b = int(input())\n    print(a/b)\nexcept ZeroDivisionError:\n    print('Ділення на нуль')\nexcept ValueError:\n    print('Введено не число')",
         8),
        (1, 8, "Практика: робота з файлами",
         "try:\n    with open('data.txt') as f:\n        content = f.read()\nexcept FileNotFoundError:\n    print('Файл не знайдено')",
         8)
    ]

    # Модуль 9: Об’єктно-орієнтоване програмування (ООП)
    lessons_module9 = [
        (1, 9, "Класи та об’єкти",
         "Клас — шаблон для створення об’єктів.\nПриклад:\nclass Person:\n    def __init__(self, name, age):\n        self.name = name\n        self.age = age\np = Person('Vlad', 20)\nprint(p.name)",
         9),
        (1, 9, "Методи класу",
         "Методи — функції всередині класу:\nclass Person:\n    def greet(self):\n        print(f'Привіт, я {self.name}')\np = Person('Anna', 25)\np.greet()",
         9),
        (1, 9, "Наслідування",
         "Клас може наслідувати інший клас:\nclass Student(Person):\n    def study(self):\n        print(f'{self.name} навчається')",
         9),
        (1, 9, "Інкапсуляція",
         "Приховані атрибути позначаються _: self._age = age\nЗовнішній доступ через методи get/set", 9),
        (1, 9, "Поліморфізм",
         "Методи з однаковою назвою в різних класах можуть вести себе по-різному.", 9),
        (1, 9, "Практика: клас автомобіль",
         "class Car:\n    def __init__(self, model):\n        self.model = model\n    def drive(self):\n        print(f'{self.model} їде')\nc = Car('BMW')\nc.drive()",
         9),
        (1, 9, "Практика: наслідування автомобілів",
         "class ElectricCar(Car):\n    def charge(self):\n        print(f'{self.model} заряджається')\nec = ElectricCar('Tesla')\nec.drive()\nec.charge()",
         9),
        (1, 9, "Практика: інкапсуляція",
         "class Person:\n    def __init__(self, age):\n        self._age = age\n    def get_age(self):\n        return self._age\np = Person(20)\nprint(p.get_age())",
         9)
    ]

    # Модуль 10: Бібліотеки та пакети Python
    lessons_module10 = [
        (1, 10, "Що таке бібліотеки та пакети",
         "Бібліотеки — це набори готових функцій та класів.\nПакети — колекції модулів.\nПриклад імпорту: import math",
         10),
        (1, 10, "Популярні бібліотеки Python",
         "math, random, datetime, os, sys, requests, numpy, pandas, matplotlib", 10),
        (1, 10, "Імпорт модулів",
         "import math\nfrom math import sqrt\nfrom math import *", 10),
        (1, 10, "Встановлення зовнішніх пакетів",
         "pip install пакет\nНаприклад: pip install requests", 10),
        (1, 10, "Практика: використання math",
         "import math\nprint(math.sqrt(25))  # 5.0\nprint(math.factorial(5))  # 120", 10),
        (1, 10, "Практика: використання random",
         "import random\nprint(random.randint(1,10))\nprint(random.choice(['a','b','c']))", 10),
        (1, 10, "Практика: використання datetime",
         "import datetime\nnow = datetime.datetime.now()\nprint(now)\nprint(now.year, now.month, now.day)", 10),
        (1, 10, "Практика: pandas та matplotlib",
         "import pandas as pd\nimport matplotlib.pyplot as plt\ndata = pd.DataFrame({'x':[1,2,3],'y':[4,5,6]})\ndata.plot(x='x', y='y', kind='line')\nplt.show()",
         10)
    ]

    # Модуль 11: Основи веб-розробки та API
    lessons_module11 = [
        (1, 11, "Вступ до веб-розробки",
         "Python використовується у веб-розробці через фреймворки Flask, Django.\nFlask — легкий фреймворк, Django — повноцінний.",
         11),
        (1, 11, "Створення простого веб-сервера Flask",
         "from flask import Flask\napp = Flask(__name__)\n@app.route('/')\ndef home():\n    return 'Hello, world!'\napp.run()",
         11),
        (1, 11, "Маршрути у Flask",
         "@app.route('/about')\ndef about():\n    return 'About page'", 11),
        (1, 11, "Отримання даних від користувача",
         "from flask import request\n@app.route('/greet')\ndef greet():\n    name = request.args.get('name')\n    return f'Hello {name}'",
         11),
        (1, 11, "Вступ до API",
         "API — це інтерфейс для взаємодії між програмами.\nПриклад: використання requests для отримання даних", 11),
        (1, 11, "Запити через requests",
         "import requests\nresponse = requests.get('https://api.github.com')\nprint(response.status_code)\nprint(response.json())",
         11),
        (1, 11, "Практика: отримання погоди",
         "import requests\ncity = 'Kyiv'\napi_key = 'ваш_ключ'\nurl = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'\nresponse = requests.get(url)\ndata = response.json()\nprint(data)",
         11),
        (1, 11, "Практика: POST-запит",
         "import requests\nurl = 'https://httpbin.org/post'\ndata = {'name':'Vlad'}\nresponse = requests.post(url, json=data)\nprint(response.json())",
         11)
    ]

    # Модуль 12: Проекти та практичні завдання
    lessons_module12 = [
        (1, 12, "Проект: калькулятор",
         "Створимо консольний калькулятор:\nnum1 = int(input())\nnum2 = int(input())\nprint(num1+num2)", 12),
        (1, 12, "Проект: список справ",
         "tasks = []\ntasks.append('Buy milk')\nfor task in tasks:\n    print(task)", 12),
        (1, 12, "Проект: генератор паролів",
         "import random, string\npassword = ''.join(random.choices(string.ascii_letters + string.digits, k=8))\nprint(password)",
         12),
        (1, 12, "Проект: гра 'Вгадай число'",
         "import random\nnum = random.randint(1,10)\nguess = int(input())\nif guess == num:\n    print('Вгадали!')\nelse:\n    print('Не вгадали')",
         12),
        (1, 12, "Практика з файлами",
         "with open('data.txt','w') as f:\n    f.write('Hello World')", 12),
        (1, 12, "Проект: робота з API",
         "import requests\nresponse = requests.get('https://api.github.com')\nprint(response.json())", 12),
        (1, 12, "Проект: аналіз даних",
         "import pandas as pd\ndata = pd.DataFrame({'x':[1,2,3],'y':[4,5,6]})\nprint(data.describe())", 12),
        (1, 12, "Проект: графіки",
         "import matplotlib.pyplot as plt\nplt.plot([1,2,3],[4,5,6])\nplt.show()", 12)
    ]


    all_lessons = (lessons_module5 + lessons_module6 + lessons_module7 + lessons_module8 +
                   lessons_module9 + lessons_module10 + lessons_module11 + lessons_module12)


    cursor.executemany("""
                       INSERT INTO lessons (course_id, module_number, title, content, module_id)
                       VALUES (?, ?, ?, ?, ?)
                       """, all_lessons)
    conn.close()

if __name__ == '__main__':
    db_init_courses()
    db_init_modules()
    db_init_lessons()