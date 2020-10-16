import pandas as pd


def main():
    form = pd.read_excel('MK.xlsx')

    form.dropna(inplace=True)
    form.drop(['Отметка времени'], axis=1, inplace=True)

    form['age'] = form['Сколько вам лет?'].map({
        '10-18': 1,
        '19-25': 2,
        '26 и больше': 3
    })
    form['is_working'] = form['Чем вы занимаетесь?'].apply(
        lambda v: v.find('работаю') >= 0 and v.find('ни то, ни то') == -1
    )
    form['is_studying'] = form['Чем вы занимаетесь?'].apply(
        lambda v: v.find('учусь') >= 0 and v.find('ни то, ни то') == -1
    )
    form['gender'] = form['Ваш пол:'].map({
        'мужской': 1,
        'женский': 2
    })
    form['has_сhildren'] = form['Есть ли у вас дети?'] == 'да'
    form['location'] = form['В какой местности вы живете?'].map({
        'город': 1,
        'поселок': 2,
        'село': 3
    })
    form['visit_frequency'] = form['Как часто вы посещаете этот магазин?'].map({
        'каждые 2 дня': 1,
        'раз в неделю': 2,
        'раз в месяц': 3
    })
    form['is_happy_with_prices'] = form['Вас устраивают цены на товары?'] == 'да'
    form['recreation_type'] = form['Какой отдых вы предпочитаете?'].map({
        'активный': 1,
        'за городом': 2,
        'Вариант 3': 3
    })
    form['has_car'] = form['Есть ли у вас автомобиль?'] == 'да'

    eng_columns_names = [
        'prefers_food',
        'prefers_appliances',
        'prefers_products_for_an_active_lifestyle',
        'prefers_products_for_giving',
        'prefers_products_for_children',
        'prefers_household_chemicals',
    ]
    ru_categories_names = [
        'Продукты питания',
        'Бытовая техника',
        'Товары для активного образа жизни',
        'для дачи',
        'детские товары',
        'бытовая химия'
    ]

    for eng_col_name, ru_col_name in zip(eng_columns_names, ru_categories_names):
        form[eng_col_name] = form['Какие товары вас интересуют (выберите 2 варианта):'].apply(
            lambda v: v.find(ru_col_name) >= 0
        )

    form.drop(columns=[
        'Сколько вам лет?',
        'Чем вы занимаетесь?',
        'Ваш пол:',
        'Какие товары вас интересуют (выберите 2 варианта):',
        'Есть ли у вас дети?',
        'В какой местности вы живете?',
        'Как часто вы посещаете этот магазин?',
        'Вас устраивают цены на товары?',
        'Какой отдых вы предпочитаете?',
        'Есть ли у вас автомобиль?'
    ], axis=1, inplace=True)

    form.to_excel('MK_prepared.xlsx')


if __name__ == '__main__':
    main()
