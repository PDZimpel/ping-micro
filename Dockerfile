from python:3.11-slim

workdir /app

run apt-get update && apt-get install -y --no-install-recommends iputils-ping && rm -rf vat/lib/apt/lists/*


copy requirements.txt .
run pip install --no-cache-dir -r requirements.txt
copy . .

#expose 5555

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5555", "main:app"]
