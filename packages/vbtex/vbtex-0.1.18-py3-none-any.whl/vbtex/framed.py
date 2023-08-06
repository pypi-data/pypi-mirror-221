
import click
import os
import sys
from rich.console import Console
from .choice_option import ChoiceOption

from datetime import datetime


@click.command(
    help="Renders tex expressions into pdf"
)
@click.option(
    '-i',
    '--input_text',
    type=click.STRING,
    default=None,
    show_default=True,
    help="It takes std inputs and try to render as pdf"
)
@click.option(
    '-s',
    '--size',
    prompt='Format',
    type=click.Choice(['SQUARE + VRECT', 'SQUARE', 'VRECT', 'HRECT']),
    cls=ChoiceOption,
    default=1,
    show_default=True,
    help="Format of the output"
)
@click.option(
    '-b',
    '--background',
    type=click.Path(),
    default=f'$BG/Wheat.jpg',
    show_default=True,
    help="Background file for png"
)
def framed(input_text, size, background):
   
    def get_file_name_png(size):
        now = datetime.now()
        file_name = now.strftime("%Y_%m_%d@%H_%M_%S")
        return f'{file_name}_{size.lower()}.png'

    def get_file_name_date_time():
        now = datetime.now()
        file_name = now.strftime("%Y_%m_%d@%H_%M_%S")
        return f'{file_name}.tex'


    with open(f'./content.tex', 'r+') as file:
        if os.stat('./content.tex').st_size == 0:
            if input_text is None:
                tex = click.edit()
                file.write(tex)
            else:
                file.write(input_text)

    
#
#    if size == 'SQUARE + VRECT':
#        os.makedirs(f'./square', exist_ok=True)
#        os.makedirs(f'./vrect', exist_ok=True)
#        path_main_square = os.path.join(f'./square', 'main.tex')
#        path_main_vrect = os.path.join(f'./vrect', 'main.tex')
#    else:
#        os.makedirs(f'./{size.lower()}', exist_ok=True)
#        path_main = os.path.join(f'./{size.lower()}', 'main.tex')
#
    os.makedirs(f'./{size.lower()}', exist_ok=True)
    path_main = os.path.join(f'./{size.lower()}', 'main.tex')


    with open(path_main, 'w') as file:
        file.write(f'\\documentclass{{article}}\n')
        file.write(f'\\usepackage{{v-equation}}\n')
        if size == 'SQUARE':
            file.write(f'\\vgeometry[5][5][0]\n')
        elif size == 'VRECT':
            file.write(f'\\vgeometry[4.5][8][0]\n')
        elif size == 'HRECT':
            file.write(f'\\vgeometry[8][4.5][0]\n')
        else:
            file.write(f'\\vgeometry[5][5][0]\n')


        file.write(f'\\begin{{document}}\n')

        file.write(f'\\vspace*{{\\fill}}\n\n')
        file.write(f'\\begin{{center}}\n')
        file.write(f'\\input{{../content.tex}}\n')
        file.write(f'\\end{{center}}\n')
        file.write(f'\\vspace*{{\\fill}}\n\n')
        file.write(f'\\end{{document}}')



    try:
        os.chdir(f'./{size.lower()}')
        try:
            os.system("pdflatex -shell-escape main.tex")
            try:
                os.system(f'vbpdf instagram -r 1 1 -b {background}')
                try:
                    os.system(f'cp ./downloads/main_f.png ../archive/{get_file_name_png(size)}')
                    os.system(f'cp ../content.tex ../archive/{get_file_name_date_time}')
                except:
                    click.echo("Failed to archive")
            except:
                click.echo("Failed to run vbpdf instagram")
        except:
            click.echo("Failed to rum pdflatex")
    except:
        click.echo("Failed to run cddir") 


    


