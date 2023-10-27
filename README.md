**Problem**

Write an HTTP API for url shortener service(https://en.wikipedia.org/wiki/URL_shortening) with three components.

Main.py contains all the request handlers and once application is started http://127.0.0.1:5000/ will be redirected to index.html file present in templates folder.

**Task1**

Create API should take a long url and return a short url. API doesn't require authentication.
_@app.route('/shorten', methods=['POST'])__ - Takes input as longurl (mimetype as json )and returns short url.
Impleted the logic to convert long url to short url in UrlShortner.py class.
  -shorten_url method will generate a hashvalue using custom_hash function and replaces the hashvalue after the first "/"-slash present in the url.
  - Returns invalid url if the url doesn't contain https://
  Ex: Longurl - https://en.wikipedia.org/wiki/URL_shortening
      shorturl - https://en.wikipedia.org/23456 where 23456 is hashvalue.
- Once the shorturl is generated , global dict is maintained to store long vs short url details. which will further help in task2.
  
<img width="660" alt="image" src="https://github.com/siddavatam-vasuda-srusti-praharshitha/helloar/assets/70091238/603aa936-b69d-4066-9b94-349433c25bd7">

**Task2**

API should have an endpoint for search. Search will return results matching the title of the url. Say term "Python", api should return all pages which have partial or full match for the term with the title of the page and url.
_@app.route('/search', methods=['GET'])_ - Takes input as substirng of the url and returns the url.

<img width="655" alt="image" src="https://github.com/siddavatam-vasuda-srusti-praharshitha/helloar/assets/70091238/61205a00-158e-4832-9f11-8dbe374ea6aa">

**Task3**

Web interface for URL shortener
In the resources folder html file with Javascript code is written to take longurl as input and return shorturl.

<img width="408" alt="image" src="https://github.com/siddavatam-vasuda-srusti-praharshitha/helloar/assets/70091238/567e501b-de99-4c7a-9073-f19383c01006">



