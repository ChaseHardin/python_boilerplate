import pytest
from pyspark import SparkConf, SparkContext


@pytest.fixture(scope="session")
def spark_context(request):
    config = (SparkConf().setMaster("local[2]").setAppName("pytest-pyspark-local-testing"))
    spark_context = SparkContext(conf=config)
    request.addfinalizer(lambda: spark_context.stop())

    return spark_context
