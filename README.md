# Collecting data from Stepik courses

This is an example of collecting collecting data for thesis project based on [Stepik](stepik.org) courses data obtained with Stepik.org REST API. The objective was to get data on each lesson and each step of several courses by its IDs. Script results in two `pandas` DataFrames with lessons and steps respectively.  

### Token

You can call Stepik.org API as a registered user, get OAuth2 keys by creating an [application]( https://stepik.org/oauth2/applications/). See [here](https://github.com/StepicOrg/Stepik-API#oauth-2) for more details. Token is obtained with `get_token()` function from [this example](https://github.com/StepicOrg/Stepik-API/blob/master/examples/get_courses_by_params.py). 

### Lessons data

Function `lessons_info_by_course(course_id, fields, delay)` returns `pandas` DataFrame with data on all lesson of a course. It takes:
* `course_id`: course ID (for example, ID of a course https://stepik.org/course/187/syllabus is 187);
* `fields`: list with lesson [parameters](https://stepik.org/api/docs/#!/lessons);
* `delay`: delay that will come in handy for multiple `GET` requests further.

### Step data

The data for steps is collected in a similar way. The function `steps_info_by_lesson(lesson_id, fields, delay)` takes:
* `lesson_id`: lesson ID obtained with `lessons_info_by_course()`;
* `fields`: list with lesson [parameters](https://stepik.org/api/docs/#!/stepss);
* `delay`: similar as above.
DataFrame with fields aas columns is returned.


Finally, you can see an example of collectind data for 3 courses. 

