# A cool little imageboard forum thingy.

This is a pretty cool little forum, it works pretty well and has all the features you'd expect.

I have an instance of it running on my server at http://473gxngybwfp7nihkzw547yu5zf7ith5jfpgjio5vzei2e3l5d2qmaid.onion/ but this is a Tor site, meaning you require the Tor Browser or some other client capable of using Tor routing in order to use the official instance.

# Installation

You can find the prebuilt Docker image at `https://mega.nz/file/DQAhTBjY#Yn0eb0koYMeaysFpMoc8JJA9dTg0nDaX7LCs7qY4qNI` (or in the releases) or build it yourself or just use the regular Python

For a Docker installation, run:

`wget https://github.com/BellaTheUni112/forum/releases/download/idkbro/forum-app.tar`

or `curl -L -o forum-app.tar https://github.com/BellaTheUni112/forum/releases/download/idkbro/forum-app.tar` if wget doesn't work for whatever reason

`docker load -i forum-app.tar`

`docker run -d -p 8094:8094 --name forum forum-app`

Replace 8094:8094 with port:port (and replace port with whatever port you want) if you want to but it's not required to function

For a Python installation, run:

`git clone https://github.com/BellaTheUni112/forum.git`

`cd forum`

`pip install -r requirements.txt`

`python app.py`

And make sure port 8094 (or whatever port you selected) is free

# Tips

If you wish to change the port which the Python version runs as (you can do this with Docker if you modify the Python then rebuild it), you can replace "port=8094" with "port=any free port)

`    app.run(host='0.0.0.0', port=8094)`

# Screenshots

<img width="1917" height="953" alt="image" src="https://github.com/user-attachments/assets/877e66c7-e928-41c4-80e7-9486c66ff8c3" />

<img width="1912" height="951" alt="image" src="https://github.com/user-attachments/assets/2297dcb1-25ee-4979-bdfc-fd55e65934c0" />

<img width="1913" height="959" alt="image" src="https://github.com/user-attachments/assets/00b55082-3f26-4237-9b94-6a778d1cbca7" />

