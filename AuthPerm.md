## Authentication & Permissions

### Superuser permissions

- first make migrations and migrate to see the database
- create superuser using this command
- python manage.py createsuperuser
- goto this link http://127.0.0.1:8000/admin
- enter the credentials

- superuser has all the permissions
- when you create a new user he only has Active permission
- when you login using this new user credentials you cannot login, because staff permissions not checked
- so to give this staff status permission to this new user you have to login using admin account
and check on staff status
- then you can login using this newuser credentials
- but this user has no permission to view/edit the data

- to give him the permissions login using admin account and in user permissions you can select and choose the permissions for that user
- we can give him the permissions say can add/change/view/delete the user
- when you login using this newuser account after giving him the permissions that user has permission to view/change/delete/update the user.

### Group Permissions

- login using admin account
- click on groups -> add group
- here you can make a group having some permssions for that group
- then you can assign that group to any user so that user has the permissions as that of the group
- no need to assign the permissions for that user individually 