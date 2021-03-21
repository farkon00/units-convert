This module uses for convert lengh, volume, mass and area from unit, to other unit.

Documentation: https://units-convert.readthedocs.io/en/latest/

How to use:

import units_convert

print(Convert.from_[ unit ].to_ unit ) # First unit converted to second unit, always return float

Example:

import units_convert

print(Convert.from_m.to_km(1200)) # 1.2

Units:

Lengh: m - meter, km - kilometer, dm - decimeter, mm - millimeter, cm - centimeter.

Weight: g - gram, kg - kilogram, mg - milligram, c - centner, t - ton.

Area: sm - square meter, skm - square kilometer, sdm - square decimeter, smm - square millimeter, scm - square centimeter.

Volume: mc - cubic meter, kmc - cubic kilometer, dmc - cubic decimeter, mmc - cubic millimeter, cmc - cubic centimeter.
