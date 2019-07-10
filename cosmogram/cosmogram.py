import os
import requests


PICS_DIRECTORY = "../images"


def check_images_dir():
    if not os.path.exists(PICS_DIRECTORY):
        os.makedirs(PICS_DIRECTORY)


def get_img_file_extension(url):
    return url.split(".")[-1]


def download_img_from_url(filename, url):
    check_images_dir()
    response = requests.get(url, verify=False)

    with open(f"./{PICS_DIRECTORY}/{filename}", "wb") as img_file:
        img_file.write(response.content)


def fetch_spacex_last_launch():
    url = "https://api.spacexdata.com/v3/launches/latest"

    response = requests.get(url).json()

    img_links = response["links"]["flickr_images"]
    for index, img_link in enumerate(img_links):
        filename = f"spacex{index}.jpg"

        download_img_from_url(filename, img_link)


def fetch_hubble_img(img_id):
    url = f"http://hubblesite.org/api/v3/image/{img_id}"
    response = requests.get(url).json()

    img_data = response["image_files"][-1]["file_url"]
    img_url = f"http:{img_data}"

    filename = f"hubble#{img_id}.{get_img_file_extension(img_url)}"

    download_img_from_url(filename, img_url)


def main():
    fetch_spacex_last_launch()


if __name__ == '__main__':
    main()
