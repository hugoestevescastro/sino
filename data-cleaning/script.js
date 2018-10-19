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
            store = parseNumber(line.Store, "store"),
            dept = parseNumber(line.Dept, "dept"),
            date = parseDate(line.Date),
            weekSales = parseNumber(line.Weekly_Sales, "week_sales"),
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
            store = parseNumber(line.Store, "store"),
            type = line.Type,
            size = parseNumber(line.Size, "size");
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
            store = parseNumber(line.Store, "store"),
            date = parseDate(line.Date),
            temperature = parseNumber(line.Temperature, "temperature"),
            fuelPrice = parseNumber(line.Fuel_Price, "fuel_price"),
            //markdowns
            cpi = parseNumber(line.CPI, "cpi"),
            unemployment = parseNumber(line.Unemployment, "unemp"),
            isHoliday = checkHoliday(line.IsHoliday);
        let row = [store, date, temperature, fuelPrice, cpi, unemployment, isHoliday];
        rows.push(row);
    }
    getCSV(rows, "features", 'Store,Date,Temperature,FuelPrice,CPI,Unemployment,isHoliday\n');
}