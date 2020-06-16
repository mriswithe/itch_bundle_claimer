# Itch add to library
Script that logs into itch and adds all the games from the racial justice and equality bundle to your library by acting like you went to the download page for that item

## Requirements
* Python3.6 or above
* libyaml if on linux

## Instructions
Install Python3, can get it from the microsoft store if you are on windows 10, otherwise depends on your OS.

Download the two files `requirements.txt` and `itch_add_to_library.py` and place them somewhere, it doesn't write 
anything to disk, so it doesn't need to be anywhere special. 

To install the required libraries, open a shell or command prompt where you have the files. 

#### Windows
on windows you can go to file explorer, go to the directory where you put the two files and hold shift while right 
clicking. The menu will have a new option: `Open command window here`

```bash
python3 -m pip install -r requirements.txt
```

On windows it may be:
```bash
python3.exe -m pip install -r requirements.txt
```

Then to execute run the following, using either `python3` or `python3.exe` or whatever equivalent you used to install 
the requirements
```bash
>python3 itch_add_to_library.py
Itch.io login
username: myname
password:
```

Enter in your username then hit enter, then enter your password. It will not show you the password as you type it.

After this, it should either give a message saying it logged in successfully, and start showing output of what page it 
is on and each game that it is either claiming or you have claimed already, or it will say your username and password 
are wrong and exit. 

It should look something like this, but with more "Claiming game <game name>"
```bash
>python itch_add_to_library.py
Itch.io login
username: myaccountname
password:
2020-06-15 19:42:52.317 | INFO     | __main__:<module>:29 - Logged in successfully!
2020-06-15 19:42:52.323 | INFO     | __main__:<module>:36 - Getting link to your claimed bundle
2020-06-15 19:42:53.120 | INFO     | __main__:<module>:42 - Found bundle page link
2020-06-15 19:42:53.122 | INFO     | __main__:<module>:43 - Paging through the bundle page
2020-06-15 19:42:53.124 | INFO     | __main__:<module>:49 - Getting page 1
2020-06-15 19:42:53.358 | INFO     | __main__:<module>:60 - Already claimed Overland
2020-06-15 19:42:53.359 | INFO     | __main__:<module>:60 - Already claimed Night in the Woods
2020-06-15 19:42:53.360 | INFO     | __main__:<module>:60 - Already claimed Kenney Game Assets 1
2020-06-15 19:42:53.360 | INFO     | __main__:<module>:60 - Already claimed Sky Rogue
2020-06-15 19:42:53.361 | INFO     | __main__:<module>:60 - Already claimed Celeste
2020-06-15 19:42:53.362 | INFO     | __main__:<module>:60 - Already claimed A Short Hike
2020-06-15 19:42:53.363 | INFO     | __main__:<module>:60 - Already claimed Gladiabots
2020-06-15 19:42:53.364 | INFO     | __main__:<module>:60 - Already claimed Lancer Core Book: First Edition PDF
2020-06-15 19:42:53.365 | INFO     | __main__:<module>:60 - Already claimed MewnBase
2020-06-15 19:42:53.366 | INFO     | __main__:<module>:60 - Already claimed ART SQOOL
2020-06-15 19:42:53.366 | INFO     | __main__:<module>:60 - Already claimed Walden, a game
2020-06-15 19:42:53.367 | INFO     | __main__:<module>:60 - Already claimed A Mortician's Tale
2020-06-15 19:42:53.368 | INFO     | __main__:<module>:60 - Already claimed Lenna's Inception
2020-06-15 19:42:53.369 | INFO     | __main__:<module>:60 - Already claimed Oikospiel Book I
2020-06-15 19:42:53.370 | INFO     | __main__:<module>:60 - Already claimed BEACON
2020-06-15 19:42:53.371 | INFO     | __main__:<module>:60 - Already claimed Odd Realm
2020-06-15 19:42:53.372 | INFO     | __main__:<module>:60 - Already claimed NIGHT OF THE CONSUMERS
2020-06-15 19:42:53.372 | INFO     | __main__:<module>:60 - Already claimed Mu Cartographer
2020-06-15 19:42:53.373 | INFO     | __main__:<module>:60 - Already claimed EXTREME MEATPUNKS FOREVER
2020-06-15 19:42:53.374 | INFO     | __main__:<module>:60 - Already claimed Hex Kit
2020-06-15 19:42:53.375 | INFO     | __main__:<module>:60 - Already claimed Airships: Conquer the Skies
2020-06-15 19:42:53.376 | INFO     | __main__:<module>:60 - Already claimed MidBoss
2020-06-15 19:42:53.377 | INFO     | __main__:<module>:60 - Already claimed Arcade Spirits
2020-06-15 19:42:53.378 | INFO     | __main__:<module>:60 - Already claimed Minit
2020-06-15 19:42:53.378 | INFO     | __main__:<module>:60 - Already claimed 2064: Read Only Memories
2020-06-15 19:42:53.379 | INFO     | __main__:<module>:60 - Already claimed One Night Stand
2020-06-15 19:42:53.380 | INFO     | __main__:<module>:60 - Already claimed LAZA KNITEZ!!
2020-06-15 19:42:53.381 | INFO     | __main__:<module>:60 - Already claimed WitchWay
2020-06-15 19:42:53.382 | INFO     | __main__:<module>:60 - Already claimed ISLANDS: Non-Places
2020-06-15 19:42:53.383 | INFO     | __main__:<module>:60 - Already claimed No Delivery
2020-06-15 19:42:53.384 | INFO     | __main__:<module>:49 - Getting page 2
2020-06-15 19:42:53.746 | INFO     | __main__:<module>:60 - Already claimed Secret Little Haven
2020-06-15 19:42:53.747 | INFO     | __main__:<module>:60 - Already claimed Loot Rascals
2020-06-15 19:42:53.747 | INFO     | __main__:<module>:60 - Already claimed Long Gone Days
2020-06-15 19:42:53.748 | INFO     | __main__:<module>:60 - Already claimed Changeling
2020-06-15 19:42:53.749 | INFO     | __main__:<module>:60 - Already claimed Fugue in Void
2020-06-15 19:42:53.750 | INFO     | __main__:<module>:60 - Already claimed Haque
2020-06-15 19:42:53.751 | INFO     | __main__:<module>:60 - Already claimed DragonRuby Game Toolkit
```

If you hit an error and it exits early, you can safely start it again, and it will skip all of the games you have 
already claimed. I have seen a couple times that a connection times out, but it is hard to reproduce as I only got one
run of it on my own account.

Otherwise enjoy your games showing up in your library!
