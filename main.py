import typer
import csv
import urllib.request
from prettytable import PrettyTable
table = PrettyTable()
table.field_names = ["URL", "STATUS"]

app = typer.Typer()

arrayOfUrls = []

# Getting the previously stored data from ./data.csv
def getData():
	with open("./data.csv", 'r') as file:
		reader = csv.reader(file)
		for row in reader:
			arrayOfUrls.append(row)

# Shows all data
@app.command("show")
def showData():
	getData()
	for i in arrayOfUrls: 
		print(i[0])
			# show data using rich


# Add new website to data
@app.command("add")
def addUrl(url):
	url = [url] # have to do this because csv writer works better with lists
	with open("./data.csv", 'a') as file:
		writer = csv.writer(file)
		writer.writerow(url)
	print("Added " + url[0])
	# Display confirmation to the user using rich!


# Checks all websites
@app.command("check")
def getUrlStatus():
	getData()
	for url in arrayOfUrls:
		url_status = urllib.request.urlopen("https://" + url[0]).getcode()
		table.add_row([url[0], url_status])
	print(table)

# Clears all data
@app.command("clear-all")
def clearAll():
	with open("./data.csv", "w") as file:
		file.write("")
	print("Cleared all data")


# Clears last entry
@app.command("clear-last")
def clearLast():
	global arrayOfUrls
	getData()
	print("Removed " + arrayOfUrls[-1][0])
	arrayOfUrls = arrayOfUrls[:-1]
	with open("./data.csv", "w") as file:
		for i in arrayOfUrls:
			writer = csv.writer(file)
			writer.writerow(i)

if __name__ == "__main__":
	app()