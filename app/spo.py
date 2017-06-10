import spotipy




def obtenerCancion(nombreCancion):
	sp = spotipy.Spotify(auth='')

	resultados = sp.search(q=nombreCancion, limit=1)
	if len(resultados['tracks']['items']) > 0:
		return resultados['tracks']['items'][0]['preview_url']
	else :
		return "lo siento"


print(obtenerCancion('el sapito'))