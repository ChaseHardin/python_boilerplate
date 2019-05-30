from operator import add


def do_word_counts(lines):
    counts = (lines.flatMap(lambda x: x.split())
              .map(lambda x: (x, 1))
              .reduceByKey(add))

    return {word: count for word, count in counts.collect()}
