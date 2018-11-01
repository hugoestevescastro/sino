let train, features, stores;

function loadTrain(cb1, cb2, cb3) {
    Papa.parse('./data/input/train.csv', {
        download: true,
        header: true,
        dynamicTyping: true,
        complete: function(results) {
            train = results.data;
            cb1(cb2, cb3); 
        }
    });
}
function loadFeatures(cb, cb2) {
    Papa.parse('./data/input/features.csv', {
        download: true,
        header: true,
        dynamicTyping: true,
        complete: function(results) {
            features = results.data;
            cb(cb2);
        }
    });
}
function loadStores(cb) {
    Papa.parse('./data/input/stores.csv', {
        download: true,
        header: true,
        dynamicTyping: true,
        complete: function(results) {
            stores = results.data;
            cb();
        }
    });
}
function merge() {
    console.log(stores);
}
function sequence() {
    loadTrain(loadFeatures, loadStores, merge);
}