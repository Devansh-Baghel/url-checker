import typer
import csv
import urllib.request

app = typer.Typer()

data = []

# Getting the previously stored data from ./data.csv
def getData():
	with open("data.csv", 'r') as file:
		reader = csv.reader(file)
		for row in reader:
			data.append(row)

# Shows all data
@app.command("show")
def showData():
	getData()
	for i in data: 
		print(i[0])
			# show data using rich


# Add new website to data
@app.command("add")
def addUrl(url):
	url = [url] # have to do this because csv writer works better with lists
	with open("data.csv", 'a') as file:
		writer = csv.writer(file)
		writer.writerow(url)
	print("Added " + url[0])
	# Display confirmation to the user using rich!


# Checks all websites
@app.command("check")
def getUrlStatus():
	getData()
	for url in data:
		print(data)
		url_status = urllib.request.urlopen("https://" + url[0]).getcode()
		print(url_status)


# Clears all data
@app.command("clear-all")
def clearAll():
	with open("data.csv", "w") as file:
		file.write("")
	print("Cleared all data")


# Clears last entry
@app.command("clear-last")
def clearLast():
	global data
	getData()
	print("Removed " + data[-1][0])
	data = data[:-1]
	with open("data.csv", "w") as file:
		for i in data:
			writer = csv.writer(file)
			writer.writerow(i)

if __name__ == "__main__":
    app()