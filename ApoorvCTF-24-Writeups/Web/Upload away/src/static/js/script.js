const dropArea = document.querySelector(".drop_box"),
  button = document.getElementById("choosefilebtn"),
  dragText = dropArea.querySelector("header"),
  input = dropArea.querySelector("input");
let file;
var filename;

button.onclick = () => {
  input.click();
};

input.addEventListener("change", function (e) {
  var fileName = e.target.files[0].name;
  let uploadText = document.getElementById("uploadText");
  uploadText.classList.add("invisible");

  let filenameText = document.getElementById("filenameText");
  filenameText.classList.remove("invisible");
  filenameText.innerHTML = `<h4>${fileName}</h4><br>`;

  let choosefilebtn = document.getElementById("choosefilebtn");
  choosefilebtn.classList.add("invisible");

  let submitButton = document.getElementById("submitButton");
  submitButton.classList.remove("invisible");

});


