from django.http import HttpResponse, HttpRequest, JsonResponse
from . import ChatModel as model
import json

chatModel = model.ChatModel()


def test(request):
    return HttpResponse("Hello Django & ChatGPT!(dev by openhe)")


def chat(request: HttpRequest):
    if request.method == 'GET':
        return HttpResponse("ERR: This api only support post method")
    else:
        question = json.loads(request.body)["question"]
        resp = chatModel.query(question)
        resp_json = {
            "resp": resp,
            "success": True if resp != "" else False
        }
        return JsonResponse(resp_json)
