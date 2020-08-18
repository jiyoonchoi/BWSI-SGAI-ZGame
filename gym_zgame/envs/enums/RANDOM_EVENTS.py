from enum import IntEnum
import random
import warnings


class WEATHERS(IntEnum):
    SUNNY = 0
    RAINY = 1
    CLOUDY = 2
    SNOWY = 3

    @staticmethod
    def print():
        for weather in WEATHERS:
            print('{0} -> {1}'.format(weather.value, weather.name))

    @classmethod
    def get_random(cls):
        return random.choice(list(WEATHERS))

    @staticmethod
    def get_value_from_string(weather):
        if weather == WEATHERS.SUNNY:
            return WEATHERS.SUNNY.value
        elif weather == WEATHERS.RAINY:
            return WEATHERS.RAINY.value
        elif weather == WEATHERS.CLOUDY:
            return WEATHERS.CLOUDY.value
        elif weather == WEATHERS.SNOWY:
            return WEATHERS.SNOWY.value
        else:
            warnings.warn('Tried to convert string ({}) to WEATHERS enum and failed; returned SUNNY'.format(weather))
            return WEATHERS.SUNNY.value

    @staticmethod
    def get_name_from_string(weather):
        if weather == WEATHERS.SUNNY:
            return WEATHERS.SUNNY.name
        elif weather == WEATHERS.RAINY:
            return WEATHERS.RAINY.name
        elif weather == WEATHERS.CLOUDY:
            return WEATHERS.CLOUDY.name
        elif weather == WEATHERS.SNOWY:
            return WEATHERS.SNOWY.name
        else:
            warnings.warn('Tried to convert string ({}) to WEATHERS enum and failed; returned NONE'.format(weather))
            return WEATHERS.SUNNY.name


class CRIMES(IntEnum):
    MURDER = 0
    SHOOTOUT = 1
    BOMBING = 2
    BANK_ROBBERY = 3
    LOOTING = 4
    TRESPASSING = 5
    CHEMICAL_ATTACK = 6

    @staticmethod
    def print():
        for crime in CRIMES:
            print('{0} -> {1}'.format(crime.value, crime.name))

    @classmethod
    def get_random(cls):
        return random.choice(list(CRIMES))

    @staticmethod
    def get_value_from_string(crime):
        if crime == CRIMES.MURDER:
            return CRIMES.MURDER.value
        elif crime == CRIMES.SHOOTOUT:
            return CRIMES.SHOOTOUT.value
        elif crime == CRIMES.BOMBING:
            return CRIMES.BOMBING.value
        elif crime == CRIMES.BANK_ROBBERY:
            return CRIMES.BANK_ROBBERY.value
        elif crime == CRIMES.LOOTING:
            return CRIMES.LOOTING.value
        elif crime == CRIMES.TRESPASSING:
            return CRIMES.TRESPASSING.value
        elif crime == CRIMES.CHEMICAL_ATTACK:
            return CRIMES.CHEMICAL_ATTACK.value
        else:
            warnings.warn('Tried to convert string ({}) to CRIMES enum and failed; returned NONE'.format(crime))
            return CRIMES.MURDER.value

    @staticmethod
    def get_name_from_string(crime):
        if crime == 'CRIME.MURDER':
            return CRIMES.MURDER.value
        elif crime == 'CRIME.SHOOTOUT':
            return CRIMES.SHOOTOUT.value
        elif crime == 'CRIME.BOMBING':
            return CRIMES.BOMBING.value
        elif crime == 'CRIME.BANK_ROBBERY':
            return CRIMES.BANK_ROBBERY.value
        elif crime == 'CRIME.LOOTING':
            return CRIMES.LOOTING.value
        elif crime == 'CRIME.TRESPASSING':
            return CRIMES.TRESPASSING.value
        elif crime == 'CRIME.CHEMICAL_ATTACK':
            return CRIMES.CHEMICAL_ATTACK.value
        else:
            warnings.warn('Tried to convert string ({}) to CRIMES enum and failed; returned NONE'.format(crime))
            return CRIMES.MURDER.name


class NATURAL_DISASTERS(IntEnum):
    TORNADO = 0
    TSUNAMI = 1
    HURRICANE = 2
    FLOOD = 3
    EARTHQUAKE = 4
    VOLCANIC_ERUPTION = 5

    @staticmethod
    def print():
        for natural_disasters in NATURAL_DISASTERS:
            print('{0} -> {1}'.format(natural_disasters.value, natural_disasters.name))

    @classmethod
    def get_random(cls):
        return random.choice(list(NATURAL_DISASTERS))

    @staticmethod
    def get_value_from_string(natural_disasters):
        if natural_disasters == NATURAL_DISASTERS.TORNADO:
            return NATURAL_DISASTERS.TORNADO.value
        elif natural_disasters == NATURAL_DISASTERS.TSUNAMI:
            return NATURAL_DISASTERS.TSUNAMI.value
        elif natural_disasters == NATURAL_DISASTERS.HURRICANE:
            return NATURAL_DISASTERS.HURRICANE.value
        elif natural_disasters == NATURAL_DISASTERS.FLOOD:
            return NATURAL_DISASTERS.FLOOD.value
        elif natural_disasters == NATURAL_DISASTERS.EARTHQUAKE:
            return NATURAL_DISASTERS.EARTHQUAKE.value
        elif natural_disasters == NATURAL_DISASTERS.VOLCANIC_ERUPTION:
            return NATURAL_DISASTERS.VOLCANIC_ERUPTION.value
        else:
            warnings.warn('Tried to convert string ({}) to NATURAL_DISASTERS enum and failed; returned NONE'.format(natural_disasters))
            return NATURAL_DISASTERS.TORNADO.value

    @staticmethod
    def get_name_from_string(natural_disasters):
        if natural_disasters == 'NATURAL_DISASTERS.TORNADO':
            return NATURAL_DISASTERS.TORNADO.value
        elif natural_disasters == 'NATURAL_DISASTERS.TSUNAMI':
            return NATURAL_DISASTERS.TSUNAMI.value
        elif natural_disasters == 'NATURAL_DISASTERS.HURRICANE':
            return NATURAL_DISASTERS.HURRICANE.value
        elif natural_disasters == 'NATURAL_DISASTERS.FLOOD':
            return NATURAL_DISASTERS.FLOOD.value
        elif natural_disasters == 'NATURAL_DISASTERS.EARTHQUAKE':
            return NATURAL_DISASTERS.EARTHQUAKE.value
        elif natural_disasters == 'NATURAL_DISASTERS.VOLCANIC_ERUPTION':
            return NATURAL_DISASTERS.VOLCANIC_ERUPTION.value
        else:
            warnings.warn('Tried to convert string ({}) to NATURAL_DISASTERS enum and failed; returned NONE'.format(natural_disasters))
            return NATURAL_DISASTERS.TORNADO.name
