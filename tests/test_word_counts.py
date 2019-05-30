import pytest

from src import word_counts


@pytest.mark.usefixtures("spark_context")
def test_do_word_counts(spark_context):
    test_input = [
        ' hello spark ',
        ' hello again spark spark'
    ]

    input_rdd = spark_context.parallelize(test_input, 1)
    actual = word_counts.do_word_counts(input_rdd)

    expected_results = {'hello': 2, 'spark': 3, 'again': 1}
    assert actual == expected_results
