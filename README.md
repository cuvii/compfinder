# Compfinder
Compfinder is a web crawler, database and search combination written for an Information Retrieval NYIT course in Fall 2017.
The following files are necessary for the program:
*compfinder.db

*gather.py

*searching.py

The program makes use of Beautiful Soup 4.

The compfinder database runs in SQlite. It contains links and various data from the arxiv.org website for the Computing Researching Repository.
Gather.py works with a connected database in SQlite, in this case, compfinder, in order to crawl the Arxiv CORR site! It currently will only add to the database, and not delete or remove duplicates.

Searching.py contains a main method. By running it in command prompt, you will be able
to search the compfinder database for various computer science related topics. Staying in the 
searching loop requires a "yes" answer.

*Report Explanation of searching file:

*The file takes an input from the user, and splits a search term on the spaces. For example, “neural network” turns into (“neural,”network”). The search loop goes through each row from the database in the tuple and when searching, loops through the row for the length of the search list.  The number of occurrences for each term is counted into a total number that is stored, along with the link title and link, in a list of “linko” objects. The search result will go into the list only if the number of occurrences is greater than 1. This list holds the results of the search. 

*Once all the tuples have been looped through, the loop closes. The list of links is then sorted in order of number of occurrences, with the highest number at the top of the list. For this, I used the sorted method. The results are then printed.  This also cut off at 10 results, as to not flood the user with irrelevant information.

Please ask if you have any questions or changes!
Enjoy!
