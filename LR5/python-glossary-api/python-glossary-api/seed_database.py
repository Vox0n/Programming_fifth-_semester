import sqlite3

def seed_database(db_path='glossary.db'):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Создаем таблицу если нет
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS terms (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        term TEXT NOT NULL UNIQUE,
        definition TEXT NOT NULL,
        category TEXT DEFAULT 'General',
        example TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    python_terms = [
        # Basic Syntax
        {"term": "Variable", "definition": "Named storage location in memory", "category": "Basic Syntax",
         "example": "x = 10"},
        {"term": "Data Type", "definition": "Classification of data like int, str, bool", "category": "Basic Syntax",
         "example": "type(42) -> int"},
        {"term": "String", "definition": "Sequence of characters", "category": "Basic Syntax",
         "example": "'hello' or \"world\""},
        {"term": "Integer", "definition": "Whole number without decimal point", "category": "Basic Syntax",
         "example": "42, -7, 0"},
        {"term": "Float", "definition": "Number with decimal point", "category": "Basic Syntax",
         "example": "3.14, -0.001"},
        {"term": "Boolean", "definition": "Logical value True or False", "category": "Basic Syntax",
         "example": "True, False"},

        # Data Structures
        {"term": "List", "definition": "Ordered, mutable collection", "category": "Data Structures",
         "example": "[1, 2, 3]"},
        {"term": "Tuple", "definition": "Ordered, immutable collection", "category": "Data Structures",
         "example": "(1, 2, 3)"},
        {"term": "Dictionary", "definition": "Key-value pairs, unordered", "category": "Data Structures",
         "example": "{'name': 'John', 'age': 30}"},
        {"term": "Set", "definition": "Unordered collection of unique elements", "category": "Data Structures",
         "example": "{1, 2, 3}"},
        {"term": "Array", "definition": "Homogeneous collection (from array module)", "category": "Data Structures",
         "example": "array('i', [1, 2, 3])"},

        # Functions
        {"term": "Function", "definition": "Reusable block of code", "category": "Functions",
         "example": "def greet(): print('Hello')"},
        {"term": "Parameter", "definition": "Variable in function definition", "category": "Functions",
         "example": "def func(param): pass"},
        {"term": "Argument", "definition": "Value passed to function", "category": "Functions",
         "example": "func('argument')"},
        {"term": "Lambda", "definition": "Anonymous inline function", "category": "Functions",
         "example": "lambda x: x*2"},
        {"term": "Decorator", "definition": "Function that modifies another function", "category": "Functions",
         "example": "@staticmethod"},

        # OOP
        {"term": "Class", "definition": "Blueprint for creating objects", "category": "OOP",
         "example": "class Car: pass"},
        {"term": "Object", "definition": "Instance of a class", "category": "OOP", "example": "my_car = Car()"},
        {"term": "Inheritance", "definition": "Deriving class from parent class", "category": "OOP",
         "example": "class Dog(Animal):"},
        {"term": "Encapsulation", "definition": "Bundling data with methods", "category": "OOP",
         "example": "Private attributes with getters/setters"},
        {"term": "Polymorphism", "definition": "Same interface, different implementation", "category": "OOP",
         "example": "len() works with strings, lists, etc."},

        # Control Flow
        {"term": "If Statement", "definition": "Conditional execution", "category": "Control Flow",
         "example": "if x > 0: print('positive')"},
        {"term": "For Loop", "definition": "Iterating over sequence", "category": "Control Flow",
         "example": "for i in range(5): print(i)"},
        {"term": "While Loop", "definition": "Loop while condition is true", "category": "Control Flow",
         "example": "while x < 10: x += 1"},

        # Modules & Packages
        {"term": "Module", "definition": "Python file containing code", "category": "Modules",
         "example": "import math"},
        {"term": "Package", "definition": "Directory containing modules", "category": "Modules",
         "example": "from sklearn import linear_model"},
        {"term": "Import", "definition": "Bringing module into namespace", "category": "Modules",
         "example": "import numpy as np"},

        # Error Handling
        {"term": "Exception", "definition": "Error detected during execution", "category": "Error Handling",
         "example": "ZeroDivisionError"},
        {"term": "Try-Except", "definition": "Handling exceptions", "category": "Error Handling",
         "example": "try: x=1/0 except: print('error')"},
        {"term": "Finally", "definition": "Code that always executes", "category": "Error Handling",
         "example": "finally: close_file()"},

        # File Operations
        {"term": "Open", "definition": "Opening file for reading/writing", "category": "File Operations",
         "example": "with open('file.txt', 'r') as f:"},
        {"term": "Read", "definition": "Reading data from file", "category": "File Operations",
         "example": "content = f.read()"},
        {"term": "Write", "definition": "Writing data to file", "category": "File Operations",
         "example": "f.write('text')"},

    ]

    added = 0
    for term in python_terms:
        try:
            cursor.execute(
                'INSERT INTO terms (term, definition, category, example) VALUES (?, ?, ?, ?)',
                (term['term'], term['definition'], term['category'], term['example'])
            )
            added += 1
            print(f"  Added: {term['term']}")
        except sqlite3.IntegrityError:
            print(f"  Skipped (exists): {term['term']}")

    conn.commit()
    conn.close()
    print(f"\n  Total terms in database: {added}")

if __name__ == "__main__":
    seed_database()