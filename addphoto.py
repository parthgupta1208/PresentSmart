import os
import glob
from pexels_api import Client

# setting dev key and cx
# gis = GoogleImagesSearch(os.getenv("GCS_DEVELOPER_KEY"), os.getenv("GCS_CX"))

# function to getcall and download
def get_images(query, n):
    client = Client(api_key=os.getenv("PEXELS_API_KEY"))
    _search_params = {
        'query': query,
        'per_page': n,
    }
    try:
        search_results = client.search(query=query, **_search_params)
        for photo in search_results.photos:
            photo.download(path='./images/')
        filenames = [f for f in os.listdir('./images/') if os.path.isfile(os.path.join('./images/', f))]
        return filenames
    except Exception as e:
        print(e)

# function to empty the images folder
def empty_images():
    folder_path = "./images/"
    file_list = glob.glob(os.path.join(folder_path, "*"))
    for file_path in file_list:
        try:
            os.remove(file_path)
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")
