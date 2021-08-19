### Configuration 
- Clone repository
- In a terminal go to root foolder and execute:
    - python manage.py migrate
    - python manage.py createsuperuser
    - python manage.py runserver
    
### Acces to adminsite with the Url:
- localhost:8000/admin/ Type the **username** and **password** 

### Use of API:

-   URL_BASE: localhost:8000/api/
-   ENDPOINTS:
    -   rooms/
    -   clients/
    -   reservations/


-   Methods http of endpoints:
    -   GET, POST, PUT, DELETE
    

## Examples make request:
-   GET Request for get all records:
    #### METHOD: GET
    -   localhost:8000/api/client/
    -   localhost:8000/api/rooms/
    -   localhost:8000/api/reservations/
    -   localhost:8000/api/invoices/
    
    #### METHOD: GET
-   Request get record by id
    -   localhost:8000/api/client/{id}/
    -   localhost:8000/api/rooms/{id}/
    -   localhost:8000/api/reservations/{id}/
    -   localhost:8000/api/invoices/{id}/

    #### METHOD: POST
-   POST Request for create a new record
    -   localhost:8000/api/client/
        ```
            {
                "firstname": (string required),
                "lastname": string optional,
                "dni": string required unique,
                "address": string optional,
            }
        ```
    -   localhost:8000/api/rooms/
        ```
            {
                "name": string required,
                "description": string optional,
                "type_room": string defaults required,
                "num_beds": integer required,
                "amount": float required,
                "status": string defaults required,
            }
        
            type_room values = ["SIMPLE", "DOUBLE", "TRIPLE", "FAMILY"]
            status values = ["FREE", "OCCUPIED"]
        ```
    -   localhost:8000/api/reservations/
        ```
            {
                "client": integer required,
                "room": integer required
            }
        ```
    -   localhost:8000/api/invoices/
        ```
            {
                "reservation": integer required,
                "amount": float required,
                "type_payment": string required
            }
        
            type_payment values = ["CC", "CASH"]
        ```
    
-   For the PUT request (update), you must send the complete object with the values you want to update, 
      as is done in the POST request, but you have to add the id in the URL, for example:
    
    #### METHOD: put
-   PUT Request for create a new record
    -   localhost:8000/api/client/{id}/
        ```
            {
                "firstname": (string required),
                "lastname": string optional,
                "dni": string required unique,
                "address": string optional,
            }
        ```
    -   localhost:8000/api/rooms/{id}/
        ```
            {
                "name": string required,
                "description": string optional,
                "type_room": string defaults required,
                "num_beds": integer required,
                "price": float required,
                "status": string defaults required,
            }
        
            type_room values = ["SIMPLE", "DOBLE", "TRIPLE", "FAMILIAR"]
            status values = ["FREE", "OCCUPIED"]
        ```
    -   localhost:8000/api/reservations/{id}/
        ```
            {
                "client": integer required,
                "room": integer required,
            }
        ```
        
    #### METHOD: DELETE
- DELETE request for logical deletion of records 
    -   localhost:8000/api/client/{id}/
       
    -   localhost:8000/api/rooms/{id}/
        
    -   localhost:8000/api/reservations/{id}/
    
    -   localhost:8000/api/invoices/{id}/
    


## Search request 
-   Base URL: localhost:8000/search
-   Params: 
    -   type=string - The "TYPE" parameter can receive the values ["client", "room", "reservation"]
    -   search=(string,integer,date) - The "SEARCH" parameter can receive the values numeric, 
        date with format (YYYY-MM-DD), string
        

### Example make request search
-   Request search clients: 
    -   Parameter:
        -   type=client (required)
        -   search= The client can be search for the firstname or the DNI fields.
    
    -   localhost:8000/api/search?type=client (This request get all client)
    -   localhost:8000/api/search?type=client&search=Client 1 (This request get the client by the firstname)
    -   localhost:8000/api/search?type=client&search=123 (This request get the client by the dni)
    
-   Request search rooms: 
    -   Parameter:
        -   type=room (required)
        -   search= The Room can be search for the name, type_room or status fields.
    
    -   localhost:8000/api/search?type=room (This request get all room)
    -   localhost:8000/api/search?type=room&search=Habitacion Simple (This request get the client by the name)
    -   localhost:8000/api/search?type=room&search=SIMPLE (This request get the room with type_room value is SIMPLE. 
        Other values are "DOBLE", "TRIPLE", "FAMILIAR")
    -   localhost:8000/api/search?type=room&search=FREE (This request get the room are FREE. Other value is OCCUPIED)

-   Request search reservations: 
    -   Parameter:
        -   type=reservation (required)
        -   search= The Reservation can be search for the date of create reservation and status fields.
    
    -   localhost:8000/api/search?type=reservation (This request get all reservation)
    -   localhost:8000/api/search?type=reservation&search=2021-08-17 (This request get the reservations from this date)
    -   localhost:8000/api/search?type=reservation&search=PENDING (This request get the reservations with status PENDING. 
        Other values for this field are "PAID", "DELETED")
        
-   Request search invoices: 
    -   Parameter:
        -   type=invoice (required)
        -   search= The Invoice can be search for the code, type payment or date.
    
    -   localhost:8000/api/search?type=invoice (This request get all invoices)
    -   localhost:8000/api/search?type=invoice&search=CADS1234 (This request get the invoice with code equal to 
            the string).
    -   localhost:8000/api/search?type=invoice&search=CC (This request get the invoice with type_payment field 
            CC "Credit Card". Other values for this search are "CASH").
        
    -   localhost:8000/api/search?type=invoice&search=YYYY-MM-DD (This request get the invoice from date field)