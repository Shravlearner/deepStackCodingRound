# importing libraries
import requests
import re
import os
from urllib.parse import urljoin


def extractImage(url):
    try:
        # Sending a GET HTTPS request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200 indicates that the requested content is available for use)
        if response.status_code == 200:
            # Extract image URLs using regex
            imageUrls = re.findall(r'<img[^>]+src="([^">]+)"', response.text)

            # Return the list of image URLs found
            return imageUrls
        else:
            print(f"There was a problem retrieving this page: {response.status_code}")
            return []

    except requests.exceptions.RequestException as e:
        print(f"Error fetching page: {e}")
        return []


def downloadingExtractedImages(imageUrls, outputDir):
    try:
        # Creating the output directory using os module
        os.makedirs(outputDir, exist_ok=True)

        # Downloading each image
        for imgUrl in imageUrls:
            # Ensuring that both absolute as well relative links would work
            imgUrl = urljoin(url, imgUrl)

            # Getting the image filename
            imgFilename = os.path.join(outputDir, os.path.basename(imgUrl))

            # Sending a GET request for the image
            imgResponse = requests.get(imgUrl)

            # Saving the image to the specified directory
            with open(imgFilename, 'wb') as imgFile:
                imgFile.write(imgResponse.content)
                print(f"Downloaded: {imgFilename}")

    except Exception as e:
        print(f"Error downloading images: {e}")


if __name__ == "__main__":
    # Example
    url = "https://en.wikipedia.org/wiki/Main_Page"
    outputDirectory = r"C:\Users\USER\OneDrive\Pictures"  # to be changed based on the system

    # Extract image URLs from the webpage
    imageUrls = extractImage(url)

    if imageUrls:
        # Download images to the specified directory
        downloadingExtractedImages(imageUrls, outputDirectory)
    else:
        print("No images found on the webpage.")
