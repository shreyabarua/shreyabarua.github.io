class Person{
  constructor(first_name, last_name, address){
    this.first_name = first_name;
    this.last_name = last_name;
    this.address = address;
  }
  getFullName(){
    return (this.first_name + " "+ this.last_name);
  }
  getAddress(){
    return (this.address);
  }
}

var TomCruise = new Person("Tom", "Cruise", "23 Beverly Hills, CA");

document.getElementById("myName").innerHTML = TomCruise.getFullName();
document.getElementById("myAddress").innerHTML = TomCruise.getAddress();
