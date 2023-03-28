# this imports the SimpleServer library
import SimpleServer
# This imports the functions you defined in searchengine.py
from searchengine import create_index, search, textfiles_in_dir
# has the json.dumps function. So useful
import json

"""
File: extension_server.py
---------------------
This starts a server! Go to http://localhost:8000 to enjoy it. Currently
the server only serves up the HTML. It does not search. Implement code in
the TODO parts of this file to make it work.
"""

# the directory of files to search over
DIRECTORY = 'bbcnews'
# perhaps you want to limit to only 10 responses per search..
MAX_RESPONSES_PER_REQUEST = 10

class SearchServer:
    def __init__(self):
        """
        load the data that we need to run the search engine. This happens
        once when the server is first created.
        """
        self.html = open('extension_client.html').read()

    # this is the server request callback function. You can't change its name or params!!!
    def handle_request(self, request):
        """
        This function gets called every time someone makes a request to our
        server. To handle a search, look for the query parameter with key "query"
        """
        # it is helpful to print out each request you receive!
        print(request)

        # if the command is empty, return the html for the search page
        if request.command == '':
            return self.html

        # if the command is search, the client wants you to perform a search!
        if request.command == 'search':
            query = request.params['query']

            # a dictionary mapping from terms to file names (i.e., inverted index)
            # (term -> list of file names that contain that term)
            index = {}

            # a dictionary mapping from a file names to the title of the article
            # in a given file (file name -> title of article in that file)
            file_titles = {}

            # a list of file names (strings)
            filenames = textfiles_in_dir(DIRECTORY)

            create_index(filenames, index, file_titles)
            result_files = search(index, query)

            response = []
            counter = 0 # to limit number of results presented
            
            for filename in result_files:
                if counter == MAX_RESPONSES_PER_REQUEST:
                    break

                response.append(
                    {
                        'title': file_titles[filename]
                    }
                )

                counter += 1

            return json.dumps(response, indent=2)

def main():
    # make an instance of your Server
    handler = SearchServer()
    # start the server to handle internet requests!
    SimpleServer.run_server(handler, 8000) # make the server

if __name__ == '__main__':
    main()