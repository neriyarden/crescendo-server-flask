
genres
search_term




games = Games.objects(
    genres=Genres.objects(id__in=genres)
    platforms
)