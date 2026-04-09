# A cool little imageboard forum

A lightweight imageboard-style forum built with Flask.  
Simple, fast, and easy to self-host.

This project includes the core features you'd expect from a classic anonymous imageboard.

---

## Live Instance (Tor)

An official instance is available:

http://473gxngybwfp7nihkzw547yu5zf7ith5jfpgjio5vzei2e3l5d2qmaid.onion/

This is a Tor hidden service, you’ll need the Tor Browser or a compatible client to access it.

---

## Tech Stack

- Python  
- Flask  

---

## Features

- **Threads** – classic forum-style discussions  
- **Replies** – respond to posts within threads  
- **Images** – upload and share images  
- **Boards** – organize content by topic  
- **Anonymity** – no accounts required  
- **Lightweight** – runs on most modern hardware  
- **Fast** – quick page loads and responses (depends on server performance)

---

## Installation

### Docker

Download the prebuilt image:

```bash
wget https://github.com/BellaTheUni112/forum/releases/download/idkbro/forum-app.tar
```

Or:

```bash
curl -L -o forum-app.tar https://github.com/BellaTheUni112/forum/releases/download/idkbro/forum-app.tar
```

Run it:

```bash
docker load -i forum-app.tar
docker run -d -p 8094:8094 --name forum forum-app
```

You can change the port if needed:

```bash
docker run -d -p <port>:<port> --name forum forum-app
```

---

### Python

```bash
git clone https://github.com/BellaTheUni112/forum.git
cd forum
pip install -r requirements.txt
python app.py
```

Make sure port `8094` (or your chosen port) is free.

---

## Configuration

To change the port:

```python
app.run(host='0.0.0.0', port=8094)
```

Replace `8094` with any available port.

---

## Notes

- No software is completely secure
- This project does not guarantee complete anonymity
- You must comply with all local laws when using this product
- This project is designed for **self-hosting**
- If you expose it publicly, consider:
  - Moderation tools  
  - Rate limiting  
  - Basic security protections  

---

## Screenshots

<img width="1917" height="953" alt="image" src="https://github.com/user-attachments/assets/877e66c7-e928-41c4-80e7-9486c66ff8c3" />

<img width="1912" height="951" alt="image" src="https://github.com/user-attachments/assets/2297dcb1-25ee-4979-bdfc-fd55e65934c0" />

<img width="1913" height="959" alt="image" src="https://github.com/user-attachments/assets/00b55082-3f26-4237-9b94-6a778d1cbca7" />

---
