def generate_latex_table(data):
    latex_code = "\\begin{tabular}{" + "c" * len(data[0]) + "}\n"
    latex_code += "\\hline\n"
    latex_code += " & ".join(str(cell) for cell in data[0]) + " \\\\\n"
    latex_code += "\\hline\n"
    for row in data[1:]:
        latex_code += " & ".join(str(cell) for cell in row) + " \\\\\n"
    latex_code += "\\hline\n"
    latex_code += "\\end{tabular}"
    return latex_code


def generate_latex_image(image_path, width=0.8):
    latex_code = f"\\includegraphics[width={width}\\textwidth]{{{image_path}}}"
    return latex_code
