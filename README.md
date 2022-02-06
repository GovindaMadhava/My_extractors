# My_extractors

1) wiki_extractor :

-> Requirements :
  - import json module (which will be used in the latter half of the script to write the output generated, into the designated .json file)
  - import the wikipedia module (we make use of functions within this module to access search results and summary)
  
-> Method of Execution :
  - Try running the "wiki_extractor.ipynb" file for the best results, as running the .py file may require additional modules to be installed before execution.
  - The notebook accepts the user input arguments during the course of its execution. Finally, it creates the corresponding output file with a .json extension in the same folder       as the notebook. This file can be opened to view the required results !!!
  
-> Logic :

a) ln[2] : Take the first input argument from the user ie., keyword and store it in the variable keyword
b) ln[3] : Next, we take the second input argument from user ie., the number of related urls to process, and store it in variable num
c) ln[4] : Variable x stores upto 'num' search results related to the 'keyword' as entered by the user
d) ln[5] : We initialize an empty list 'list' which will be later used to store all the dictionaries. 
           We then use a for loop to iterate through the "num" number of words stored in var x (which are related to the given keyword)
           Next, we define the structure of each dictionary as mentioned in the problem statement
           The "url" contains url of each search related to the given keyword. We use wikipedia.page(i).url to obtain the url of corresponding ith page.
           The "paragraph" contains the summary of the corresponding ith wikipedia page. We use  wikipedia.summary(i,sentences = 2) to obtain the summary and limit the summary to            2 sentences each.
           We append each dictionary to the list
e) ln[6] : We use a loop to iterate through the list[] to check its contents and make sure it works as intended.
f) ln[7] : We the the third and last argument from the user and store it in variable 'op'. This stores the name entered by the user, which must be used to name the output json                file
g) ln[8] : We first create a json object named "json_object"
           Then, we create a .json file with the the name given by the user (third argument). This file is used to store the output of the above code, ie., we store the list of              dictionaries "list[]" in this file.
           
Once the last line is executed, we find a file named as the third argument "op" with a .json extension created in the same folder as the jupyter notebook. This folder contains the output of the code.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

2) pdf_extractor : 
