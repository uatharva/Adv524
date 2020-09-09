from url_parser import parser_requester

if __name__ == '__main__':
    f = open('companies.txt', 'r')
    fw = open("urls.txt", "w")
    for company_name in f:
        fw.write(parser_requester(company_name.strip()) + '\n')