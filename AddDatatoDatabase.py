import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattendacerealtime-12671-default-rtdb.firebaseio.com/"
})
ref = db.reference('Students')

data = {
    "321654":
        {
            "name": "Souraj khatua",
            "major": "MCA",
            "starting_year": 2022,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-07-15 00:54:34"
        },
    "852741":
        {
            "name": "Roumick Das",
            "major": "MCA",
            "starting_year": 2022,
            "total_attendance": 12,
            "standing": "B",
            "year": 3,
            "last_attendance_time": "2023-07-25 00:54:34"
        },
    "963852":
        {
            "name": "Payel Debnath",
            "major": "MCA",
            "starting_year": 2022,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)