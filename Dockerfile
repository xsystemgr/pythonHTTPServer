# Χρησιμοποίησε την επίσημη Python εικόνα
FROM python:3.9-slim

# Καθορισμός του working directory
WORKDIR /app

# Αντιγραφή του script στον container
COPY pyhttp.py .

# Καθορισμός της εντολής εκτέλεσης
CMD ["python", "pyhttp.py"]

# Εκθέτει τη θύρα 8080
EXPOSE 8080
