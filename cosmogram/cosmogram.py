import os
import requests


PICS_DIRECTORY = "./images"


def create_images_dir():
    if not os.path.exists(PICS_DIRECTORY):
        os.makedirs(PICS_DIRECTORY)


def load_image_from_url(filename, url):
    create_images_dir()
    response = requests.get(url)

    with open(f"./{PICS_DIRECTORY}/{filename}", "wb") as img_file:
        img_file.write(response.content)


def fetch_spacex_last_launch():
    url = "https://api.spacexdata.com/v3/launches/latest"

    response = requests.get(url).json()

    img_links = response["links"]["flickr_images"]
    for index, img_link in enumerate(img_links):
        filename = f"spacex{index}.jpg"

        load_image_from_url(filename, img_link)


def main():
    fetch_spacex_last_launch()


if __name__ == '__main__':
    main()
