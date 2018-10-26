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
                case 'test':
                    cleanTest(results);
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
    getCSV(rows, "trains", 'Store,Dept,Date,WeeklySales,isHoliday\n');
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
            md1 = parseMarkDown(line.MarkDown1),
            md2 = parseMarkDown(line.MarkDown2),
            md3 = parseMarkDown(line.MarkDown3),
            md4 = parseMarkDown(line.MarkDown4),
            md5 = parseMarkDown(line.MarkDown5),
            cpi = parseNumber(line.CPI, "cpi"),
            unemployment = parseNumber(line.Unemployment, "unemp"),
            isHoliday = checkHoliday(line.IsHoliday);
        console.log("Markdown1: " + line.MarkDown1 + " || " + typeof line.MarkDown1);
        let row = [store, date, temperature, fuelPrice, md1, md2, md3, md4, md5, cpi, unemployment, isHoliday];
        rows.push(row);
    }
    getCSV(rows, "features", 'Store,Date,Temperature,FuelPrice,Markdown1,Markdown2,Markdown3,Markdown4,Markdown5,CPI,Unemployment,isHoliday\n');
}

function cleanTest(result) {
    let data = result.data;
    let rows = [];
    for(let i = 0; i < data.length; i++) {
        let line = data[i],
            store = parseNumber(line.Store, "store"),
            dept = parseNumber(line.Dept, "dept"),
            date = parseDate(line.Date),
            isHoliday = checkHoliday(line.IsHoliday);
        let row = [store, dept, date, isHoliday];
        rows.push(row);
    }
    getCSV(rows, "test", 'Store,Dept,Date,isHoliday\n');
}