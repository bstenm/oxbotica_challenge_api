Python Api built with [Flask Restful](https://github.com/flask-restful/flask-restful/) to serve [React Charts Experiment](https://github.com/bstenm/react_charts_experiment).

#### Run it

1. create and activate a virtual env

   > virtualenv venv
   > source venv/bin/activate

2. install dependecies

   > pip install flask flask-restful flask-cors pandas

3. run it
   > python app.py

#### Test it

See Youtube video for guidance: https://youtu.be/i_ze5WTygek

1.  Get [Postman](https://www.getpostman.com/)

2.  Import Oxbotica_Telemetry_Data_Api.postman_collection.json file from this repository into Postman

3.  Run the server

    > python app.py

4.  Run the Oxbotica_Telemetry_Data_Api collection

#### Notes

    - Returns errors if start or end arguments are not integers
    - Returns empty array without warnings if start > end
