import json
data = {}
data['scripts'] = []
data['scripts'].append({
    'id': 0,
    'script': 'Сценарий не выбран'})
data['scripts'].append({
    'id': 1,
    'script': 'Death match'})
data['scripts'].append({
    'id': 2,
    'script': 'Death match +'})
data['scripts'].append({
    'id': 3,
    'script': 'Контрольная точка'})
data['scripts'].append({
    'id': 4,
    'script': 'Контрольная точка +'})
data['scripts'].append({
    'id': 5,
    'script': 'Флаги'})
data['scripts'].append({
    'id': 6,
    'script': 'Флаги +'})
data['scripts'].append({
    'id': 7,
    'script': 'Штурм'})
data['scripts'].append({
    'id': 8,
    'script': 'Штурм +'})
data['scripts'].append({
    'id': 9,
    'script': 'Бомба'})
data['scripts'].append({
    'id': 10,
    'script': 'Бомба +'})
data['scripts'].append({
    'id': 11,
    'script': 'Без сценария'})
data['scripts'].append({
    'id': 12,
    'script': 'Без сценария +'})

data['scripts_map'] = []
data['scripts_map'].append({
    'id': 0,
    'name': 'Сценарная карта не выбрана',
    'numberOfStage': 0,
    'scripts': (
        'Сценарий не выбран',
        'Сценарий не выбран',
        'Сценарий не выбран',
        'Сценарий не выбран',
        'Сценарий не выбран')
    })
data['scripts_map'].append({
    'id': 1,
    'name': 'Без сценарной карты',
    'numberOfStage': 4,
    'scripts': (
        'Без сценария',
        'Без сценария',
        'Без сценария +',
        'Без сценария +',
        'Сценарий не выбран')
    })
data['scripts_map'].append({
    'id': 2,
    'name': 'Сценарная карта №1',
    'numberOfStage': 4,
    'scripts': (
        'Death match',
        'Контрольная точка',
        'Штурм',
        'Death match +',
        'Сценарий не выбран')
    })
data['scripts_map'].append({
    'id': 3,
    'name': 'Сценарная карта №2',
    'numberOfStage': 4,
    'scripts': (
        'Death match',
        'Контрольная точка',
        'Флаги',
        'Death match +',
        'Сценарий не выбран')
    })
data['scripts_map'].append({
    'id': 4,
    'name': 'Сценарная карта №3',
    'numberOfStage': 4,
    'scripts': (
        'Death match',
        'Контрольная точка',
        'Бомба',
        'Death match +',
        'Сценарий не выбран')
    })
data['scripts_map'].append({
    'id': 5,
    'name': 'Сценарная карта №4',
    'numberOfStage': 4,
    'scripts': (
        'Death match',
        'Контрольная точка +',
        'Бомба',
        'Death match +',
        'Сценарий не выбран')
    })
data['scripts_map'].append({
    'id': 6,
    'name': 'Сценарная карта №5',
    'numberOfStage': 4,
    'scripts': (
        'Death match',
        'Контрольная точка',
        'Бомба +',
        'Death match +',
        'Сценарий не выбран')
    })
data['time'] = []
data['time'].append({
    'mainTime': 5340,
    't1': 0.5,
    't2': 240,
    't3': 1,
    't4': 300,
    't5': 600,
    })

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)#, ensure_ascii=False)
