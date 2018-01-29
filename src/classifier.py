import xml.etree.cElementTree as ET
from util.similarity import compare, compare_measures
from util.index import create_index
from multiprocessing import Pool
import csv
import time


XML_1 = '../dataset/mambo.xml'
XML_2 = '../dataset/paodeacucar.xml'
ofile = open('../output/common_products.csv', 'w')

first_tree = ET.parse(XML_1)
second_tree = ET.parse(XML_2)

first_root = first_tree.getroot()
second_root = second_tree.getroot()

index = create_index(second_root)

def classify(data):
    if data[0].text is not None:
        it = 0
        start_with = data[0].text[0].lower()
        text = data[0].text.lower()
        lower = None
        for text_cmp in index[start_with]:
            if it == 0:
                lower = (compare(text, text_cmp), text_cmp)
            else:
                dist = (compare(text, text_cmp), text_cmp)
                if lower[0] > dist[0]:
                    lower = dist
            it += 1

        if lower and lower[0] < 1.5:
            if compare_measures(text, lower[1]):
                print('Product Equal')
                index[start_with].remove(lower[1])
                ofile.write("{0},{1},{2}\n".format(text, lower[1], lower[0]))


if __name__ == "__main__":
    ofile.write("PRODUCT, PRODUCT, LEVENSHTEIN\n")
    p = Pool(5)
    start_time = time.time()
    p.map(classify, first_root)
    ofile.close()
    print(time.time()-start_time)

