# Itinerary

 - **[GET] api/v1/itinerary/**  
   *Trae todos los itinerarios no eliminados*  

   **REQUEST**
    ```sh

    ```

    **RESPONSE**
     ```sh
     [{
       "id": 04,
       "year": "2017",
       "name": "Viaje a Europa 2017",
       "Deleted": False
       },{
       ...
     }]
     ```

 - **[GET] api/v1/itinerary/:id**  
   *Trae un itinerario no esá eliminado*  

   **REQUEST**
    ```sh

    ```

    **RESPONSE**
     ```sh
     {
       "id": 04,
       "name": "Viaje a Europa 2017",
       "Deleted": False,
       "year": "2017",
       "geoPoints": [
       {
         "id": 01,
         "Place": "Madrid",
         "Activity": "Pasear por la ciudad",
         "DateTime": "2012-01-01 00:00:00",
         "Cords": "99.89768768, -97.89787",
         "Notes": [
           {
             "color": "#885736",
             "content": "Llevar cámara fotográfica"
           },
         ],
         "Deleted": False
       }, {
         ...
       }]
       },{
       ...
     }
     ```

 - **[POST] api/v1/itinerary/**  
   *Crea un itinerario*  

   **REQUEST**
    ```sh
    {
      "name": "Viaje a Europa 2017",
      "year": "2017"
    }
    ```

    **RESPONSE**
     ```sh
     {
       "id": 04,
       "name": "Viaje a Europa 2017",
       "year": "2017",
       "Deleted": False
     }
     ```


 - **[PUT] api/v1/itinerary/:id**  
   *Actualiza un itinerario*  

   **REQUEST**
    ```sh
    {
      "name": "Viaje a Europa familia 2017"
      "year": "2017"
    }
    ```

    **RESPONSE**
     ```sh
     {
      "id": 04,
      "name": "Viaje a Europa familia 2017",
      "year": "2017",
      "Deleted": False
     }
     ```

 - **[POST] api/v1/itinerary/:id/remove**  
   *Elimina lógicamente una nota*  

   **REQUEST**
    ```sh

    ```

    **RESPONSE**
     ```sh
     {
      "id": 04,
      "name": "Viaje a Europa familia 2017",
      "year": "2017",
      "Deleted": True
     }
     ```
 - **[POST] api/v1/itinerary/:id/addGeoPoint**  
   *Agrega un geopunto al itinerario*  

   **REQUEST**
    ```sh
    {
      "Place": "Barcelona",
      "Activity": "Pasear por la ciudad",
      "DateTime": "2012-01-01 00:00:00",
      "Cords": "99.89768768, -97.89787"
    }
    ```

    **RESPONSE**
     ```sh
     {
       "id": 04,
       "name": "Viaje a Europa 2017",
       "year": "2017",
       "Deleted": False,
       "geoPoints": [
       {
         "id": 01,
         "Place": "Madrid",
         "Activity": "Pasear por la ciudad",
         "DateTime": "2012-01-01 00:00:00",
         "Cords": "99.89768768, -97.89787",
         "Notes": [ ]
       }, {
         ...
       }]
       },{
       ...
     }
     ```

 - **[GET] api/v1/itinerary/:id/geopoints**  
   *Consigue los geopoints no eliminados*  

   **REQUEST**
    ```sh
    ```

    **RESPONSE**
     ```sh
     [
       {
           "id": 2,
           "place": "Tuxtla",
           "activity": "Comienza el viaje ex tuxla",
           "dateTime": "2017-09-04T06:00:00Z",
           "coords": "41.368927, 2.157792"
       }, {
         ...
       }
     ]
     ```
