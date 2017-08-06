import media
import fresh_tomatoes

spiderman=media.Movie("Spiderman_homecoming","griughfngtu","https://en.wikipedia.org/wiki/Spider-Man:_Homecoming#/media/File:Spider-Man_Homecoming_poster.jpg","https://www.youtube.com/watch?v=U0D3AOldjMU")
#print(spiderman.title)

terminator=media.Movie("terminator","skynet","https://en.wikipedia.org/wiki/Terminator_(franchise)#/media/File:Terminator_(franchise_logo).svg","https://www.youtube.com/watch?v=VVZQ39i5G1s")
#spiderman.show_trailer()

dunkirk=media.Movie("dunkirk","mass evacuation","https://goo.gl/images/goKctV","https://www.youtube.com/watch?v=T7O7BtBnsG4")

dead_poets=media.Movie("dead poets society","poets aren't really dead","https://en.wikipedia.org/wiki/Dead_Poets_Society#/media/File:Dead_poets_society.jpg","https://www.youtube.com/watch?v=wrBk780aOis")
movies=[spiderman,terminator,dunkirk,dead_poets]
fresh_tomatoes.open_movies_page(movies)
