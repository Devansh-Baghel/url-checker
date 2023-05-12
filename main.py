import typer
import csv
import urllib.request

app = typer.Typer()

data = [];

# Getting the previously stored data from ./data.csv
@app.command("show")
def getData():
	with open("data.csv", 'r') as file:
		reader = csv.reader(file)
		for row in reader:
			data.append(row)
			print(row)
			# show data using rich

# getData()

@app.command("check")
def getUrlStatus():
	getData()
	for url in data:
		print(data)
		url_status = urllib.request.urlopen("https://" + url[0]).getcode()
		print(url_status)


@app.command("add")
def addUrl(url):
	url = [url] # have to this because csv writer works better with lists
	with open("data.csv", 'a') as file:
		writer = csv.writer(file)
		writer.writerow(url)
	print("Added " + url[0])
	# Display confirmation to the user using rich!


if __name__ == "__main__":
    app()