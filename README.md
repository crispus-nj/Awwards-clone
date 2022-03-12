## Awwards Clone
## Author: Crispus Njenga
## User Stories
* Post a project.

* The project is reviewed by peers and peers leave a comment. 
* Peers can leave a rating about the project. 
* The application will output the average rate.
## Technologies Used
1. Django
2. Html
3. Css
4. Bootstrap 5
## set up and installation
clone the project to your local machine

Install project requirements with the following command.
    
    pip3 install -r requirements.txt

Configure the database of choice: Either Sqlite or Postgresql.

create a .env file in the root project folder and include all the secret keys.

Make sure all your keys are accessible in the settings.py file by writing the following commands:

    set -o allexport
    source .env
    echo $SECRET_KEY
Create the admin username by:

    python3 manage.py createsuperuser
run the project by:

    python3 manage.py runserver
## Contacts
Incase of any question or want to add some new features to the project. Contact me through the following to be added as a collaborator.

    Phone Number: 254716554593
    Email: njengacris250@gmail.com
## License MIT
Copyright(c){2022}{Crispus Njenga} Permission is hereby granted, free of charge, to any person obtaining a copy of this project. The person can clone to add any specification that meets his or her requirements.

MIT ©2022 Crispus-Njenga