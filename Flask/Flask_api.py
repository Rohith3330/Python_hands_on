from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error
import datetime
import sys
import os
from flask_cors import cross_origin 
import uuid

app = Flask(__name__)

def month_string_to_number(string):
    m = {
        'jan': 1,
        'feb': 2,
        'mar': 3,
        'apr':4,
         'may':5,
         'jun':6,
         'jul':7,
         'aug':8,
         'sep':9,
         'oct':10,
         'nov':11,
         'dec':12
        }
    out = m[string]
    return out

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='Rohith@123',
            database='API_Testing'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        # print("Error while connecting to MySQL Here", e)
        return None

@app.route('/Users', methods=['GET'])
@cross_origin()
def get_users():
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Users")
        users = cursor.fetchall()
        cursor.close()
        connection.close()
    except Exception as e:
        return jsonify({"error":repr(e)}),401
    else:
        return jsonify(users), 200
    
@app.route('/Events', methods=['GET'])
@cross_origin()
def get_events():
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        query = """
        SELECT e.id AS event_id, e.day, e.title, e.event_time, u.id AS user_id, u.name AS user_name, u.username
        FROM Events e
        LEFT JOIN EventAttendees ea ON e.id = ea.event_id
        LEFT JOIN Users u ON ea.user_id = u.id
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        connection.close()

        events_by_day = {}
        for row in rows:
            day = row['day'].strftime("%a, %d %b %Y %H:%M:%S GMT")
            event_id = row['event_id']
            event_time = row['event_time']
            total_seconds = abs(event_time.total_seconds())
            hours = (total_seconds // 3600) % 12 or 12
            minutes = total_seconds % 3600 // 60
            minutes=str(int(minutes))
            if(len(minutes)==1):
                minutes='0'+minutes
            period = "pm" if event_time.total_seconds() >= 0 else "am"
            time_str = f"{int(hours)}:{minutes} {period}"
            
            if day not in events_by_day:
                events_by_day[day] = {"day": day, "events": []}

            event_entry = next((event for event in events_by_day[day]["events"]
                                if event["id"] == event_id), None)
            if event_entry is None:
                event_entry = {
                    "id": event_id,
                    "title": row["title"],
                    "time": time_str,
                    "users": []
                }
                events_by_day[day]["events"].append(event_entry)

            if row["user_name"] not in event_entry["users"]:
                event_entry["users"].append(row["user_name"])

        response = list(events_by_day.values())

    except Exception as e:
        return jsonify({"error": repr(e)}), 401
    else:
        return jsonify(response), 200
        
@app.route('/Users', methods=['POST'])
@cross_origin()
def add_user():
    try:
        user_data = request.get_json()
        user_id = str(uuid.uuid4())
        username = user_data['username']
        name = user_data['name']

        connection = get_db_connection()
        cursor = connection.cursor()
        query = "INSERT INTO Users (id, username, name) VALUES (%s, %s, %s)"
        cursor.execute(query, (user_id, username, name))
        connection.commit()
        cursor.close()
        connection.close()
    except Exception as e:
        return jsonify({"error":repr(e)}),401
    else:

        return jsonify({"id": user_id, "username": username, "name": name}), 201

@app.route('/Events', methods=['POST'])
@cross_origin()
def add_event():
    try:
        event_data = request.get_json()
        # print(event_data)
        events = event_data['events']

        connection = get_db_connection()
        cursor = connection.cursor()

        new_events = []
        for event in events:
            event_id = str(uuid.uuid4())
            day=event_data['day']
            day=day.split(' ')
            # print(day[1][:3].lower())
            day=''+str(day[-1])+'-'+str(month_string_to_number(day[1][:3].lower()))+'-'+str(day[2])
            # print(day)
            # print(day)
            title = event['title']
            event_time = event['time']
            event_time = datetime.datetime.strptime(event_time, "%I:%M %p")
            # print(event_time)
            users = event['users']

            cursor.execute(
                "INSERT INTO Events (id, day, event_time, title) VALUES (%s, %s, %s, %s)",
                (event_id, day, event_time, title)
            )

            for user in users:
                user_id = user
                cursor.execute("SELECT id FROM Users WHERE name = %s", (user_id,))
                user_row = cursor.fetchone()
                # print(user_row)
                if user_row:
                    cursor.execute(
                        "INSERT INTO EventAttendees (event_id, user_id) VALUES (%s, %s)",
                        (event_id, user_row[0])
                    )

            new_events.append({
                "id": event_id,
                "title": title,
                "time": event_time,
                "users": users
            })

        connection.commit()
        cursor.close()
        connection.close()
        response = {
            "day": day,
            "events": new_events
        }
    except Exception as e:
        # exc_type, exc_obj, exc_tb = sys.exc_info()
        # fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        # print(exc_type, fname, exc_tb.tb_lineno)
        return jsonify({"error":repr(e)}),401
    else:
        return jsonify(response), 201



if __name__ == '__main__':
    app.run(debug=True)
