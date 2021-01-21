let prevText = null;
let maxCols = 32;
let maxRows = 24;


// OK so there is wrap="hard" in textareas which does help a bit with lines that are longer than maxCols
// BUT maxCols is not accurate.

let newTextArea = document.getElementById('new-tiny-text-area');
if (newTextArea) {
    newTextArea.addEventListener("keyup", cleanText);
}

function cleanText() {
    let currText = this.value
    if (currText == prevText) { return };
    prevText = currText
    let splitText = currText.split('\n').slice(0, maxRows);
    let overflow = 0
    for (const line of splitText) {
        if (line.length > maxCols) {
            overflow += Math.floor(line.length / maxCols);
        }
    }
    let cleanText = '';
    for (const c of splitText.join('\n')) {
        if (/^[\x00-\x7F]*$/.test(c)) {
            cleanText += c;
        }
    }
    this.value = cleanText
}


function allowedCharsOnly(str) {
    let clean = '';
    for (const c of str) {
        if (/^[\x00-\x7F]*$/.test(c)) {
            clean += c;
        }
    }
    return clean;
}

function showRules() {
    let x = document.getElementById("rules-toast");
    x.className = "show";
    setTimeout(function () { x.className = x.className.replace("show", ""); }, 6000);
}

function upvote(id) {
    document.getElementById('tiny_text_id').value = id;
    document.getElementById('upvote-form').submit();
}

function showDeletePWInput() {
    let delForm = document.getElementById('delete-form');
    delForm.hidden = !delForm.hidden;
    let delHint = document.getElementById('delete-hint');
    delHint.hidden = !delHint.hidden;
}


let infoStyles = [
    "color: #fff",
    "background-color: #444",
    "padding: 2px 4px",
    "border-radius: 5px",
].join(';');

console.info(`%cWelcome to tinyprints 👋
If you're interested in reading the code, reporting an issue or even contributing
you can find the project on my GitHub: https://github.com/StefanAvra/tinyprints
✌ avra`, infoStyles)
