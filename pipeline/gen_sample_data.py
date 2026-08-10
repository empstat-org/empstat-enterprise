#!/usr/bin/env python3
"""
Country roster shared by the sample-data generators.

This module exists mainly to provide the COUNTRIES list (ISO3, name, region and a
rough illustrative `maturity` used only to shape sample data). The Enterprise
index generates its sample via gen_enterprise_sample.py, which imports COUNTRIES
from here.

NOTE: `maturity` is an illustrative estimate of statistical-system development
used only to shape the sample. It is NOT a real ILOSTAT figure. Real numbers
require fetch_and_rank.py.
"""

AF = "Africa"
AM = "Americas"
AR = "Arab States"
AP = "Asia and the Pacific"
EU = "Europe and Central Asia"

# (iso3, name, region, maturity 0-1)  maturity shapes coverage/frequency/recency
COUNTRIES = [
    # ------------------------- Africa -------------------------
    ("DZA", "Algeria", AF, 0.55), ("AGO", "Angola", AF, 0.30), ("BEN", "Benin", AF, 0.42),
    ("BWA", "Botswana", AF, 0.58), ("BFA", "Burkina Faso", AF, 0.35), ("BDI", "Burundi", AF, 0.22),
    ("CPV", "Cabo Verde", AF, 0.55), ("CMR", "Cameroon", AF, 0.36), ("CAF", "Central African Republic", AF, 0.15),
    ("TCD", "Chad", AF, 0.20), ("COM", "Comoros", AF, 0.28), ("COG", "Congo", AF, 0.30),
    ("COD", "Congo, Democratic Republic of the", AF, 0.26), ("CIV", "Côte d'Ivoire", AF, 0.47),
    ("DJI", "Djibouti", AF, 0.30), ("EGY", "Egypt", AF, 0.68), ("GNQ", "Equatorial Guinea", AF, 0.20),
    ("ERI", "Eritrea", AF, 0.12), ("SWZ", "Eswatini", AF, 0.45), ("ETH", "Ethiopia", AF, 0.40),
    ("GAB", "Gabon", AF, 0.38), ("GMB", "Gambia", AF, 0.36), ("GHA", "Ghana", AF, 0.54),
    ("GIN", "Guinea", AF, 0.30), ("GNB", "Guinea-Bissau", AF, 0.22), ("KEN", "Kenya", AF, 0.56),
    ("LSO", "Lesotho", AF, 0.44), ("LBR", "Liberia", AF, 0.30), ("LBY", "Libya", AF, 0.28),
    ("MDG", "Madagascar", AF, 0.34), ("MWI", "Malawi", AF, 0.38), ("MLI", "Mali", AF, 0.33),
    ("MRT", "Mauritania", AF, 0.38), ("MUS", "Mauritius", AF, 0.74), ("MAR", "Morocco", AF, 0.70),
    ("MOZ", "Mozambique", AF, 0.34), ("NAM", "Namibia", AF, 0.58), ("NER", "Niger", AF, 0.30),
    ("NGA", "Nigeria", AF, 0.46), ("RWA", "Rwanda", AF, 0.58), ("STP", "Sao Tome and Principe", AF, 0.32),
    ("SEN", "Senegal", AF, 0.49), ("SYC", "Seychelles", AF, 0.55), ("SLE", "Sierra Leone", AF, 0.32),
    ("SOM", "Somalia", AF, 0.12), ("ZAF", "South Africa", AF, 0.82), ("SSD", "South Sudan", AF, 0.14),
    ("SDN", "Sudan", AF, 0.24), ("TZA", "Tanzania, United Republic of", AF, 0.48), ("TGO", "Togo", AF, 0.38),
    ("TUN", "Tunisia", AF, 0.66), ("UGA", "Uganda", AF, 0.50), ("ZMB", "Zambia", AF, 0.44),
    ("ZWE", "Zimbabwe", AF, 0.42),

    # ------------------------- Arab States -------------------------
    ("BHR", "Bahrain", AR, 0.55), ("IRQ", "Iraq", AR, 0.40), ("JOR", "Jordan", AR, 0.64),
    ("KWT", "Kuwait", AR, 0.58), ("LBN", "Lebanon", AR, 0.42), ("OMN", "Oman", AR, 0.58),
    ("PSE", "Occupied Palestinian Territory", AR, 0.48), ("QAT", "Qatar", AR, 0.66),
    ("SAU", "Saudi Arabia", AR, 0.72), ("SYR", "Syrian Arab Republic", AR, 0.20),
    ("ARE", "United Arab Emirates", AR, 0.68), ("YEM", "Yemen", AR, 0.16),

    # ------------------------- Asia and the Pacific -------------------------
    ("AFG", "Afghanistan", AP, 0.20), ("AUS", "Australia", AP, 0.96), ("BGD", "Bangladesh", AP, 0.55),
    ("BTN", "Bhutan", AP, 0.45), ("BRN", "Brunei Darussalam", AP, 0.55), ("KHM", "Cambodia", AP, 0.44),
    ("CHN", "China", AP, 0.70), ("FJI", "Fiji", AP, 0.42), ("IND", "India", AP, 0.66),
    ("IDN", "Indonesia", AP, 0.76), ("IRN", "Iran, Islamic Republic of", AP, 0.55), ("JPN", "Japan", AP, 0.93),
    ("KIR", "Kiribati", AP, 0.25), ("PRK", "Korea, Democratic People's Republic of", AP, 0.10),
    ("KOR", "Korea, Republic of", AP, 0.93), ("LAO", "Lao People's Democratic Republic", AP, 0.40),
    ("MYS", "Malaysia", AP, 0.83), ("MDV", "Maldives", AP, 0.50), ("MHL", "Marshall Islands", AP, 0.22),
    ("FSM", "Micronesia, Federated States of", AP, 0.22), ("MNG", "Mongolia", AP, 0.63),
    ("MMR", "Myanmar", AP, 0.35), ("NPL", "Nepal", AP, 0.45), ("NZL", "New Zealand", AP, 0.94),
    ("PAK", "Pakistan", AP, 0.50), ("PLW", "Palau", AP, 0.25), ("PNG", "Papua New Guinea", AP, 0.28),
    ("PHL", "Philippines", AP, 0.80), ("WSM", "Samoa", AP, 0.35), ("SGP", "Singapore", AP, 0.88),
    ("SLB", "Solomon Islands", AP, 0.26), ("LKA", "Sri Lanka", AP, 0.68), ("THA", "Thailand", AP, 0.82),
    ("TLS", "Timor-Leste", AP, 0.35), ("TON", "Tonga", AP, 0.32), ("TUV", "Tuvalu", AP, 0.20),
    ("VUT", "Vanuatu", AP, 0.28), ("VNM", "Viet Nam", AP, 0.72),

    # ------------------------- Europe and Central Asia -------------------------
    ("ALB", "Albania", EU, 0.68), ("AND", "Andorra", EU, 0.52), ("ARM", "Armenia", EU, 0.70),
    ("AUT", "Austria", EU, 0.93), ("AZE", "Azerbaijan", EU, 0.62), ("BLR", "Belarus", EU, 0.66),
    ("BEL", "Belgium", EU, 0.94), ("BIH", "Bosnia and Herzegovina", EU, 0.66), ("BGR", "Bulgaria", EU, 0.85),
    ("HRV", "Croatia", EU, 0.87), ("CYP", "Cyprus", EU, 0.88), ("CZE", "Czechia", EU, 0.90),
    ("DNK", "Denmark", EU, 0.95), ("EST", "Estonia", EU, 0.90), ("FIN", "Finland", EU, 0.96),
    ("FRA", "France", EU, 0.95), ("GEO", "Georgia", EU, 0.74), ("DEU", "Germany", EU, 0.96),
    ("GRC", "Greece", EU, 0.89), ("HUN", "Hungary", EU, 0.87), ("ISL", "Iceland", EU, 0.92),
    ("IRL", "Ireland", EU, 0.90), ("ISR", "Israel", EU, 0.90), ("ITA", "Italy", EU, 0.93),
    ("KAZ", "Kazakhstan", EU, 0.72), ("KGZ", "Kyrgyzstan", EU, 0.55), ("LVA", "Latvia", EU, 0.89),
    ("LIE", "Liechtenstein", EU, 0.52), ("LTU", "Lithuania", EU, 0.89), ("LUX", "Luxembourg", EU, 0.92),
    ("MLT", "Malta", EU, 0.86), ("MDA", "Moldova, Republic of", EU, 0.62), ("MCO", "Monaco", EU, 0.50),
    ("MNE", "Montenegro", EU, 0.64), ("NLD", "Netherlands", EU, 0.97), ("MKD", "North Macedonia", EU, 0.66),
    ("NOR", "Norway", EU, 0.95), ("POL", "Poland", EU, 0.90), ("PRT", "Portugal", EU, 0.91),
    ("ROU", "Romania", EU, 0.86), ("RUS", "Russian Federation", EU, 0.78), ("SMR", "San Marino", EU, 0.50),
    ("SRB", "Serbia", EU, 0.80), ("SVK", "Slovakia", EU, 0.89), ("SVN", "Slovenia", EU, 0.90),
    ("ESP", "Spain", EU, 0.94), ("SWE", "Sweden", EU, 0.98), ("CHE", "Switzerland", EU, 0.94),
    ("TJK", "Tajikistan", EU, 0.45), ("TUR", "Türkiye", EU, 0.85), ("TKM", "Turkmenistan", EU, 0.30),
    ("UKR", "Ukraine", EU, 0.62), ("GBR", "United Kingdom", EU, 0.94), ("UZB", "Uzbekistan", EU, 0.55),

    # ------------------------- Americas -------------------------
    ("ATG", "Antigua and Barbuda", AM, 0.45), ("ARG", "Argentina", AM, 0.82), ("BHS", "Bahamas", AM, 0.55),
    ("BRB", "Barbados", AM, 0.60), ("BLZ", "Belize", AM, 0.48), ("BOL", "Bolivia", AM, 0.66),
    ("BRA", "Brazil", AM, 0.86), ("CAN", "Canada", AM, 0.95), ("CHL", "Chile", AM, 0.85),
    ("COL", "Colombia", AM, 0.83), ("CRI", "Costa Rica", AM, 0.82), ("CUB", "Cuba", AM, 0.45),
    ("DMA", "Dominica", AM, 0.40), ("DOM", "Dominican Republic", AM, 0.74), ("ECU", "Ecuador", AM, 0.77),
    ("SLV", "El Salvador", AM, 0.68), ("GRD", "Grenada", AM, 0.42), ("GTM", "Guatemala", AM, 0.58),
    ("GUY", "Guyana", AM, 0.48), ("HTI", "Haiti", AM, 0.24), ("HND", "Honduras", AM, 0.55),
    ("JAM", "Jamaica", AM, 0.60), ("MEX", "Mexico", AM, 0.85), ("NIC", "Nicaragua", AM, 0.55),
    ("PAN", "Panama", AM, 0.72), ("PRY", "Paraguay", AM, 0.70), ("PER", "Peru", AM, 0.79),
    ("KNA", "Saint Kitts and Nevis", AM, 0.40), ("LCA", "Saint Lucia", AM, 0.45),
    ("VCT", "Saint Vincent and the Grenadines", AM, 0.42), ("SUR", "Suriname", AM, 0.45),
    ("TTO", "Trinidad and Tobago", AM, 0.62), ("USA", "United States", AM, 0.95),
    ("URY", "Uruguay", AM, 0.84), ("VEN", "Venezuela, Bolivarian Republic of", AM, 0.40),
]
