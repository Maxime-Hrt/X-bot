import os
from dotenv import load_dotenv

load_dotenv()


class Ninjas:
    url = 'https://api.api-ninjas.com/v1/'
    key = os.getenv('NINJAS_KEY')
    headers = {'X-Api-Key': key}

    def __init__(self, endpoint):
        self.endpoint = endpoint


COUNTRIES = ["Afghanistan", "Albania", "Algeria", "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan",
             "Bangladesh", "Belarus", "Belgium", "Botswana", "Brazil", "Bulgaria", "Burundi", "Cambodia",
             "Cameroon", "Chile", "China", "Colombia", "Costa Rica", "Cote D\'Ivoire", "Croatia",
             "Cuba", "Cyprus", "Czech Republic", "Denmark", "Dominican Republic", "Ecuador",
             "Egypt", "El Salvador", "Estonia", "Ethiopia", "Finland", "France", "Gabon", "Georgia", "Germany",
             "Ghana", "Greece", "Guatemala", "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia",
             "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya",
             "Kyrgyz Republic", "Lao", "Latvia", "Lebanon", "Lithuania", "Luxembourg", "Madagascar",
             "Malaysia", "Mali", "Mexico", "Moldova", "Morocco", "Mozambique", "Namibia", "Nepal", "Netherlands",
             "New Caledonia", "New Zealand", "Nicaragua", "Niger", "Nigeria", "Norway", "Oman", "Pakistan",
             "Palestine", "Panama",
             "Papua New Guinea", "Peru", "Philippines", "Poland", "Portugal", "Qatar",
             "Romania", "Russia",
             "Saudi Arabia", "Senegal", "Serbia", "Singapore",
             "Slovakia", "Slovenia", "South Africa", "Spain", "Sri Lanka",
             "Sweden", "Switzerland", "Tajikistan", "Thailand",
             "Tunisia", "Turkey", "Turkmenistan", "Uganda",
             "Ukraine", "United Arab Emirates", "United Kingdom", "Uruguay", "Uzbekistan", "Venezuela", "Vietnam",
             "Yemen"]
