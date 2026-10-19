from utils import fib
from edit_distance import levenshtein, damerau, edit_distance

lines = """
Винничук. Галицька кухня: історія, рецепти та обличчя: Біґос мисливський
Винничук. Галицька кухня: історія, рецепти та обличчя: Кавове суфле
Винничук. Галицька кухня: історія, рецепти та обличчя: Налисники з сиром
Винничук. Галицька кухня: історія, рецепти та обличчя: Пироги
Винничук. Галицька кухня: історія, рецепти та обличчя: Святвечірній борщ з вушками
Винничук. Галицька кухня: історія, рецепти та обличчя: Страви з м’яса
Войтенко. National Geographic Україна: Місто майстрів
Клименко. Квіти України: Духмяний сад - то справжня крихта раю
Куцай. National Geographic Україна: Степова пісня
Панова. National Geographic Україна: Донбас та голуби
Панова. National Geographic Україна: Поклик предків
Рубцова. Квіти України: Весна в саду троянд
Фарина. National Geographic Україна: Вавилонська арка
Хорошунов. Нумізматика і фалеристика: Новий вигляд знайомих відзнак
Шевченко. National Geographic Україна: Колоністи боліт
""".strip().split("\n")


def main():
    print(lines)

    for i in range(len(lines)):
        for j in range(i+1, len(lines)):
            metric = edit_distance(lines[i], lines[j])
            if metric >= 0.75:
                print(lines[i])
                print(lines[j])
                print(f"({i},{j}) = {metric * 100:.2f}%")

    # print(fib(10))
    # print(levenshtein("intention", "execution"), damerau("intention", "execution"))
    # print(levenshtein("Hello World", "Hello! How are you?"), damerau("Hello World", "Hello! How are you?"))
    # print(levenshtein("Hello World", "Where are you from?"), damerau("Hello World", "Where are you from?"))


if __name__ == "__main__":
    main()
