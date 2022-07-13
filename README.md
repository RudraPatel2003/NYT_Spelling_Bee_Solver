<h1 align="center">
  <br>
    <img src="https://raw.githubusercontent.com/RudraPatel2003/NYT_Spelling_Bee_Solver/main/src/assets/images/Logo.png">
  <br>
  NYT Spelling Bee Solver
  <br>
</h1>

<h2 align="center">Obtain a list of possible answers to the <a href="https://www.nytimes.com/puzzles/spelling-bee">New York Times Spelling Bee Game</a> or launch a Selenium bot that will play the game for you on <a href="https://nytimes-spellingbee.com">different website</a> (due to paywalls).</h2>

https://user-images.githubusercontent.com/85089368/178854082-9d66120f-cba6-4022-916b-17477a08488d.mp4

## 🔨 Installation and Usage

### 1\. Clone the repository
```bash
git clone https://github.com/RudraPatel2003/NYT_Spelling_Bee_Solver.git
```   
### 2\. Change the working directory
```bash
cd NYT_Spelling_Bee_Solver
```
### 3\. Install dependencies   

Windows:
```bash
py -m pip install -r requirements.txt
```
Unix/macOS:
```bash
python -m pip install -r requirements.txt
```

### 4\. Install Chrome Webdriver
Go to [this website](https://sites.google.com/chromium.org/driver/) and download Chrome Webdriver onto your machine.

### answer_generator.py
Input the central letter into "central_letter" and the remaining 6 letters into "satellite_letters". Then, run the program to obtain a list of possible answers and panagrams.

### Selenium_Bot.py  
Run the program to launch the Selenium bot. The bot will then play the game and input all possible guesses into the game. Then, it will print all correct answers onto the command line. Input anything into the command line to close the game window.

## 🤝 Contributing
Pull requests are welcome.  
If you have access to a database of all possible answers to the game (as some websites seem to have), please email me at patelrudra2003@gmail.com.

## 📖 License

[MIT](https://choosealicense.com/licenses/mit/)
