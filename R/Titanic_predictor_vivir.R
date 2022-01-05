library(tidyr)
library(ggplot2)
library(corrr)
library(rsample)
library(recipes)
library(parsnip)
library(yardstick)
library(titanic)
data <- titanic::titanic_train
data_split <- initial_split(data)
train <- training(data_split)
test <- testing(data_split)

skimr::skim(train)

data_red <- recipe(Survived ~.,train) %>%
  step_mutate(Survived = ifelse(Survived == 0, "died" ,"Survived")) %>%
  step_string2factor(Survived)%>%
  step_rm(PassengerId, Name, Ticket,Cabin) %>%
  step_impute_mean(Age)%>%
  step_dummy(all_nominal(), -all_outcomes()) %>%
  step_zv(all_predictors()) %>%
  step_center(all_predictors(),-all_nominal()) %>%
  step_scale(all_predictors(),-all_nominal())

data_prep <- data_red %>%
  prep()

model <-logistic_reg() %>%
  set_engine("glm") %>%
  set_mode("classification") %>%
  fit(Survived ~.,data =bake(data_prep,train))

library(waldo)

model %>%
  predict(new_data = bake(data_prep, test)) %>%
  bind_cols(bake(data_prep,test) %>%
              select(Survived))

predictions <- model %>% 
  predict(new_data = bake(data_prep, test)) %>%
  bind_cols(bake(data_prep,test) %>%
              select(Survived)
  )
predictions

predictions %>%
  conf_mat(Survived, .pred_class)

predictions %>%
  metrics(Survived, .pred_class) %>%
  select(-.estimator) %>%
  filter(.metric == "accuracy")

predictions %>%
  precision(Survived, .pred_class)