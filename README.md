[Oxbotica Challenge Api](https://github.com/bstenm/oxbotica_challenge_api) built with [Flask Restful](https://github.com/flask-restful/flask-restful/).

#### Run it

1. clone this repository

   > git clone git@github.com:bstenm/oxbotica_challenge_api.git

2. cd into the repository

   > cd oxbotica_challenge_api

3. install dependecies

   > pip install flask flask-restful flask-cors pandas

4. run it
   > python app.py

#### Test it

See Youtube video for guidance: https://youtu.be/AYa9gr7PxhM

1.  Get [Postman](https://www.getpostman.com/)

2.  Import Oxbotica_Telemetry_Data_Api.postman_collection.json file from this repository into Postman

3.  Run the server

    > python app.py

4.  Run the Oxbotica_Telemetry_Data_Api collection

#### Notes

    - Returns errors if start or end arguments are not integers
    - Returns empty array without warnings if start > end
