# AutoCreateApp - Django Project Automation

AutoCreateApp is a Python package that automates the process of creating Django projects with multiple apps and models based on user input. With this tool, you can quickly set up Django projects without manually creating apps, models, and migration files.

## Installation

You can install AutoCreateApp via pip:

```bash
pip install autocreateapp
```

## Usage

Once AutoCreateApp is installed, you can use the `autocreateapp` command to create your Django project interactively.

```bash
autocreateapp
```

Follow the prompts to provide the project name, the number of apps to create, app names, model names, and model fields. The package will automatically generate the necessary files and set up the Django project with your specified apps and models.

## How It Works

AutoCreateApp uses Python's built-in `os` module to create and navigate directories, and it utilizes Django's command-line tools (`django-admin` and `manage.py`) to create projects, apps, and migration files.

The `add_app_to_installed_apps` function ensures that the newly created apps are added to the `INSTALLED_APPS` list in the Django project's `settings.py` file.

The package also supports interactive model creation, allowing you to specify model names and their respective fields, such as strings (`CharField`) or integers (`IntegerField`).

## Example

Here's a simple example of how to use AutoCreateApp:

```bash
# Create a new Django project with two apps and models
autocreateapp
Enter the name of your Django project: myproject
How many apps do you want to create? 2

Enter the name of your app: app1
Enter the name of your app: app2

Enter the name of your first model in app1: MyModel
Enter model fields (comma-separated, e.g., name:str, age:int): name:str, age:int

Enter the name of your first model in app2: AnotherModel
Enter model fields (comma-separated, e.g., title:str, description:str): title:str, description:str
```

After the above steps, you'll have a new Django project called `myproject`, with two apps (`app1` and `app2`), each containing one model (`MyModel` and `AnotherModel`) with the specified fields.

## License

AutoCreateApp is distributed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contributions

Contributions are welcome! If you have any suggestions, bug reports, or improvements, please open an issue or submit a pull request.

---

Happy coding! 🚀