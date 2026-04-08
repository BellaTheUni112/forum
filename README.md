a cool little imageboard forum thingy.

you can find the prebuilt docker image at https://mega.nz/file/DQAhTBjY#Yn0eb0koYMeaysFpMoc8JJA9dTg0nDaX7LCs7qY4qNI (or in the releases) or build it yourself or just use the regular python

i have an instance of it running on my server at http://473gxngybwfp7nihkzw547yu5zf7ith5jfpgjio5vzei2e3l5d2qmaid.onion/

once you have the docker image (you don't need it, it's just for portability) run these

`docker load -i forum-app.tar`

`docker run -d -p 8094:8094 --name forum forum-app`

replace 8094:8094 with <whatever port you want>:<whatever port you want> if you want to but it's not required to function
