import re

import pandas as pd
import csv

"""
Defining classes and functions for accessing and 
manipulating Texas PEIMS data (including data in TAPR
and statistics typically accessed through Snapshot) programmatically.
"""


def pad_district_number(district_number_local, leading_apostrophe=True):
    district_number_local = str(district_number_local)
    district_number_local = district_number_local.replace("'", "")
    district_number_local = district_number_local.replace("`", "")

    if len(district_number_local) < 6:
        diff = 6 - len(district_number_local)
        district_number_local = ("0" * diff) + district_number_local

        return "'" + district_number_local if leading_apostrophe is True else district_number_local
    else:
        return "'" + district_number_local if leading_apostrophe is True else district_number_local


def extract_six_digit_number(s):
    match = re.search(r'(?:^|\D)(\d{6})(?:\D|$)', s)
    if match:
        return match.group(1)
    else:
        return None


def get_special_education_funding_gap_tea(district_number):
    district_number = pad_district_number(district_number)

    df = pd.read_excel("src/data/Special Education Funding Gap/SPED data request_SY2022_3.14.2023_PROCESSED.xlsx")

    df["CDN"] = df["CDN"].apply(pad_district_number)

    df = df[df["CDN"] == district_number]

    df = df.reset_index()

    special_education_funding_gap_21_22 = df.at[0, "Difference"]

    if special_education_funding_gap_21_22 < 0:
        return special_education_funding_gap_21_22

    else:
        return "n/a"


if __name__ == "__main__":

    # TEST:
    print(get_special_education_funding_gap_tea("227901"))

