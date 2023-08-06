"""
Peak load module
SPDX - License - Identifier: LGPL - 3.0 - or -later
Copyright © 2023 Project Coder Guille Gutierrez guillermo.gutierrezmorote@concordia.ca
Code contributor Pilar Monsalvete Alvarez de Uribarri pilar.monsalvete@concordia.ca
Code contributor Oriol Gavalda Torrellas oriol.gavalda@concordia.ca
"""

import pandas as pd

import hub.helpers.constants as cte


class PeakLoad:
  """
  Peak load class
  """

  def __init__(self, building):
    self._building = building

  @property
  def electricity_peak_load(self):
    """
    Get the electricity peak load in W
    """
    array = [None] * 12
    heating = 0
    cooling = 0
    for system in self._building.energy_systems:
      for demand_type in system.demand_types:
        if demand_type == cte.HEATING:
          heating = 1
        if demand_type == cte.COOLING:
          cooling = 1
    if cte.MONTH in self._building.heating_peak_load.keys() and cte.MONTH in self._building.cooling_peak_load.keys():
      peak_lighting = 0
      peak_appliances = 0
      for thermal_zone in self._building.internal_zones[0].thermal_zones:
        lighting = thermal_zone.lighting
        for schedule in lighting.schedules:
          peak = max(schedule.values) * lighting.density * thermal_zone.total_floor_area
          if peak > peak_lighting:
            peak_lighting = peak
        appliances = thermal_zone.appliances
        for schedule in appliances.schedules:
          peak = max(schedule.values) * appliances.density * thermal_zone.total_floor_area
          if peak > peak_appliances:
            peak_appliances = peak
      monthly_electricity_peak = [0.9 * peak_lighting + 0.7 * peak_appliances] * 12
      conditioning_peak = []
      for i, value in enumerate(self._building.heating_peak_load[cte.MONTH]):
        if cooling * self._building.cooling_peak_load[cte.MONTH][i] > heating * value:
          conditioning_peak.append(cooling * self._building.cooling_peak_load[cte.MONTH][i])
        else:
          conditioning_peak.append(heating * value)
        monthly_electricity_peak[i] += 0.8 * conditioning_peak[i]
      electricity_peak_load_results = pd.DataFrame(
        monthly_electricity_peak,
        columns=[f'{self._building.name} electricity peak load W']
      )
    else:
      electricity_peak_load_results = pd.DataFrame(array, columns=[f'{self._building.name} electricity peak load W'])

    return electricity_peak_load_results
