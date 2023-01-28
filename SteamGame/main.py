from urllib.request import urlopen
import certifi
import json

def game_start():
    
    return



def main():
    
    url = "https://steamspy.com/api.php?request=top100in2weeks"
    
    response = urlopen(url, cafile=certifi.where())
    
    json_data = json.loads(response.read())
    print(json_data)
    
    game_start(json_data)
    
    return


if __name__ == '__main__':
    main()
    