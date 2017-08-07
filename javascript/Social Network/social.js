/*
INSTRUCTIONS:

1. Create a list of 5 names of girls
2. Store 3 friends for each of these 5 girls
3. When the user enters the name of a girl from the list,
   and clicks "Get Friends" display friends of that girl
*/

/*ENTER CODE HERE*/
rachelFriends = ["phoebe", "monica", "ross"];
robinFriends = ["marshall", "lily", "ted"];
meredithFriends = ["cristina", "alex", "george"];
jjFriends = ["prentiss", "hotchner", "garcia"];
erinFriends = ["andy", "michael", "pam"];
var socialNetwork =
{
  "rachel": rachelFriends,
  "robin": robinFriends,
  "meredith": meredithFriends,
  "jj": jjFriends,
  "erin": erinFriends
}
function getFriends() {
  var name = document.getElementById("nameInput").value;
  document.getElementById("friends").innerHTML = socialNetwork[name];
}

/*EXTENSION*/

function addFriend() {
  girl = document.getElementById("nameOfGirl").value;
  newFriend = document.getElementById("nameOfFriend").value;
  socialNetwork[girl].push(newFriend);
  console.log(socialNetwork[girl]);
}
