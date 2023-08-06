from configparser import ConfigParser
from hapne.convert.tools import split_convert_vcf_in_parallel


def test_split():
    config = ConfigParser()
    config.read("tests/files/foragers.ini")
    split_convert_vcf_in_parallel(0, config)
    split_convert_vcf_in_parallel(38, config)


if __name__ == "__main__":
    test_split()
