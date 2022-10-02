# foo_genius

foo_genius is a working [Genius](https://genius.com) source for Lyric Panel 3.

## Installation
Create an account on the [Genius](https://genius.com/developers) developers page.

Download [foo_lyricsource](https://github.com/tripod31/foo_lyricsource) and install it.
 
 Go into your terminal, and run the following
```
 cd C:\Program Files (x86)\foobar2000
 
 git clone https://github.com/zyme-xd/foo_genius

 echo > .env
```
Open `.env` with notepad, and make it look like something upon these lines
```
APIKEY=keyhere
```
 Save, adjust your lyric source hierarchy accordingly and you should be all set!
## Testing
You can test the lyric searching capabilities by running the following in your terminal.
```python
get_lyric.py --track "Be Nice 2 Me" --artist "Bladee"
```
