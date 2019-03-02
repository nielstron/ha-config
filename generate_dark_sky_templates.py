"""
Generates sensors for each of the available temperature and precipitation forecasts
provided by the dark sky sensor
"""

print("""\
  - platform: template
    sensors:\
""")

for i in range(0, 48):
    tmp = f"""\
        dark_sky_temperature_{i}:
            value_template: >
                {{{{ state_attr("weather.dark_sky", "forecast")[{i}].temperature }}}}
            friendly_name: "Temperature Dark Sky {i} hour forecast"
            unit_of_measurement: '°C'
        dark_sky_precipitation_{i}:
            value_template: >
                {{% set tmp = state_attr("weather.dark_sky", "forecast")[{i}].precipitation %}}
                {{% if  tmp == None %}} 0 {{% else %}} {{{{tmp}}}} {{% endif %}}
            friendly_name: "Precipitation Dark Sky {i} hour forecast"
            unit_of_measurement: '°C'\
        """
    print(tmp)
