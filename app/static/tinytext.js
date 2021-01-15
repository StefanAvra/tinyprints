let prevText = null;
let maxCols = 32;
let maxRows = 24;


// OK so there is wrap="hard" in textareas which does help a bit with lines that are longer than maxCols
// but the actual value of textarea will not contain these "fake" line breaks, so I have to handle overflowing rows
// this is not yet done

$('#tinytext').on('keyup', function () {
    let currText = $('#tinytext').val()
    if (currText == prevText) { return };
    prevText = currText
    let splitText = currText.split('\n').slice(0, maxRows);
    let overflow = 0
    for (const line of splitText) {
        if (line.length > maxCols) {
            overflow += Math.floor(line.length / 32);
        }
    }
    let cleanText = '';
    for (const c of splitText.join('\n')) {
        if(/^[\x00-\x7F]*$/.test(c)) {
            cleanText += c;
        }
    }
    $(this).val(cleanText)
});