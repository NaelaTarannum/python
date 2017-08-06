import webbrowser
class Movie():
     def __init__(self,movie_title,movie_storyline,poster_image,trailer_yt):
         self.title=movie_title
         storyline=movie_storyline
         self.poster_image_url=poster_image
         self.trailer_url=trailer_yt

     def show_trailer(self):
         webbrowser.open(self.trailer_url)
