from urllib.request import urlopen

# url = 'https://pokeapi.co/api/v2/pokemon/ditto'
url = 'http://worldtimeapi.org/api/timezone/etc/UTC.txt'
with urlopen(url) as response:
    for line in response:
        print(line)