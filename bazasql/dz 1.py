import pandas as pd
import psycopg2
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import seaborn as sns

# Настройка подключения к PostgreSQL
def create_connection():
    try:
        # параметры подключения
        connection = psycopg2.connect(
            host="localhost",
            database="nort",
            user="kot",
            password="123",
            port="5432"
        )
        print("Подключение к PostgreSQL успешно установлено")
        return connection
    except Exception as e:
        print(f"Ошибка подключения: {e}")
        return None

# Создание подключения через SQLAlchemy для pandas
def create_engine_connection():
    try:
        engine = create_engine('postgresql://kot:123@localhost:5432/nort')
        return engine
    except Exception as e:
        print(f"Ошибка создания engine: {e}")
        return None

# Создаем подключения
conn = create_connection()
engine = create_engine_connection()

# Запрос 1: LEFT JOIN с фильтрацией категорий
query1 = """
SELECT 
    p.*,
    c.CategoryName
FROM Products p
LEFT JOIN Categories c ON p.CategoryID = c.CategoryID
WHERE c.CategoryName LIKE 'C%'
"""

df1 = pd.read_sql(query1, conn)
print("Результат задания 1:")
print(df1.head())
print(f"Количество строк: {len(df1)}")


'''

# Запрос 2: Присоединение поставщиков и средняя цена
query2 = """
WITH ProductCategories AS (
    SELECT 
        p.*,
        c.CategoryName
    FROM Products p
    LEFT JOIN Categories c ON p.CategoryID = c.CategoryID
    WHERE c.CategoryName LIKE 'C%'
)
SELECT 
    pc.*,
    s.CompanyName as SupplierName,
    AVG(pc.UnitPrice) OVER (PARTITION BY pc.SupplierID) as AvgPriceBySupplier
FROM ProductCategories pc
LEFT JOIN Suppliers s ON pc.SupplierID = s.SupplierID
"""

df2 = pd.read_sql(query2, engine)
print("\nРезультат задания 2:")
print(df2[['ProductName', 'CategoryName', 'SupplierName', 'UnitPrice', 'AvgPriceBySupplier']].head())




# Визуализация результатов задания 2
plt.figure(figsize=(12, 6))

# Средняя цена по поставщикам
plt.subplot(1, 2, 1)
supplier_avg_prices = df2.groupby('SupplierName')['AvgPriceBySupplier'].mean().sort_values(ascending=False)
supplier_avg_prices.head(10).plot(kind='bar', color='skyblue')
plt.title('Средняя цена товара по поставщикам')
plt.xticks(rotation=45, ha='right')
plt.ylabel('Средняя цена')

# Распределение цен
plt.subplot(1, 2, 2)
plt.hist(df2['UnitPrice'], bins=20, alpha=0.7, color='lightgreen')
plt.title('Распределение цен товаров')
plt.xlabel('Цена')
plt.ylabel('Количество')

plt.tight_layout()
plt.show()

# Визуализация результатов задания 3
plt.figure(figsize=(15, 10))

# Выберем несколько городов для наглядности
top_cities = df3['ShipCity'].value_counts().head(5).index

for i, city in enumerate(top_cities, 1):
    city_data = df3[df3['ShipCity'] == city].head(20)

    plt.subplot(2, 3, i)
    plt.plot(city_data['OrderDate'], city_data['CumulativeFreight'], marker='o', label='Кумулятивная сумма')
    plt.plot(city_data['OrderDate'], city_data['MovingAvg3Rows'], marker='s', label='Скользящее среднее (3 строки)')
    plt.title(f'Город: {city}')
    plt.xticks(rotation=45)
    plt.legend()

plt.tight_layout()
plt.show()

'''