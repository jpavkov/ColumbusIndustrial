# import local functions
import code.helper helper

# import global functions
import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import seaborn as sns

user = "root"
pw = "" ## tdown10!!
loc = "localhost"
db_name = "fn"

# connect to database (or create?)
my_conn = create_engine("mysql+mysqldb://" + 
                        user + ":" + pw + "@" +
                        loc + "/" + db_name)

# import csv file
costar = pd.read_csv('data/costar.csv')
re_contacts = pd.read_csv('data/re_contacts.csv')
re_occupant_contacts = pd.read_csv('data/re_occupant_contacts.csv')
re_occupants = pd.read_csv('data/re_occupants.csv')
re_properties = pd.read_csv('data/re_properties.csv')

# write csv file via to_sql function for costar + reonomy
costar.to_sql(con = my_conn, name = "costar", if_exists = "replace")
re_contacts.to_sql(con = my_conn, name = "re_contacts", if_exists = "replace")
re_occupant_contacts.to_sql(con = my_conn, name = "re_occupant_contacts", if_exists = "replace")
re_occupants.to_sql(con = my_conn, name = "re_occupants", if_exists = "replace")
re_properties.to_sql(con = my_conn, name = "re_properties", if_exists = "replace")

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Doylestown01!",
    database="fn"
)

# import coStar info
sql_query = ("SELECT costar.`index`,"
    "costar.`Property Address` propAddress,"
    "costar.`Property Name` propName,"
    "costar.`PropertyType` propType,"
    "costar.`Building Status` buildingStatus,"
    "costar.`Submarket Cluster` submarket,"
    "costar.`Submarket Name` submarketName,"
    "costar.`City` propCity,"
    "costar.`State` propState,"
    "costar.`Zip` propZip,"
    "costar.`County Name` propCounty,"
    "costar.`Year Built` yearBuilt,"
    "costar.`RBA` squareFt,"
    "costar.`Max Building Contiguous Space` squareFtContiguous,"
    "costar.`Leasing Company Name` leasingCo,"
    "costar.`Primary Agent Name` agent,"
    "costar.`Property Manager Name` propManager,"
    "costar.`Developer Name` developerName,"
    "costar.`Owner Name` ownerName,"
    "costar.`Building Park` buildingPark,"
    "costar.`Land Area (AC)` acres,"
    "costar.`Latitude` latitude,"
    "costar.`Longitude` longitude,"
    "costar.`Sale Company Contact` saleCoContact,"
    "costar.`True Owner Contact` trueOwnerContact,"
    "costar.`True Owner Name` trueOwnerName,"
    "costar.`Leasing Company Contact` leasingCoContact,"
    "costar.`Star Rating` starRating,"
    "costar.`Building Class` buildingClass"
    " FROM fn.costar;")

# assign to datatable
cs = pd.read_sql(sql_query, db)


# analyze cs
type(cs) 
cs.head()
cs.describe()

# analyze square feet
sns.stripplot(x="propCounty",
              y="squareFt",
              data=cs)

plt.show()
# by county
sns.swarmplot(x="propCounty",
              y="squareFt",
              data=cs)

plt.show()

# owner counts

# agents (leasing, etc) counts



x.to_sql()
with pd.option_context('display.max_rows', None):
    print(x.dtypes)

x.info()
x.columns
x.dtypes


x = helper.clean_costar(x)

# data and folders
HOME_DIR = '/Users/jonathanpavkov/Code/MyCarrierAnalytics'
DATA_DIR = HOME_DIR + '/data'

# data import
x = pd.read_csv(DATA_DIR + '/cust_vint_6_mos_stats.csv')


cust_vint = cust_vint_clean(x)
cust_vint.head
cust_vint.info()
cust_vint.describe()
cust_vint['revenue'].isna().sum()
cust_vint['employees'].isna().sum()

cust_vint_na = cust_vint.dropna()
cust_vint_not_na = cust_vint.dropna()

# cleanse data


# save data to MySQL db
