from exceptions import ImpossibleTitlesError, InvalidYearCupError, NegativeTitlesError
from datetime import datetime


def data_processing(data):
    titles = data.get('titles')
    first_cup = data.get('first_cup')
    first_cup_year = datetime.strptime(first_cup, "%Y-%m-%d").year
    current_year = datetime.now().year

    if titles < 0:
        raise NegativeTitlesError()

    if (first_cup_year < 1930 or (first_cup_year - 1930) % 4 != 0):
        raise InvalidYearCupError()
    elif (first_cup_year == 1942 or first_cup_year == 1946):
        raise InvalidYearCupError()

    if (first_cup_year < 1950):
        number_of_possible_cups = (current_year - first_cup_year) // 4 + 1 - 2
    else:
        number_of_possible_cups = (current_year - first_cup_year) // 4 + 1

    if (titles > number_of_possible_cups):
        raise ImpossibleTitlesError()


data = {
    "name": "França",
    "titles": 3,
    "top_scorer": "Zidane",
    "fifa_code": "FRA",
    "first_cup": "2002-10-18"
    }

print(data_processing(data))
