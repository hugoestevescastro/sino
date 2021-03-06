function parseNumber(value, field) {
    let parsed = Number(value);
    if (isNaN(parsed)) {
        return null;
    } else {
        return parsed;
    }
}
function checkHoliday(value) {
    if(typeof value == "boolean") {
        return value;
    }
    else {
        return null;
    }
}
function parseDate(value) {
    try {
        return new Date(value);
    }
    catch(exception) {
        return "Invalid Date";
    }
}
function parseMarkDown(value) {
    let parsed = Number(value);
    if (isNaN(parsed)) {
        return null;
    }
    else {
        return parsed;
    }
}
function getCSV(data, name, titleRow) {
    // Follow the given structure
    // data = [ [...,...], [...,...], ...]
    let csv = titleRow;
    data.forEach((row) => {
        csv += row.join(',');
        csv += "\n";
    });
    let link = document.createElement('a')
    link.id = 'download-csv'
    link.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(csv));
    link.setAttribute('download', name + '.csv');
    document.body.appendChild(link)
    document.querySelector('#download-csv').click()
}