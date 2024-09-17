
# DeepInfra Python Interface
This is a Python interface for interacting with the DeepInfra API. DeepInfra provides access to powerful machine learning models, which include large language models (LLMs), automatic speech recognition (ASR), text-to-speech (TTS), and zero-shot image classification models.
# Authors

- [@sujalrajpoot](https://github.com/sujalrajpoot)

# Features

This project provides a Python interface to interact with various models hosted by the DeepInfra API, enabling users to leverage state-of-the-art machine learning technologies. Here are the main features:

### Text Generation:
- Generate coherent and contextually relevant text based on user-provided prompts.
- Supports custom system prompts to guide the tone and purpose of responses.
- Adjustable parameters such as maximum token count and temperature for creative or focused outputs.
- Stream or chunk outputs for efficient processing of large text generations.

### Automatic Speech Recognition (ASR):
- Transcribe audio files into text using cutting-edge models like Whisper-large-v3.
- Supports both transcription and translation tasks from audio.
- Handles different file formats and audio quality variations.

### Text-to-Speech (TTS):
- Convert written text into human-like speech.
- Choose from multiple voices (e.g., "Aura") for customized audio outputs.
- Save generated speech files locally in formats like .mp3 for easy playback.
- Ideal for accessibility tools, virtual assistants, or voice-driven applications.

### Zero-Shot Image Classification:
- Classify images into categories that the model has not explicitly been trained on.
- Leverages models like Clip-vit-base-patch32 to perform image classification tasks with no prior training data.
- Highly flexible for classifying images in industries such as healthcare, manufacturing, and e-commerce.

### API Interaction:
- Simplifies the process of interacting with DeepInfra’s API.
- Offers customizable model parameters, allowing users to tailor results for different use cases.
- Supports bearer token authentication for secure access to DeepInfra's services.

### Model Listing:
- List available models for each task (text generation, speech recognition, text-to-speech, image classification).
- Helps users discover and choose the right model for their specific use case.

### Modular Structure:
- Organized into separate classes for each type of task (TextGeneration, ASR, TTS, and ZeroShotImageClassification), allowing for easy integration and extension.
- Clean, readable code that can be extended with additional tasks or model functionalities as DeepInfra expands its offerings.

### Cross-Task Integration:
- Use generated text from one task as input for another (e.g., generate text and convert it to speech).
- Seamlessly combine various AI tasks to build complex AI-driven applications.

# How It Can Help

- This feature set makes the project versatile and powerful, ideal for developers who need to integrate advanced machine learning capabilities such as text generation, speech recognition, and image classification into their applications.

# Requirements

- Make sure you have the following Python packages installed:

- re (part of Python’s standard library)
- json (part of Python’s standard library)
- base64 (part of Python’s standard library)
- random (part of Python’s standard library)
- Literal (part of Python’s standard library typing's part)
- requests

### You can install the required packages using pip:

- pip install requests
# Usage/Examples

```python
from DeepInfra import DeepInfra

if __name__=="__main__":
    init = DeepInfra()
    # For Testing of TextGeneration
    print(init.TextGeneration().generate(message="Hello, How are you?", model="Meta-Llama-3.1-70B-Instruct"))
    print(init.TextGeneration().generate(message="Hello, How are you?", model="Meta-Llama-3.1-70B-Instruct", stream=True))

    # For Testing of AutomaticSpeechRecognition
    print(init.AutomaticSpeechRecognition().generate(audio_file_path="./Test_Data/English.mp3", task="transcribe", model="Whisper-large-v3"))
    print(init.AutomaticSpeechRecognition().generate(audio_file_path="./Test_Data/Hindi.mp3", task="translate", model="Whisper-large-v3"))

    # For Testing of TextToSpeech
    print(init.TextToSpeech().generate(text="Text-to-Speech technology converts written text into spoken words using advanced speech synthesis by the DeepInfra API.",voice="Aura",output_filename="output_file.mp3"))

    # For Testing of ZeroShotImageClassification
    print(init.ZeroShotImageClassification().generate(image_path="./Test_Data/cat.jpg", model="Clip-vit-base-patch32", bearer_token="Bearer jwt:eyJxxxfc", candidate_labels=["cat", "dog"]))
    print(init.ZeroShotImageClassification().generate(image_path="./Test_Data/dog.jpg", model="Clip-vit-base-patch32", bearer_token="Bearer jwt:eyJxxxfc", candidate_labels=["cat", "dog"]))
```
## Running Tests

To run tests, run the following command

```python
python Test.py
```
## License

[MIT](https://choosealicense.com/licenses/mit/)


## Installation


```bash
Clone the repository:
git clone https://github.com/sujalrajpoot/deepinfra-python-interface.git

Install the required packages: 
pip install requests
```
    
## 🚀 About Me
I'm a skilled Python programmer and experienced web developer. With a strong background in programming and a passion for creating interactive and engaging web experiences, I specialize in crafting dynamic websites and applications. I'm dedicated to transforming ideas into functional and user-friendly digital solutions. Explore my portfolio to see my work in action.
# Hi, I'm Sujal Rajpoot! 👋


## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://sujalrajpoot.netlify.app/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sujal-rajpoot-469888305/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/sujalrajpoot70)


# Disclaimer
This project is for educational and personal use only. The script scrapes data from DeepInfra and other related sources without explicit permission from these websites. Usage of this script must comply with the terms and conditions and policies of DeepInfra and other websites being used.
