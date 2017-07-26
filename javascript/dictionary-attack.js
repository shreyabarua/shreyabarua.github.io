//creates an array for the list of words
var wordsList = [];

function init() {
  // Load the words from the dictionary text file to wordsList
  //wordsFile is the text file of words on internet
  var wordsFile = "https://raw.githubusercontent.com/GirlsFirst/SIP-2017/master/Unit2_Applications/dictionary-attack/dictionary.txt?token=ADcVhZjRMd86ZdhPE2jVvIaJdQdzLA6Yks5YvvVSwA%3D%3D";
//$.get() is a method that loads data from the URL using GET request
//it is loading data from the wordsFile and also pass data to the server
//gets response from the wordsFileURL and passes it to the callback
//function in the form of data parameter and eventually invokes the callback function
  $.get(wordsFile, function(data) {
    //disables the submit button because you dont want someoene submitting a password until the data is formatted
    //into separate strings
    document.getElementById("btnSubmit").disabled = true;
    //splits dictionary words into a new line so they can be recognized as separate strings
    //stores each separate string as an element in wordsList array
    //external info must be converted into a js data type for it to be accessed
    wordsList = data.split('\n');
    //makes the submit button usable again
    document.getElementById("btnSubmit").disabled = false;
  });
}
//gets js ready to go as soon as window browser(web page) is loaded
window.onload = init;

/* ADD YOUR CODE BELOW */
var leet = {
  0: "o",
  1: "i",
  3: "e",
  4: "a",
  5: "s",
  7: "l",
  8: "b"
}

function checkPassword()
{
  var word = document.getElementById("pw").value;
  var new_word = "";
  for(j=0; j < word.length; j++)
  {
    var letter = word.charAt(j);
    if(leet[letter])
    {
      new_word += leet[letter]
    }
    else
    {
      new_word += letter;
    }
  }
  checkPasswordHelper(new_word);
}

function checkPasswordHelper(word_to_check)
{
  var bool=false;
  for (i = 0; i < wordsList.length; i++)
  {
    if (word_to_check == wordsList[i])
    {
      bool = true;
      break;
    }
    else
    {
      bool = false;
    }
  }

  if (bool == true)
  {
    alert("NOT SAFE");
  }
  else
  {
    alert("SAFE");
  }
}

checkPassword()
