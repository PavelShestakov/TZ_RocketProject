import ast
import requests


def get_movie(movie_title):
    url_API_OMDB = 'http://www.omdbapi.com/'
    key_API_OMDB = 'ff80fae5'
    error_text = 'Нe нашёл такой фильм:( Вероятно, вы неправильно ввели название или такого фильма нет в базе.'

    try:
        resp = requests.get(f'{url_API_OMDB}?apikey={key_API_OMDB}&t={movie_title}')

        if '"Error":"Movie not found!"' in resp.text:
            raise NameError("Неправильное название.")

        output_data = ast.literal_eval(resp.text)
        output_text = (f"\nНазвание: {output_data.get('Title')}"
                       f"\nГод выпуска: {output_data.get('Year')}"
                       f"\nРежиссер: {output_data.get('Director')}"
                       f"\nОписание: {output_data.get('Plot')}\n")
        print(output_text)

    except:
        print(error_text)


if __name__ == '__main__':
    while True:
        movie_title = str(input('Введите название фильма: '))
        if movie_title=='':
            break
        get_movie(movie_title)
