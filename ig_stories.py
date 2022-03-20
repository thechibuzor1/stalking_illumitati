import instaloader
from instaloader import Profile, Post

instance = instaloader.Instaloader()

instance.login(user="something_different_was_taken",passwd="111111118k")

profile = Profile.from_username(instance.context, username="illumitati")
instance.download_stories(userids=[profile.userid],filename_target='{}/stories'.format(profile.username))