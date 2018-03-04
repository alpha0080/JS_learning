//class test

function importClassTest(){
	var myName = {

　　　　name : "alpha",

　　　　createNew: function(){

　　　　　　var nameList = {};

　　　　　　nameList.printName = function(){ console.log(myName.name); };

　　　　　　nameList.changeName = function(getName){ myName.name =getName ; };

　　　　　　return nameList;

　　　　}

　　};
	return myName;
};
