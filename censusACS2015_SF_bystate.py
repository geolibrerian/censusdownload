
server = "https://www2.census.gov/programs-surveys/acs/summary_file/2015/data/1_year_by_state/"

import urllib2,os

states = {'AK':'Alaska',
'AL':'Alabama',
'AR':'Arkansas',
'AZ':'Arizona',
'CA':'California',
'CO':'Colorado',
'CT':'Connecticut',
'DC':'District of Columbia',
'DE':'Delaware',
'FL':'Florida',
'GA':'Georgia',
'HI':'Hawaii',
'IA':'Iowa',
'ID':'Idaho',
'IL':'Illinois',
'IN':'Indiana',
'KS':'Kansas',
'KY':'Kentucky',
'LA':'Louisiana',
'MA':'Massachusetts',
'MD':'Maryland',
'ME':'Maine',
'MI':'Michigan',
'MN':'Minnesota',
'MO':'Missouri',
'MS':'Mississippi',
'MT':'Montana',
'NC':'North Carolina',
'ND':'North Dakota',
'NE':'Nebraska',
'NH':'New Hampshire',
'NJ':'New Jersey',
'NM':'New Mexico',
'NV':'Nevada',
'NY':'New York',
'OH':'Ohio',
'OK':'Oklahoma',
'OR':'Oregon',
'PA':'Pennsylvania',
'RI':'Rhode Island',
'SC':'South Carolina',
'SD':'South Dakota',
'TN':'Tennessee',
'TX':'Texas',
'UT':'Utah',
'VA':'Virginia',
'VT':'Vermont',
'WA':'Washington',
'WI':'Wisconsin',
'WV':'West Virginia',
'WY':'Wyoming'}

for code, state in states.iteritems():
    outpath = os.path.join("C:/data", state.replace(" ","") + "_2015_1yr_All_Geographies.zip")
    if os.path.exists(outpath) != True:
        url = server + state.replace(" ","") + "_All_Geographies.zip"
        print url
        response = urllib2.urlopen(url)
        zipcontent= response.read()

    
    
        with open(outpath, 'w') as f:
            f.write(zipcontent)
            print "wrote" , outpath
