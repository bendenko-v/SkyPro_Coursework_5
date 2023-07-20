# SkyPro / Coursework 5

Web game "Heroes of SkyWars" based on Flask and templates.

![Starting page](https://habrastorage.org/webt/tf/wd/yf/tfwdyfdcecps9vcq6o8jlpw4tqo.jpeg)

![Arena](https://habrastorage.org/webt/5n/jx/ln/5njxln0o8s8ko8vb56m2jieqo1m.jpeg)

### Requirements
* Python v3.10
* Docker

## Usage

Install the required dependencies by running the following command: `pip install -r requirements.txt`

Run the command to start the Docker containers and build the project: `docker-compose up -d --build`

Run `app.py` to start the app.

## App features

You can choose a hero for yourself and the enemy and join the battle!

Use your weapons and skills to defeat the enemy!

The application was created as a practice for working with OOP and type annotation.

## Unrealized functionality

Redis and sessions have not been implemented so only one user can play at a time
