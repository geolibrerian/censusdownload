
server = "http://www2.census.gov/census_2010/05-Summary_File_2/"
outfolder = "C:/data"
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
        'US': 'United States'}

for state in states:
    outpath = os.path.join(outfolder, state.lower() + "2010.sf2.zip")
    if os.path.exists(outpath) != True:
        url = server + states[state].replace(" ","_") + "/" + state.lower() + "2010.sf2.zip"
        print url
        response = urllib2.urlopen(url)
        zipcontent= response.read()

    
    
        with open(outpath, 'wb') as f:
            f.write(zipcontent)
            print "wrote" , outpath
pgdb = 'http://www2.census.gov/census_2010/05-Summary_File_2/SF2_MSAccess_2007.accdb'
response = urllib2.urlopen(pgdb)
zipcontent= response.read()
outpath = os.path.join(outfolder, "SF2_MSAccess_2007.accdb")
with open(outpath, 'wb') as f:
    f.write(zipcontent)
    print "wrote" , outpath


