# enrollment-App

Usecase:
There is a university named AKTU and it has multiple courses in it. Each course has multiple syllabuses linked to it. Every student has a unique enrollment number and he is linked with a single syllabus and course. Create CRUD API for courses, syllabus, and students. Also create GET APIs to fetch students on the basis of course, syllabus and enrollment number.

Comments:
1. Added all relevant apis on http://localhost:8000/
2. Student, Course, University, Syllabus are seperated in different modules.
3. Get API to fetch students based on course, syllabus and enrollment Number is merged into single API. 
   Example - http://localhost:8000/search-students/?syllabusId=1&courseId=1&enrollmentId=1
