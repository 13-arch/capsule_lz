import pandas as pd
import matplotlib.pyplot as plt
import llloogg


@llloogg.logging
class Gist():
    def __init__(self):
        self.df = None

    def loading(self):
        self.df = pd.read_csv('steam_players.csv')


    def delete(self):
    # Удаляем строки с пустыми значениями в столбце 'страна'
        self.df = self.df[self.df['country'].notna()]

    def drawing(self):
        # Подсчитываем количество участников по странам
        country_counts = self.df['country'].value_counts()

        # Оставляем только 10 самых популярных стран
        top_countries = country_counts.head(10)

        top_countries = top_countries / 10000

    # Создаем гистограмму

        plt.figure(figsize=(10, 6))
        top_countries.plot(kind='bar')
        plt.title('Количество участников по странам (в десятках тысяч)')
        plt.xlabel('Страна')
        plt.ylabel('Количество участников (сотни тысяч)')
        plt.xticks(rotation=45)
        plt.tight_layout()


        plt.show()


    def run(self):
        self.loading()
        self.delete()
        self.drawing()