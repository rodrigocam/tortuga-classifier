from util.levenshtein import distance
import ruamel.yaml as yaml
import re

"""
    This module implements the idea of the
    user Alain in this stackoverflow topic
    https://stackoverflow.com/questions/5859561/getting-the-closest-string-match
    and a trick that I develop to improve the precision of the comparison.
"""

def get_measure(product, pattern):
    start, end = pattern.search(product).span()
    if start and end:
        measure = product[start:end]
        return measure
    return None


def compare_measures(product_1, product_2):
    with open('../dictionary.yml') as stream:
        pattern = re.compile(yaml.safe_load(stream)['measure_units'][0])
        
        measure_1 = get_measure(product_1, pattern)
        measure_2 = get_measure(product_2, pattern)

        if measure_1 and measure_2:
            measure_1 = measure_1.replace(' ', '')
            measure_2 = measure_2.replace(' ', '')
            if measure_1 == measure_2:
                return True
        return False


def value_words(string_1, string_2):
    words_1 = string_1.split(' ')
    words_2 = string_2.split(' ')
    words_total = 0

    for word_1 in words_1:
        word_best = len(string_2)
        for word_2 in words_2:
            dist = distance(word_1, word_2)
            if dist < word_best:
                word_best = dist
        if dist == 0:
            words_total += word_best
    return words_total


def compare(string_1, string_2):
    phrase_value =  distance(string_1, string_2)-0.8*abs(len(string_1)-len(string_2))
    words_value = value_words(string_1, string_2)

    phrase_weight = 0.5
    words_weight = 1.0
    length_weight = -0.3
    min_weight = 10
    max_weight = 1

    min_value = min([phrase_value * phrase_weight, words_value * words_weight])
    max_value = max(phrase_value * phrase_weight, words_value * words_weight)

    sim_value =  min_value * min_weight + max_value * max_weight 
    return sim_value