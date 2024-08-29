# SaaSCalc: A Dockerized SaaS Pricing Calculator

SaaSCalc is a simple web application that calculates the price of a SaaS product based on different tiers and features. It's built using Python Flask and containerized with Docker, making it easy to deploy and run on any system with Docker installed.

## Features

- Calculate SaaS pricing based on tier, number of users, and storage requirements
- Simple and responsive design
- Easy to deploy using Docker

## Prerequisites

- Docker
- Docker Compose (optional, but recommended)

## Getting Started

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/saascalc.git
   cd saascalc
   ```

2. Build and run the Docker container:

   Using Docker Compose (recommended):
   ```
   docker-compose up --build
   ```

   Or using Docker directly:
   ```
   docker build -t saascalc .
   docker run -p 5000:5000 saascalc
   ```

3. Open your web browser and navigate to `http://localhost:5000` to see the application in action.

## Project Structure

- `app.py`: The main Flask application
- `templates/index.html`: The HTML template for the web page (includes CSS and JavaScript)
- `Dockerfile`: Instructions for building the Docker image
- `docker-compose.yml`: Configuration for Docker Compose
- `README.md`: This file, containing project information and instructions

## Customization

To modify pricing tiers or calculation logic, edit the `tiers` dictionary and the `calculate` function in `app.py`. You can also adjust the frontend by modifying the `index.html` file.

## Contributing

Feel free to fork this project and submit pull requests with improvements or additional features.

## License

This project is open source and available under the [MIT License](LICENSE).
