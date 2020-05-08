# Using custom management commands in Django
This is the code used in my article on how to use custom management commands in a Django app, available at https://www.jimwritescode.com/creating-custom-management-commands-in-django

## To use:
- create a new Django project
- copy the **customer_manager** folder into your Django project's root directory
- add the customer_manager app to the `INSTALLED_APPS` section of your Django project's `settings.py` file - you can add the line `'customer_manager.apps.CustomerManagerConfig',` to that section
- from the command line, run `manage.py makemigrations` and then `manage.py migrate`
- you can run the management commands using `manage.py` followed by the command name - for example, `manage.py delete_all_customers`

If you have any questions or comments, please email me at jim@jimwritescode.com or leave a comment on the blog at www.jimwritescode.com

-Jim Armstrong
