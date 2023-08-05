import hapne.convert.mathii_scripts.py3Eigenstrat as pyEigenstrat
from configparser import ConfigParser
from hapne.convert.tools import eigenstrat2vcf
import pandas as pd


def test_py3Eigenstrat():
    GT_DICT = {2: "0/0", 1: "0/1", 0: "1/1", 9: "./."}
    data = pyEigenstrat.load("tests/files/Foragers/Foragers")
    print("##fileformat=VCFv4.0")
    print("##source=eigenstrat2vcf.py")
    print("##FORMAT=<ID=GT,Number=1,Type=String,Description=\"Genotype\">")
    print("#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT\t" + "\t".join(data.ind["IND"]))
    #Now line by line write data
    for i, d in enumerate(data):
        this_snp = data.snp[i]
        line = "\t".join([this_snp["CHR"], str(this_snp["POS"]), this_snp["ID"],
                         this_snp["REF"], this_snp["ALT"], "100", "PASS", ".", "GT"])
        line = line + "\t" + "\t".join([GT_DICT[x] for x in d])
        break
    assert i == 0


def test_vcf_conversion():
    config = ConfigParser()
    config.read("tests/files/foragers.ini")
    eigenstrat2vcf(config)
    converted_samples = pd.read_csv("tests/files/Foragers/DATA/Foragers.vcf.gz",
                                    compression="gzip", skiprows=31, sep="\t").shape[1] - 9
    assert 2 == converted_samples


if __name__ == "__main__":
    test_vcf_conversion()
