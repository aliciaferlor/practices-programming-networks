import http.server
import http.client
import socketserver
import termcolor
from pathlib import Path
import jinja2 as j
import json
from urllib.parse import parse_qs, urlparse
from seq1 import Seq

# Define the Server's port
PORT = 8080
html_folder = "./html/"


def read_html_file(filename):
    contents = Path(html_folder + filename).read_text()
    contents = j.Template(contents)
    return contents


def ensembl_info(endpoint):
    SERVER = "rest.ensembl.org"
    PARAMS = "?content-type=application/json"
    connection = http.client.HTTPConnection(SERVER)
    connection.request("GET", endpoint + PARAMS)
    response = connection.getresponse()
    data = response.read().decode("utf-8")
    data_dic = json.loads(data)
    return data_dic


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


# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritance all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""
        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        # IN this simple server version:
        # We are NOT processing the client's request
        # It is a happytest server: It always returns a message saying
        # that everything is ok
        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)   #is the dictionary with the values we input
        print("The old path was", self.path)
        print("The new path is", path)
        print("arguments", arguments)

        # Message to send back to the client
        if self.path == "/":
            contents = read_html_file("index.html").render()

        elif path == "/listSpecies":
            try:
                limit = int(arguments["limit"][0])
                endpoint = '/info/species'
                new_dic = ensembl_info(endpoint)["species"]
                list_species = []
                for n in range(0, limit):
                    list_species.append(new_dic[n]["common_name"])

                if "json" in arguments:
                    contents = {"limit": limit,
                    "list_species": list_species,
                    "number_species": len(new_dic)}
                else:
                    contents = read_html_file("list_species.html").render(context={
                    "limit": limit,
                    "list_species": list_species,
                    "number_species": len(new_dic)})

            except TypeError:
                if "json" in arguments:
                    contents = {"error": list_species}
                else:
                    contents = read_html_file('error.html').render(context={"error": list_species})

            except ValueError:
                if "json" in arguments:
                    contents = {"error": "The entry should be an integer"}
                else:
                    contents = read_html_file('error.html').render()

        elif path == "/karyotype":
            try:
                specie = arguments["specie"][0].replace(' ', '_')
                endpoint = '/info/assembly/'
                new_dic = ensembl_info(endpoint + specie)
                context = {"Karyotype": new_dic["karyotype"], "specie": specie}

                if "json" in arguments:
                    contents = {"karyotype": new_dic["karyotype"]}
                else:
                    contents = read_html_file("karyotype.html").render(context = context)

            except KeyError:
                if "json" in arguments:
                    contents = {"error": "The key is not in the ensembl data"}
                else:
                    contents = read_html_file('error.html').render()


        elif path == "/chromosomeLength":
            try:
                specie = arguments["specie"][0].strip()
                chromosome = arguments["chromosome"][0].strip()
                endpoint = '/info/assembly/'
                new_dic = ensembl_info(endpoint + specie + '/' + chromosome)
                #print(new_dic)

                if "json" in arguments:
                    contents = {"length": new_dic["length"]}
                else:
                    contents = read_html_file("chromosome_length.html").render(context={
                    "specie": specie,
                    "length": new_dic["length"]
                })
            except KeyError:
                if "json" in arguments:
                    contents = {"error": "The key is not in the ensembl data"}
                else:
                    contents = read_html_file('error.html').render()

        elif path == '/geneSeq':
            endpoint = '/sequence/id/'
            gene = arguments["gene"][0]
            if gene in gene_dic.keys():
                gene = gene_dic[gene]

            new_dic = ensembl_info(endpoint + gene)
            if "json" in arguments:
                contents = {"seq": new_dic["seq"]}
            else:
                contents = read_html_file("gene_seq.html").render(context={
                "id": new_dic["id"],
                "gene_seq": new_dic["seq"]
            })
        elif path == '/geneInfo':
            endpoint = '/sequence/id/'
            gene = arguments["gene"][0]
            if gene in gene_dic.keys():
                gene = gene_dic[gene]

            new_dic = ensembl_info(endpoint + gene)
            desc_dic = new_dic["desc"].split(":") #turns the items of the key desc into a list

            if "json" in arguments:
                contents = {"start": int(desc_dic[3]), "end": int(desc_dic[4]), "length": len(new_dic["seq"])}
            else:
                contents = read_html_file("gene_info.html").render(context={
                "start": desc_dic[3],
                "end": desc_dic[4],
                "length": len(new_dic["seq"]),
                "id": new_dic["id"],
                "chromosome": desc_dic[2] })

        elif path == '/geneCalc':
            endpoint = '/sequence/id/'
            gene = arguments["gene"][0]
            if gene in gene_dic.keys():
                gene = gene_dic[gene]

            new_dic = ensembl_info(endpoint + gene)
            s = Seq(new_dic["seq"])

            if "json" in arguments:
                contents = {"length": len(new_dic["seq"]), "percentages": Seq.percentages(s)}
            else:
                contents = read_html_file("gene_calc.html").render(context={
                "id": new_dic["id"],
                "percentages": Seq.percentages(s),
                "length": len(new_dic["seq"])
            })

        elif path == '/geneList':
            try:
                endpoint = '/phenotype/region/homo_sapiens/'
                chromo = arguments["chromo"][0].strip()
                start = arguments["start"][0].strip()
                end = arguments["end"][0].strip()
                new_dic = ensembl_info(endpoint + chromo + ":" + start + "-" + end)
                gene_list = []
                try:
                    for d in new_dic:
                        for dict in d["phenotype_associations"]:
                            if "attributes" in dict:
                                if "associated_gene" in dict["attributes"]:
                                    gene_list.append(dict["attributes"]["associated_gene"])
                    print("Gene list:", gene_list)

                    if "json" in arguments:
                        contents = {"gene": gene_list}
                    else:
                        contents = read_html_file("gene_list.html").render(context={
                        "chromo": chromo,
                        "start": start,
                        "end": end,
                        "gene_list": gene_list,
                    })
                except TypeError:
                   contents = read_html_file("error.html").render()
            except KeyError:
                contents = read_html_file("error.html").render()

        else:
            contents = read_html_file('error.html').render()

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:

        if "json" in arguments.keys():
            contents = json.dumps(contents)
            self.send_header("Content-Type", "application/json")
        else:
            self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents.encode()))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by user")
        httpd.server_close()