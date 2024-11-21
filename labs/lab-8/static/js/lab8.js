/****************************************************************************************************************/
/* In-Class Exercises                                                                                           */
/****************************************************************************************************************/
/* 1. create an array called "fruits" and assign the values "Strawberry", "Raspberry", and "Apple" to it         */
// add code here

let fruits = [];
fruits = ["Strawberry", "Raspberry", "Apple"];

/* 2. add two more fruits to the "fruits" array using the correct array method                                   */
// add code here

fruits.push("Kiwi");
fruits.push("Pineapple");

/* 3. sort the fruits array alphabetically using the correct array method                                        */
// add code here

fruits.sort();

/* 4. create a function called printFruit that prints each item in the fruits array to the console              */
/*    and call the printFruit function                                                                          */
// add code here

function printFruit() {
  for (let fruit of fruits) {
    console.log(fruit);
  }
}

printFruit();

/* 5. create a fruit class that has three properties: name, color, and season and one method: printFruit()      */
/*    that prints all three properties of the fruit to the console. Then, create 3 fruit objects and print      */
/*    them using the printFruit() method             
// add code here */

class Fruit {
  constructor(name, color, season) {
    this.name = name;
    this.color = color;
    this.season = season;
  }

  printFruit() {
    console.log(`\n`);
    console.log(`Name: ${this.name}`);
    console.log(`Color: ${this.color}`);
    console.log(`Season: ${this.season}`);
  }
}

let myFavoriteFruits = new Fruit("Pomegranate", "Red", "Fall");
let fruitNeverTried = new Fruit("Cherimoya", "Green", "Spring");
let youShouldTry = new Fruit("Tamarind", "Brown", "Summer");

myFavoriteFruits.printFruit();
fruitNeverTried.printFruit();
youShouldTry.printFruit();

/****************************************************************************************************************/
/* In-Class Lab                                                                                                 */
/****************************************************************************************************************/
/* 1. Write a function that asks the user if they want to say hi. If the user selects "Okay" (true), then       */
/*    display a welcome message. If the user selects "Cancel" (false), then display a different message         */
function areYouSure() {
  let text = "Do you want to say hi?";
  if (confirm(text) === true) {
    text = "Welcome to Lab 8!";
  } else {
    text = "Rude!";
  }
  document.getElementById("welcome").innerHTML = text;
}

/* 2. Write a function to change 3 styles on the webpage                                                        */
let colorState = "black"; // Initial state

function changeStyle() {
  let docElement = document.getElementById("welcome");

  switch (colorState) {
    case "black":
      // Change styles for black state
      docElement.style.color = "red";
      docElement.style.fontSize = "32px";
      docElement.style.fontWeight = "bold";
      document.body.style.backgroundColor = "white";
      document.body.style.fontFamily = "Arial, sans-serif";
      colorState = "red"; // Update state
      break;
    case "red":
      // Change styles for red state
      docElement.style.color = "blue";
      docElement.style.fontSize = "64px";
      docElement.style.fontWeight = "normal";
      document.body.style.backgroundColor = "lightgray";
      document.body.style.fontFamily = "Courier New, monospace";
      colorState = "blue"; // Update state
      break;
    case "blue":
      // Change styles for blue state
      docElement.style.color = "green";
      docElement.style.fontSize = "128px";
      docElement.style.fontWeight = "bold";
      document.body.style.backgroundColor = "black";
      document.body.style.fontFamily = "Georgia, serif";
      colorState = "black"; // Update state
      break;
    default:
      console.log("Invalid state");
      break;
  }
}

// Add event listener to the button
document
  .getElementById("changeStyleBtn")
  .addEventListener("click", changeStyle);
