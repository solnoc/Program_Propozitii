python3 format_for_cpp.py < send_cpp.txt > prop_for_graphic.txt
rm send_cpp.txt
g++ -c main.cpp -I/mnt/d/Librari/SFML-2.5.1-linux/include
g++ main.o -o sfml-app -L/mnt/d/Librari/SFML-2.5.1-linux/lib -lsfml-graphics -lsfml-window  -lsfml-system
LD_LIBRARY_PATH=/mnt/d/Librari/SFML-2.5.1-linux/lib
export LD_LIBRARY_PATH
gnome-terminal -- ./sfml-app
