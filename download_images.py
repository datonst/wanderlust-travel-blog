import requests
import os
import shutil
from pathlib import Path
import sys


def download_image(url, save_path):
    """Download an image from URL and save it to the specified path"""
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        with open(save_path, "wb") as file:
            shutil.copyfileobj(response.raw, file)

        print(f"Downloaded: {save_path}")
        return True
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return False


def main():
    # Create directories if they don't exist
    image_dir = Path("static/images")
    image_dir.mkdir(parents=True, exist_ok=True)

    # First, ensure pexels-api-py is installed
    try:
        from pexelsapi.pexels import Pexels
    except ImportError:
        print("Installing pexels-api-py package...")
        try:
            import subprocess

            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", "pexels-api-py"]
            )
            from pexelsapi.pexels import Pexels
        except Exception as e:
            print(f"Error installing pexels-api-py: {e}")
            print("Please install manually with: pip install pexels-api-py")
            sys.exit(1)

    # You need to get a Pexels API key from https://www.pexels.com/api/
    # Sign up for a free account and get an API key
    PEXELS_API_KEY = os.environ.get("PEXELS_API_KEY")
    if not PEXELS_API_KEY:
        print("\n" + "=" * 80)
        print("ERROR: No Pexels API key found!")
        print("Please get a free API key from https://www.pexels.com/api/")
        print("Then set it as an environment variable:")
        print("  export PEXELS_API_KEY=your_api_key_here")
        print("Or update this script to include your API key directly:")
        print("  PEXELS_API_KEY = 'your_api_key_here'")
        print("=" * 80 + "\n")
        sys.exit(1)

    pexels = Pexels(PEXELS_API_KEY)

    # Define image queries and save paths
    images = [
        # Hero image
        {
            "query": "travel landscape",
            "path": image_dir / "hero-bg.jpg",
            "width": 1600,
            "height": 900,
        },
        # Destination images
        {
            "query": "bali beach",
            "path": image_dir / "destination-1.jpg",
            "width": 800,
            "height": 600,
        },
        {
            "query": "tokyo city",
            "path": image_dir / "destination-2.jpg",
            "width": 800,
            "height": 600,
        },
        {
            "query": "santorini greece",
            "path": image_dir / "destination-3.jpg",
            "width": 800,
            "height": 600,
        },
        {
            "query": "paris eiffel",
            "path": image_dir / "destination-4.jpg",
            "width": 800,
            "height": 600,
        },
        {
            "query": "machu picchu",
            "path": image_dir / "destination-5.jpg",
            "width": 800,
            "height": 600,
        },
        {
            "query": "kyoto japan",
            "path": image_dir / "destination-6.jpg",
            "width": 800,
            "height": 600,
        },
        # About page image
        {
            "query": "travel friends",
            "path": image_dir / "about-img.jpg",
            "width": 1000,
            "height": 600,
        },
        # Team images
        {
            "query": "woman portrait",
            "path": image_dir / "team-1.jpg",
            "width": 400,
            "height": 400,
        },
        {
            "query": "man portrait",
            "path": image_dir / "team-2.jpg",
            "width": 400,
            "height": 400,
        },
        {
            "query": "woman face",
            "path": image_dir / "team-3.jpg",
            "width": 400,
            "height": 400,
        },
        {
            "query": "man face",
            "path": image_dir / "team-4.jpg",
            "width": 400,
            "height": 400,
        },
        # Footer background
        {
            "query": "world map",
            "path": image_dir / "footer-bg.jpg",
            "width": 1600,
            "height": 900,
        },
    ]

    # Download all images
    success_count = 0
    for img in images:
        try:
            # Search for images
            search_result = pexels.search_photos(
                query=img["query"],
                per_page=1,  # We just need one image per query
                page=1,
            )

            # Get the first photo from the results
            photos = search_result.get("photos", [])
            if photos:
                photo = photos[0]
                # Get the appropriate size URL (medium or large based on dimensions)
                if img["width"] > 800 or img["height"] > 600:
                    download_url = photo.get("src", {}).get("large2x")
                else:
                    download_url = photo.get("src", {}).get("medium")

                if download_url and download_image(download_url, img["path"]):
                    success_count += 1
            else:
                print(f"No images found for query: {img['query']}")
        except Exception as e:
            print(f"Error processing query '{img['query']}': {e}")

    print(f"Downloaded {success_count} of {len(images)} images successfully.")


if __name__ == "__main__":
    main()
