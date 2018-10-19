function handle(evt, checked) {
    var file = evt.target.files[0];
    Papa.parse(file, {
        header: true,
        dynamicTyping: true,
        complete: function(results) {
            switch(checked){
                case 'train':
                    console.log("cleanTrains()");
                    cleanTrain(results);
                    break;
                case 'stores':
                    console.log("cleanStores()");
                    cleanStores(results);
                    break;
                case 'features':
                    console.log("cleanFeatures()");
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
            isHoliday = checkHoliday(line.IsHoliday);
        let row = [store, dept, date, weekSales, isHoliday];
        rows.push(row);
    }
    getCSV(rows, "trains", 'Store,Dept,Date,WeeklySales,isHolyday\n');
}

function cleanStores(result) {
    let data = result.data;
    let rows = [];
    for(let i = 0; i < data.length; i++) {
        let line = data[i],
            store = parseNumber(line.Store),
            type = line.Type,
            size = parseNumber(line.Size);
        let row = [store, type, size];
        rows.push(row);
    }
    getCSV(rows, "stores", 'Store,Type,Size\n');
}

function cleanFeatures(result) {
    let data = result.data;
    let rows = [];
    for(let i = 0; i < data.length; i++) {
        let line = data[i],
            store = parseNumber(line.Store),
            date = parseDate(line.Date),
            temperature = parseNumber(line.Temperature),
            fuelPrice = parseNumber(line.Fuel_Price),
            //markdowns
            cpi = parseNumber(line.CPI),
            unemployment = parseNumber(line.Unemployment),
            isHoliday = checkHoliday(line.IsHoliday);
        let row = [store, date, temperature, fuelPrice, cpi, unemployment, isHoliday];
        rows.push(row);
    }
    getCSV(rows, "features", 'Store,Date,Temperature,FuelPrice,CPI,Unemployment,isHoliday\n');
}