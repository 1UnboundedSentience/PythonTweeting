#Instructions
Clone the repository, and run the request.py on your terminal. If you want to find a random tweet for "elon musk", in the terminal run 'request.py elon musk', or for tweets from Kobe Bryant's official twitter type "request.py @kobebryant".  You will receive information about the query results and the detailed information of your random tweet in pretty print Python Dictionary.

#How it Works

I used Twitter's [Search API](https://dev.twitter.com/rest/public/search) to search for tweets on twitter's homepage.  The random tweet is chosen from the first 15 results.  I accessed tweets with the [Python OAuth library](https://github.com/joestump/python-oauth2).  The JSON data received from the request was changed into a Python dictionary, which is then printed to the user.

# Expanding on Twitter Queries

Overall, I liked Twitter's extensive API documentation, but maybe in the future they should have explain CORS and other common API request issues in addition to telling how everything works.  If I were to expand on this as a project, I would let the client submit a request through an HTML form, which would require resovles Cross-Origin Request issues. You can see from the html file provided how such a request might work.  I would integrate this a more complete Python framework such as Django.