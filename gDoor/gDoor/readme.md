# gDoor Garage Door Opener
 
Django app to control garage door.  Based on the excellent tutorial: https://github.com/shrocky2/GarageWeb
This is my attempt to:
- Learn some Django
- Create a better interface for my garage door than the simple one in GarageWeb. And do somewhat cleaner software design for it.
- No changes made to wiring although I am using sensors that are normally closed so I believe I have the door open and closed reversed from the tutorial.
- Create a more stable solution by deploying it to nginx.
 
I have been running this for months and it's very stable, I do have the rasperi Pi restarting every night at 2 am. I don't really think that is needed but it's working well so haven't tried changing that.
 
My current uwsgi and nginx install based on: https://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html
 
Currently using TCP socket which is updated in ini but not in ngnix config file.
