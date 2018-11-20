# Options
WORKING_DIRECTORY = '~/Git/university/sino/development/modeling/brain_dead'
setwd(WORKING_DIRECTORY)

library("rio")

stores <- import("./csv/stores.csv")
saveRDS(stores, "./rds/stores.rds")

features <- import("./csv/features.csv")
saveRDS(features, "./rds/features.rds")

train <- import("./csv/train.csv")
saveRDS(train, "./rds/train.rds")

test <- import("./csv/test.csv")
saveRDS(test, "./rds/test.rds")