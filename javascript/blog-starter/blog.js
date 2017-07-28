class BlogEntry {
//name, blogText
    constructor(name, blogText){
    this.name = name;
    this.blogText = blogText;
  }
}

function addEntryToBlog() {
  //Create new blog entry
  name = document.getElementById("blogEntryName").value  //assigning input value to name
  blogText = document.getElementById("blogEntryText").value //assigning input value to blogText
  var blogEntry = new BlogEntry(name, blogText);  //create object called BlogEntry that has name & text

  //calling the functions we made below
  createBlogEntryElement(blogEntry);
  createFooterElement(blogEntry);

  //Clear the inputs after blog has been posted
  document.getElementById("blogEntryName").value = "";
  document.getElementById("blogEntryText").value = "";
}

function createBlogEntryElement(blogEntry) {
  var entryDiv = document.createElement("div"); //creates a div for text to be posted in
  entryDiv.className = "blogEntry";  //text looks a certain way (in css)
  entryDiv.innerText = blogEntry.blogText; //inner text is assigned to be the blog text
  var blogDetails= document.getElementById("blogDetails"); //variable called blog details(called from html)
  blogDetails.appendChild(entryDiv); //add the blog to blog details
}

function createFooterElement(blogEntry) {
  var blogDetails= document.getElementById("blogDetails");
  var footerDiv = document.createElement("div");
  footerDiv.className = "blogDate";
  footerDiv.innerText = "by " + blogEntry.name + " on " + Date(); //date function in js
  blogDetails.appendChild(footerDiv);
}
