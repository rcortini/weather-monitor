# :sunny: Weather Monitor
---
An open-source project to set up a local server that monitors the weather at a given location, and shows a dashboard with historical data and statistics.

## Installation

### Requirements
- Docker

### Setup
First, copy the sample `.env.example` file to your `.env` file, and fill in the [OpenWeatherMap](https://openweathermap.org/price) API key. They offer a free subscription with 1000 API calls per day, which is more than enough to get the data we want.

Then, do a simple
```bash
docker compose up -d --build
```

### Under the hood
There is a [Mage](mage.ai) server running behind the scenes, with a pipeline that is triggered every hour. To view the status of the Mage server, point your browser to [localhost:6789](localhost:6789).