var doc = app.activeDocument;
var rootXML = doc.xmlElements[0];

// Find all custom table tags (table1, table2, etc.)
var tables = rootXML.evaluateXPathExpression("//table1 | //table2");

var yOffset = 20; // to space out multiple tables vertically

for (var i = 0; i < tables.length; i++) {
    var tableElement = tables[i];

    // Get all rows
    var rows = tableElement.evaluateXPathExpression("tr");
    var rowCount = rows.length;
    var colCount = rows[0].evaluateXPathExpression("tc").length;

    // Create an empty text frame to hold the table
    var tf = doc.pages[0].textFrames.add();
    tf.geometricBounds = [yOffset + "mm", "20mm", yOffset + 50 + "mm", "180mm"]; // Adjust size
    yOffset += 60; // shift down for next table

    // Insert the table into the frame
    var table = tf.insertionPoints[0].tables.add({bodyRowCount: rowCount, columnCount: colCount});

    // Fill the table cell-by-cell
    for (var r = 0; r < rowCount; r++) {
        var rowElement = rows[r];
        var cells = rowElement.evaluateXPathExpression("tc");
        for (var c = 0; c < cells.length; c++) {
            var textContent = cells[c].contents;
            table.rows[r].cells[c].contents = textContent;
        }
    }
}
