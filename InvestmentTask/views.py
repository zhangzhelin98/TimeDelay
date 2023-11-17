from otree.api import View
from django.http import JsonResponse

class SaveVideo(View):
    def post(self):
        video_file = self.request.FILES['video']
        participant_code = self.request.POST['participant_code']
        file_path = f'_static/video/{participant_code}.mp4'
        with open(file_path, 'wb') as f:
            for chunk in video_file.chunks():
                f.write(chunk)
        return JsonResponse({'status': 'ok'})


