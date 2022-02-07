# My_extractors

1) wiki_extractor :-

-> Requirements :
  - import json module (which will be used in the latter half of the script to write the output generated, into the designated .json file)
  - import the wikipedia module (we make use of functions within this module to access search results and summary)
  
-> Method of Execution :
  - Try running the "wiki_extractor.ipynb" file for the best results, as running the .py file may require additional modules to be installed before execution.
  - The notebook accepts the user input arguments during the course of its execution. Finally, it creates the corresponding output file with a .json extension in the same folder       as the notebook. This file can be opened to view the required results !!!
  
-> Logic :

- ln[2] : Take the first input argument from the user ie., keyword and store it in the variable keyword
- ln[3] : Next, we take the second input argument from user ie., the number of related urls to process, and store it in variable num
- ln[4] : Variable x stores upto 'num' search results related to the 'keyword' as entered by the user
- ln[5] : - We initialize an empty list 'list' which will be later used to store all the dictionaries. 
- We then use a for loop to iterate through the "num" number of words stored in var x (which are related to the given keyword)
- Next, we define the structure of each dictionary as mentioned in the problem statement
- The "url" contains url of each search related to the given keyword. We use wikipedia.page(i).url to obtain the url of corresponding ith page.
- The "paragraph" contains the summary of the corresponding ith wikipedia page. We use  wikipedia.summary(i,sentences = 2) to obtain the summary and limit the summary             to 2 sentences each.
- We append each dictionary to the list

- ln[6] : We use a loop to iterate through the list[] to check its contents and make sure it works as intended.
- ln[7] : We the the third and last argument from the user and store it in variable 'op'. This stores the name entered by the user, which must be used to name the output json             file
- ln[8] : We first create a json object named "json_object"
          Then, we create a .json file with the the name given by the user (third argument). This file is used to store the output of the above code, ie., we store the list of             dictionaries "list[]" in this file.
           
Once the last line is executed, we find a file named as the third argument "op" with a .json extension created in the same folder as the jupyter notebook. This folder contains the output of the code.
Refer "output_screenshot.jpg"  to know how the output file appears.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

2) pdf_extractor :-

-> Requirements : import the following modules
    import PyPDF2
    import urllib.request
    from urllib.request import urlopen
    from urllib.request import urlretrieve
    import json 
    import csv
    import requests
    from urllib.parse import urlparse, urljoin
    from bs4 import BeautifulSoup

-> Method of Execution : Execute the "pdf_extractor.ipynb" file.

-> Logic : Once all the required modules are impported, we proceed to the logic of the code to solve the given task.

- We first convert the given google sheet document into a csv file "Data Engineer Task - Data Engineer Task.csv". We will be working on this file from this point onwards due to its compatibility with jupyter notebook.
- Defining a function "download_file" which take a url as an argument and downloads the pdf file into the same folder as the jupyter notebook. We will use this funciton later to download the pdfs into the folder to read them.
- Defining the structure of the dictionary as expected in the output
  
- For the 2 types of URLS present in the google sheet, we deinfe a function("is_pdf") to differentiate between the 2 types.
  Type-A : We download the pdfs, read them using csv.reader() function and append it to the dictionary. These links will have the same page-url and pdf-url. We then append the     list with each dictionary.
   
  Type-B : defining a function "is_pdf" to iterate over all the links in csv file and determine if they are of Type-A or Type-B.
  If they are Type-B links, then we use the function "get_all_links" to all .pdf link from within the page. We use function "findAll" to scrape off the html content and obtain     just the links from each page. 
  From this point, we can treat these links as Type-A links.
   
- Now we iterate over all the rows present in the "data.csv" file and access row[0](this is the url present in each line). We run the above logic on each link which will be       either of type-A or type-B. 
- We use ".lxmi" parsing technique to parse text from pdf files.
- In order to convert the marathi characters to english, we may use an encoding function.

- Next, we append the corresponding dictionary as and when each row is encountered. All the dictionaries are then appended to list[] which contains all the dictionaries.
- Lastly, we create a json object named "json_object". Then, we create a "output.json" file. This file is used to store the output of the above code, ie., we store the list of     dictionaries "list[]" in this file.
