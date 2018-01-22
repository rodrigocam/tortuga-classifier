import xml.etree.cElementTree as ET
from similarity import compare
from util import make_index


XML_1 = '../dataset/mambo.xml'
XML_2 = '../dataset/paodeacucar.xml'
cp = open('../common_products.txt', 'w+')

first_tree = ET.parse(XML_1)
second_tree = ET.parse(XML_2)

first_root = first_tree.getroot()
second_root = second_tree.getroot()

index = make_index(second_root)

count = 0
for data in first_root:
    it = 0
    print(count)
    count += 1
    if data[0].text is not None:
        start_with = data[0].text[0].lower()
        text = data[0].text.lower()
        for text_cmp in index[start_with]:
            if it == 0:
                lower = (compare(text, text_cmp), text_cmp)
            else:
                dist = (compare(text, text_cmp), text_cmp)
                if lower[0] > dist[0]:
                    lower = dist
            it += 1

        if lower[0] < 1.5:
            print('Product Equal')
            print(text)
            print(lower[1])
            index[start_with].remove(lower[1])
            cp.write(" '{0}' = '{1}' - {2}\n".format(text, lower[1], lower[0]))

# dataset_1 = []
# dataset_2 = []

# for element in first_root:
#     if element[0].text is not None:
#         dataset_1.append(element[0].text.lower())

# for element in second_root:
#     if element[1].text is not None:
#         dataset_2.append(element[1].text.lower())


# count = 0
# for data in dataset_1:
#     it = 0
#     for data_cmp in dataset_2:
#         if data_cmp.startswith(data[0]):
#             if it == 0:
#                 lower = (compare(data, data_cmp), data_cmp)
#             else:
#                 dist = (compare(data, data_cmp), data_cmp)
#                 if lower[0] > dist[0]:
#                     lower = dist
#             it += 1
#     print(count)
#     count += 1
#     # print(" '{0}' is equal to '{1}'? lv = '{2}'".format(data, lower[1], lower[0]))
#     # answer = input()
#     if lower[0] < 1.5:
#         print('Product Equal')
#         cp.write(" '{0}' = '{1}' - {2}\n".format(data, lower[1], lower[0]))

    