# Play with exchanges from BCCR and Python
I want to get all the exchange rates reported by the different financial entities to the Banco Central of Costa Rica

The first problem is that looks like the web page was created by a five years old kid that started to use Visual Studio, I am very sure that the kids will make anything to destroy the page again and this work will need a rework.

Because above, parse the web page to extract the HTML table is very hard, so I used Selenium to press the button and download the report.

Surprise! The kid not happy with wrong programming HTML, made a wrong spreadsheet file, despite the file have the xls extension in the reallity is the HTML table LOL.

So that is an advance, extract only one table with the exchange rates will save time. Here is when BeautifulSoup enter to the scene, so I cleaned the mess and try to get the correct table that we need to introduce Pandas, I created a dataset with the information. So, you can play with that.

Other thing that I made is create a correct CSV file to import on a spreadsheet software properly.

Take on consideration that you will notice that the exchange amount doesn't contains the floating point... is a bug... So little leech fix that and send me a PR...
