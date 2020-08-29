import http.server
import socketserver
from urllib.parse import urlparse
from urllib.parse import parse_qs
import glob

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Sending an '200 OK' response
        self.send_response(200)

        # Setting the header
        self.send_header("Content-type", "text/html")

        # Whenever using 'send_header', you also have to call 'end_headers'
        self.end_headers()

        # Extract query param
        searchTerm = 'null'
        query_components = parse_qs(urlparse(self.path).query)
        if 'q' in query_components:
            searchTerm = query_components["q"][0]


        # WEBPAGE
        html = rf("static/index.html")
        html += "<body>"

        # get and display links
        links = getLinks("https://www.google.com/search?q=" + searchTerm)
        for i in range(len(links)):

            # test that it is a link that we want
            if "/url?q=" in links[i]:
                # remove substring and append to page
                linkToAppend = links[i].replace('/url?q=','')
                html += f"""<a class='websiteLink' href='{linkToAppend}'>{linkToAppend}</a><br>"""
            
            # scanning sequence
            continue

        # html imports
        html += ("</body></html><style>"+rf("./static/css/style.css")+"</style>"+
            "<script>"+rf("./static/js/func.js")+"</script>"+
            "<script>"+rf("./static/js/script.js")+"</script>")



        # Writing the HTML contents with UTF-8
        self.wfile.write(bytes(html, "utf8"))
        return

def rf(filename):
    return open(filename, "r").read()

# EXTERNAL IMPORTS
exec(rf("parse.py"))

# arg 1 is server port
def startServer(PORT):
    # Create an object of the above class
    handler_object = MyHttpRequestHandler

    my_server = socketserver.TCPServer(("", PORT), handler_object)

    # Star the server
    print("Started File Server on :", PORT)
    my_server.serve_forever()