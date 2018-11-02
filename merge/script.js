let train, features, stores;

function loadTrain(cb1, cb2, cb3, cb4) {
    Papa.parse('./data/input/train.csv', {
        download: true,
        header: true,
        dynamicTyping: true,
        complete: function(results) {
            train = results.data;
            cb1(cb2, cb3, cb4); 
        }
    });
}
function loadFeatures(cb, cb2, cb3) {
    Papa.parse('./data/input/features.csv', {
        download: true,
        header: true,
        dynamicTyping: true,
        complete: function(results) {
            features = results.data;
            cb(cb2, cb3);
        }
    });
}
function loadStores(cb, cb2) {
    Papa.parse('./data/input/stores.csv', {
        download: true,
        header: true,
        dynamicTyping: true,
        complete: function(results) {
            stores = results.data;
            cb(cb2);
        }
    });
}
function merge(callback) {
    train.forEach(_train => {
        const storeID = _train.Store;
        const date = _train.Date;
        // merging train with stores 
        stores.forEach(_store => {
            const _storeID = _store.Store;
            if(_storeID == storeID) {
                _train['Type'] = _store.Type;
                _train['Size'] = _store.Size;
            }
        });
        // merging train with features 
        features.forEach(_features => {
            const _storeID = _features.Store;
            const _date = _features.Date;
            if(_storeID == storeID && date == _date) {
                _train['Temperature'] = _features.Temperature;
                _train['FuelPrice'] = _features.FuelPrice;
                _train['Markdown1'] = _features.Markdown1;
                _train['Markdown2'] = _features.Markdown2;
                _train['Markdown3'] = _features.Markdown3;
                _train['Markdown4'] = _features.Markdown4;
                _train['Markdown5'] = _features.Markdown5;
                _train['CPI'] = _features.CPI;
                _train['Unemployment'] = _features.Unemployment;
                _train['isHoliday'] = _features.isHoliday;
            }
        });
    });
    $('#loading-msg').html("Finished!");
    callback();

}
function sequence() {
    loadTrain(loadFeatures, loadStores, merge, toCSV);
}
function toCSV() {
    let json = train;
    var csv = "";
    var keys = (json[0] && Object.keys(json[0])) || [];
    csv += keys.join(',') + '\n';
    for (var line of json) {
      csv += keys.map(key => line[key]).join(',') + '\n';
    }
    let link = document.createElement('a')
    link.id = 'download-csv'
    link.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(csv));
    link.setAttribute('download', 'output.csv');
    document.body.appendChild(link)
    document.querySelector('#download-csv').click()
}