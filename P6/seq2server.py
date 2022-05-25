import http.server
import socketserver
import termcolor
from pathlib import Path
from seq1 import Seq
import jinja2 as j
from urllib.parse import parse_qs, urlparse

html_folder = "./html/"
list_sequences = ["AAACCTATCC", "GCCACGGT", "CAGGTTAA","CGACTACTTGC", "TGCATGCCGAT"]
list_genes = ["ADA", "FRAT1", "FXN", "RNU6_269P", "U5"]


def read_html_file(filename):
    contents = Path(html_folder + filename).read_text()
    contents = j.Template(contents)
    return contents


def count_bases(sequence):
    d = {"A": 0, "C": 0, "G": 0, "T": 0}
    for c in sequence:
        d[c] = d[c] + 1

    total = sum(d.values())
    for k,v in d.items():
        d[k] = [v, round((v * 100) / total, 2)]
    return d


def convert(count_bases):
    message = ""
    for k,v in count_bases.items():
        message += k + ": " + str(v[0]) + " (" + str(v[1]) + "%)" +"\n"
    return message


def info_operation(sequence):
    bases = count_bases(sequence)
    response = "<p> " + sequence + "</p>"
    response += "<p> Total length: " + str(len(sequence)) + "</p>"
    response += convert(bases)
    return response


def comp(sequence):
    s = Seq(sequence)
    response = Seq.complement(s)
    return response


def rev(sequence):
    s = Seq(sequence)
    response = Seq.reverse(s)
    return response


# Define the Server's port
PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
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
        arguments = parse_qs(url_path.query)
        print("The old path was", self.path)
        print("The new path is", url_path.path)
        print("arguments", arguments)
        # Message to send back to the client
        if self.path == "/":
            contents = read_html_file("index.html").render(context=
                        {"n_sequences": len(list_sequences),
                         "genes": list_genes})
        elif path == "/ping":
            contents = read_html_file(path[1:] + ".html").render()
        elif path == "/get":
            n_sequence = int(arguments["n_sequence"][0])
            sequence = list_sequences[n_sequence]
            contents = read_html_file(path[1:] + ".html")\
                .render(context = {
                "n_sequence": n_sequence,
                "sequence": sequence})
        elif path == "/gene":
            gene_name = arguments["gene_name"][0]
            sequence = Path("./sequences/" + gene_name ).read_text()
            sequence = sequence[sequence.find("\n"):].replace("\n", "")
            contents = read_html_file(path[1:] + ".html").render(context={
                "gene_name": gene_name,
                "sequence": sequence
            })
        elif path == "/operation":
            sequence = arguments["sequence"][0]
            operation = arguments["calculation"][0]
            if operation == "Rev":
                contents = read_html_file(path[1:] + ".html").render(context={
                    "sequence": sequence,
                    "operation": operation,
                    "result": rev(sequence)
                })
            elif operation == "Info":
                contents = read_html_file(path[1:] + ".html").render(context={
                    "sequence": sequence,
                    "operation": operation,
                    "result": info_operation(sequence)
                })
            elif operation == "Comp":
                contents = read_html_file(path[1:] + ".html").render(context={
                    "sequence": sequence,
                    "operation": operation,
                    "result": comp(sequence)
                })
        else:
            contents = "I am the happy server! :-)"

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
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