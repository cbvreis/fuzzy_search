from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import argparse
import pandas as pd


def load_options(filename) -> list:
    '''
    Loads the options from the csv file
    :param filename:
    :return:
    '''
    try:
        df = pd.read_csv(filename)
        df = pd.DataFrame(df['nome'].drop_duplicates())
        df.to_csv('data/data.csv', index=False)
        return df['nome'].drop_duplicates()
    except:
        print('Error loading options')
    return None


def fuzzy_ratio(string1, string2):
    '''
    Returns the ratio of the best match
    :param string1:
    :param string2:
    :return:
    '''
    return fuzz.ratio(string1, string2)


def fuzzy_partial_ratio(string1, string2):
    '''
    Returns the ratio of the best match
    :param string1:
    :param string2:
    :return:
    '''
    return fuzz.partial_ratio(string1, string2)


def fuzzy_token_sort_ratio(string1, string2):
    '''
    Returns the ratio of the best match
    :param string1:
    :param string2:
    :return:
    '''
    return fuzz.token_sort_ratio(string1, string2)


def fuzzy_options(string):
    '''
    Returns the ratio of the best match
    :param string:
    :return:
    '''
    options = load_options('data/data.csv')
    return process.extract(string, options, limit=3, scorer=fuzzy_partial_ratio)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-fo", "--fuzzy_options", help="Ajuda para os argumentos", action="store_true")
    parser.add_argument("-ftr", "--fuzzy_token_sort_ratio", help="Argumento para inclusao da media",
                        action="store_true")
    parser.add_argument("-fr", "--fuzzy_ratio", help="Argumento para inclusao da media", action="store_true")
    parser.add_argument("-fpr", "--fuzzy_partial_ratio", help="Argumento para inclusao da media", action="store_true")

    args = parser.parse_args()
    text_1 = 'O rato roeu a roupa do rei de Roma'
    text_2 = 'A ropa do rei de Roma o rato roeu'
    try:
        if args.fuzzy_options:
            print(f'Coronavirus {fuzzy_options("Coronavirus")}')

        if args.fuzzy_token_sort_ratio:
            print(f'Função fuzzy_token_sort_ratio: {fuzzy_token_sort_ratio(text_1, text_2)}')

        if args.fuzzy_ratio:
            print(f'Função fuzzy_ratio: {fuzzy_ratio(text_1, text_2)}')

        if args.fuzzy_partial_ratio:
            print(f'Função fuzzy_partial_ratio: {fuzzy_partial_ratio(text_1, text_2)}')

    except:
        print("Ocorreu um erro")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
