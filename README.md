a cool little imageboard forum thingy.

you can find the prebuilt docker image at https://mega.nz/file/DQAhTBjY#Yn0eb0koYMeaysFpMoc8JJA9dTg0nDaX7LCs7qY4qNI (or in the releases) or build it yourself or just use the regular python

i have an instance of it running on my server at http://473gxngybwfp7nihkzw547yu5zf7ith5jfpgjio5vzei2e3l5d2qmaid.onion/

for docker run

`wget https://github.com/BellaTheUni112/forum/releases/download/idkbro/forum-app.tar`

or `curl wget https://github.com/BellaTheUni112/forum/releases/download/idkbro/forum-app.tar -o forum_app.tar` if wget doesn't work for whatever reason

`docker load -i forum-app.tar`

`docker run -d -p 8094:8094 --name forum forum-app`

replace 8094:8094 with port:port (and replace port with whatever port you want) if you want to but it's not required to function



for python run

`git clone https://github.com/BellaTheUni112/forum.git`

`cd forum`

`pip install -r requirements.txt`

`python app.py`

and make sure port 8094 (or whatever port you selected) is free

replace the port=8094

`    app.run(host='0.0.0.0', port=8094)`

with whatever port you want
