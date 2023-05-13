import typer
import csv
import urllib.request
from prettytable import PrettyTable

check_table = PrettyTable()
show_table = PrettyTable()

check_table.field_names = ["URL", "STATUS"]
show_table.field_names = ["URL"]

app = typer.Typer()

array_of_urls = []

# Getting the previously stored data from ./data.csv
def getData():
	with open("./data.csv", 'r') as file:
		reader = csv.reader(file)
		for row in reader:
			array_of_urls.append(row)

# Shows all data
@app.command("show")
def showData():
	getData()
	for i in array_of_urls:
		show_table.add_row(i)
			# show data using rich
	print(show_table)

# Add new website to data
@app.command("add")
def addUrl(url):
	with open("./data.csv", 'a') as file:
		writer = csv.writer(file)
		writer.writerow([url])
	print("Added " + url)
	# Display confirmation to the user using rich!


# Checks all websites
@app.command("check")
def getUrlStatus():
	getData()
	for url in array_of_urls:
		url_status = urllib.request.urlopen("https://" + url[0]).getcode()
		check_table.add_row([url[0], url_status])
	print(check_table)

# Clears all data
@app.command("clear-all")
def clearAll():
	with open("./data.csv", "w") as file:
		file.write("")
	print("Cleared all data")


# Clears last entry
@app.command("clear-last")
def clearLast():
	global array_of_urls
	getData()
	print("Removed " + array_of_urls[-1][0])
	array_of_urls = array_of_urls[:-1]
	with open("./data.csv", "w") as file:
		for i in array_of_urls:
			writer = csv.writer(file)
			writer.writerow(i)

if __name__ == "__main__":
	app()