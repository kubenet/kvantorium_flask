from flask import Flask, request, render_template
import random

app = Flask(__name__)

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


@app.route('/')
def index():
    animal = list_animals[random.randint(0, (len(list_animals) - 1))]
    return render_template('index.html', animal=animal, animals=list_animals)


@app.route('/descriptionAnimal/{index}')
def descriptionAnimal(index):
    animal = list_animals[random.randint(0, (len(list_animals) - 1))]
    return render_template('descriptionAnimal.html', animal=animal, animals=list_animals)


@app.route('/about/')
def about():
    return '<h3>About</h3>'


if __name__ == '__main__':
    app.run(debug=True)
