# ChatGPT Django Server
## Introduction
This project is a python web server built by Django, 
enabling you to construct your own ChatGPT API/service on your server. 
ChatGPT rev project is
powered by [acheong08/ChatGPT](https://github.com/acheong08/ChatGPT).
## How to Use
### Requirements
* system environment
  * python >= 3.8    
* python libs  
  * django  
  * revChatGPT
### Deployment
```bash
git clone https://github.com/openhe-hub/chatgpt-django-server.git
cd chatgpt-django-server
pip3 install -r requirements.txt
cd ./src/chat_server/
python3 manage.py runserver
```
Now the server is running at `http://127.0.0.1:9000/`
### Configuration
modify `./src/chat_server/assets/config.json`
```json
{
    "email": "your openai account email",
    "password": "your openai account password",
    "session_token": "cookie: __Secure-next-auth.session-token"
}
```
### API Example
post: `http://www.openhe-station.com/api/chat`
## Data Format
* Http request(post): `/api/chat`
    ```json
    {
      "question": "your question"
    }
    ```
* Http response: `/api/chat`
    ```json
    {
      "resp": "respond from ChatGPT",
      "status": true  
    }
    ```
## Special Notice
This is not an official api or server demo from ChatGPT



