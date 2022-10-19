
```
docker search home-assistant
docker pull homeassistant/home-assistant
docker run -d --name="hass" -v $PWD/conf -p 8123:8123 homeassistant/home-assistant


```

