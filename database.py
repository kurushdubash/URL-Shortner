from firebase import firebase
firebase = firebase.FirebaseApplication('https://b-side.firebaseio.com', None)
result = firebase.get('/shortcodes', None)
print(result)
result = firebase.post('/shortcodes', '235235', {'print': 'pretty'}, {'X_FANCY_HEADER': 'VERY FANCY'})