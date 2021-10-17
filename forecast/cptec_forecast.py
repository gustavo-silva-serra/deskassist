from cptec import Cptec
from cptec import estacoes
from .weather import Weather

class CptecWeather:
    @classmethod
    def current(self):
        c = Cptec.condicoes_atuais(estacoes['RS']['Salgado Filho'])
        return Weather(c.temperatura, c.temperatura, c.tempo, self.get_icon(c.tempo))

    @classmethod
    def next_days(self):
        weather_array = []
        for c in Cptec.previsao(237):
            print(c)
            weather_array.append(Weather(c.min, c.max, c.tempo, self.get_icon(c.tempo)))
        return weather_array

    @classmethod
    def get_icon(self, condition):
        for key,value in self.__icon.items():
            if condition in value:
                return "icon/"+key
        return 'undefined.png'

    __icon = {
        'sun.png': [
            "Predomínio de Sol", "Céu Claro", "Nevoeiro"
        ],
        'thunderstorm.png': [
            "Tempestade", "Nublado com Pancadas a Tarde", "Nublado com Pancadas a Noite", "Nublado com Pancadas pela Manhã", "Poss. de Panc. de Chuva a Noite",
            "Poss. de Panc. de Chuva a Tarde","Poss. de Panc. de Chuva pela Manhã"
        ],
        'rain.png': [
            "Chuva", "Instável", "Poss. de Pancadas de Chuva", "Chuva pela Manhã", "Chuva a Noite", "Chuvas Isoladas", "Encoberto com Chuvas Isoladas",
            "Pancadas de Chuva a Tarde", "Pancadas de Chuva pela Manhã", "Nublado e Pancadas de Chuva", "Pancadas de Chuva", "Chuvisco", "Chuvoso",
            "Pancadas de Chuva a Noite", "Possibilidade de Chuva", "Nublado com Poss. de Chuva a Noite", "Nublado com Poss. de Chuva a Tarde", "Nubl. c/ Poss. de Chuva pela Manhã", "Nublado com Possibilidade de Chuva",
            "Chuva a Tarde", 
        ],
        'cloudy-day.png': [
            "Parcialmente Nublado"
        ],
        'rain_sun.png': [
            "Possibilidade de Chuva pela Manhã", "Possibilidade de Chuva a Tarde", "Possibilidade de Chuva a Noite",
        ],
        'clouds.png': [
            "Encoberto", "Nublado", "Variação de Nebulosidade"
        ],
        'undefined.png': [
            "Geada", "Neve", "Não Definido"
        ]
    }