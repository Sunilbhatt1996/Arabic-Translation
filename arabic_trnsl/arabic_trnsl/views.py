from django.http import HttpResponse
from transformers import pipeline
import speech_recognition as sr
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


def index(request):


        return HttpResponse("Hello")

@csrf_exempt
def translation(request):
    # if request.method == 'POST':
        # print(request.body,"asfjhasfjhsjafh")
        # req_body=json.loads(request.body)
        # text=req_body.get('text')
        # to_lang=req_body.get('to_lang')
        # from_lang=req_body.get('from_lang')
        text = request.GET.get('q')
        from_lang = request.GET.get('langpair').split('|')[0]
        to_lang = request.GET.get('langpair').split('|')[1]
        # Initialize the translation pipeline


        if to_lang==from_lang:
             return JsonResponse({'translatedText': to_lang})
        if to_lang=="eng":
            translator = pipeline("translation", model="Helsinki-NLP/opus-mt-ar-en")
            translated_text = translator(text)
        elif to_lang=="ar":
            translator = pipeline("translation_en_to_ar", model="Helsinki-NLP/opus-mt-en-ar")
            translated_text = translator(text, max_length=40)
        # Translate text
        print(translated_text)
        return JsonResponse({'translatedText': translated_text[0]['translation_text']})
    
