# Chat-Room-Python

## Docker

### Docker File

- 7777 etant le port qui ecoute sur le pc , qu'il faut mettre coté client
- 1337 est le port d'écoute du programme

```powershell
docker build . -t chat  
docker run -d -p 7777:13337 -e CALC_PORT=13337 chat
```

### Docker Compose

```powershell
docker compose up --build
```

pour changer le port d'ecoute du pc dans le docker compose :
    ports:  
      - "**7777**:13337"  
pour changer le port d'ecoute du programme changez ces valeurs:  
    ports:  
      - "7777:**13337**"  
    environment:  
      - CHAT_PORT=**13337**
      - MAX_USERS=**20**
