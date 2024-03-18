import os
from malodetz_latex_utils.latex_utils import generate_latex_table, generate_latex_image

if __name__ == '__main__':
    table_data = [
        ['Header 1', 'Header 2', 'Header 3'],
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    table_latex = generate_latex_table(table_data)
    with open('artifacts/task1.tex', 'w') as f:
        f.write(table_latex)

    image_latex = generate_latex_image('lena.png')

    latex_document = f"""
    \\documentclass{{article}}
    \\usepackage{{graphicx}}
    \\begin{{document}}
    {table_latex}


    {image_latex}
    \\end{{document}}
    """

    with open('artifacts/task2.tex', 'w') as f:
        f.write(latex_document)
    os.system('pdflatex -output-directory=artifacts artifacts/task2.tex')
