meme_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное",
            "ГАНГАНИ МИД": "Прийди помоги на центральную линию",
            "ВАЙБ": "Атмосфера",
            "КРИПОВО": "Очень страшно",
            "РОФЛ": "Шутка"
            }

word = input("Введите непонятное слово (большими буквами!): ")
if word in meme_dict.keys():
    print(meme_dict[word])
else:
 print('Не найдено слово, извините, добавим в будущем!')

