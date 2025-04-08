#Act_1
# Utilice el mapa para crear una nueva lista cambiando cada país a mayúsculas 
# en la lista de países
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];
uppercase_countries = list(map(lambda country: country.upper(), countries))

print(uppercase_countries)

#Act_2
# Use el mapa para crear una nueva lista cambiando cada número a su cuadrado 
# en la lista de números
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)

#Act_3
# Utilice el mapa para cambiar cada nombre a mayúsculas en la lista de nombres
names = ['Asabeneh', 'David', 'Donald', 'Bill', 'Elon']
uppercase_names = list(map(lambda name: name.upper(), names))
print(uppercase_names)

#Act_4
# Utilice el filtro para filtrar los países que contienen 'tierra'.
countries_with_land = list(filter(lambda country: 'land' in country.lower(), countries))
print(countries_with_land)

#Act_5
# Utilice el filtro para filtrar los países que tienen exactamente seis caracteres.
six_character_countries = list(filter(lambda country: len(country) == 6, countries))
print(six_character_countries)

#Act_6
# Utilice el filtro para filtrar los países que contienen seis letras o más en la lista 
# de países.
countries_with_six_or_more_letters = list(filter(lambda country: len(country) >= 6, countries))
print(countries_with_six_or_more_letters)

#Act_7
# Use el filtro para filtrar los países que comienzan con una 'E'
countries_starting_with_e = list(filter(lambda country: country.startswith('E'), countries))
print(countries_starting_with_e)

#Act_8
# Encadene dos o más iteradores de lista
from itertools import chain
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
chained_list = list(chain(list1, list2, list3))
print(chained_list)

#Act_9
# Declare una función denominada get_string_lists que toma una lista como 
# parámetro y, a continuación, devuelve una lista que contiene solo elementos 
# de cadena.
def get_string_lists(input_list):
    return [item for item in input_list if isinstance(item, str)]
mixed_list = [1, 'hola', 3.14, 'mundo', True, 'Python', None]
string_list = get_string_lists(mixed_list)
print(string_list)

#Act_10
# Utilice reducir para sumar todos los números de la lista de números.
from functools import reduce
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)

#Act_11
# Use reduce para concatenar todos los países y producir esta oración: Estonia, 
# Finlandia, Suecia, Dinamarca, Noruega e Islandia son países del norte de 
# Europa
from functools import reduce
sentence = reduce(lambda x, y: f"{x}, {y}", countries[:-1]) + f" y {countries[-1]} son países del norte de Europa"
print(sentence)

#Act_12
# Declare una función llamada categorize_countries que devuelve una lista de 
# países con algún patrón común
def categorize_countries(countries, pattern):
    categorized = [country for country in countries if pattern.lower() in country.lower()]
    return categorized
pattern = 'land'
categorized_countries = categorize_countries(countries, pattern)
print("Países categorizados:", categorized_countries)

#Act_13
# Cree una función que devuelva un diccionario, donde las teclas representan las 
# letras iniciales de los países y los valores son el número de nombres de países 
# que comienzan con esa letra.
def count_countries_by_initial(countries):
    initial_counts = {}
    for country in countries:
        initial = country[0].upper()
        initial_counts[initial] = initial_counts.get(initial, 0) + 1
    return initial_counts
result = count_countries_by_initial(countries)
print(result)

#Act_14
# Declarar una función get_first_ten_countries: devuelve una lista de los primeros 
# diez países de la lista countries.js en la carpeta de datos.
def get_first_ten_countries(countries):
    return countries[:10]
first_ten_countries = get_first_ten_countries(countries)
print(first_ten_countries)

#Act_15
# Declare una función get_last_ten_countries que devuelva los últimos diez 
# países de la lista de países.
def get_last_ten_countries(countries):
    return countries[-10:]
last_ten_countries = get_last_ten_countries(countries)
print(last_ten_countries)

print("Revisado")