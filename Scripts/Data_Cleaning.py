import pandas as pd

acs_path = '/data/ACS_Estimates_2010-2022.xlsx'
demographics_path = '../data/Bldg_Dem_2006-2023.xlsx'
grade_enrollment_path = '../data/Bldg_Grade_Enroll_2006_2023.xlsx'

acs_data = pd.read_excel(acs_path)
demographics_data = pd.read_excel(demographics_path)
grade_enrollment_data = pd.read_excel(grade_enrollment_path)

print(acs_data.head())
print(demographics_data.head())
print(grade_enrollment_data.head())

print(acs_data.info())
print(demographics_data.info())
print(grade_enrollment_data.info())
