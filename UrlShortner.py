def custom_hash(data):
    hash_value = 0
    for char in data:
        hash_value = (hash_value * 31 + ord(char)) % 1000000
    return hash_value

def shorten_url(url):
    if url.startswith("https://"):
        index = url.find('/', 8)
        if index != -1:
            base_url = url[:index]
            remaining_path = url[index:]
            hash_value = custom_hash(remaining_path)
            short_url = base_url + '/' + str(hash_value)
            return short_url
        else:
            return url
    else:
        return "Invalid URL. Please use 'https://'."
