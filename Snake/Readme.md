## How To Run
1. Have Python Installed - Tkinter(usually bundled)

2. Download all the files

3. Run the game with: 
python main.py

4. Enjoy!

Quick Resizing Tips

Screen size: In main.py change screen.setup(...) to your desired resolution screen.setup(width=1200, height=800) etc.

ex. 1920×1080, GRID_SIZE=20, margin=40 → MAX_INDEX ≈ floor((1080/2 - 40)/20) = floor((540 - 40)/20) = 25 

Grid Cell Size: in food.py / snake.py adjust GRID_SIZE and MOVE_DISTANCE (MAKE SURE THEY ARE EQUAL)* 

Board bounds: : MAX_INDEX controls the number of cells from center to edge. It’s commonly set so GRID_SIZE * MAX_INDEX ≈ half the playable area minus margin. Update MAX_INDEX in food.py and any boundary checks in main.py.

Scoreboard placement: scoreboard.py uses self.goto(0,260) — change the 260 to something appropriate for larger heights (e.g. height/2 - margin).

If unsure
MAX_INDEX = floor((min(screen_width, screen_height)/2 - margin) / GRID_SIZE)



TROUBLESHOOTING:

If score not updating: ensure scoreboard.increase_score() is called ()
Food spawning on Snake: adjust MAX_INDEX and or ensure food.refresh(occupied_positions=...) is used