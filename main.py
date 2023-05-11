import typer
import csv
import urllib.request

app = typer.Typer()

data = [];

# Getting the previously stored data from ./data.csv
def getData():
	with open("data.csv", 'r') as file:
		reader = csv.reader(file)
		for row in reader:
			data.append(row)

getData()

def displayInfo(url_status):
	if url_status >= 400 and url_status < 499:
		pass
		# Use rich lib to display the error
	else:
		pass
		# Use rich lib to display the success

def getUrlStatus(data):
	for url in data:
		url_status = urllib.request.urlopen(url).getcode()
		displayInfo(url)

@app.command()
def addUrl(url):
	url = [url] 
	with open("data.csv", 'a') as file:
		writer = csv.writer(file)
		writer.writerow(url)
	# Display confirmation to the user using rich!


if __name__ == "__main__":
    app()