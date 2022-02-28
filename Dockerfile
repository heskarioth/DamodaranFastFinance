FROM python:3.10.1

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

# this copies files from my current directory (the workdir) to my workdirictory in the container (/user/src/app)
# the idea is to first copy the dependencies and install them, this way if we change our source code
# only the actual code change will be compiled, not the entire application from scratch.
COPY . .  

CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8000"]

