import instaloader 
from instaloader import Profile, Post

res = instaloader.Instaloader()
res.login(user="something_different_was_taken",passwd="111111118k")
res.download_profile(profile_name="sdcarderror")