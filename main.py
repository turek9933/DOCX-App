import json
import click

# Funkcje zarządzające danymi
def save_data(data):
    with open('data.json', 'w') as file:
        json.dump(data, file)

def load_data():
    try:
        with open('data.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"projects": []}

# Funkcje CLI
@click.group()
def cli():
    """Aplikacja do zarządzania projektami"""
    pass

@cli.command()
@click.argument('name')
def create_project(name):
    """Tworzy nowy projekt"""
    data = load_data()
    data["projects"].append({"id": len(data["projects"]) + 1, "name": name, "tasks": []})
    save_data(data)
    click.echo(f'Projekt {name} został utworzony.')

@cli.command()
def list_projects():
    """Wyświetla listę projektów"""
    data = load_data()
    for project in data["projects"]:
        click.echo(f'{project["id"]}: {project["name"]}')

# Tutaj mogą zostać dodane kolejne funkcje CLI do zarządzania zadaniami, edycji, itp.

if __name__ == '__main__':
    cli()
