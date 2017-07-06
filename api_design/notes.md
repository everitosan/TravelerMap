# Notes

 - **[GET] api/v1/note/**  
   *Trae todos las notas no eliminados*  

   **REQUEST**
    ```sh

    ```

    **RESPONSE**
     ```sh
     [{
       "id": 04,
       "color": "#885736",
       "content": "Llevar cámara fotográfica"
       "Deleted": False
       },{
       ...
     }]
     ```

 - **[GET] api/v1/note/:id**  
   *Trae una nota si no esá eliminado*  

   **REQUEST**
    ```sh

    ```

    **RESPONSE**
     ```sh
    {
       "id": 04,
       "color": "#885736",
       "content": "Llevar cámara fotográfica"
       "Deleted": False
    }
     ```

 - **[POST] api/v1/note/**  
   *Crea una nota*  

   **REQUEST**
    ```sh
    {
      "color": "#885736",
      "content": "Llevar cámara fotográfica"
    }
    ```

    **RESPONSE**
     ```sh
    {
      "id": 04,
      "color": "#885736",
      "content": "Llevar cámara fotográfica"
      "Deleted": False
    }
     ```


 - **[PUT] api/v1/note/:id**  
   *Actualiza una nota*  

   **REQUEST**
    ```sh
    {
      "color": "#885736",
      "content": "Llevar paraguas"
    }
    ```

    **RESPONSE**
     ```sh
    {
      "id": 04,
      "color": "#885736",
      "content": "Llevar paraguas"
      "Deleted": False
    }
     ```

 - **[PUT] api/v1/deleteNote/:id**  
   *Elimina lógicamente una nota*  

   **REQUEST**
    ```sh

    ```

    **RESPONSE**
     ```sh
     {
       "id": 04,
       "color": "#885736",
       "content": "Llevar paraguas"
       "Deleted": True
     }
     ```
