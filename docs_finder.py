documents = [
  {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
  {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
  {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
  ]
directories = {
  '1': ['2207 876234', '11-2'],
  '2': ['10006'],
  '3': []
  }
def docs_finder():
  while (x := input('Введите команду:')) != 'q':
    if x == 'p':
      num_doc = input('Введите номер документа:')
      for i in documents:
        if i['number'] == num_doc:
          print('Владелец документа:', i['name'])
          break
      else:
        print('Владелец не найден')
    if x == 's':
      num_doc = input('Введите номер документа:')
      for key, i in directories.items():
        if num_doc in i:
          print('Документ хранится на полке:', key)
          break
      else:
        print('Документ не найден')
    if x == 'q':
      print('Конец операции')

docs_finder()
