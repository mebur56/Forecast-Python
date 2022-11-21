# Forecast
This a python project using https://openweathermap.org/ free API

## Requirements


### Python

Install Python3  on https://www.python.org/downloads/ open a terminal write and exec
```Python --version```

If everythins is right you should see your python version E.G
```Python 3.10.8```

### MongoDB

Download and install MongoDB on https://www.mongodb.com/try/download/community

## Installation

Open the project and create a `.env` file, copy the content from `.env_sample` and configure the env E.G

```
API_KEY=OPENWEATHER_API_KEY
API_BASE_URL=https://api.openweathermap.org/data/2.5/forecast
CONNECTION_STRING=MONGODB_CONNECTION_STRING 
 ```

 Leave the API_BASE_URL as it is. On API_KEY put your Openweathermap API_KEY you can get on https://home.openweathermap.org/api_keys

 On CONNECTION_STRING put your mongoDB connection string E.G

 #### Default
 ```
 mongodb://localhost:27017/
 ``` 
 #### Custom
 ```
 mongodb://myDBReader:password@mongodb0.example.com:27017/?authSource=admin
 ``` 

 ### Install packages

 On the root of the project run
 ``` pip install -r requirements.txt ```
 To install required packages

 ## Running

 To run the project from root run 
 ```
 python -m flask --app ./src/main.py run 
 ```

 ## Endpoints
 Get Forecast for each 3 hours from the next 5 days from Salvador-BA Brazil
```/forecast```


Get Forecast with minimal data for each 3 hours from the next 5 days from Salvador-BA Brazil__
```/forecast/minimal```


Get Forecast for each 3 hours from the next 5 days from the specified latitude and longitude__
```/forecast/<lat>/<lon>```


Get Forecast with minimal data for each 3 hours from the next 5 days from the specified latitude and longitude__

```/forecast/minimal/<lat>/<lon>```

Get previous requests made with full data__
```/consults ```

Get previous request made with minimal data__
```/consults/minimal```