let unorderedList = document.querySelector("#unorderedList");

let taskInput = document.querySelector("#taskInput");

let create = document.querySelector("#create");
let remove = document.querySelector("#remove");
let removeAll = document.querySelector("#removeAll");
let removeCompleted = document.querySelector("#removeCompleted");

function createNewTask(parent, prompt){
    let newTask = document.createElement("li");
    
    let tickBox = document.createElement("input");
    let textContent = document.createTextNode(" " + prompt);

    tickBox.type = "checkbox";

    newTask.appendChild(tickBox);
    newTask.appendChild(textContent);

    parent.appendChild(newTask);
}

create.addEventListener("click", () => {
    createNewTask(unorderedList, taskInput.value)
    console.log("Created task.");
});

remove.addEventListener("click", () => {
    console.log("Removed task.");
});

removeAll.addEventListener("click", () => {
    console.log("Removed all tasks.");
});

removeCompleted.addEventListener("click", () => {
    console.log("Removed completed tasks.");
});

console.log("Website is running.");