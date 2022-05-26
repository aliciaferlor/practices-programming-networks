import http.client
import termcolor
import json

PORT = 8080
IP = 'localhost'
SERVER = 'rest.ensembl.org'

print(f"\nConnecting to server: {IP}:{PORT}\n")


def ensembl_info(endpoint, params):
    connection = http.client.HTTPConnection(IP, PORT)
    connection.request("GET", endpoint + params)
    response = connection.getresponse()
    data = response.read().decode("utf-8")
    data_dic = json.loads(data)
    return data_dic


def get_menu():

    termcolor.cprint("OPTIONS OF GENOME BROWSER:", 'blue')
    termcolor.cprint("Basic level:", 'magenta')
    print("""
         1. List of species
         2. Karyotype of a specie
         3. Length of the chromosome of a specie""")
    termcolor.cprint("Medium level:", 'magenta')
    print("""
         4. Sequence of a gene
         5. The information of a gene
         6. Calculations gene
         7. List of genes of a chromosome
         ---
         8. Finish program""")

def get_option():
    exit = False
    while not exit:
        option = input("Choose an option: ")
        if option.isdigit():
            option = int(option)
            exit = True
        else:
            print("The selected option needs to be an integer number: ", end = "")
    return option

exit = False

GENES = ["SCRAP", "FRAT1", "ADA", "FXN", "RNU6_269P", "MIR633", "TTTY4C", "RBMY2YP", "FGFR3",  "KDR", "ANK2"]

while not exit:
    get_menu()
    option = get_option()

    if option == 1:
        try:
            termcolor.cprint("BASIC: ", 'magenta')

            limit = input("How many species are you looking for?: ")
            species = ensembl_info("/list_species?", "limit=" + str(limit) + "&json=1")

            termcolor.cprint("The total amount of species in the database is: ", 'red', end="")
            print(species["number_species"])
            termcolor.cprint("The limit chosen is: ", 'red', end="")
            print(species["limit"])
            termcolor.cprint("The list of species is: ", 'red')
            for i in species["list_species"]:
                print(" --> ", i)
        except TypeError:
            termcolor.cprint("That option is not in the ensembl database", 'yellow')


    elif option == 2:
        termcolor.cprint("BASIC: ", 'magenta')
        specie = input("Choose a specie: ")
        try:
            karyotype = ensembl_info("/karyotype?", "specie=" + str(specie) + "&json=1")
            termcolor.cprint("The karyotype is: ", 'red')
            for n in karyotype["karyotype"]:
                print(n)
        except TypeError:
            termcolor.cprint("That option is not in the ensembl database", 'yellow')

    elif option == 3:
        termcolor.cprint("BASIC: ", 'magenta')
        specie = input("Choose a specie: ")
        chromo = input("Choose a chromosome: ")
        try:
            length = ensembl_info("/chromosomeLength?", "specie=" + str(specie) + "+&chromosome=" + str(chromo) + "&json=1")
            termcolor.cprint("The length of the chromosome is: ", 'red', end="" )
            print(length["length"])
        except TypeError:
            termcolor.cprint("That option is not in the ensembl database",
                             'yellow')

    elif option == 4:
        termcolor.cprint("MEDIUM: ", 'magenta')

        termcolor.cprint("""The genes you can choose from are: 
        FRAT1,  ADA,  FXN,  RNU6_269P,  MIR633, TTTY4C,  RBMY2YP,  FGFR3,  KDR,  ANK2""", 'yellow')
        gene = input("Choose a gene: ")
        try:
            if gene in GENES:

                seq = ensembl_info("/geneSeq?", "seq=" + str(gene) + "&json=1")
                termcolor.cprint("The sequence of the gene is:", 'red')
                print(seq)
            else:
                termcolor.cprint("The gene is not in the list", 'yellow')
        except TypeError:
            termcolor.cprint("That option is not in the ensembl database",
                             'yellow')

    elif option == 5:
        termcolor.cprint("MEDIUM: ", 'magenta')
        termcolor.cprint("""The genes you can choose from are: 
                FRAT1,  ADA,  FXN,  RNU6_269P,  MIR633, TTTY4C,  RBMY2YP,  FGFR3,  KDR,  ANK2""", 'magenta')
        try:
            gene = input("Choose a gene: ")
            if gene in GENES:
                info = ensembl_info("/geneInfo?", "info=" + str(gene) + "&json=1")
                termcolor.cprint("The chosen gene is: ", 'red', end="")
                print(gene)
                termcolor.cprint("The gene starts at: ", 'red', end="")
                print(info["start"])
                termcolor.cprint("The gene ends at: ", 'red', end="")
                print(info["end"])
                termcolor.cprint("The length of the gene is: ", 'red', end="")
                print(info["length"])
            else:
                termcolor.cprint("That gene is not in the list", 'yellow')
        except TypeError:
            termcolor.cprint("That option is not in the ensembl database",
                             'yellow')

    elif option == 6:
        termcolor.cprint("MEDIUM: ", 'magenta')
        termcolor.cprint("""The genes you can choose from are: 
                        FRAT1,  ADA,  FXN,  RNU6_269P,  MIR633, TTTY4C,  RBMY2YP,  FGFR3,  KDR,  ANK2""", 'magenta')
        gene = input("Choose a gene: ")
        try:
            if gene in GENES:
                calc = ensembl_info("/geneCalc?", "calc=" + str(gene) + "&json=1")
                percentages = calc["percentages"].split("%")
                percentages.remove(percentages[-1])
                termcolor.cprint("The percentages of the bases are: ", 'red')
                for i in percentages:
                    i.split(":")
                    print(i+"%")
                termcolor.cprint("The length of the gene is: ", 'red', end="")
                print(calc["length"])

            else:
                termcolor.cprint("That gene is not in the list", 'yellow')
        except TypeError:
            termcolor.cprint("That option is not in the ensembl database",
                             'yellow')

    elif option == 7:
        termcolor.cprint("MEDIUM: ", 'magenta')
        specie = input("Choose a specie: ")
        chromo = input("Choose a chromosome: ")
        start = input("Choose a startpoint: ")
        end = input("Choose an endpoint: ")
        try:
            gene_list = ensembl_info("/geneList?", "specie=" + str(specie) + "+&name_chromo=" + str(chromo) + "&start=" +
                                        str(start) + "&end=" + str(end) + "&json=1")
            termcolor.cprint("The list of the genes is: ", 'red')
            for i in gene_list["gene"]:
                print(" - ", i)
        except TypeError:
            termcolor.cprint("That option is not in the ensembl database",
                             'yellow')

    elif option == 8:
        termcolor.cprint("This is the end of the program!!!", 'red')

        exit = True










