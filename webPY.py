import os
import time

from flask import Flask, request, render_template
from pydub import AudioSegment
from countdays import countDaysDiffer
from predictWavPath  import use_clf_predict_wav_type

app = Flask(__name__)


def save_upload_files(file, now_time_str):
    filename = file.filename
    filename = now_time_str + '.' + filename.split('.')[-1]
    save_upload_dir = 'upload'
    upload_file_path = os.path.join(save_upload_dir, filename)
    if not os.path.isdir(save_upload_dir):
        os.makedirs(save_upload_dir)
    file.save(upload_file_path)
    return upload_file_path


def convert_2_wav(audio_path):
    format_of_audio = audio_path.split('.')[-1]
    sound = AudioSegment.from_file(audio_path, format_of_audio)
    sound = sound.set_channels(1)
    sound = sound.set_frame_rate(16000)
    sound.export(audio_path.replace('.' + format_of_audio, '.wav'), 'wav')
    return audio_path.replace('.' + format_of_audio, '.wav')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        start = request.form['start']
        end = request.form['end']
        total = countDaysDiffer(start, end)
        # =========================================
        audio = request.files['audio']
        now_time_str = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
        audio = save_upload_files(audio, now_time_str)
        audio = convert_2_wav(audio)
        audio_type = use_clf_predict_wav_type(audio)
        os.remove(audio)
        return render_template('index.html', countDays=total, hidden='', audioType=audio_type)
    else:
        return render_template('index.html', hidden='hidden')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)