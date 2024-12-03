movieDict = {"movie":"Endgame","duration":3,"collection":7412589633}
def fun(**kwargs):
    print(f"movie:{kwargs["movie"]}, duration: {kwargs['duration']}")
    print(f"movie: {kwargs['movie']}, duration: {kwargs['duration']}")

fun(movie = "Endgame",duration = 3)
