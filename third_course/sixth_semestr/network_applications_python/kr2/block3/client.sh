curl -X POST -H "Content-Type: application/json" -d '{"name":"John Doe","email":"john@example.com"}' http://localhost:5000/users

curl -X POST -H "Content-Type: application/json" -d '{"name":"Jane Smith","email":"jane@example.com"}' http://localhost:5000/users

curl -X GET http://localhost:5000/users

curl -X PUT -H "Content-Type: application/json" -d '{"name":"John Updated","email":"john.updated@example.com"}' http://localhost:5000/users/1

curl -X GET http://localhost:5000/users

curl -X DELETE http://localhost:5000/users/2

curl -X GET http://localhost:5000/users