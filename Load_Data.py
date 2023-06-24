import requests, zipfile, io, os

url = "https://diffuseur.datatourisme.fr/webservice/2ec30f842b6e5041ba7fc1fba7ff8a1c/"
api_key = "1aaa09f5-35ca-4823-8671-9f4fe964ddab"


'''Télécharge un fichier zip de données et en extrait le contenu dans un dossier data'''
def load_data_from_API(url : str, api_key : str):
    response = requests.get(url+api_key)
    directory = "./data"
    try: 
        os.makedirs(directory)
    except OSError:
        if not os.path.isdir(directory):
            raise
    z = zipfile.ZipFile(io.BytesIO(response.content))
    z.extractall(directory)

load_data_from_API(url, api_key)