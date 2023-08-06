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


def get_district_transfer_stats(district_number, school_year):
    district_number = pad_district_number(district_number, leading_apostrophe=False)

    total_transfers_in = None
    total_transfers_out = None

    with open(f"src/pypeims/data/District Transfer Reports/xfers_district_{district_number}_{school_year.split('-')[0]}_{school_year.split('-')[1][2:]}.csv", "r") as csvfile:
        reader = csv.reader(csvfile)

        header = False
        header_indexes = {}

        for row in reader:
            if header is False:
                header = True

                for i, header_label in enumerate(row):
                    header_indexes[header_label] = i

            else:
                if school_year in ["2022-2023"]:
                    if row[8].strip() == "Total Transfers In":
                        total_transfers_in = row[9]
                    elif row[8].strip() == "Total Transfers Out":
                        total_transfers_out = row[9]

    return {"Total Transfers In": total_transfers_in, "Total Transfers Out": total_transfers_out}


def get_percentage_served(district_number, school_year):
    school_year = school_year.split("-")[1][2:]

    df = pd.read_csv(f"src/pypeims/data/PEIMS Standard Reports - Students/StudPgmStateDistrict{school_year}state.csv")

    df["DISTRICT NUMBER"] = df["DISTRICT NUMBER"].apply(pad_district_number)

    district_number = pad_district_number(district_number)

    df = df[df["DISTRICT NUMBER"] == district_number].reset_index()

    special_ed = df.at[0, "SPECIAL EDUCATION"]

    all_count = df.at[0, "ALL ENROLLMENT"]

    if "<" not in str(all_count) and "-" not in str(special_ed):
        percent_served = float(special_ed)/float(all_count)

        percent_served = round(percent_served * 100, 2)

        percent_served = str(percent_served) + "%"
    else:
        percent_served = str(special_ed) + "/" + str(all_count)

    return {"SPECIAL EDUCATION": special_ed, "ALL ENROLLMENT": all_count, "Percent Served": percent_served}


if __name__ == "__main__":

    # TEST:
    print(get_special_education_funding_gap_tea("227901"))

