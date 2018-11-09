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
    const limit = data.length - 1; // começa no 0 e tem o header, logo discarda 2 linhas
    let nlines = 0;
    for(let i = 0; i <= limit; i++) {
        nlines++;
        let line = data[i],
            store = parseNumber(line.Store, "store"),
            dept = parseNumber(line.Dept, "dept"),
            //date = parseDate(line.Date), use line bellow for brain_dead method
            date = line.Date,
            weekSales = parseNumber(line.Weekly_Sales, "week_sales"),
            isHoliday = checkHoliday(line.IsHoliday);
        let row = [store, dept, date, weekSales, isHoliday];
        rows.push(row);
    }
    console.log("Train lines: " + nlines);
    getCSV(rows, "train", 'Store,Dept,Date,Weekly_Sales,IsHoliday\n');
}

function cleanStores(result) {
    let data = result.data;
    let rows = [];
    const limit = data.length - 1; // começa no 0 e tem o header, logo discarda 2 linhas
    let nlines = 0;
    for(let i = 0; i <= limit; i++) {
        nlines++;
        let line = data[i],
            store = parseNumber(line.Store, "store"),
            type = line.Type,
            size = parseNumber(line.Size, "size");
        let row = [store, type, size];
        rows.push(row);
        console.log("store: " + store)
    }
    console.log("Stores lines: " + nlines);
    getCSV(rows, "stores", 'Store,Type,Size\n');
}

function cleanFeatures(result) {
    let data = result.data;
    let rows = [];
    const limit = data.length - 1; // começa no 0 e tem o header, logo discarda 2 linhas
    let nlines = 0;
    for(let i = 0; i <= limit; i++) {
        nlines++;
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
        let row = [store, date, temperature, fuelPrice, md1, md2, md3, md4, md5, cpi, unemployment, isHoliday];
        rows.push(row);
    }
    console.log("Features lines: " + nlines);
    getCSV(rows, "features", 'Store,Date,Temperature,Fuel_Price,Markdown1,Markdown2,Markdown3,Markdown4,Markdown5,CPI,Unemployment,IsHoliday\n');
}
