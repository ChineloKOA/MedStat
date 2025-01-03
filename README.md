
# STATISTICAL REPORT ON NIGERIAN'S PHYSICIANS MIGRATION
This statistical report provides an insight on the background on the Nigeria medical doctors that are not satisfy with
the current situation of the country and hence migrating to other countries. This looks at the professional cadre,
gender, religion, marital status etc.

## 📁 Project Structure
```
├── datacleaning/                       
        ├── datacleansing.ipynb                           # Get data from source, analyse and clean data.
├── helper/                             
        ├── aws_helper.py                                 # Class that defines all the methods required for aws s3 services
├── config.yaml                                           # Parameter / configuration for the graphics
├── nigeria-physician-migration-statistics.ipynb          # Statistical graphics from cleaned data
├── README.md                                             # Here .
├── requirements.txt                                      # Required installations
└── statistics_functions.py                               # Written functions for the graphics
```

About information used:
The dataset used in this report is from BioMed Central (BMC) website. Research and work published on the 20 December 2022 
by Cosmas Kenan Onah,Benedict Ndubueze Azuogu, Casmir Ndubuisi Ochie, Christian Obasi Akpa, Kingsley Chijioke Okeke, 
Anthony Okoafor Okpunwa, Hassan Muhammad Bello & George Onyemaechi Ugwu on the Physician emigration from Nigeria and the 
associated factors: the implications to safeguarding the Nigeria health system Human Resources for Health 
https://human-resources-health.biomedcentral.com/articles/10.1186/s12960-022-00788-z#MOESM1
