from collections import Counter


def task1():
    print('задача 1')
    moscow = {201, 202, 203, 204}
    kazan = {203, 204, 205, 206}
    print(*(moscow & kazan))
    print(*(moscow - kazan))
    print(*(kazan - moscow))
    print(len(moscow | kazan))


def task2():
    print('задача 2')
    queries = [
        "чехол", "iphone", "чехол", "наушники", "iphone",
        "iphone", "кабель", "чехол", "iphone",
    ]
    print(len(queries))
    counts = Counter(queries)
    
    for query, count in counts.items():
        print(f'{query} ввели {count} раз')
        
    most_common = counts.most_common(1)[0]
    print(f'самый частый запрос: {most_common[0]}')
    print(f'его доля среди всех запросов = {(most_common[1] / len(queries)):.2f}')
    
    unique = [query for query, count in counts.items() if count == 1]
    print('уникальные запросы:', *unique)


def task3():
    print('задача 3')
    orders = [
        {"id": 1, "buyer": "anya", "status": "delivered", "amount": 900},
        {"id": 2, "buyer": "boris", "status": "returned", "amount": 4_500},
        {"id": 3, "buyer": "anya", "status": "delivered", "amount": 1_500},
        {"id": 4, "buyer": "vera", "status": "delivered", "amount": 3_200},
        {"id": 5, "buyer": "boris", "status": "delivered", "amount": 700},
        {"id": 6, "buyer": "gleb", "status": "returned", "amount": 2_100},
    ]
    print(
        'сумма возвратов:',
        sum([order['amount'] for order in orders if order['status'] == 'returned'])
    )
    who_returned = {order['buyer'] for order in orders if order['status'] == 'returned'}
    print('заказ вернули:', *who_returned)
    delivered_amount = [
        order['amount'] for order in orders if order['status'] == 'delivered'
    ]
    print('доставлено заказов:', len(delivered_amount))
    print(
        'средний чек доставленных заказов:',
        sum(delivered_amount) / len(delivered_amount)
    )


def task4():
    print('задача 4')
    days = [
        {"day": "пн", "orders": 20, "revenue": 40_000, "returns": 2},
        {"day": "вт", "orders": 16, "revenue": 19_200, "returns": 4},
        {"day": "ср", "orders": 25, "revenue": 55_000, "returns": 1},
        {"day": "чт", "orders": 10, "revenue": 12_000, "returns": 3},
        {"day": "пт", "orders": 30, "revenue": 48_000, "returns": 3},
    ]
    print('выручка за всю неделю =', sum([day['revenue'] for day in days]))
    print(
        'день с наибольшей выручкой:',
        max(days, key=lambda x: x['revenue'])['day']
    )
    print(
        'средняя выручка на один заказ для каждого дня:\n',
        {day['day']: day['revenue'] / day['orders'] for day in days}
    )
    print(
        'дни где возвратов >20%:',
        *[day['day'] for day in days if day['returns'] / day['orders'] > 0.2]
    )


def task5():
    print('задача 5')
    reviews = [
        {"id": 1, "product": "Чехол", "stars": 5},
        {"id": 1, "product": "Чехол", "stars": 3},
        {"id": 1, "product": "Чехол", "stars": 4},
        {"id": 2, "product": "Наушники", "stars": 2},
        {"id": 2, "product": "наушники", "stars": 2},
        {"id": 2, "product": "НАУШНИКИ", "stars": 5},
        {"id": 3, "product": "Планшет", "stars": 5},
        {"id": 4, "product": "Колонка", "stars": 4},
        {"id": 4, "product": "Колонка", "stars": 4},
        {"id": 5, "product": "Кабель", "stars": 1},
    ]
    products = {}
    for review in reviews:
        review_id = review['id']
        if review_id not in products:
            products[review_id] = {
                'product': review['product'].lower(),
                'sum': 0,
                'count': 0,
            }
        products[review_id]['sum'] += review['stars']
        products[review_id]['count'] += 1

    for _, product_data in products.items():
        average = product_data['sum'] / product_data['count']
        print(f'{product_data["product"]}: {average}')

    worse_product = min(
        [
            (review_id, product_data)
            for review_id, product_data in products.items()
            if product_data['count'] > 1
        ],
        key=lambda x: x[1]['sum'] / x[1]['count']
    )
    print(
        'худший товар хотя бы с 2 отзывами:',
        worse_product[1]['product']
    )

    bad_reviews = [review for review in reviews if review['stars'] < 3]
    print('отзывов на 1 или 2 звезды:', len(bad_reviews))
    print('их доля:', len(bad_reviews) / len(reviews))


if __name__ == '__main__':
    task1()
    task2()
    task3()
    task4()
    task5()
