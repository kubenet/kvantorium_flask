import random
from flask import Flask, request, render_template
from data import tours, departures
import operator

app = Flask(__name__)

# список животных для отображения демо версии продукта
list_animals = [
    'Абронии',
    'Абудефдуфы',
    'Авацератопс',
    'Авдотка',
    'Авдотки',
    'Авдотковые',
    'Авеметатарзалии',
    'Авиалы',
    'Авиатираннис',
    'Авимимы',
    'Авлакоцефалодон',
    'Авлациды',
    'Аганиновые',
    'Агаониды',
    'Агаристиновые',
    'Агилизавр',
    'Агиртиды',
    'Аглии',
    'Агностиды',
    'Агносфитис',
    'Агнотозои',
    'Агоноксениды',
    'Агономалы',
    'Агрозавр',
    'Агуйа',
    'Агути',
    'Аддакс',
    'Аделобазилевс',
    'Аделоспондилы',
    'Адеопаппозавр',
    'Адериды',
    'Адинотерии',
    'Адрианихтиевые',
    'Аждархиды',
    'Аждархо',
    'Аждархоиды'
]

description = [
    'Ящерицы из рода Аброний обычно очень медленные, но при опасности могут спрыгнуть на землю',
    'Абудефдуф обыкновенный (Abudefduf vaigiensis) или рыба-сержант - одна из самых часто встречающихся',
    'Авацератопс относится к семейству цератопсидов -травоядных динозавров с клювами, подобными клювам попугаев, которые процветали во время мелового периода на территории Северной Америки и Азии.'
]

dict_animals = {
    "Аброний": "Ящерицы из рода Аброний обычно очень медленные, но при опасности могут спрыгнуть на землю",
    'Абудефдуф': "Абудефдуф обыкновенный (Abudefduf vaigiensis) или рыба-сержант - одна из самых часто встречающихся",
    'Авацератопс': "Авацератопс относится к семейству цератопсидов -травоядных динозавров с клювами, подобными клювам попугаев, которые процветали во время мелового периода на территории Северной Америки и Азии."
}

dict_animals_img = {
    "Аброний": "https://ru.wikipedia.org/wiki/%D0%90%D0%B1%D1%80%D0%BE%D0%BD%D0%B8%D0%B8#/media/%D0%A4%D0%B0%D0%B9%D0%BB:Arboreal_Alligator_Lizard_Abronia_graminea_2900px.jpg",
    'Абудефдуф': "Абудефдуф обыкновенный (Abudefduf vaigiensis) или рыба-сержант - одна из самых часто встречающихся",
    'Авацератопс': "Авацератопс относится к семейству цератопсидов -травоядных динозавров с клювами, подобными клювам попугаев, которые процветали во время мелового периода на территории Северной Америки и Азии."
}

# создание словаря с ценами туров
list_tours = {}
for tour in tours:
    list_tours.setdefault(tour, tours[tour]["price"])

sorted_x = sorted(list_tours.items(), key=operator.itemgetter(1))
print(sorted_x)
print(sorted_x[0][0])
print(sorted_x[0][1])
print(list_tours)


@app.route('/')
def index():
    # animal = list_animals[random.randint(0, (len(list_animals) - 1))]
    return render_template('index.html', tours=tours, list_tours=list_tours)


@app.route('/indexSortCostMax')
def indexSortCostMax():
    return render_template('indexSortCostMax.html', tours=tours, list_tours=list_tours)


@app.route('/descriptionAnimal/<key>')
def descriptionAnimal(key):
    animal = list_animals[random.randint(0, (len(list_animals) - 1))]
    return render_template('descriptionAnimal.html', key=key, animal=animal, animals=list_animals, tours=tours,
                           departures=departures)


@app.route('/about/')
def about():
    return '<h3>About</h3>'


if __name__ == '__main__':
    app.run(debug=True)
