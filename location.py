import requests
import json

def grt_location_by_ip():
    try:
        response = requests.get("https://ipapi.com/json")

        if response.status_code == 200:
            data = response.json()

            print(f"IP Address:{data.get('ip')}")
            print(f"City: {data.get('city')}")
            print(f"Region: {data.get('region')}" )
            print(f"Country: {data.get('country')}")
            print(f"Latitude: {data.get('latitude')}")
            print(f"Longitude: {data.get('longitude')}")

            return data
        else:
            print(f"Error: {response.status_code}")
            return None
        
    except Exception as e:
        print(f"Exception: {e}")
        return None
    
if __name__ == "__main__":
    grt_location_by_ip()
    

    
