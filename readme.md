<h2 align="center">Wars Game python  || yossef </h2>

![game](./view/Screenshot%20from%202023-08-19%2011-23-05.png)
---
<ul> <li>Imports 📥 <ul> <li>pygame 🎮 for game functionality</li> <li>os 💻 to access files</li> </ul> </li> <li>Initialization 🚦 <ul> <li>WIDTH 🖥️ and HEIGHT 🖥️ of game window</li> <li>WIN 🖥️ display surface</li> <li>Colors 🎨 WHITE ⚪, BLACK ⬛, RED 🔴, YELLOW 🟡</li> <li>FPS 📈 frames per second</li> <li>VEL 🚗 ship speed</li> <li>BULLET_VEL 💫 bullet speed</li> <li>MAX_BULLETS 🔫 max bullets allowed</li> <li>BORDER 🖱️ rect for middle border</li> <li>Loads 🔈 sounds for bullet fire and hit</li> </ul> </li> <li>Spaceships 🚀 <ul> <li>WIDTH and HEIGHT for ships 🛸</li> <li>Loads yellow 🟡 and red ❤️ ship images</li> <li>Rotates and resizes images</li> </ul> </li> <li>Background 🌌 <ul> <li>Loads space image</li> <li>Resizes to fill window 🖥️</li> </ul> </li> <li>Fonts 🖊️ <ul> <li>For health ❤️ and winner 🏆 text</li> </ul> </li> <li>Functions 🧠 <ul> <li>draw_window 🖥️ renders all game objects</li> <li>yellow_handle_movement ➡️⬅️ moves yellow ship</li> <li>red_handle_movement ➡️⬅️ moves red ship</li> <li>handle_bullets ➡️⬅️ moves and deletes bullets</li> <li>draw_winner 🏆 displays winner text</li> </ul> </li> <li>Main Game Loop 🔁 <ul> <li>Initializes ship rects and bullet lists</li> <li>Clock ⏱️ to control framerate</li> <li>Event loop 📊 checks for quit or keys</li> <li>Shoots bullets on key down ⬇️</li> <li>Checks for hits and reduces health ❤️</li> <li>Calls ship movement and bullet functions</li> <li>Renders everything to the window 🖥️</li> <li>Shows winner 🏆 when health ❤️ is 0</li> </ul> </li> </ul>


---

### Email : yossefsabry66@gmail.com