import csv
import json

class SumIter:

    def __init__(self, path):
        self.file = open(path)
        self.text = json.load(self.file)
        x1 = len(self.text)
        start = 0
        self.start = start - 1
        self.end = x1

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start == self.end:
            self.file.close()
            raise StopIteration

        x = self.text[self.start]['name']['common']
        return x

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


def read_write(name):
    list_c = [['Ссылки на страны Wikipedia']]
    with SumIter(name) as sum_iter:
        for s in sum_iter:
            counrty = s.replace(' ', '_')
            list_c.append([f'https://en.wikipedia.org/wiki/{counrty}'])

    with open("links_c.csv", "w", encoding='utf-8', newline='') as f:
        datawriter = csv.writer(f)
        datawriter.writerows(list_c)
        print("*"*30)
        print("--->Файл успешно создан<----")
        print("*" * 30)
