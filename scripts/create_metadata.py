from brownie import Adavanced_collectible, network
from scripts.helpful_scripts import get_breed
from metadata.sample_metadata import metadata_template
from pathlib import Path

 
def meta():                     

    adavanced_collectible = Adavanced_collectible[-1]
    number_of_Adavanced_collectible = adavanced_collectible.tokenCounter()
    print(f"{number_of_Adavanced_collectible} da metadata abn gaya kake")
    for token_id in range(number_of_Adavanced_collectible):
        breed = get_breed(adavanced_collectible.tokenIdToBreed(token_id))
        metadata_file_name = (
            f"./metadata/{network.show_active()}/{token_id}-{breed}.json"
        )
        collectiable_metadata = metadata_template
        if Path(metadata_file_name).exists():
            print(f"{metadata_file_name} alredy exists dlete it to override")
        else:
            print(f"Creating metadata filr {metadata_file_name}")
            collectiable_metadata["name"] = breed
            collectiable_metadata["description"] = f"A khubsurat {breed} pilla"
            image_path = "./img/" + breed.lower().replace("_", "-") + ".png"
            
            
def upload_to_ipfs(filepath):
    with Path(filepath).open("rb") as fp:
    #open file at filepath as binary(rb) as fp(its name)
        image_binary= fp.read()#now we are reading it 
    pass




def main():
    meta()
