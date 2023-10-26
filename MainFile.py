import random
import string
from flask import Flask, request, jsonify, render_template
import UrlShortner

app = Flask(__name__)

url_store = {}
metadata_store = {}
hits=0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten_url():
    long_url = request.json.get('long_url')
    if not long_url:
        return jsonify({'error': 'Missing long_url parameter'}), 400
    short_url = UrlShortner.shorten_url(long_url)
    url_store[short_url] = long_url
    metadata_store[short_url] = {'hits': hits+1}
    return jsonify({'short_url': short_url}), 201


@app.route('/search', methods=['GET'])
def search_urls():
    search_term = request.args.get('term')
    print(search_term)
    if not search_term:
        return jsonify({'error': 'Missing term parameter'}), 400
    results = []
    for short_url, metadata in metadata_store.items():
        long_url = url_store.get(short_url, '')
        print(long_url)
        if search_term in long_url:
            results.append({'short_url': short_url, 'long_url': long_url})

    return jsonify({'results': results})


@app.route('/metadata/<short_url>', methods=['GET'])
def get_metadata(short_url):
    if short_url not in metadata_store:
        return jsonify({'error': 'Short URL not found'}), 404
    metadata = metadata_store[short_url]
    return jsonify(metadata)

def generate_short_url():
    characters = string.ascii_letters + string.digits
    while True:
        short_url = ''.join(random.choice(characters) for _ in range(6))
        if short_url not in url_store:
            return short_url


if __name__ == '__main__':
    app.run(debug=True)
