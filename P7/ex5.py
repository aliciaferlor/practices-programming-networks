# -- Example of a client that uses the HTTP.client library
# -- for requesting the main page from the server
import http.client
import json
import seq1
from termcolor import colored

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
ENDPOINT = '/sequence/id/'
PARAMS = '?content-type=application/json'

print(f"\nConnecting to server: {SERVER}\n")

# Connect with the server
conn = http.client.HTTPConnection(SERVER)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
try:
    for k,id in gene_dic.items():
        conn.request("GET", ENDPOINT + id + PARAMS)
        # -- Read the response message from the server
        r1 = conn.getresponse()
        # -- Print the status line
        print(f"Response received!: {r1.status} {r1.reason}\n")
        if r1.status == 200:
            # -- Read the response's body
            data1 = json.loads(r1.read().decode())
            sequence = seq1.Seq(data1["seq"])
            seq_len = sequence.len()
            percentages = sequence.percentages()
            freq_base = sequence.frequent_base(sequence.count())
            print("Gene", colored(k, "green"))
            print("Total length: ", colored(seq_len, "yellow"))
            print(percentages)
            print("Most frequent base: ", colored(freq_base, "cyan"))


except KeyError:
    print("The gene is not in this dictionary. Choose one of the following:", list(gene_dic.keys()))
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()
