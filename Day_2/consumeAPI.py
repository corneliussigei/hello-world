from argparse import ArgumentParser
import http.client
import json
"""Gets input from the command-line and uses github.com Markdown API to convert the text to html"""

#ArgumentParser enables arguments to be passed at the terminal
theParser = ArgumentParser(description = "Process integers")

#getting the data that the user wants to be converted to html
theParser.add_argument("user_input",help = "Input to be processed by GitHub API. For more than one word use quotes.")

args = theParser.parse_args()
connection = http.client.HTTPSConnection("api.github.com")

request_header = {"content-type":"application/json", "User-Agent":"Cornelius"}

user_string = {'text': args.user_input}
json_user_str = json.dumps(user_string)

#post json data to Github.com
#Github markdown api converts the text to html
connection.request('POST', '/markdown', json_user_str, request_header)

#getting response from the server and decoding it
response = connection.getresponse()
print(response.read().decode())