import requests
import os
import time

# make the plugins folder if it doesn't exist yet
os.makedirs("plugins", exist_ok=True)


def save(url, filename):
    # grab the file from the url and write it to disk
    response = requests.get(url)
    with open(f"plugins/{filename}", "wb") as f:  # open the file in binary write mode
        f.write(response.content)  # dump the downloaded bytes into it
    print(f"Saved {filename}")


def get_modrinth_jar(slug):
    # ask modrinth for the latest version of this plugin
    response = requests.get(f"https://api.modrinth.com/v2/project/{slug}/version")
    versions = response.json()  # parse the json response into a list of versions
    latest = versions[0]  # first item is always the newest

    # find the .jar file in the list of files for that version
    for file in latest["files"]:
        if file["filename"].endswith(".jar"):
            return file["url"]
    return None  # no jar found, so give up


# get the url for the latest chunky, then save it
url = get_modrinth_jar("chunky")
if url:
    save(url, "Chunky.jar")   
    time.sleep(0.5)

# bubblevillagers
url = get_modrinth_jar("bubblevillagers")
if url:
    save(url, "BubbleVillagers.jar")
    time.sleep(0.5)

# spark (direct url, no api needed)
save("https://spark.lucko.me/download/spark.jar", "Spark.jar")
save("https://dev.bukkit.org/projects/worldedit/files/latest", "WorldEdit.jar")

# essentialsx
url = get_modrinth_jar("essentialsx")
if url:
    save(url, "EssentialsX.jar")
    time.sleep(0.5)

# farm limiter
url = get_modrinth_jar("farm-limiter-applexial")
if url:
    save(url, "FarmLimiter.jar")
    time.sleep(0.5)

url = get_modrinth_jar("grimac")
if url:
    save(url, "GrimAC.jar")
    time.sleep(0.5)

url = get_modrinth_jar("hibernate-fabric")
if url:
    save(url, "Hibernate-Fabric.jar")   
    time.sleep(0.5)
