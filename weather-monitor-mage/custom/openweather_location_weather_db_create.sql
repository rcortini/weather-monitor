CREATE TABLE IF NOT EXISTS weather_location (
    obs_time TIMESTAMP WITH TIME ZONE,
    latitude FLOAT,
    longitude FLOAT,
    temperature FLOAT,
    humidity FLOAT,
    pressure FLOAT,
    weather TEXT,
    wind_speed FLOAT,
    wind_deg FLOAT
)