import os

def add_app_to_installed_apps(project_name, app_name):
    # Get the path to the settings.py file
    settings_file = os.path.join(project_name, "settings.py")

    # Open the settings.py file
    with open(settings_file, "r") as f:
        content = f.read()

    # Check if the app is already in the INSTALLED_APPS list
    if " '{}',".format(app_name) not in content:
        # Add the app name to the INSTALLED_APPS list
        app_line = "'{}'".format(app_name)
        content = content.replace("]\n", "\n    {},\n]".format(app_line))

        # Write the modified content back to the settings.py file
        with open(settings_file, "w") as f:
            f.write(content)

# Rest of the code remains the same...
def create_django_project():
    # Prompt user for project name
    project_name = input("Enter the name of your Django project: ")

    # Create Django project
    os.system("django-admin startproject {}".format(project_name))
    os.chdir(project_name)

    # Prompt user for the number of apps to create
    num_apps = int(input("How many apps do you want to create? "))

    for i in range(num_apps):
        # Prompt user for app name
        app_name = input("Enter the name of your app: ")
        # Create the app
        os.system("python manage.py startapp {}".format(app_name))

        # Add the app to the INSTALLED_APPS list in settings.py
        add_app_to_installed_apps(project_name, app_name)

        # Prompt user for model information
        model_name = input("Enter the name of your first model in {}: ".format(app_name))
        model_fields = input("Enter model fields (comma-separated, e.g., name:str, age:int): ").split(",")

        # Create the Django model based on user input
        model_template = """
from django.db import models

class {}(models.Model):
    {}
    
    def __str__(self):
        return self.name
""".format(model_name, "".join(["{} = models.CharField(max_length=100)\n    ".format(field_name) if field_type == "str" else "{} = models.IntegerField()\n    ".format(field_name) for field_name, field_type in [f.split(":") for f in model_fields]]))

        with open(os.path.join(app_name, "models.py"), "w") as model_file:
            model_file.write(model_template)

        # Finally, run the Django migrations for the app
        os.system("python manage.py makemigrations {}".format(app_name))
        os.system("python manage.py migrate")

if __name__ == "__main__":
    create_django_project()
