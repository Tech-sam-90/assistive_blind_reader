# Blind Reader

Blind Reader is a hardware-software solution designed to assist visually impaired individuals by reading printed text aloud. It captures text using a camera, processes it with Microsoft Azure AI services, and converts it to speech using Text-to-Speech (TTS).

Features

Capture text using a camera connected to a Raspberry Pi.

Optical Character Recognition (OCR) with Azure Cognitive Services.

Text-to-Speech conversion for audible reading.

High accuracy text recognition (~98%).

Tech Stack

Hardware: Raspberry Pi, Camera Module

Software: Python

AI Services: Microsoft Azure Cognitive Services (OCR & TTS)

Installation

Clone the repository:

git clone https://github.com/YourUsername/blind_reader.git
cd blind_reader


Install dependencies:

pip install -r requirements.txt


Set up Azure credentials:

Create a Cognitive Services resource in Azure.

Store your API key and endpoint URL in a .env file or environment variables.

Run the application:

python main.py

Usage

Point the camera at text.

The system captures the image and extracts the text.

The text is read aloud through speakers or headphones.

Contributing

Contributions are welcome! Please fork the repo, make your changes, and submit a pull request.
