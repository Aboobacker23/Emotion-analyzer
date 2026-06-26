from django.shortcuts import render

def home(request):
    result = ""

    if request.method == "POST":
        text = request.POST.get("text", "").lower()

        if any(word in text for word in ["happy", "great", "good", "awesome"]):
            result = "Happy 😊"
        elif any(word in text for word in ["sad", "upset", "cry"]):
            result = "Sad 😢"
        elif any(word in text for word in ["angry", "mad", "hate"]):
            result = "Angry 😠"
        else:
            result = "Neutral 😐"

    return render(request, "index.html", {"result": result})