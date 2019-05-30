from pyspark import SparkContext
import os

PWD = '/Users/chasehardin/dev/deere/analytics/python_boilerplate/'
FILE_NAME = 'diamonds.csv'


def main():
    sc = SparkContext(master="local", appName="Spark Demo")

    _add_file(sc)
    _display_file_content(sc)


def _add_file(sc):
    path = os.path.join(PWD, FILE_NAME)
    sc.addFile(path)


def _display_file_content(sc):
    content = sc.textFile('{}{}'.format(PWD, FILE_NAME))

    for row in content.collect():
        print(row)


main()
