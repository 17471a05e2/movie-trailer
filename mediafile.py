import webbrowser
class FavouriteMoviesFestival():
    def __init__(self,mt,msl,mp,mtr):
        self.mt=mt
        self.msl=msl
        self.mp=mp
        self.mtr=mtr
    def play_trailer(self):
        webbrowser.open(self.mtr)

