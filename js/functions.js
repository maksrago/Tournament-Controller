newWin.onload = function(){
  var ident = newWin.document.getElementById('runner-one-username');
  ident.href = './output.html';
};

function myFunction() {
  var runnerOneScore = document.getElementById("runnerOneScoreInput");
  var runnerTwoScore = document.getElementById("runnerTwoScoreInput");
  if (!runnerOneScore.checkValidity()) {
    document.getElementById("demo").innerHTML = runnerOneScore.validationMessage;
  } else {
    document.getElementById("demo").innerHTML = "Input OK";
  } 
} 