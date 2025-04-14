# PyWordle
PyWordle is a simple word-guessing game in the terminal that is inspired by the popular New York Times game Wordle. 

## Set Up
<ol>
	<li>Create new anaconda environment using these commands</li>
	<ul>
		<li>conda create --name wordle python=3.13.1</li>
		<li>conda activate wordle</li>
	    <li>conda install -c anaconda colorama</li>
    </ul>
</ol>

## How to Play
<ul>
	<li>Guess a word by typing it into the terminal.</li>
	<li>The game will then provide feedback for your guess:</li>
	<ul>
		<li>A green letter indicates that the letter is correct and in the correct position</li>
		<li>A yellow letter indicates that the letter is correct but in the wrong position </li>
		<li>A grey letter indicates that the letter is incorrect and not in the word</li>
	</ul>
	<li>Keep guessing until you find the correct word! You have six attempts to get it!</li>
</ul>