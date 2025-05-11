# Wanderlust Travel Blog

A beautiful responsive travel blog website built with Flask and Bootstrap, containerized with Docker.

## Features

- Responsive design for all devices
- Beautiful modern UI with animations
- Multiple page templates (Home, Destinations, About)
- Ready to be deployed in a Docker container

## Project Structure

```
├── main.py             # Flask application
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker configuration
├── download_images.py  # Script to download placeholder images
├── static/
│   ├── css/            # Custom CSS
│   ├── js/             # JavaScript files
│   └── images/         # Image assets
└── templates/          # HTML templates
    ├── base.html       # Base template with common elements
    ├── index.html      # Home page
    ├── destinations.html # Destinations page
    └── about.html      # About page
```

## Prerequisites

- Python 3.6 or higher
- Docker

## Getting Started

### Running locally

1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Download placeholder images:
   ```
   python download_images.py
   ```
4. Run the Flask application:
   ```
   python main.py
   ```
5. Open your browser and navigate to `http://localhost:5000`

### Building and running with Docker

1. Build the Docker image:
   ```
   docker build -t wanderlust-travel-blog .
   ```
2. Run the Docker container:
   ```
   docker run -p 5000:5000 wanderlust-travel-blog
   ```
3. Open your browser and navigate to `http://localhost:5000`

## Deployment

To deploy to production:

1. Build the Docker image:
   ```
   docker build -t wanderlust-travel-blog:production .
   ```
2. Push to your container registry:
   ```
   docker tag wanderlust-travel-blog:production your-registry/wanderlust-travel-blog:latest
   docker push your-registry/wanderlust-travel-blog:latest
   ```
3. Deploy to your cloud provider using the container image

## Customization

- Modify templates in the `templates/` directory to change page structure
- Update styles in `static/css/style.css` to customize the appearance
- Replace placeholder images in `static/images/` with your own images

## License

This project is open source and available under the [MIT License](LICENSE). 