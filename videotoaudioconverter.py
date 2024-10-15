import os
import sys
from audio_extract import extract_audio

#cwd = os.path.dirname(os.path.abspath(__file__))
cwd = '.'
#print(cwd)
output_path = os.path.join(cwd, 'converted_mp3')


def convert_to_mp3():
    print("Buscando aquivos de vídeo na pasta atual. Um momento...\n")
    res = []
    for file in os.listdir(cwd):
        if file.endswith('.mp4'):
            res.append(file)
        if file.endswith('.mkv'):
            res.append(file)
        if file.endswith('.m4a'):
            res.append(file)
        if file.endswith('.avi'):
            res.append(file)
        if file.endswith('.wav'):
            res.append(file)
    #print(res)
    convert_to_audio(res)

def convert_to_audio(files):
   files_converted = 0

   for file in files:
       #print(os.path.join(cwd, file))
       if not os.path.isfile(os.path.join(cwd, file)):
           print(f"O arquivo {file} não existe.")
       else:
           input_file = os.path.join(cwd, file)
           output_file = os.path.join(output_path, os.path.splitext(file)[0] + '.mp3')
           
           print("Extraindo audio do arquivo" + os.path.splitext(file)[0] + "\n")
            
           progress(files_converted, len(files))
           
           try:
             extract_audio(input_path=input_file,output_path=output_file,overwrite=True)
           except:
             print("Erro ao converter arquivo")
          
       files_converted += 1

def progress(count, total, suffix=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', suffix))
    sys.stdout.flush()

convert_to_mp3()
