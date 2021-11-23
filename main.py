from tkinter import *
import time
from PIL import Image, ImageTk
import random
import requests
from bs4 import BeautifulSoup as bs

'''
def findWeather():
    cities = [['New York', 'New York'], ['Los Angeles', 'California'], ['Chicago', 'Illinois'], ['Houston', 'Texas'],
              ['Philadelphia', 'Pennsylvania'], ['Phoenix', 'Arizona'], ['San Antonio', 'Texas'],
              ['San Diego', 'California'], ['Dallas', 'Texas'], ['San Jose', 'California'], ['Austin', 'Texas'],
              ['Indianapolis', 'Indiana'], ['Jacksonville', 'Florida'], ['San Francisco', 'California'],
              ['Columbus', 'Ohio'], ['Charlotte', 'North Carolina'], ['Fort Worth', 'Texas'], ['Detroit', 'Michigan'],
              ['El Paso', 'Texas'], ['Memphis', 'Tennessee'], ['Seattle', 'Washington'], ['Denver', 'Colorado'],
              ['Washington', 'District of Columbia'], ['Boston', 'Massachusetts'], ['Nashville-Davidson', 'Tennessee'],
              ['Baltimore', 'Maryland'], ['Oklahoma City', 'Oklahoma'], ['Louisville/Jefferson County', 'Kentucky'],
              ['Portland', 'Oregon'], ['Las Vegas', 'Nevada'], ['Milwaukee', 'Wisconsin'],
              ['Albuquerque', 'New Mexico'], ['Tucson', 'Arizona'], ['Fresno', 'California'],
              ['Sacramento', 'California'], ['Long Beach', 'California'], ['Kansas City', 'Missouri'],
              ['Mesa', 'Arizona'], ['Virginia Beach', 'Virginia'], ['Atlanta', 'Georgia'],
              ['Colorado Springs', 'Colorado'], ['Omaha', 'Nebraska'], ['Raleigh', 'North Carolina'],
              ['Miami', 'Florida'], ['Oakland', 'California'], ['Minneapolis', 'Minnesota'], ['Tulsa', 'Oklahoma'],
              ['Cleveland', 'Ohio'], ['Wichita', 'Kansas'], ['Arlington', 'Texas'], ['New Orleans', 'Louisiana'],
              ['Bakersfield', 'California'], ['Tampa', 'Florida'], ['Honolulu', 'Hawaii'], ['Aurora', 'Colorado'],
              ['Anaheim', 'California'], ['Santa Ana', 'California'], ['St. Louis', 'Missouri'],
              ['Riverside', 'California'], ['Corpus Christi', 'Texas'], ['Lexington-Fayette', 'Kentucky'],
              ['Pittsburgh', 'Pennsylvania'], ['Anchorage', 'Alaska'], ['Stockton', 'California'],
              ['Cincinnati', 'Ohio'], ['St. Paul', 'Minnesota'], ['Toledo', 'Ohio'], ['Greensboro', 'North Carolina'],
              ['Newark', 'New Jersey'], ['Plano', 'Texas'], ['Henderson', 'Nevada'], ['Lincoln', 'Nebraska'],
              ['Buffalo', 'New York'], ['Jersey City', 'New Jersey'], ['Chula Vista', 'California'],
              ['Fort Wayne', 'Indiana'], ['Orlando', 'Florida'], ['St. Petersburg', 'Florida'], ['Chandler', 'Arizona'],
              ['Laredo', 'Texas'], ['Norfolk', 'Virginia'], ['Durham', 'North Carolina'], ['Madison', 'Wisconsin'],
              ['Lubbock', 'Texas'], ['Irvine', 'California'], ['Winston-Salem', 'North Carolina'],
              ['Glendale', 'Arizona'], ['Garland', 'Texas'], ['Hialeah', 'Florida'], ['Reno', 'Nevada'],
              ['Chesapeake', 'Virginia'], ['Gilbert', 'Arizona'], ['Baton Rouge', 'Louisiana'], ['Irving', 'Texas'],
              ['Scottsdale', 'Arizona'], ['North Las Vegas', 'Nevada'], ['Fremont', 'California'],
              ['Boise City', 'Idaho'], ['Richmond', 'Virginia'], ['San Bernardino', 'California'],
              ['Birmingham', 'Alabama'], ['Spokane', 'Washington'], ['Rochester', 'New York'], ['Des Moines', 'Iowa'],
              ['Modesto', 'California'], ['Fayetteville', 'North Carolina'], ['Tacoma', 'Washington'],
              ['Oxnard', 'California'], ['Fontana', 'California'], ['Columbus', 'Georgia'], ['Montgomery', 'Alabama'],
              ['Moreno Valley', 'California'], ['Shreveport', 'Louisiana'], ['Aurora', 'Illinois'],
              ['Yonkers', 'New York'], ['Akron', 'Ohio'], ['Huntington Beach', 'California'],
              ['Little Rock', 'Arkansas'], ['Augusta-Richmond County', 'Georgia'], ['Amarillo', 'Texas'],
              ['Glendale', 'California'], ['Mobile', 'Alabama'], ['Grand Rapids', 'Michigan'],
              ['Salt Lake City', 'Utah'], ['Tallahassee', 'Florida'], ['Huntsville', 'Alabama'],
              ['Grand Prairie', 'Texas'], ['Knoxville', 'Tennessee'], ['Worcester', 'Massachusetts'],
              ['Newport News', 'Virginia'], ['Brownsville', 'Texas'], ['Overland Park', 'Kansas'],
              ['Santa Clarita', 'California'], ['Providence', 'Rhode Island'], ['Garden Grove', 'California'],
              ['Chattanooga', 'Tennessee'], ['Oceanside', 'California'], ['Jackson', 'Mississippi'],
              ['Fort Lauderdale', 'Florida'], ['Santa Rosa', 'California'], ['Rancho Cucamonga', 'California'],
              ['Port St. Lucie', 'Florida'], ['Tempe', 'Arizona'], ['Ontario', 'California'],
              ['Vancouver', 'Washington'], ['Cape Coral', 'Florida'], ['Sioux Falls', 'South Dakota'],
              ['Springfield', 'Missouri'], ['Peoria', 'Arizona'], ['Pembroke Pines', 'Florida'],
              ['Elk Grove', 'California'], ['Salem', 'Oregon'], ['Lancaster', 'California'], ['Corona', 'California'],
              ['Eugene', 'Oregon'], ['Palmdale', 'California'], ['Salinas', 'California'],
              ['Springfield', 'Massachusetts'], ['Pasadena', 'Texas'], ['Fort Collins', 'Colorado'],
              ['Hayward', 'California'], ['Pomona', 'California'], ['Cary', 'North Carolina'], ['Rockford', 'Illinois'],
              ['Alexandria', 'Virginia'], ['Escondido', 'California'], ['McKinney', 'Texas'], ['Kansas City', 'Kansas'],
              ['Joliet', 'Illinois'], ['Sunnyvale', 'California'], ['Torrance', 'California'],
              ['Bridgeport', 'Connecticut'], ['Lakewood', 'Colorado'], ['Hollywood', 'Florida'],
              ['Paterson', 'New Jersey'], ['Naperville', 'Illinois'], ['Syracuse', 'New York'], ['Mesquite', 'Texas'],
              ['Dayton', 'Ohio'], ['Savannah', 'Georgia'], ['Clarksville', 'Tennessee'], ['Orange', 'California'],
              ['Pasadena', 'California'], ['Fullerton', 'California'], ['Killeen', 'Texas'], ['Frisco', 'Texas'],
              ['Hampton', 'Virginia'], ['McAllen', 'Texas'], ['Warren', 'Michigan'], ['Bellevue', 'Washington'],
              ['West Valley City', 'Utah'], ['Columbia', 'South Carolina'], ['Olathe', 'Kansas'],
              ['Sterling Heights', 'Michigan'], ['New Haven', 'Connecticut'], ['Miramar', 'Florida'], ['Waco', 'Texas'],
              ['Thousand Oaks', 'California'], ['Cedar Rapids', 'Iowa'], ['Charleston', 'South Carolina'],
              ['Visalia', 'California'], ['Topeka', 'Kansas'], ['Elizabeth', 'New Jersey'], ['Gainesville', 'Florida'],
              ['Thornton', 'Colorado'], ['Roseville', 'California'], ['Carrollton', 'Texas'],
              ['Coral Springs', 'Florida'], ['Stamford', 'Connecticut'], ['Simi Valley', 'California'],
              ['Concord', 'California'], ['Hartford', 'Connecticut'], ['Kent', 'Washington'],
              ['Lafayette', 'Louisiana'], ['Midland', 'Texas'], ['Surprise', 'Arizona'], ['Denton', 'Texas'],
              ['Victorville', 'California'], ['Evansville', 'Indiana'], ['Santa Clara', 'California'],
              ['Abilene', 'Texas'], ['Athens-Clarke County', 'Georgia'], ['Vallejo', 'California'],
              ['Allentown', 'Pennsylvania'], ['Norman', 'Oklahoma'], ['Beaumont', 'Texas'],
              ['Independence', 'Missouri'], ['Murfreesboro', 'Tennessee'], ['Ann Arbor', 'Michigan'],
              ['Springfield', 'Illinois'], ['Berkeley', 'California'], ['Peoria', 'Illinois'], ['Provo', 'Utah'],
              ['El Monte', 'California'], ['Columbia', 'Missouri'], ['Lansing', 'Michigan'], ['Fargo', 'North Dakota'],
              ['Downey', 'California'], ['Costa Mesa', 'California'], ['Wilmington', 'North Carolina'],
              ['Arvada', 'Colorado'], ['Inglewood', 'California'], ['Miami Gardens', 'Florida'],
              ['Carlsbad', 'California'], ['Westminster', 'Colorado'], ['Rochester', 'Minnesota'], ['Odessa', 'Texas'],
              ['Manchester', 'New Hampshire'], ['Elgin', 'Illinois'], ['West Jordan', 'Utah'], ['Round Rock', 'Texas'],
              ['Clearwater', 'Florida'], ['Waterbury', 'Connecticut'], ['Gresham', 'Oregon'],
              ['Fairfield', 'California'], ['Billings', 'Montana'], ['Lowell', 'Massachusetts'],
              ['San Buenaventura (Ventura)', 'California'], ['Pueblo', 'Colorado'], ['High Point', 'North Carolina'],
              ['West Covina', 'California'], ['Richmond', 'California'], ['Murrieta', 'California'],
              ['Cambridge', 'Massachusetts'], ['Antioch', 'California'], ['Temecula', 'California'],
              ['Norwalk', 'California'], ['Centennial', 'Colorado'], ['Everett', 'Washington'], ['Palm Bay', 'Florida'],
              ['Wichita Falls', 'Texas'], ['Green Bay', 'Wisconsin'], ['Daly City', 'California'],
              ['Burbank', 'California'], ['Richardson', 'Texas'], ['Pompano Beach', 'Florida'],
              ['North Charleston', 'South Carolina'], ['Broken Arrow', 'Oklahoma'], ['Boulder', 'Colorado'],
              ['West Palm Beach', 'Florida'], ['Santa Maria', 'California'], ['El Cajon', 'California'],
              ['Davenport', 'Iowa'], ['Rialto', 'California'], ['Las Cruces', 'New Mexico'],
              ['San Mateo', 'California'], ['Lewisville', 'Texas'], ['South Bend', 'Indiana'], ['Lakeland', 'Florida'],
              ['Erie', 'Pennsylvania'], ['Tyler', 'Texas'], ['Pearland', 'Texas'], ['College Station', 'Texas'],
              ['Kenosha', 'Wisconsin'], ['Sandy Springs', 'Georgia'], ['Clovis', 'California'], ['Flint', 'Michigan'],
              ['Roanoke', 'Virginia'], ['Albany', 'New York'], ['Jurupa Valley', 'California'],
              ['Compton', 'California'], ['San Angelo', 'Texas'], ['Hillsboro', 'Oregon'], ['Lawton', 'Oklahoma'],
              ['Renton', 'Washington'], ['Vista', 'California'], ['Davie', 'Florida'], ['Greeley', 'Colorado'],
              ['Mission Viejo', 'California'], ['Portsmouth', 'Virginia'], ['Dearborn', 'Michigan'],
              ['South Gate', 'California'], ['Tuscaloosa', 'Alabama'], ['Livonia', 'Michigan'],
              ['New Bedford', 'Massachusetts'], ['Vacaville', 'California'], ['Brockton', 'Massachusetts'],
              ['Roswell', 'Georgia'], ['Beaverton', 'Oregon'], ['Quincy', 'Massachusetts'], ['Sparks', 'Nevada'],
              ['Yakima', 'Washington'], ["Lee's Summit", 'Missouri'], ['Federal Way', 'Washington'],
              ['Carson', 'California'], ['Santa Monica', 'California'], ['Hesperia', 'California'], ['Allen', 'Texas'],
              ['Rio Rancho', 'New Mexico'], ['Yuma', 'Arizona'], ['Westminster', 'California'], ['Orem', 'Utah'],
              ['Lynn', 'Massachusetts'], ['Redding', 'California'], ['Spokane Valley', 'Washington'],
              ['Miami Beach', 'Florida'], ['League City', 'Texas'], ['Lawrence', 'Kansas'],
              ['Santa Barbara', 'California'], ['Plantation', 'Florida'], ['Sandy', 'Utah'], ['Sunrise', 'Florida'],
              ['Macon', 'Georgia'], ['Longmont', 'Colorado'], ['Boca Raton', 'Florida'], ['San Marcos', 'California'],
              ['Greenville', 'North Carolina'], ['Waukegan', 'Illinois'], ['Fall River', 'Massachusetts'],
              ['Chico', 'California'], ['Newton', 'Massachusetts'], ['San Leandro', 'California'],
              ['Reading', 'Pennsylvania'], ['Norwalk', 'Connecticut'], ['Fort Smith', 'Arkansas'],
              ['Newport Beach', 'California'], ['Asheville', 'North Carolina'], ['Nashua', 'New Hampshire'],
              ['Edmond', 'Oklahoma'], ['Whittier', 'California'], ['Nampa', 'Idaho'], ['Bloomington', 'Minnesota'],
              ['Deltona', 'Florida'], ['Hawthorne', 'California'], ['Duluth', 'Minnesota'], ['Carmel', 'Indiana'],
              ['Suffolk', 'Virginia'], ['Clifton', 'New Jersey'], ['Citrus Heights', 'California'],
              ['Livermore', 'California'], ['Tracy', 'California'], ['Alhambra', 'California'],
              ['Kirkland', 'Washington'], ['Trenton', 'New Jersey'], ['Ogden', 'Utah'], ['Hoover', 'Alabama'],
              ['Cicero', 'Illinois'], ['Fishers', 'Indiana'], ['Sugar Land', 'Texas'], ['Danbury', 'Connecticut'],
              ['Meridian', 'Idaho'], ['Indio', 'California'], ['Concord', 'North Carolina'], ['Menifee', 'California'],
              ['Champaign', 'Illinois'], ['Buena Park', 'California'], ['Troy', 'Michigan'], ["O'Fallon", 'Missouri'],
              ['Johns Creek', 'Georgia'], ['Bellingham', 'Washington'], ['Westland', 'Michigan'],
              ['Bloomington', 'Indiana'], ['Sioux City', 'Iowa'], ['Warwick', 'Rhode Island'], ['Hemet', 'California'],
              ['Longview', 'Texas'], ['Farmington Hills', 'Michigan'], ['Bend', 'Oregon'], ['Lakewood', 'California'],
              ['Merced', 'California'], ['Mission', 'Texas'], ['Chino', 'California'], ['Redwood City', 'California'],
              ['Edinburg', 'Texas'], ['Cranston', 'Rhode Island'], ['Parma', 'Ohio'], ['New Rochelle', 'New York'],
              ['Lake Forest', 'California'], ['Napa', 'California'], ['Hammond', 'Indiana'],
              ['Fayetteville', 'Arkansas'], ['Bloomington', 'Illinois'], ['Avondale', 'Arizona'],
              ['Somerville', 'Massachusetts'], ['Palm Coast', 'Florida'], ['Bryan', 'Texas'], ['Gary', 'Indiana'],
              ['Largo', 'Florida'], ['Brooklyn Park', 'Minnesota'], ['Tustin', 'California'], ['Racine', 'Wisconsin'],
              ['Deerfield Beach', 'Florida'], ['Lynchburg', 'Virginia'], ['Mountain View', 'California'],
              ['Medford', 'Oregon'], ['Lawrence', 'Massachusetts'], ['Bellflower', 'California'],
              ['Melbourne', 'Florida'], ['St. Joseph', 'Missouri'], ['Camden', 'New Jersey'], ['St. George', 'Utah'],
              ['Kennewick', 'Washington'], ['Baldwin Park', 'California'], ['Chino Hills', 'California'],
              ['Alameda', 'California'], ['Albany', 'Georgia'], ['Arlington Heights', 'Illinois'],
              ['Scranton', 'Pennsylvania'], ['Evanston', 'Illinois'], ['Kalamazoo', 'Michigan'], ['Baytown', 'Texas'],
              ['Upland', 'California'], ['Springdale', 'Arkansas'], ['Bethlehem', 'Pennsylvania'],
              ['Schaumburg', 'Illinois'], ['Mount Pleasant', 'South Carolina'], ['Auburn', 'Washington'],
              ['Decatur', 'Illinois'], ['San Ramon', 'California'], ['Pleasanton', 'California'],
              ['Wyoming', 'Michigan'], ['Lake Charles', 'Louisiana'], ['Plymouth', 'Minnesota'],
              ['Bolingbrook', 'Illinois'], ['Pharr', 'Texas'], ['Appleton', 'Wisconsin'],
              ['Gastonia', 'North Carolina'], ['Folsom', 'California'], ['Southfield', 'Michigan'],
              ['Rochester Hills', 'Michigan'], ['New Britain', 'Connecticut'], ['Goodyear', 'Arizona'],
              ['Canton', 'Ohio'], ['Warner Robins', 'Georgia'], ['Union City', 'California'], ['Perris', 'California'],
              ['Manteca', 'California'], ['Iowa City', 'Iowa'], ['Jonesboro', 'Arkansas'], ['Wilmington', 'Delaware'],
              ['Lynwood', 'California'], ['Loveland', 'Colorado'], ['Pawtucket', 'Rhode Island'],
              ['Boynton Beach', 'Florida'], ['Waukesha', 'Wisconsin'], ['Gulfport', 'Mississippi'],
              ['Apple Valley', 'California'], ['Passaic', 'New Jersey'], ['Rapid City', 'South Dakota'],
              ['Layton', 'Utah'], ['Lafayette', 'Indiana'], ['Turlock', 'California'], ['Muncie', 'Indiana'],
              ['Temple', 'Texas'], ['Missouri City', 'Texas'], ['Redlands', 'California'], ['Santa Fe', 'New Mexico'],
              ['Lauderhill', 'Florida'], ['Milpitas', 'California'], ['Palatine', 'Illinois'], ['Missoula', 'Montana'],
              ['Rock Hill', 'South Carolina'], ['Jacksonville', 'North Carolina'], ['Franklin', 'Tennessee'],
              ['Flagstaff', 'Arizona'], ['Flower Mound', 'Texas'], ['Weston', 'Florida'], ['Waterloo', 'Iowa'],
              ['Union City', 'New Jersey'], ['Mount Vernon', 'New York'], ['Fort Myers', 'Florida'],
              ['Dothan', 'Alabama'], ['Rancho Cordova', 'California'], ['Redondo Beach', 'California'],
              ['Jackson', 'Tennessee'], ['Pasco', 'Washington'], ['St. Charles', 'Missouri'],
              ['Eau Claire', 'Wisconsin'], ['North Richland Hills', 'Texas'], ['Bismarck', 'North Dakota'],
              ['Yorba Linda', 'California'], ['Kenner', 'Louisiana'], ['Walnut Creek', 'California'],
              ['Frederick', 'Maryland'], ['Oshkosh', 'Wisconsin'], ['Pittsburg', 'California'],
              ['Palo Alto', 'California'], ['Bossier City', 'Louisiana'], ['Portland', 'Maine'],
              ['St. Cloud', 'Minnesota'], ['Davis', 'California'], ['South San Francisco', 'California'],
              ['Camarillo', 'California'], ['North Little Rock', 'Arkansas'], ['Schenectady', 'New York'],
              ['Gaithersburg', 'Maryland'], ['Harlingen', 'Texas'], ['Woodbury', 'Minnesota'], ['Eagan', 'Minnesota'],
              ['Yuba City', 'California'], ['Maple Grove', 'Minnesota'], ['Youngstown', 'Ohio'], ['Skokie', 'Illinois'],
              ['Kissimmee', 'Florida'], ['Johnson City', 'Tennessee'], ['Victoria', 'Texas'],
              ['San Clemente', 'California'], ['Bayonne', 'New Jersey'], ['Laguna Niguel', 'California'],
              ['East Orange', 'New Jersey'], ['Shawnee', 'Kansas'], ['Homestead', 'Florida'], ['Rockville', 'Maryland'],
              ['Delray Beach', 'Florida'], ['Janesville', 'Wisconsin'], ['Conway', 'Arkansas'],
              ['Pico Rivera', 'California'], ['Lorain', 'Ohio'], ['Montebello', 'California'], ['Lodi', 'California'],
              ['New Braunfels', 'Texas'], ['Marysville', 'Washington'], ['Tamarac', 'Florida'],
              ['Madera', 'California'], ['Conroe', 'Texas'], ['Santa Cruz', 'California'],
              ['Eden Prairie', 'Minnesota'], ['Cheyenne', 'Wyoming'], ['Daytona Beach', 'Florida'],
              ['Alpharetta', 'Georgia'], ['Hamilton', 'Ohio'], ['Waltham', 'Massachusetts'],
              ['Coon Rapids', 'Minnesota'], ['Haverhill', 'Massachusetts'], ['Council Bluffs', 'Iowa'],
              ['Taylor', 'Michigan'], ['Utica', 'New York'], ['Ames', 'Iowa'], ['La Habra', 'California'],
              ['Encinitas', 'California'], ['Bowling Green', 'Kentucky'], ['Burnsville', 'Minnesota'],
              ['Greenville', 'South Carolina'], ['West Des Moines', 'Iowa'], ['Cedar Park', 'Texas'],
              ['Tulare', 'California'], ['Monterey Park', 'California'], ['Vineland', 'New Jersey'],
              ['Terre Haute', 'Indiana'], ['North Miami', 'Florida'], ['Mansfield', 'Texas'],
              ['West Allis', 'Wisconsin'], ['Bristol', 'Connecticut'], ['Taylorsville', 'Utah'],
              ['Malden', 'Massachusetts'], ['Meriden', 'Connecticut'], ['Blaine', 'Minnesota'],
              ['Wellington', 'Florida'], ['Cupertino', 'California'], ['Springfield', 'Oregon'], ['Rogers', 'Arkansas'],
              ['St. Clair Shores', 'Michigan'], ['Gardena', 'California'], ['Pontiac', 'Michigan'],
              ['National City', 'California'], ['Grand Junction', 'Colorado'], ['Rocklin', 'California'],
              ['Chapel Hill', 'North Carolina'], ['Casper', 'Wyoming'], ['Broomfield', 'Colorado'],
              ['Petaluma', 'California'], ['South Jordan', 'Utah'], ['Springfield', 'Ohio'], ['Great Falls', 'Montana'],
              ['Lancaster', 'Pennsylvania'], ['North Port', 'Florida'], ['Lakewood', 'Washington'],
              ['Marietta', 'Georgia'], ['San Rafael', 'California'], ['Royal Oak', 'Michigan'],
              ['Des Plaines', 'Illinois'], ['Huntington Park', 'California'], ['La Mesa', 'California'],
              ['Orland Park', 'Illinois'], ['Auburn', 'Alabama'], ['Lakeville', 'Minnesota'], ['Owensboro', 'Kentucky'],
              ['Moore', 'Oklahoma'], ['Jupiter', 'Florida'], ['Idaho Falls', 'Idaho'], ['Dubuque', 'Iowa'],
              ['Bartlett', 'Tennessee'], ['Rowlett', 'Texas'], ['Novi', 'Michigan'], ['White Plains', 'New York'],
              ['Arcadia', 'California'], ['Redmond', 'Washington'], ['Lake Elsinore', 'California'],
              ['Ocala', 'Florida'], ['Tinley Park', 'Illinois'], ['Port Orange', 'Florida'],
              ['Medford', 'Massachusetts'], ['Oak Lawn', 'Illinois'], ['Rocky Mount', 'North Carolina'],
              ['Kokomo', 'Indiana'], ['Coconut Creek', 'Florida'], ['Bowie', 'Maryland'], ['Berwyn', 'Illinois'],
              ['Midwest City', 'Oklahoma'], ['Fountain Valley', 'California'], ['Buckeye', 'Arizona'],
              ['Dearborn Heights', 'Michigan'], ['Woodland', 'California'], ['Noblesville', 'Indiana'],
              ['Valdosta', 'Georgia'], ['Diamond Bar', 'California'], ['Manhattan', 'Kansas'], ['Santee', 'California'],
              ['Taunton', 'Massachusetts'], ['Sanford', 'Florida'], ['Kettering', 'Ohio'],
              ['New Brunswick', 'New Jersey'], ['Decatur', 'Alabama'], ['Chicopee', 'Massachusetts'],
              ['Anderson', 'Indiana'], ['Margate', 'Florida'], ['Weymouth Town', 'Massachusetts'],
              ['Hempstead', 'New York'], ['Corvallis', 'Oregon'], ['Eastvale', 'California'],
              ['Porterville', 'California'], ['West Haven', 'Connecticut'], ['Brentwood', 'California'],
              ['Paramount', 'California'], ['Grand Forks', 'North Dakota'], ['Georgetown', 'Texas'],
              ['St. Peters', 'Missouri'], ['Shoreline', 'Washington'], ['Mount Prospect', 'Illinois'],
              ['Hanford', 'California'], ['Normal', 'Illinois'], ['Rosemead', 'California'], ['Lehi', 'Utah'],
              ['Pocatello', 'Idaho'], ['Highland', 'California'], ['Novato', 'California'], ['Port Arthur', 'Texas'],
              ['Carson City', 'Nevada'], ['San Marcos', 'Texas'], ['Hendersonville', 'Tennessee'], ['Elyria', 'Ohio'],
              ['Revere', 'Massachusetts'], ['Pflugerville', 'Texas'], ['Greenwood', 'Indiana'],
              ['Bellevue', 'Nebraska'], ['Wheaton', 'Illinois'], ['Smyrna', 'Georgia'], ['Sarasota', 'Florida'],
              ['Blue Springs', 'Missouri'], ['Colton', 'California'], ['Euless', 'Texas'], ['Castle Rock', 'Colorado'],
              ['Cathedral City', 'California'], ['Kingsport', 'Tennessee'], ['Lake Havasu City', 'Arizona'],
              ['Pensacola', 'Florida'], ['Hoboken', 'New Jersey'], ['Yucaipa', 'California'],
              ['Watsonville', 'California'], ['Richland', 'Washington'], ['Delano', 'California'],
              ['Hoffman Estates', 'Illinois'], ['Florissant', 'Missouri'], ['Placentia', 'California'],
              ['West New York', 'New Jersey'], ['Dublin', 'California'], ['Oak Park', 'Illinois'],
              ['Peabody', 'Massachusetts'], ['Perth Amboy', 'New Jersey'], ['Battle Creek', 'Michigan'],
              ['Bradenton', 'Florida'], ['Gilroy', 'California'], ['Milford', 'Connecticut'], ['Albany', 'Oregon'],
              ['Ankeny', 'Iowa'], ['La Crosse', 'Wisconsin'], ['Burlington', 'North Carolina'], ['DeSoto', 'Texas'],
              ['Harrisonburg', 'Virginia'], ['Minnetonka', 'Minnesota'], ['Elkhart', 'Indiana'], ['Lakewood', 'Ohio'],
              ['Glendora', 'California'], ['Southaven', 'Mississippi'], ['Charleston', 'West Virginia'],
              ['Joplin', 'Missouri'], ['Enid', 'Oklahoma'], ['Palm Beach Gardens', 'Florida'],
              ['Brookhaven', 'Georgia'], ['Plainfield', 'New Jersey'], ['Grand Island', 'Nebraska'],
              ['Palm Desert', 'California'], ['Huntersville', 'North Carolina'], ['Tigard', 'Oregon'],
              ['Lenexa', 'Kansas'], ['Saginaw', 'Michigan'], ['Kentwood', 'Michigan'], ['Doral', 'Florida'],
              ['Apple Valley', 'Minnesota'], ['Grapevine', 'Texas'], ['Aliso Viejo', 'California'],
              ['Sammamish', 'Washington'], ['Casa Grande', 'Arizona'], ['Pinellas Park', 'Florida'],
              ['Troy', 'New York'], ['West Sacramento', 'California'], ['Burien', 'Washington'],
              ['Commerce City', 'Colorado'], ['Monroe', 'Louisiana'], ['Cerritos', 'California'],
              ['Downers Grove', 'Illinois'], ['Coral Gables', 'Florida'], ['Wilson', 'North Carolina'],
              ['Niagara Falls', 'New York'], ['Poway', 'California'], ['Edina', 'Minnesota'],
              ['Cuyahoga Falls', 'Ohio'], ['Rancho Santa Margarita', 'California'], ['Harrisburg', 'Pennsylvania'],
              ['Huntington', 'West Virginia'], ['La Mirada', 'California'], ['Cypress', 'California'],
              ['Caldwell', 'Idaho'], ['Logan', 'Utah'], ['Galveston', 'Texas'], ['Sheboygan', 'Wisconsin'],
              ['Middletown', 'Ohio'], ['Murray', 'Utah'], ['Roswell', 'New Mexico'], ['Parker', 'Colorado'],
              ['Bedford', 'Texas'], ['East Lansing', 'Michigan'], ['Methuen', 'Massachusetts'],
              ['Covina', 'California'], ['Alexandria', 'Louisiana'], ['Olympia', 'Washington'], ['Euclid', 'Ohio'],
              ['Mishawaka', 'Indiana'], ['Salina', 'Kansas'], ['Azusa', 'California'], ['Newark', 'Ohio'],
              ['Chesterfield', 'Missouri'], ['Leesburg', 'Virginia'], ['Dunwoody', 'Georgia'],
              ['Hattiesburg', 'Mississippi'], ['Roseville', 'Michigan'], ['Bonita Springs', 'Florida'],
              ['Portage', 'Michigan'], ['St. Louis Park', 'Minnesota'], ['Collierville', 'Tennessee'],
              ['Middletown', 'Connecticut'], ['Stillwater', 'Oklahoma'], ['East Providence', 'Rhode Island'],
              ['Lawrence', 'Indiana'], ['Wauwatosa', 'Wisconsin'], ['Mentor', 'Ohio'], ['Ceres', 'California'],
              ['Cedar Hill', 'Texas'], ['Mansfield', 'Ohio'], ['Binghamton', 'New York'], ["Coeur d'Alene", 'Idaho'],
              ['San Luis Obispo', 'California'], ['Minot', 'North Dakota'], ['Palm Springs', 'California'],
              ['Pine Bluff', 'Arkansas'], ['Texas City', 'Texas'], ['Summerville', 'South Carolina'],
              ['Twin Falls', 'Idaho'], ['Jeffersonville', 'Indiana'], ['San Jacinto', 'California'],
              ['Madison', 'Alabama'], ['Altoona', 'Pennsylvania'], ['Columbus', 'Indiana'], ['Beavercreek', 'Ohio'],
              ['Apopka', 'Florida'], ['Elmhurst', 'Illinois'], ['Maricopa', 'Arizona'], ['Farmington', 'New Mexico'],
              ['Glenview', 'Illinois'], ['Cleveland Heights', 'Ohio'], ['Draper', 'Utah'], ['Lincoln', 'California'],
              ['Sierra Vista', 'Arizona'], ['Lacey', 'Washington'], ['Biloxi', 'Mississippi'], ['Strongsville', 'Ohio'],
              ['Barnstable Town', 'Massachusetts'], ['Wylie', 'Texas'], ['Sayreville', 'New Jersey'],
              ['Kannapolis', 'North Carolina'], ['Charlottesville', 'Virginia'], ['Littleton', 'Colorado'],
              ['Titusville', 'Florida'], ['Hackensack', 'New Jersey'], ['Newark', 'California'],
              ['Pittsfield', 'Massachusetts'], ['York', 'Pennsylvania'], ['Lombard', 'Illinois'],
              ['Attleboro', 'Massachusetts'], ['DeKalb', 'Illinois'], ['Blacksburg', 'Virginia'], ['Dublin', 'Ohio'],
              ['Haltom City', 'Texas'], ['Lompoc', 'California'], ['El Centro', 'California'],
              ['Danville', 'California'], ['Jefferson City', 'Missouri'], ['Cutler Bay', 'Florida'],
              ['Oakland Park', 'Florida'], ['North Miami Beach', 'Florida'], ['Freeport', 'New York'],
              ['Moline', 'Illinois'], ['Coachella', 'California'], ['Fort Pierce', 'Florida'], ['Smyrna', 'Tennessee'],
              ['Bountiful', 'Utah'], ['Fond du Lac', 'Wisconsin'], ['Everett', 'Massachusetts'],
              ['Danville', 'Virginia'], ['Keller', 'Texas'], ['Belleville', 'Illinois'], ['Bell Gardens', 'California'],
              ['Cleveland', 'Tennessee'], ['North Lauderdale', 'Florida'], ['Fairfield', 'Ohio'],
              ['Salem', 'Massachusetts'], ['Rancho Palos Verdes', 'California'], ['San Bruno', 'California'],
              ['Concord', 'New Hampshire'], ['Burlington', 'Vermont'], ['Apex', 'North Carolina'],
              ['Midland', 'Michigan'], ['Altamonte Springs', 'Florida'], ['Hutchinson', 'Kansas'],
              ['Buffalo Grove', 'Illinois'], ['Urbandale', 'Iowa'], ['State College', 'Pennsylvania'],
              ['Urbana', 'Illinois'], ['Plainfield', 'Illinois'], ['Manassas', 'Virginia'], ['Bartlett', 'Illinois'],
              ['Kearny', 'New Jersey'], ['Oro Valley', 'Arizona'], ['Findlay', 'Ohio'], ['Rohnert Park', 'California'],
              ['Westfield', 'Massachusetts'], ['Linden', 'New Jersey'], ['Sumter', 'South Carolina'],
              ['Wilkes-Barre', 'Pennsylvania'], ['Woonsocket', 'Rhode Island'], ['Leominster', 'Massachusetts'],
              ['Shelton', 'Connecticut'], ['Brea', 'California'], ['Covington', 'Kentucky'], ['Rockwall', 'Texas'],
              ['Meridian', 'Mississippi'], ['Riverton', 'Utah'], ['St. Cloud', 'Florida'], ['Quincy', 'Illinois'],
              ['Morgan Hill', 'California'], ['Warren', 'Ohio'], ['Edmonds', 'Washington'], ['Burleson', 'Texas'],
              ['Beverly', 'Massachusetts'], ['Mankato', 'Minnesota'], ['Hagerstown', 'Maryland'],
              ['Prescott', 'Arizona'], ['Campbell', 'California'], ['Cedar Falls', 'Iowa'], ['Beaumont', 'California'],
              ['La Puente', 'California'], ['Crystal Lake', 'Illinois'], ['Fitchburg', 'Massachusetts'],
              ['Carol Stream', 'Illinois'], ['Hickory', 'North Carolina'], ['Streamwood', 'Illinois'],
              ['Norwich', 'Connecticut'], ['Coppell', 'Texas'], ['San Gabriel', 'California'],
              ['Holyoke', 'Massachusetts'], ['Bentonville', 'Arkansas'], ['Florence', 'Alabama'],
              ['Peachtree Corners', 'Georgia'], ['Brentwood', 'Tennessee'], ['Bozeman', 'Montana'],
              ['New Berlin', 'Wisconsin'], ['Goose Creek', 'South Carolina'], ['Huntsville', 'Texas'],
              ['Prescott Valley', 'Arizona'], ['Maplewood', 'Minnesota'], ['Romeoville', 'Illinois'],
              ['Duncanville', 'Texas'], ['Atlantic City', 'New Jersey'], ['Clovis', 'New Mexico'],
              ['The Colony', 'Texas'], ['Culver City', 'California'], ['Marlborough', 'Massachusetts'],
              ['Hilton Head Island', 'South Carolina'], ['Moorhead', 'Minnesota'], ['Calexico', 'California'],
              ['Bullhead City', 'Arizona'], ['Germantown', 'Tennessee'], ['La Quinta', 'California'],
              ['Lancaster', 'Ohio'], ['Wausau', 'Wisconsin'], ['Sherman', 'Texas'], ['Ocoee', 'Florida'],
              ['Shakopee', 'Minnesota'], ['Woburn', 'Massachusetts'], ['Bremerton', 'Washington'],
              ['Rock Island', 'Illinois'], ['Muskogee', 'Oklahoma'], ['Cape Girardeau', 'Missouri'],
              ['Annapolis', 'Maryland'], ['Greenacres', 'Florida'], ['Ormond Beach', 'Florida'],
              ['Hallandale Beach', 'Florida'], ['Stanton', 'California'], ['Puyallup', 'Washington'],
              ['Pacifica', 'California'], ['Hanover Park', 'Illinois'], ['Hurst', 'Texas'], ['Lima', 'Ohio'],
              ['Marana', 'Arizona'], ['Carpentersville', 'Illinois'], ['Oakley', 'California'],
              ['Huber Heights', 'Ohio'], ['Lancaster', 'Texas'], ['Montclair', 'California'], ['Wheeling', 'Illinois'],
              ['Brookfield', 'Wisconsin'], ['Park Ridge', 'Illinois'], ['Florence', 'South Carolina'], ['Roy', 'Utah'],
              ['Winter Garden', 'Florida'], ['Chelsea', 'Massachusetts'], ['Valley Stream', 'New York'],
              ['Spartanburg', 'South Carolina'], ['Lake Oswego', 'Oregon'], ['Friendswood', 'Texas'],
              ['Westerville', 'Ohio'], ['Northglenn', 'Colorado'], ['Phenix City', 'Alabama'], ['Grove City', 'Ohio'],
              ['Texarkana', 'Texas'], ['Addison', 'Illinois'], ['Dover', 'Delaware'], ['Lincoln Park', 'Michigan'],
              ['Calumet City', 'Illinois'], ['Muskegon', 'Michigan'], ['Aventura', 'Florida'],
              ['Martinez', 'California'], ['Greenfield', 'Wisconsin'], ['Apache Junction', 'Arizona'],
              ['Monrovia', 'California'], ['Weslaco', 'Texas'], ['Keizer', 'Oregon'], ['Spanish Fork', 'Utah'],
              ['Beloit', 'Wisconsin'], ['Panama City', 'Florida']]
    city, state = random.choice(cities)
    url = "https://www.google.com/search?q=" + "weather in " + city
    html = requests.get(url).content
    soup = bs(html, 'html.parser')
    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    s = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
    data = s.split('\n')
    timings = data[0]
    skyStatus = data[1]
    listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
    data = listdiv[5].text
    return [city, state, temp, timings, skyStatus, data]
weatherInfo = findWeather()
city, state, temp, timings, sky, otherData = weatherInfo
tempNum = 0
if temp[1] == "°":
    tempNum = int(temp[0])
if temp[2] == "°":
    tempNum = int(temp[0:2])
if temp[3] == "°":
    tempNum = int(temp[0:3])

if tempNum < 60:
    environment = "cold"
elif tempNum > 75:
    environment = "hot"
else:
    environment = "normal"

'''
tk = Tk()
tk.title("Wizard Weather Wars")
tk.iconbitmap("assets\\images\\wizard.ico")
tk.resizable(0,0)
# Place window at topleft of screen
tk.geometry("+0+0")
# tk.wm_attributes("-topmost", 1)
# 720x1280 screen
canvas = Canvas(tk, width=1280, height=720, bd=0, highlightthickness=0)
canvas.configure(bg="skyblue")
canvas.pack()
tk.update()
canvas.create_text(600,50,fill="darkblue",font="Comic_Sans 40 italic bold",
                        text="WIZARD WEATHER WARS")

'''
wInfo1 = canvas.create_text(1150, 200)
wInfo2 = canvas.create_text(1150, 220)
wInfo3 = canvas.create_text(1150, 240)
wInfo4 = canvas.create_text(1150, 260)
wInfo5 = canvas.create_text(1150, 280)

s1 = city, state
s1part2 = timings
s2 = temp
s3 = sky
s4 = otherData
canvas.itemconfig(wInfo1, text=s1, font="Times 15 bold", fill="black")
canvas.itemconfig(wInfo2, text=s1part2, font="Times 15 bold", fill="black")
canvas.itemconfig(wInfo3, text=s2, font="Times 15 bold", fill="black")
canvas.itemconfig(wInfo4, text=s3, font="Times 15 bold", fill="black")
canvas.itemconfig(wInfo5, text=s4, font="Times 8 italic", fill="black")
'''

class Tile:
    def __init__(self, canvas, x1, y1, x2, y2, color):
        self.canvas = canvas
        self.id = self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")
        #self.canvas.move(self.id, 245, 100)


class HealthBar:
    def __init__(self, canvas, startingposX, startingposY):
        self.canvas = canvas
        self.fillid = self.canvas.create_rectangle(0, 0, 0, 10, fill="Red")
        self.outline = self.canvas.create_rectangle(0, 0, 100, 10)
        self.startingposX = startingposX
        self.startingposY = startingposY
        self.canvas.move(self.fillid, self.startingposX, self.startingposY)
        self.canvas.move(self.outline, self.startingposX, self.startingposY)
    
    def update(self, newhealth):
        x0,y0,x1,y1 = self.canvas.coords(self.fillid)
        x1 = self.startingposX + newhealth
        # x1 = newhealth
        self.canvas.coords(self.fillid, x0, y0, x1, y1)


class Weapon:
    def __init__(self, canvas, sprite, damage) -> None:
        self.canvas = canvas
        self.img = Image.open(sprite).resize((8, 45), Image.ANTIALIAS).rotate(-10, resample=Image.BICUBIC, expand=True)
        self.file = ImageTk.PhotoImage(self.img)
        self.id = self.canvas.create_image((100,100), image=self.file)
        self.rotation = 0
        self.attacking = False
        self.damage = damage

        self.animation_frames = [self.img]
        rotation = -10
        while rotation <= 12:
            self.animation_frames.append(self.animation_frames[-1].rotate(rotation, resample=Image.BICUBIC, expand=True))
            rotation += 1
        self.animation_frames = [ImageTk.PhotoImage(frame) for frame in self.animation_frames]
        
        self.attacking_frame = 0
    
    def draw(self, playercoords):
        if self.attacking:
            self.canvas.delete(self.id)
            self.id = self.canvas.create_image((playercoords[2]+3,playercoords[3]-37), image=self.animation_frames[self.attacking_frame])
            self.attacking_frame += 1
            if self.attacking_frame >= 23:
                self.attacking_frame = 0
                self.attacking = False
        else:
            coords = self.canvas.coords(self.id)
            self.canvas.move(self.id, playercoords[2] - coords[0]+3, playercoords[3] - coords[1]-37)

    def attack(self, button):
        if not self.attacking:
            self.attacking_frame = 1
            self.attacking = True

class Environment:
    def __init__(self, canvas) -> None:
        self.canvas = canvas
        self.delete_countdown = -1
        self.environment = "normal"
    
    def draw(self):
        if self.delete_countdown > 0:
            self.delete_countdown -= 1
        elif self.delete_countdown == 0:
            self.canvas.delete(self.loadingtext1)
            self.delete_countdown = -1

    def drawHot(self, sprite1):
        self.img = Image.open(sprite1).resize((100, 100), Image.ANTIALIAS)
        self.file = ImageTk.PhotoImage(self.img)
        self.id = self.canvas.create_image((100, 100), image=self.file)
        self.loadingtext1 = canvas.create_text(600, 200, text="Power UP! Environment is now HOT!", font="Comic_Sans 20 italic bold", fill="orange")
        self.delete_countdown = 100
    
    def drawCold(self, sprite2, sprite3):
        self.img = Image.open(sprite2).resize((100, 100), Image.ANTIALIAS)
        self.file = ImageTk.PhotoImage(self.img)
        self.id = self.canvas.create_image((100, 100), image=self.file)
        self.img2 = Image.open(sprite2).resize((100, 100), Image.ANTIALIAS)
        self.file2 = ImageTk.PhotoImage(self.img2)
        self.id2 = self.canvas.create_image((100, 100), image=self.file2)
        self.loadingtext1 = canvas.create_text(600, 200, text="Power UP! Environment is now COLD!", font="Comic_Sans 20 italic bold", fill="blue")
        self.delete_countdown = 100

class Player:
    def __init__(self, canvas, Up, Left, Right, Attack, color, startingposX, startingposY, weapon: Weapon, healthbar: HealthBar, name, Power, isHot):
        self.canvas = canvas
        self.color = color
        self.Attack = Attack
        self.Up = Up
        self.Left = Left
        self.Right = Right
        self.Power = Power
        self.id = self.canvas.create_rectangle(0, 0, 10, 50, fill=self.color)
        self.canvas.move(self.id, startingposX, startingposY)
        self.acceleration_y = 0.6
        self.velocity_y = 0
        self.velocity_x = 0
        self.jump_count = 0
        self.left_stop = True
        self.right_stop = True
        self.isHot = isHot
        self.name = name
        # player inertia is friction
        self.player_inertia = 0.08
        self.deactivated = True
        self.weapon = weapon
        self.healthbar = healthbar
        self.enemy = None
        self.damagecooldown = 0

        self.canvas.bind_all(f"<KeyPress-{self.Up}>", self.jump)
        self.canvas.bind_all(f"<KeyPress-{self.Left}>", self.left)
        self.canvas.bind_all(f"<KeyPress-{self.Right}>", self.right)
        self.canvas.bind_all(f"<KeyRelease-{self.Left}>", self.left_stopper)
        self.canvas.bind_all(f"<KeyRelease-{self.Right}>", self.right_stopper)
        self.canvas.bind_all(f"<KeyRelease-{self.Attack}>", self.weapon.attack)
        self.canvas.bind_all(f"<KeyRelease-{self.Power}>", self.powerUp)

        self.canvas.tag_raise(self.id)

        self.health = 100
        self.healthbar.update(self.health)
        # This will range from 0.1 to 1.9 depending on the weather
        self.attack_multiplier = 1
        self.defense_multiplier = 1
    
    def left_stopper(self, button):
        self.left_stop = True
        if self.left_stop and self.right_stop:
            self.deactivated = True
    
    def right_stopper(self, button):
        self.right_stop = True
        if self.left_stop and self.right_stop:
            self.deactivated = True

    def draw(self):
        self.canvas.move(self.id, self.velocity_x, self.velocity_y)
        self.velocity_y += self.acceleration_y
        coords = canvas.coords(self.id)
        if coords[3] > 680:
            self.velocity_y = 0
            self.canvas.move(self.id, 0, 680-coords[3])
            self.jump_count = 2
            self.player_inertia = 0.4
        
        if coords[2] < 10:
            self.velocity_x = 0
            self.canvas.move(self.id, 10-coords[2], 0)
        elif coords[2] > 1271:
            self.velocity_x = 0
            self.canvas.move(self.id, 1271-coords[2], 0)
        
        # Check if we're attacked
        if self.enemy.weapon.id in self.canvas.find_overlapping(coords[0], coords[1], coords[2], coords[3]) and self.enemy.weapon.attacking:
            self.damage(self.enemy.weapon.damage)
        
        # Slowly adding drift so it's more natural
        if self.deactivated:
            if self.velocity_x < 0:
                self.velocity_x += self.player_inertia
                if self.velocity_x > 0:
                    self.velocity_x = 0
            elif self.velocity_x > 0:
                self.velocity_x -= self.player_inertia
                if self.velocity_x < 0:
                    self.velocity_x = 0

    def damage(self, damage_amount):
        # Small attack cooldown
        if self.damagecooldown:
            self.canvas.itemconfig(self.id, fill=self.color)
            self.damagecooldown -= 1
        else:
            self.health -= damage_amount
            self.healthbar.update(self.health)
            self.canvas.itemconfig(self.id, fill='darkred')
            self.damagecooldown = 5
        
        if self.health <= 0:
            self.die()
    
    def die(self):
        self.canvas.create_text(600,320,fill=self.enemy.color,font="Times 50 bold",text=f"{self.enemy.name} wins!")

        self.canvas.unbind(f"<KeyPress-{self.Attack}>")
        self.canvas.unbind(f"<KeyPress-{self.enemy.Attack}>")
        self.canvas.unbind(f"<KeyPress-{self.Power}>")
        self.canvas.unbind(f"<KeyPress-{self.enemy.Power}>")
        btn = Button(tk, text='New Game', width=40, height=5, bd='10', command=startgame)
        btn.place(x=65, y=100)
        global isdone
        isdone = True
    
    def jump(self, button):
        if self.jump_count:
            self.velocity_y = -12
            self.jump_count -= 1
            # The friction needs to change in the air so the jump is smooth
            self.player_inertia = 0.08
    
    def left(self, button):
        self.velocity_x = -7
        self.left_stop = False
        self.deactivated = False
    
    def right(self, button):
        self.velocity_x = 7
        self.right_stop = False
        self.deactivated = False
    
    def powerUp(self, button):
        global environment
        if self.isHot:
            environment = "hot"
            self.drawHot("assets\\images\\Ellipse 231.png")
        else:
            environment = "cold"
            self.drawCold("assets\\images\\Cloud 1.png", "assets\\images\\Cloud 2.png")



isdone = False
def on_quit():
    global isdone
    isdone = True
    tk.destroy()

tk.protocol("WM_DELETE_WINDOW", on_quit)

def startgame():
    isdone = False
    canvas.delete("all")

    ground = Tile(canvas, 0, 720, 1280, 680, "green")
    p1weapon = Weapon(canvas, "assets\\images\\firesword.png", 15)
    p1healthbar = HealthBar(canvas, 0, 50)
    player1 = Player(canvas, "w", "a", "d", "v", "Red", 245, 100, p1weapon, p1healthbar, "Player 1", "b", True)

    env = Environment(canvas)


    p2healthbar = HealthBar(canvas, 1180, 50)
    p2weapon = Weapon(canvas, "assets\\images\\icesword.png", 15)
    player2 = Player(canvas, "Up", "Left", "Right", "k", "Green", 1035, 100, p2weapon, p2healthbar, "Player 2", "l", False)

    player1.enemy = player2
    player2.enemy = player1

    '''
    if env.environment == "hot":
        env.drawHot("assets\\images\\Ellipse 231.png")
    if env.environment == "cold":
        env.drawCold("assets\\images\\Cloud 1.png", "assets\\images\\Cloud 2.png")
    '''
    
    try:
        while not isdone:
            env.draw()

            player1.draw()
            p1weapon.draw(canvas.coords(player1.id))

            player2.draw()
            p2weapon.draw(canvas.coords(player2.id))

            tk.update_idletasks()
            tk.update()
            # 80 fps
            time.sleep(0.0125)
        else:
            del ground

            del p1weapon
            del p1healthbar
            del player1

            del p2weapon
            del p2healthbar
            del player2
    except KeyboardInterrupt:
        print('breh just use the x')

if __name__ == "__main__":
    startgame()
