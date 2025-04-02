import pandas as pd
import matplotlib.pyplot as plt
import llloogg

@llloogg.logging
class DataFrameProcessor:
    def __init__(self, dataframe):
        """
        Инициализация класса с переданным датафреймом.
        """
        if isinstance(dataframe, pd.DataFrame):
            self.dataframe = dataframe
        else:
            raise ValueError("Ожидается объект типа pandas DataFrame.")

    def show_statistics(self, column_name):
        """
        Выводит статистику для указанного столбца и строит гистограмму.
        """
        if column_name not in self.dataframe.columns:
            raise ValueError(f"Столбец '{column_name}' не найден в датафрейме.")

        # Расчет статистики
        print(f"Статистика для столбца '{column_name}':")
        print(self.dataframe[column_name].describe())

        # Построение гистограммы
        plt.hist(self.dataframe[column_name], bins=10, color='blue', alpha=0.7)
        plt.xlabel('Значения')
        plt.ylabel('Частота')
        plt.title(f'Гистограмма столбца {column_name}')
        plt.show()

# Пример использования:
if __name__ == "__main__":
    # Создаем пример датафрейма
    data = {
        "Возраст": [23, 45, 31, 35, 25, 41, 33, 24, 44, 30],
        "Зарплата": [500, 800, 700, 750, 600, 900, 850, 550, 820, 720]
    }
    df = pd.DataFrame(data)

    # Инициализируем класс и выводим гистограмму
    processor = DataFrameProcessor(df)
    processor.show_statistics("Возраст")



