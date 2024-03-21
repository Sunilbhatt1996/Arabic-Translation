Steps to run application.

1. Install Python 3.8 +.
2. Add python path to global environment
3. Open folder and run "python -m venv t_env" command
4. "t_env\Scripts\activate"
5. "cd arabic_trnsl"
6. "pip install -r requirement.txt
7. "python manage.py runserver"
8. Go back to main folder and Open ui.html

Note:
first time it require internet. after that it can run on offline mode. 
Run both translate Eng to Arabic and Arabic to Eng.



Steps for linux

1. Install Python 3.8+ 
2. Create Virual Env 
"sudo apt install -y python3-pip"
"sudo apt install build-essential libssl-dev libffi-dev python3-dev"
"sudo apt install -y python3-venv"
"python3 -m venv my_env"
"source my_env/bin/activate

3. "pip3 install torch torchvision torchaudio"
4. "pip install vosk SpeechRecognition setuptools django-rest-framework django-cors-headers transformers sentencepiece sacremoses"
5. "sudo apt-get install portaudio19-dev python-pyaudio"
6. "pip install pyaudio"
7. download models from https://alphacephei.com/vosk/models according to your requirement
8. Extract the downloaded file and extract it to speech_recogition folder.
9. Add condition for newly file in api in view file 
9. "cd arabic_trnsl"
10. "pip install -r requirement.txt
11. "python manage.py runserver"
12. Go back to main folder and Open ui.html






