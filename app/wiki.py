from wikiapi import WikiApi
wiki = WikiApi()
wiki = WikiApi({ 'locale' : 'es'}) 


def obtenerBiografia(nombre):
	results = wiki.find(nombre)
	article = wiki.get_article(results[0])
	return article.summary
	pass

# print(obtenerBiografia("Maluma"))