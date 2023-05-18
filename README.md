# PresentSmart

PresentSmart is a Python-based tool that utilizes AI to create on-point and in-depth PowerPoint presentations by generating notes. It is designed for both teachers and students, making it a versatile tool for educational purposes. The tool leverages the powerful GPT-3.5 Turbo engine for text generation, the Google Cloud Storage (GCS) for attaching related images, and the pptx library to generate PowerPoint files and add slides. Additionally, PresentSmart provides a user-friendly graphical user interface (GUI) implemented using the Tkinter library.

## Demo Video



https://github.com/parthgupta1208/PresentSmart/assets/114602309/dc8a0ded-af9f-4ce3-a284-746798a917b2



## Features

- Automatically generates notes-based PowerPoint presentations using AI technology.
- Makes use of the advanced GPT-3.5 Turbo engine for accurate and relevant text generation.
- Integrates with Google Cloud Storage (GCS) to attach related images to the presentations.
- Utilizes the `pptx` library to create and manipulate PowerPoint files, adding slides dynamically.
- Offers a user-friendly GUI powered by the Tkinter library, allowing for an intuitive user experience.

## Installation

1. Clone the PresentSmart repository to your local machine.
- ```git clone https://github.com/parthgupta1208/PresentSmart.git```


2. Install the required dependencies using pip.
    - ```pip install pptx```
    - ```pip install openai```
    - ```pip install tkinter```
    - ```pip install google_images_search```

3. Setup a `.env` file as below:
    - OPENAI_KEY="user-value"
    - OLDKEY="user-value"
    - GCS_DEVELOPER_KEY=user-value
    - GCS_CX=user-value

## Usage

1. Launch the application by running the `gui.py` script.
- ```python gui.py```

2. Use the graphical user interface to input your topics (comma-seperated).

3. Press `Enter` to initiate the presentation generation process.

4. Wait for PresentSmart to generate the PowerPoint presentation. This may take a few moments depending on the complexity of the topic.

5. Once the presentation is generated, you will be prompted to save the PowerPoint file. Choose a suitable location on your machine and click "Save".

6. PresentSmart will also open the saved PowerPoint file.

## Contributing

Contributions are welcome! If you'd like to contribute to PresentSmart, please follow these steps:

1. Fork the repository on GitHub.

2. Create a new branch.

3. Make your changes and additions.

4. Commit and push your changes to your forked repository.

5. Submit a pull request detailing the changes you made.

## License

[MIT License](LICENSE)


