from django.shortcuts import HttpResponse, render
# from MedicalQASystem.code.answer_search import AnswerSearcher
# from MedicalQASystem.code.question_classifier import QuestionClassifier
# from MedicalQASystem.code.question_parser import QuestionPaser
#
#
# class ChatBotGraph:
#     def __init__(self):
#         self.classifier = QuestionClassifier()
#         self.parser = QuestionPaser()
#         self.searcher = AnswerSearcher()
#
#     def chat_main(self, sent):
#         answer = '您好，我是智能医疗助手，希望可以帮到您。如果没答上来，可联系wenius@qq.com。祝您身体健康！'
#         res_classify = self.classifier.classify(sent)
#         if not res_classify:
#             return answer
#         res_sql = self.parser.parser_main(res_classify)
#         final_answers = self.searcher.search_main(res_sql)
#         if not final_answers:
#             return answer
#         else:
#             return '\n'.join(final_answers)

from MedicalQASystem.models import ChatBotGraph
handler = ChatBotGraph()


def MedicalQA(request):
    data_from_html = ""
    # handler = ChatBotGraph()
    if request.method == 'POST':
        data_from_html = request.POST.get('html_data_to_views_name')
        HttpResponse(f'views得到表单数据{data_from_html}')
    answer = handler.chat_main(data_from_html)
    # print(python_data)
    return render(request, "MedicalQA.html", {"html_data_name": answer})
