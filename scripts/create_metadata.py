from brownie import Adavanced_collectible, network
from scripts.helpful_scripts import get_breed
from scripts.Create_collectible import create_collectible
from metadata.sample_metadata import metadata_template
from pathlib import Path
import requests
import os
import json

breed_to_image_uri = {
    "PUG": "https://ipfs.io/ipfs/QmSsYRx3LpDAb1GZQm7zZ1AuHZjfbPkD6J7s9r41xu1mf8?filename=pug.png",
    "SHIBA_INU": "https://ipfs.io/ipfs/QmYx6GsYAKnNzZ9A6NvEKV9nf1VaDzJrqDR23Y8YSkebLU?filename=shiba-inu.png",
    "ST_BERNARD": "https://ipfs.io/ipfs/QmUPjADFGEKmfohdTaNcWhp7VGk26h5jXDA7v3VtTnTLcW?filename=st-bernard.png",
}

 
def meta():                     
   # d=create_collectible()
    adavanced_collectible = Adavanced_collectible[-1]
    number_of_Adavanced_collectible = adavanced_collectible.tokenCounter()
    print(f"{number_of_Adavanced_collectible} da metadata abn gaya kake")
    for token_id in range(number_of_Adavanced_collectible):
        breed = get_breed(adavanced_collectible.tokenIdToBreed(token_id))
        metadata_file_name = (
            f"./metadata/{network.show_active()}/{token_id}-{breed}.json"
        )
        # print(metadata_file_name)
        collectiable_metadata = metadata_template
        if Path(metadata_file_name).exists():
            print(f"{metadata_file_name} alredy exists dlete it to override")
        else:
            print(f"Creating metadata file {metadata_file_name}")
            collectiable_metadata["name"] = breed
            collectiable_metadata["description"] = f"A khubsurat {breed} pilla"
            # print(collectiable_metadata)
            image_path = "./img/" + breed.lower().replace("_", "-") + ".png"
            
            image_uri = None
            if os.getenv("UPLOAD_IPFS") == "true":
                image_uri = upload_to_ipfs(image_path)
            image_uri = image_uri if image_uri else breed_to_image_uri[breed]
            
            collectiable_metadata["image"] = image_uri
            with open(metadata_file_name, "w") as file:
                json.dump(collectiable_metadata, file)
            if os.getenv("UPLOAD_IPFS") == "true":
                upload_to_ipfs(metadata_file_name)

            
            
            
def upload_to_ipfs(filepath):
    with Path(filepath).open("rb") as fp:
    #open file at filepath as binary(rb) as fp(its name)
        image_binary= fp.read()#now we are reading it 
        ipfs_url= "http://127.0.0.1:5001/"
        endpoint="api/v0/add"#making Post request to api of ipfs
        response= requests.post(ipfs_url+endpoint , files={"file":image_binary})
        #if we got to ipfs docs it return few things bytes,hash,name and size
        ipfs_hash = response.json()["Hash"]
        filename=filepath.split("/")[-1:][0]
        # converting "./img/0-PUG.png" -> "0-PUG.png" {by convertint the patf in to array by slicing it from(/) and fetcing the last one}
        image_uri = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={filename}"
        print(image_uri)
        return image_uri






def main():
    meta()
