
server = "https://www2.census.gov/programs-surveys/acs/summary_file/2015/data/5_year_seq_by_state/"

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
        'WY':'Wyoming',
        'PR': 'Puerto Rico',
        'US': 'United States'
          }
folders = ["All_Geographies_Not_Tracts_Block_Groups", "Tracts_Block_Groups_Only"]

for code, state in states.iteritems():
    for folder in folders:
        x = 1
        
        while x < 200:
            if x < 10:
                inter = "000"
            elif x >=10 and x < 100:
                inter = '00'
            elif x >=100:
                inter = "0"
            outpath = os.path.join("C:/data", state.replace(" ","") + folder + "_20155" + code.lower() + inter + str(x) + "000.zip")
            if os.path.exists(outpath) != True:
                url = server + state.replace(" ","")+"/"+ folder +"/20155" + code.lower() + inter + str(x) + "000.zip"
                print url
                try:
                    response = urllib2.urlopen(url)
                    zipcontent= response.read()

                
                
                    with open(outpath, 'w') as f:
                        f.write(zipcontent)
                        print "wrote" , outpath
                except Exception as e:
                    print e
            x +=1
 
