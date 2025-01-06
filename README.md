
# STATISTICAL REPORT ON NIGERIAN'S PHYSICIANS MIGRATION
This statistical report offers an analysis of the background of Nigerian medical doctors who are dissatisfied with the
current situation in the country and are consequently migrating abroad. The report examines various factors, including
professional cadre, gender, religion, marital status, and other relevant demographics, to provide a comprehensive
understanding of the motivations behind this migration trend.

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
