# 1

query = """
SELECT * FROM (
SELECT bike_number, start_station, duration
FROM trips
ORDER BY duration DESC
LIMIT 1
)
"""


#2

query = """
SELECT bike_number, birth_date, start_station
FROM trips
WHERE bike_number LIKE "%7"
  AND start_station IN (10, 20, 30,40, 50)
LIMIT 10
"""





