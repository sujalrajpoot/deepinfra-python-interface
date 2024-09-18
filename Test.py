from DeepInfra import DeepInfra

if __name__=="__main__":
    init = DeepInfra()
    # For Testing of TextGeneration
    print(init.TextGeneration().generate(message="Hello, How are you?", model="Meta-Llama-3.1-70B-Instruct"))

    print(init.TextGeneration().generate(message="Hello, How are you?", model="Meta-Llama-3.1-70B-Instruct", stream=True))

    # For Testing of TextToImage
    print(init.TextToImage().generate(prompt="Generate an image of a white elephant.", model="FLUX-1-dev", bearer_token="Bearer jwt:eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkaToxNzA2MDU2MzE2IiwiZXhwIjoxNzI5MTg2NjQ3fQ.GK7r69ADISIYVqbheLtBmUZDNk68RE9r8mOyEkGc-vM"))

    # For Testing of AutomaticSpeechRecognition
    print(init.AutomaticSpeechRecognition().generate(audio_file_path="./Test_Data/English.mp3", task="transcribe", model="Whisper-large-v3"))

    print(init.AutomaticSpeechRecognition().generate(audio_file_path="./Test_Data/Hindi.mp3", task="translate", model="Whisper-large-v3"))

    # For Testing of TextToSpeech
    print(init.TextToSpeech().generate(text="Text-to-Speech technology converts written text into spoken words using advanced speech synthesis by the DeepInfra API.",voice="Aura",output_filename="output_file.mp3"))

    # For Testing of ZeroShotImageClassification
    print(init.ZeroShotImageClassification().generate(image_path="./Test_Data/cat.jpg", model="Clip-vit-base-patch32", bearer_token="Bearer jwt:eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkaToxNzEyNjMwNjI4IiwiZXhwIjoxNzI4OTc1MzA2fQ.NL8HsBTRuOzNWUtNYY-63TYJsrrqEU1HuJeFVSu8ifc", candidate_labels=["cat", "dog"]))

    print(init.ZeroShotImageClassification().generate(image_path="./Test_Data/dog.jpg", model="Clip-vit-base-patch32", bearer_token="Bearer jwt:eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkaToxNzEyNjMwNjI4IiwiZXhwIjoxNzI4OTc1MzA2fQ.NL8HsBTRuOzNWUtNYY-63TYJsrrqEU1HuJeFVSu8ifc", candidate_labels=["cat", "dog"]))
