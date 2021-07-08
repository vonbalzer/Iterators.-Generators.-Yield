from md5 import my_range
from links_wiki import read_write

if __name__ == '__main__':

    x = 0
    for i in my_range('links_c.csv'):
        print(f'{x}: {i}')
        x += 1

    read_write('countries.json')