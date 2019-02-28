import mediafile
import fresh_tomatoes
findingnemo=mediafile.FavouriteMoviesFestival("finding nemo","comedy entertainer","https://images-na.ssl-images-amazon.com/images/I/51ZSMWko1BL.jpg","https://youtu.be/UwBVt4TR8YA")
findingdory=mediafile.FavouriteMoviesFestival("finding dory","comedy entertainer","https://pisces.bbystatic.com/image2/BestBuy_US/images/products/5329/5329712_sa.jpg;maxHeight=640;maxWidth=550","https://youtu.be/3JNLwlcPBPI")
taxiwala=mediafile.FavouriteMoviesFestival("taxiwala","suspense thriller","https://3.bp.blogspot.com/-IROwaGzaEYo/W-COtXquRbI/AAAAAAAAAHg/g7RZPq7EnRgpnkXN5qL3RGzqyknYtSOpACLcBGAs/s1600/05-Vijay-Deverakonda-TaxiWala-Movie-First-Look-ULTRA-HD-Posters-WallPapers.jpg","https://youtu.be/tEValM1Fhbw")
toystory2=mediafile.FavouriteMoviesFestival("toystory2","animation","https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-12561-9x29vp_d58d0519.jpeg?region=0%2C0%2C300%2C450&optimize=true","https://youtu.be/Lu0sotERXhI")
padmavath=mediafile.FavouriteMoviesFestival("padmavath","historical ","https://akm-img-a-in.tosshub.com/indiatoday/images/story/201801/Padmaavat-jauhar_0.jpeg?v5uFzB8GbyAqUVSAynGgq.z1SlGTSOkC","https://youtu.be/X_5_BLt76c0")
savyasachi=mediafile.FavouriteMoviesFestival("savyasachi","blockbuster entertainer","https://upload.wikimedia.org/wikipedia/en/thumb/e/ec/Savyasachi_poster.jpg/220px-Savyasachi_poster.jpg","https://youtu.be/Z_BpYivtf5I")
mowgli=mediafile.FavouriteMoviesFestival("mowgli","children entertainer","http://animediaonline.com/wp-content/uploads/2018/07/Mowgli_Vine_Poster.jpg","https://youtu.be/FB1KTG-O1V0")
anabelle=mediafile.FavouriteMoviesFestival("anabelle2","horror","https://pm1.narvii.com/6577/5d4b2df40761dc8b7f9df6a75b25440cb70e45ec_hq.jpg","https://youtu.be/11taaQy2KBg")
subrahmanyapuram=mediafile.FavouriteMoviesFestival("subrahmanyapuram","comedy action thriller","https://in.bmscdn.com/iedb/movies/images/website/poster/large/subrahmanyapuram-et00079086-04-07-2018-11-54-57.jpg","https://youtu.be/TrWKQtHw5R4")
movies=[findingnemo,taxiwala,toystory2,padmavath,savyasachi,mowgli,anabelle,subrahmanyapuram,findingdory]
fresh_tomatoes.open_movies_page(movies)

