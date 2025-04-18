from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import datetime
import pandas
import collections


def main():
    excel_read = pandas.read_excel("wine_сatalog.xlsx", sheet_name='Лист1', keep_default_na=False)
    wine_catalog = excel_read.to_dict(orient='records')
    excel_wine = collections.defaultdict(list)


    for wine in wine_catalog:
        category = wine['Категория']
        name = wine['Название']
        sort = wine['Сорт']
        price = wine['Цена']
        image = wine['Картинка']
        favorable_offer = wine['Акция']

        excel_wine[category].append(wine)


    today = datetime.datetime.now()
    wine_found_year = 1920
    together_years = today.year - wine_found_year


    def get_year_word(together_years):
        if together_years % 100 in range(11, 20):
            return "лет"
        else:
            last_digit = together_years % 10
            if last_digit == 1:
                return "год"
            elif last_digit in [2, 3, 4]:
                return "года"
            else:
                return "лет"



    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    rendered_page = template.render(
        together_years=together_years,
        time_period=get_year_word(together_years),
        excel_wine=excel_wine
        )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()
