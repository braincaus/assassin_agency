# Assassin Agency

This Project was built as a programming challenge.
It was configured with docker and docker compose to be able to test it and work with it more easily.

In order to run the project, run:

    docker compose up -d

This will up the environment.

    docker compose execute python manage.py migrate
    docker compose execute python manage.py loaddata fixtures

This, will create and ingest database with dummydata.

    boss@mail.com
    manager01@mail.com
    manager02@mail.com
    manager03@mail.com
    hitman01@mail.com
    hitman02@mail.com
    hitman03@mail.com
    hitman04@mail.com
    hitman05@mail.com

Password is **demo1234** for all users.