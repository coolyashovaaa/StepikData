import json
import requests

def get_token():
    client_id = "..."
    client_secret = "..."

    auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
    resp = requests.post('https://stepik.org/oauth2/token/',
                         data={'grant_type': 'client_credentials'},
                         auth=auth)
    token = json.loads(resp.text)['access_token']
    return token

api_url = 'https://stepik.org/api/'


import pandas as pd
import time

def lessons_info_by_course(course_id, fields, delay):
    """
    Get data on all lessons of a Stepik course by course ID
    :param course_id: Stepik course ID
    :param fields: list fields to return, see: https://stepik.org/api/docs/#!/lessons
    :param delay: request delay
    :return: dataframe with fields as columns
    """
    lessons_response = json.loads(requests.get(api_url + 'lessons?course=' + str(course_id), headers={'Authorization': 'Bearer ' + get_token()}).text)
    df = pd.DataFrame()
    for i in range(len(lessons_response['lessons'])):
        for j in fields:
            try:
                df.loc[i, j] = lessons_response['lessons'][i][j]
            except ValueError:
                df.loc[i, j] = str(lessons_response['lessons'][i][j])
    time.sleep(int(delay))
    return df


def steps_info_by_lesson(lesson_id, fields, delay):
    """
    Get data on all steps in a lesson of a Stepik course by lesson ID
    :param lesson_id: lesson ID
    :param fields: list fields to return, see: https://stepik.org/api/docs/#!/steps
    :param delay: request delay
    :return: dataframe with fields as columns
    """
    steps_response = json.loads(requests.get(api_url + 'steps?lesson=' + str(lesson_id), headers={'Authorization': 'Bearer ' + get_token()}).text)
    df = pd.DataFrame()
    for i in range(len(steps_response['steps'])):
        for j in fields:
            try:
                df.loc[i, j] = steps_response['steps'][i][j]
            except ValueError:
                df.loc[i, j] = str(steps_response['steps'][i][j])
    time.sleep(int(delay))
    return df


courses_id = [187, 512, 2223]
lessons_fields = ['id', 'viewed_by', 'passed_by', 'epic_count', 'abuse_count']
df_lessons = pd.DataFrame(columns=lessons_fields)

for i in courses_id:
    df_temp = lessons_info_by_course(i, lessons_fields, 3)
    df_lessons = pd.concat([df_lessons, df_temp], ignore_index=True)


lessons_id = [int(x) for x in df_lessons['id']]
step_fields = ['id', 'position', 'viewed_by', 'passed_by', 'correct_ratio']
df_steps = pd.DataFrame(columns=step_fields)

for i in lessons_id:
    df_temp = steps_info_by_lesson(i, step_fields, 3)
    df_steps = pd.concat([df_steps, df_temp], ignore_index=True)

