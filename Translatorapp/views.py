from django.shortcuts import render

# Create your views here.
def result(request):
    if request.method == "POST":
        text = request.POST['source']
        lang = request.POST['lang']
        from googletrans import Translator
        translator = Translator()

        translated = translator.translate(text, dest=lang)
        print(translated.text)
    return render(request, 'result.html', {'trns' : translated.text})

def translate(request):
    return render(request, 'Translate.html')