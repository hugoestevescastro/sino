function handle(evt, checked) {
    var file = evt.target.files[0];
    Papa.parse(file, {
        header: true,
        dynamicTyping: true,
        complete: function(results) {
            switch(checked){
                case 'train':
                    cleanTrain(results);
                    break;
                case 'stores':
                    cleanStores(results);
                    break;
                case 'features':
                    cleanFeatures(results);
                    break;
            }
        }
    });
} 
function cleanTrain(result) {
    let data = result.data;
    let rows = [];
    for(let i = 0; i < data.length; i++) {
        let line = data[i],
            store = parseNumber(line.Store),
            dept = parseNumber(line.Dept),
            date = parseDate(line.Date),
            weekSales = parseNumber(line.Weekly_Sales),
            isHolyday = checkHoliday(line.IsHoliday);
        let row = [store, dept, date, weekSales, isHolyday];
        rows.push(row);
    }
    getCSV(rows, "trains");
}

function cleanStores(result) {
    console.log(result);
}

function cleanFeatures(result) {
    console.log(result);
}