# Project Name - Pitch Management

## Overview
The Pitch Management API is designed to provide a simple and efficient solution for monitoring the pitches.
## Prerequisites


- Docker: [Install Docker](https://docs.docker.com/get-docker/)
- Docker Compose (if applicable): [Install Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started


1. **Clone the Repository:**

    ```bash
    git clone https://github.com/RiddhiiSuthar/Pitch_Management.git
    cd Pitch_Management
    ```

2. **Build and Run with Docker Compose:**

    ```bash
    docker-compose build
    docker-compose up
    ```



## Features

1. **Pitch Data CRUD Operations:**
   - This endpoints for managing pitch data, allowing you to perform CRUD (Create, Read, Update, Delete) operations on pitch entries.
   
    ## Endpoints

    1. **Create (POST):**
    - Endpoint: `pitch_manage/pitch-create`
    - Description: Create a new pitch entry.

    2. **Read (GET):**
    - Endpoint: `/pitch_manage/pitch-list`
    - Description: Retrieve a list of all pitch entries.
    

    3. **Update (POST):**
    - Endpoint: `/pitch_manage/pitch-update/{pitch_id}`
    - Description: Update an existing pitch entry by ID.

    4. **Delete (DELETE):**
    - Endpoint: `/pitch_manage/pitch-delete/{pitch_id}`
    - Description: Delete an existing pitch entry by ID.
    
2. **Weather Data Integration:**
    - To enhance the functionality of the Pitch Management API, integrated external weather data from OpenWeatherMap. This feature allows you to fetch real-time weather information for a given location.

    ### Fetch Weather Data:

    - Function: get_weather_data(pitch_id)
    - Description: Fetch current weather data for a specific location of pitch.

3. **Weather-Driven Maintenance Logic:**
    -Utilize weather information to enhance pitch management:
    ## Condition Scale

    The pitch condition is represented on a scale from 1 to 10, where:

    - 10: Excellent (Good condition)
    - ...
    - 1: Poor (Not good condition)

    ### Next Maintenance Day and Update 'Current Condition:
    - Determine maintenance scheduling based on weather conditions.
        ### 1. Rainy Weather Handling

        If the weather is identified as "Rain," the script performs the following actions:

        - For natural turf, maintenance is scheduled every 3 days with a condition update to 3.
        - For artificial turf, maintenance is scheduled every 5 days with a condition update to 5.
        - For hybrid turf, maintenance is scheduled every 4 days with a condition update to 4.

        ### 2. Regular Maintenance

        If the weather is not "Rain," regular maintenance is scheduled based on the defined `REGULAR_MAINTENANCE_DAY` in the settings.


    ### List Pitches Requiring Maintenance Soon:
    - Endpoint: `/pitch_manage`
    - Get pitches needing maintenance soon
4. **Access the Application:**

    Open your web browser and go to [http://localhost:8000/pitch_manage].


