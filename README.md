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

```

#More :

main.py calls into users/auth to validate login and build a JWT (config).

It returns that JWT (schemas.Token).

On protected routes, FastAPI invokes dependencies, which uses config + users to decode and verify that token.

Role checks happen in dependencies.admin_required.

This modular separation keeps concerns clean:

config for settings

schemas for data shapes

auth for crypto

users for user data

dependencies for request‑time security

main for HTTP routing


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
