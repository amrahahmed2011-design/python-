student_data ={
       "id1": {"name": "John", "age": 20, "grade": "A"},
       "id2": {"name": "Alice", "age": 22, "grade": "B"},
       "id3": {"name": "John", "age": 20, "grade": "A"},#DUPLICATE OF ID1
       "id4": {"name": "Bob", "age": 21, "grade": "C"}
}
result = {}
seen_keys = []

for student_id,details in student_data.items():
    # Create a tuple of the student's details to use as a unique identifier
    unique_key = (details["name"], details["age"], details["grade"])
    
    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id] = details
    
for k , v in result.items():
    print(k,":",v)