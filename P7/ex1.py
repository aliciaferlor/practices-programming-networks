# -- Example of a client that uses the HTTP.client library
# -- for requesting the main page from the server
import http.client
import json

gene_dic = {"SCRAP": "ENSG00000080603",
            "FRAT1": "ENSG00000165879",
            "ADA":"ENSG00000196839",
            "FXN":"ENSG00000165060",
            "RNU6_269P":"ENSG00000212379",
            "MIR633":"ENSG00000207552",
            "TTTY4C":" ENSG00000228296",
            "RBMY2YP": "ENSG00000227633",
            "FGFR3": "ENSG00000068078",
            "KDR": "ENSG00000128052",
            "ANK2": "ENSG00000145362",}


SERVER = 'rest.ensembl.org'
ENDPOINT = '/info/ping'
PARAMS = '?content-type=application/json'

print(f"\nConnecting to server: {SERVER}\n")

# Connect with the server
conn = http.client.HTTPConnection(SERVER)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
try:
    conn.request("GET", ENDPOINT + PARAMS)

    # -- Read the response message from the server
    response = conn.getresponse()

    # -- Print the status line
    print(f"Response received!: {response.status} {response.reason}\n")

    # -- Read the response's body
    data1 = response.read().decode("utf-8")  #data 1 is a dictionary
    data1 = json.loads(data1)
    print(f"CONTENT: {type(data1)}")

# -- Print the received data
    if data1["ping"] == "1":
        print("PING OK, the database is running")
    else:
        print("ERROR!, the database is not running")


except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()