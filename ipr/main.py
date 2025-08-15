from weasyprint import HTML, CSS
from jinja2 import Environment, FileSystemLoader
import os



data = {
	"title":""
}

# HTML-шаблон
env = Environment(loader=FileSystemLoader('./templates'))
template = env.get_template("template.html")
html_content = template.render(data)

# Преобразуем в PDF
HTML(string=html_content).write_pdf("report.pdf",stylesheets=[
	CSS(filename='./templates/styles/index.css'),
	CSS(filename='./templates/styles/Normalize.css'),
	CSS(filename='./templates/styles/styles.css')
	])

print("PDF создан: report.pdf")
