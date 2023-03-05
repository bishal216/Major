function displayText() {
    let fileInput = document.getElementById('file-input');
    let textInput = document.getElementById('text-input');
    let file = fileInput.files[0];
    let reader = new FileReader();
    reader.onload = function() {
       textInput.value = reader.result;
    };
    reader.readAsText(file);
 }

// setInterval(function(){location.reload();}, 5000);