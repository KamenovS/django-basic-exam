from django.db import models

class DriverCategoryChoices(models.TextChoices):
    CLASS_1 = 'C1', 'CLASS 1'
    CLASS_2 = 'C2', 'CLASS 2'
    HAZMAT = 'HM', 'HazMat'
    HEAVY_HAULERS = 'HH', 'Heavy Haulers'
    LONG_HAUL = 'LH', 'Long-Haul'
    SHORT_HAUL = 'SH', 'Short-Haul'

class TrailerTypeChoices(models.TextChoices):
    DRY_VAN = 'DV', 'Dry Van'
    REFRIGERATED = 'FRG', 'Refrigerated (Reefer)'
    FLATBED = 'FB', 'Flatbed'
    DROP_DECK = 'DD', 'Drop-Deck/Step-Deck'
    LOWBOY = 'LB', 'Lowboy/Double Drop'
    TANKER = 'TNK', 'Tanker'
    CONTAINER = 'CON', 'Container'