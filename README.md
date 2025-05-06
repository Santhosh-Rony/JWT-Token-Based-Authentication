# JWT-Token-Based-Authentication

#File Structure :
root/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── auth.py
│   ├── users.py
│   ├── dependencies.py
│   ├── config.py
│   └── schemas.py
├── requirements.txt
└── README.md


#Auth Flow :

+----------+            POST /login            +-----------------+
|          |---------------------------------->|                 |
|  Client  |  username & password (form-data) |   FastAPI App   |
|          |<----------------------------------|  (login route)  |
+----------+        JWT issued on success     +-----------------+
       │                                          │
       │ Store JWT (e.g. in memory/localStorage) │
       └──────────────────────────────────────────┘
                            
       │                                          
       │  GET /dashboard with                  
       │  Authorization: Bearer <JWT>          
       ▼                                          

+-----------------+         Depends on         +----------------------------+
|                 |<--------------------------|                            |
| FastAPI App     |   get_current_user()      | OAuth2PasswordBearer +     |
| (dashboard)     |                           | JWT decode & verify logic  |
+-----------------+-------------------------->+----------------------------+
       │                                           │
       │ Returns user info & message               │
       │                                           │
       └───────────────────────────────────────────┘

       │                                          
       │  GET /admin with                        
       │  Authorization: Bearer <JWT>          
       ▼                                          

+-----------------+        Depends on          +---------------------+
|                 |<---------------------------|                     |
| FastAPI App     |      admin_required()       | get_current_user()  |
| (admin route)   |  (role check after decode)  |  + role‑check logic |
+-----------------+--------------------------->+---------------------+
       │                                           │
       │ Returns admin‑only message                │
       └───────────────────────────────────────────┘


#Connection :

    config --> auth
    config --> dependencies

    schemas --> users
    schemas --> main

    auth --> users
    auth --> main

    users --> dependencies
    dependencies --> main

    main[main.py] 
