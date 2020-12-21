from pytube import YouTube as yt


url = 'https://www.youtube.com/watch?v=TYcyqgS_LRg'

try:
    youtube = yt(url)
    video = youtube.streams.get_highest_resolution()
    video.download('C:/Users/????/Downloads')   #Informar caminho onde deseja salvar os vídeos; a pasta do projeto é default
    print("Vídeo foi gravado com sucesso!")
except Exception as err:
    print('Vídeo não foi baixado. Ocorreu o seguinte erro: ' + str(err))