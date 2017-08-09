array = [28, 4, 19, 9, 6, 17, 34, 11, 89, 43];
document.getElementById("array").innerHTML = array;
function swap(x, y)
{
  var temp = array[y];
  array[y] = array[x];
  array[x] = temp;
}

function sort()
{
  for (i = 0; i < array.length; i++)
  {
    var element = array[i];
    var j = i;
    while (j > 0 && array[j-1] > array[j])
    {
     swap(j, j-1);
     j = j - 1;
    }
  }
document.getElementById("newarray").innerHTML = array;
}
