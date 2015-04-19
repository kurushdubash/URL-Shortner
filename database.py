from firebase import firebase
firebase = firebase.FirebaseApplication('https://b-side.firebaseio.com', None)


def check_database(short_code):
	return firebase.get(('/shortcodes/' + short_code), None)

def add_shortcode_site(url, short_code):
	firebase.put('/shortcodes', data=url, name=str(short_code))
