from pyspark import SparkContext
import os

PWD = '/Users/chasehardin/dev/deere/analytics/python_boilerplate/'
FILE_NAME = 'diamonds.csv'


def main():
    sc = SparkContext(master="local", appName="Spark Demo")

    _add_file(sc)
    content = _file_content(sc)
    sc.stop()

    return content


def _add_file(sc):
    path = os.path.join(PWD, FILE_NAME)
    sc.addFile(path)


def _file_content(sc):
    return sc.textFile('{}{}'.format(PWD, FILE_NAME)).collect()


print(main())
