# Geo points

 - **[GET] api/v1/geoPoint/**  
   *Trae todos los geo puntos no eliminados*  

   **REQUEST**
    ```sh

    ```

    **RESPONSE**
     ```sh
     [{
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
        "Deleted": False
       ]
     }, {
       ...
     }]
     ```

 - **[GET] api/v1/geoPoint/:id**  
   *Trae un geo punto si no esá eliminado*  

   **REQUEST**
    ```sh

    ```

    **RESPONSE**
     ```sh
     {
       "id": 01,
       "Place": "Madrid",
       "Activity": "Pasear por la ciudad",
       "DateTime": "2012-01-01 00:00:00",
       "Cords": "99.89768768, -97.89787"
       "Notes": [
         {
           "color": "#885736",
           "content": "Llevar cámara fotográfica"
         },
        "Deleted": false
       ]
     }
     ```

 - **[POST] api/v1/geoPoint/**  
   *Crea un geo punto*  

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
       "id": 01,
       "Place": "Barcelona",
       "Activity": "Pasear por la ciudad",
       "DateTime": "2012-01-01 00:00:00",
       "Cords": "99.89768768, -97.89787"
       "Notes": [],
       "Deleted": False
     }
     ```


 - **[PUT] api/v1/geoPoint/:id**  
   *Actualiza un geo punto*  

   **REQUEST**
    ```sh
    {
      "Place": "Barcelona"  
    }
    ```

    **RESPONSE**
     ```sh
     {
       "id": 01,
       "Place": "Barcelona",
       "Activity": "Pasear por la ciudad",
       "DateTime": "2012-01-01 00:00:00",
       "Cords": "99.89768768, -97.89787"
       "Notes": [
         {
           "color": "#885736",
           "content": "Llevar cámara fotográfica"
         }
       ],
      "Deleted": false
     }
     ```

 - **[POST] api/v1/geoPoint/:id/remove/**  
   *Elimina lógicamente un geo punto*  

   **REQUEST**
    ```sh

    ```

    **RESPONSE**
     ```sh
     {
      "id": 01,
      "Place": "Barcelona",
      "Activity": "Pasear por la ciudad",
      "DateTime": "2012-01-01 00:00:00",
      "Cords": "99.89768768, -97.89787"
      "Notes": [
         {
           "color": "#885736",
           "content": "Llevar cámara fotográfica"
         }
       ],
      "Deleted": true
     }
     ```

 - **[POST] api/v1/geoPoint/:id/addNote/**  
   *Agrega una nota al geo punto*  

   **REQUEST**
    ```sh
    {
      "color": "#678374",
      "content": "Llevar paraguas"
    }
    ```

    **RESPONSE**
     ```sh
     {
      "id": 01,
      "Place": "Barcelona",
      "Activity": "Pasear por la ciudad",
      "DateTime": "2012-01-01 00:00:00",
      "Cords": "99.89768768, -97.89787"
      "Notes": [
         {
           "color": "#885736",
           "content": "Llevar cámara fotográfica"
         },
         {
           "color": "#678374",
           "content": "Llevar paraguas"
         }
       ],
      "Deleted": true
     }
     ```  

 - **[GET] api/v1/geoPoint/:id/notes/**  
   *Consigue las notas no eliminadas*  

   **REQUEST**
    ```sh

    ```

    **RESPONSE**
     ```sh
    [
      {
          "id": 3,
          "color": "#885736",
          "content": "Buscar transporte ir a brucelas"
      },
      {
          "id": 5,
          "color": "#885736",
          "content": "Revisar los precios"
      }
    ]
     ```
